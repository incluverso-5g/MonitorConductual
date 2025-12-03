from argparse import ArgumentParser
from typing import Optional
import threading
import requests
from adbutils import adb#, adb2 #adb2 is the HMD
from PySide6.QtGui import QImage, QKeyEvent, QMouseEvent, QPixmap, Qt
from PySide6.QtCore import QTimer, Qt, QTime
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
import cv2
import os
import time
import json
import faulthandler
import subprocess
from ui_mainwindow import Ui_MainWindow
from functools import partial
import socket
import sys
import os
import av
import traceback

# Screen Recording Imports
import configparser
from pathlib import Path
import re
from datetime import datetime

if not QApplication.instance():
    app = QApplication([])
else:
    app = QApplication.instance()

# ======== Carpeta de Vídeos ========
def _expand_path(p: str) -> str:
    """Expande %USERPROFILE% / ~ y convierte rutas relativas a absolutas (basadas en cwd)."""
    if not p:
        return ''
    p = os.path.expandvars(os.path.expanduser(p))
    if not os.path.isabs(p):
        p = os.path.abspath(os.path.join(os.getcwd(), p))
    return p

def _drive_exists(path_str: str) -> bool:
    """Devuelve True si la unidad (C:, D:, etc.) existe o si no hay unidad explícita."""
    drive, _ = os.path.splitdrive(path_str)
    return (drive == '') or os.path.exists(drive + os.sep)

def _ensure_writable_dir(preferred: str, fallback: str) -> str:
    """
    Devuelve un directorio utilizable. Si 'preferred' apunta a una unidad que no existe
    o no se puede crear/escribir, usa 'fallback'.
    """
    try:
        pref = _expand_path(preferred)
        if not _drive_exists(pref):
            raise FileNotFoundError(f"Unidad no existente para: {pref}")
        Path(pref).mkdir(parents=True, exist_ok=True)
        # prueba de escritura
        test = Path(pref) / ".write_test.tmp"
        with open(test, "w", encoding="utf-8") as f:
            f.write("ok")
        test.unlink()
        return pref
    except Exception as e:
        print(f"[WARN] Carpeta preferida no usable ({e}). Probando fallback...")
        fb = _expand_path(fallback)
        Path(fb).mkdir(parents=True, exist_ok=True)
        return fb
# ========================================================================

class ServerTCPIP():
    def __init__(self, host: str = '192.168.31.160', port: int = 3001):
        self.host = host
        self.port = port

    def set_host(self, host: str, port: int = None):
        """Permite actualizar el destino en caliente (desde el template)."""
        self.host = host
        if port is not None:
            self.port = port
        print(f"[TCP] Destino actualizado -> {self.host}:{self.port}")

    def emit(self, dr_command, msg):
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        msg = msg.get("uri", "")
        server_address = (self.host, self.port)

        print('connecting to {} port {}'.format(*server_address))
        sock.connect(server_address)
        print('EL mensaje es'+msg)
        try:
            message = msg.encode('ascii')
            print('sending {!r}'.format(message))
            sock.sendall(message)
        finally:
            print('closing socket')
            sock.close()

class MainWindow(QMainWindow):
    def __init__(
        self,
        max_width: Optional[int],
        serial: Optional[str] = None,
        encoder_name: Optional[str] = None,
    ):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.max_width = max_width
        self.lock = threading.Lock()
        self.uri = None

        self.load_cfg() # Carga configuración del .ini

        self.sio = ServerTCPIP()

        # Setup devices
        self.devices = self.list_devices()
        self.SmartPhoneHTTP = f"http://{self.phone_ip}:8080/stream.mjpeg"

        if len(self.devices) == 1:
            self.device = adb.device(serial=self.devices[0])
            self.alive = True
        else:
            self.device = None
            self.cap = None
            self.alive = False

        self.escena_buttons = [
            self.ui.EscenariosNeutros_,
            self.ui.Capturas_Escaleras_,
            self.ui.EscalerasInterioresGrises_,
            self.ui.EscalerasInterioresGrisesBaj_,
            self.ui.EscalerasInterioresNaranjas_,
            self.ui.EscalerasInterioresNaranjasBaj_,
            self.ui.EscalerasMecanicas_,
            self.ui.EscalerasMecanicasBaj_,
            self.ui.EscalerasAutobus_,
            self.ui.EscalerasAutobusBaj_,
            self.ui.Escenario_Playa_,
            self.ui.EscenarioNeutroMontana,
            self.ui.EscenarioNeutroSalonCasa_,
            self.ui.EscenarioNeutroPlaya2_,
            self.ui.CapturasAmigables01,
            self.ui.CapturasAmigables02,
            self.ui.CapturasAmigables03,
            self.ui.CapturasAmigables04,
            self.ui.CapturasAmigables05,
            self.ui.EscenarioCapturaEscaleras01,
            self.ui.EscenarioCapturaEscaleras02,
            self.ui.EscenarioCapturaEscaleras03,
            self.ui.EscenarioCapturaEscaleras04,
            self.ui.EscenarioCapturaEscaleras05,
            self.ui.EscenarioCapturaEscaleras06,
            self.ui.EscenarioCapturaEscaleras08,
            self.ui.EscenarioCapturaEscaleras09,
            self.ui.EscenarioCapturaEscaleras11,
            self.ui.EscenarioCapturaEscaleras13,
        ]

        # Bind controllers
        self.ui.button_home_.clicked.connect(self.StartApp)
        self.ui.button_back_.clicked.connect(self.StopApp)

        #CONTADOR
        self.time = QTime(0, 0, 0)
        self.ui.button_home_.clicked.connect(self.startTimer)
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateLCD)

        self.ui.RestartTimer.clicked.connect(self.restartTimer)

        #IP GAFAS
        self.ui.ActualizarIP.clicked.connect(lambda: self.get_device_ip(self.devices[0]))

        #BATERIA GAFAS
        self.timer2 = QTimer()
        self.timer2.start(1000)
        #print('Bateria actualizada')
        self.timer2.timeout.connect(self.actualizarBateria)

        #VER VISTA GAFAS
        self.ui.mirror_hmd.clicked.connect(self.scrcpy_mirror)
        self.ui.mirror_biosensors.clicked.connect(self.biosensors_mirror)

        #POSICION
        self.ui.reiniciarPos.clicked.connect(partial(self.on_click_button, 'CentrarPos'))
        self.ui.girar90.clicked.connect(partial(self.on_click_button, 'girar90'))
        self.ui.girarmenos90.clicked.connect(partial(self.on_click_button, 'girarmenos90'))
        self.ui.girar180.clicked.connect(partial(self.on_click_button, 'girar180'))

        self.ui.MasAltura.clicked.connect(partial(self.on_click_button, 'MasAltura'))
        self.ui.MenosAlutra.clicked.connect(partial(self.on_click_button, 'MenosAltura'))

        #AUDIOS
        self.ui.DesplegableMusicaRelajante.activated.connect(lambda value: self.on_combo_box_select('pistaRelajante', self.ui.DesplegableMusicaRelajante.currentText()))
        self.ui.ReproducirMusicaRelajante.clicked.connect(partial(self.on_click_button, 'reproducirMusicaRelajante'))
        self.ui.MusicaRelajante_.clicked.connect(lambda value: self.on_click_check_box(value, 'trueAudioRelajante', 'falseAudioRelajante'))
        self.ui.VolumenMusicaRelajante_.sliderMoved.connect(lambda value: self.on_click_slider(value, 'AudioRelajante'))
        self.ui.DesplegableAudioInstrucciones.activated.connect(lambda value: self.on_combo_box_select('pistaInstrucciones', self.ui.DesplegableAudioInstrucciones.currentText()))
        self.ui.ReproducirAudiosInstrucciones.clicked.connect(partial(self.on_click_button, 'reproducirAudiosInstrucciones'))
        self.ui.AudioInstrucciones_.clicked.connect(lambda value: self.on_click_check_box(value, 'trueAudioInstrucciones', 'falseAudioInstrucciones'))
        self.ui.VolumenAudioInstrucciones_.sliderMoved.connect(lambda value: self.on_click_slider(value, 'AudioInstrucciones'))
        self.ui.AudioInstruccionesFinales.clicked.connect(lambda value: self.on_click_check_box(value, 'trueInstruccionesFinales', 'falseInstruccionesFinales'))
        self.ui.VolumenAudioInstruccionesFinales.sliderMoved.connect(lambda value: self.on_click_slider(value, 'InstruccionesFinales'))
        self.ui.ReproducirAudioInstruccionesFinales.clicked.connect(partial(self.on_click_button, 'reproducirInstruccionesFinales'))

        # ESCENAS
        for button in self.escena_buttons:
            button.setStyleSheet("""
                                    QPushButton {
                                        background-color: none;
                                        border: 1px solid gray;
                                    }
                                """)
            button.clicked.connect(self.on_escena_button_clicked)

        #VOTACION
        self.ui.LanzarVot.clicked.connect(partial(self.on_click_button, 'trueVotacion'))
        self.ui.PararVot.clicked.connect(partial(self.on_click_button, 'falseVotacion'))
        self.ui.VotacionErronea.clicked.connect(partial(self.on_click_button, 'votacionErronea'))
        self.ui.VisibilidadRayo.clicked.connect(lambda value: self.on_click_check_box(value, 'trueRayo', 'falseRayo'))

        #ESCENARIOS NEUTROS
        self.ui.AudioEscenariosNeutros_.clicked.connect(lambda value: self.on_click_check_box(value, 'trueAudio', 'falseAudio'))
        self.ui.VolumenEscenariosNeutros_.sliderMoved.connect(lambda value: self.on_click_slider(value, 'volume'))
        self.ui.EscenarioNeutroSalonCasa_.clicked.connect(partial(self.on_click_button, 'SalonCasa.mp4'))
        self.ui.Escenario_Playa_.clicked.connect(partial(self.on_click_button, 'AtardecerPlaya.mp4'))
        self.ui.EscenarioNeutroPlaya2_.clicked.connect(partial(self.on_click_button, 'Playa2.mp4'))
        self.ui.EscenarioNeutroMontana.clicked.connect(partial(self.on_click_button, 'Montana.mp4'))

        #CAPTURAS ESCALERAS AMIGABLES
        self.ui.CapturasAmigables01.clicked.connect(partial(self.on_click_button, 'CapturaAmigable01_1_15.mp4'))
        self.ui.CapturasAmigables02.clicked.connect(partial(self.on_click_button, 'CapturaAmigable02_1_15.mp4'))
        self.ui.CapturasAmigables03.clicked.connect(partial(self.on_click_button, 'CapturaAmigable03_1_15.mp4'))
        self.ui.CapturasAmigables04.clicked.connect(partial(self.on_click_button, 'CapturaAmigable04_1_15.mp4'))
        self.ui.CapturasAmigables05.clicked.connect(partial(self.on_click_button, 'CapturaAmigable05.mp4'))

        #CAPTURAS ESCALERAS
        self.ui.EscenarioCapturaEscaleras01.clicked.connect(partial(self.on_click_button, 'Captura_Exterior_Bajada.mp4'))
        self.ui.EscenarioCapturaEscaleras02.clicked.connect(partial(self.on_click_button, 'Captura_Exterior_Subida.mp4'))
        self.ui.EscenarioCapturaEscaleras03.clicked.connect(partial(self.on_click_button, 'Captura_Ruta_Dentro.mp4'))
        self.ui.EscenarioCapturaEscaleras04.clicked.connect(partial(self.on_click_button, 'Captura_Ruta_Fuera.mp4'))
        self.ui.EscenarioCapturaEscaleras05.clicked.connect(partial(self.on_click_button, 'Captura_Naranjas_Bajada.mp4'))
        self.ui.EscenarioCapturaEscaleras09.clicked.connect(partial(self.on_click_button, 'Captura_Naranjas_Subida.mp4'))
        self.ui.EscenarioCapturaEscaleras06.clicked.connect(partial(self.on_click_button, 'Captura_Grises_Bajada.mp4'))
        self.ui.EscenarioCapturaEscaleras08.clicked.connect(partial(self.on_click_button, 'Captura_Grises_Subida.mp4'))
        self.ui.EscenarioCapturaEscaleras11.clicked.connect(partial(self.on_click_button, 'Captura_Mecanicas_Bajada.mp4'))
        self.ui.EscenarioCapturaEscaleras13.clicked.connect(partial(self.on_click_button, 'Captura_Mecanicas_Subida.mp4'))


        #ESCALERAS INTERIORES GRISES
        self.ui.MasTransparenciaGris.clicked.connect(partial(self.on_click_button, "+"))
        self.ui.MasTransparenciaGrisBaj.clicked.connect(partial(self.on_click_button, "+"))
        self.ui.MasTransparenciaNaranja.clicked.connect(partial(self.on_click_button, "+"))
        self.ui.MasTransparenciaNaranjaBaj.clicked.connect(partial(self.on_click_button, "+"))

        self.ui.MenosTransparenciaGris.clicked.connect(partial(self.on_click_button, "-"))
        self.ui.MenosTransparenciaGrisBaj.clicked.connect(partial(self.on_click_button, "-"))
        self.ui.MenosTransparenciaNaranja.clicked.connect(partial(self.on_click_button, "-"))
        self.ui.MenosTransparenciaNaranjaBaj.clicked.connect(partial(self.on_click_button, "-"))

        self.ui.BarandillaEscalerasInterioresGris_.clicked.connect(lambda value: self.on_click_check_box(value, "trueBarandilla", "falseBarandilla"))
        self.ui.BarandillaInterioresGrisesBaj_.clicked.connect(lambda value: self.on_click_check_box(value, "trueBarandilla", "falseBarandilla"))
        self.ui.BarandillaInterioresNaranjasSub_.clicked.connect(lambda value: self.on_click_check_box(value, "trueBarandilla", "falseBarandilla"))
        self.ui.BarandillaInterioresNaranjasBaj_.clicked.connect(lambda value: self.on_click_check_box(value, "trueBarandilla", "falseBarandilla"))

        #ESCALERAS MECÁNICAS
        self.ui.AudioEscalerasMecanicasSubida_.clicked.connect(lambda value: self.on_click_check_box(value, "trueAudioMec", "falseAudioMec"))
        self.ui.VolumenEscalerasMecanicasSubida_.sliderMoved.connect(lambda value: self.on_click_slider(value, 'AudioMec'))
        self.ui.AudioEscalerasMecanicasBajada_.clicked.connect(lambda value: self.on_click_check_box(value, "trueAudioMec", "falseAudioMec"))
        self.ui.VolumenEscalerasMecanicasBajada_.sliderMoved.connect(partial(self.on_click_slider,'AudioMec'))
        self.ui.StartMecSub_.clicked.connect(partial(self.on_click_button, "Poner en movimiento"))
        self.ui.StartMecBaj_.clicked.connect(partial(self.on_click_button, "Poner en movimiento"))
        self.ui.StopMecSub_.clicked.connect(partial(self.on_click_button, "Parar"))
        self.ui.StopMecBaj_.clicked.connect(partial(self.on_click_button, "Parar"))

        #ESCALERAS BUS
        self.ui.AbrirPuertasBusSub_.clicked.connect(partial(self.on_click_button, 'Abrir Puertas Bus'))
        self.ui.CerrarPuertasBusSub_.clicked.connect(partial(self.on_click_button, 'Cerrar Puertas Bus'))
        self.ui.AbrirPuertasBusBaj_.clicked.connect(partial(self.on_click_button, 'Abrir Puertas Bus'))
        self.ui.CerrarPuertasBusBaj_.clicked.connect(partial(self.on_click_button, 'Cerrar Puertas Bus'))

        if len(self.devices) == 0:
            QMessageBox.information(self, "Meta Quest 2 no encontradas", "Cierra el terminal y repite los pasos de conexión de las gafas al ordenador.")


    def get_device_ip(self, serial):
        template_path = r'../../TemplateTerapiaEscaleras.ini'
        try:
            device = adb.device(serial)
            output = device.shell("ip route")
            match = re.search(r"(\d+\.\d+\.\d+\.\d+)$", output)
            print("Device IP is: " + match.group(1))
            self.load_cfg()
            self.cfg.set('TCP', 'hmd_ip', match.group(1))
            with open(template_path, 'w') as configfile:
                self.cfg.write(configfile)
            return match.group(1) if match else None
        except Exception as e:
            return None

    def load_cfg(self):
        # Then optionally override with TemplateTerapiaEscaleras.ini
        template_path = r'../../TemplateTerapiaEscaleras.ini'
        self.cfg = configparser.ConfigParser()

        if os.path.isfile(template_path):
            self.cfg.read(template_path, encoding="utf-8")
            if self.cfg.has_section('Biosensors'):
                self.phone_ip = self.cfg.get('Biosensors', 'phone_ip') #, fallback=self.phone_ip)

    def actualizarBateria(self):
        if len(self.devices) > 0:
            self.bateria = self.device.shell("dumpsys battery | grep level").split(":")[1]
            #print(self.bateria)
            if (int(self.bateria) < 20):
                self.ui.BateriaGafas.setStyleSheet("color:red;")
            else:
                self.ui.BateriaGafas.setStyleSheet("color:black;")
            self.ui.BateriaGafas.setText(self.bateria+"%")

    def startTimer(self):
        self.timer.start(1000)

    def stopTimer(self):
        self.timer.stop()

    def restartTimer(self):
        self.time = QTime(0, 0, 0)
        self.startTimer()

    def updateLCD(self):
        self.time = self.time.addSecs(1)
        self.ui.LCDNumber.display(self.time.toString("hh:mm:ss"))

    def StartApp(self):
        self.load_cfg()

        hmd_ip = self.cfg.get('TCP', 'hmd_ip', fallback=self.sio.host)
        try:
            self.sio.set_host(hmd_ip, 3001)  # si cambias puerto en el futuro, léelo aquí también
        except Exception as e:
            print(f"[TCP] No se pudo aplicar hmd_ip del template ({hmd_ip}): {e}")

        try:
            if self.cfg.has_section('Paths'):
                if not self.cfg.has_section('Paths'):
                    self.cfg.add_section('Paths')
                for k, v in self.cfg.items('Paths'):
                    self.cfg.set('Paths', k, v)
                print("[CFG] Paths importado del Template para esta sesión.")
        except Exception as e:
            print(f"[CFG] No se pudo importar sección Paths: {e}")

        self.cfg['Defaults']['user_id'] = self.ui.idPaciente.text()
        self.cfg['Defaults']['nsession'] = self.ui.nSesion.text()
        self.cfg['Defaults']['tiempo_votacion'] = self.ui.tiempo_votacion.text()

        if (self.ui.ManoEmpatica.currentIndex() == 0):
            self.cfg['Defaults']['mano'] = 'mano_izquierda'
        elif (self.ui.ManoEmpatica.currentIndex() == 1):
            self.cfg['Defaults']['mano'] = 'mano_derecha'

        localfilepath = os.path.join(os.getcwd(), 'TerapiaEscaleras.ini')
        with open(localfilepath, 'w') as configfile:
            self.cfg.write(configfile)
            #/sdcard/Android/data/com.GTI.BehavioralTherapy_stairs_phobia/files

        if self.ui.idPaciente.text() != "" and self.ui.nSesion.text() != "":
            self.device.sync.push(localfilepath,"/sdcard/Android/data/com.GTI.BehavioralTherapy_stairs_phobia_true/files/TerapiaEscaleras.ini")
            self.device.shell("am force-stop com.GTI.BehavioralTherapy_stairs_phobia_true")
            self.device.shell("am start -n com.GTI.BehavioralTherapy_stairs_phobia_true/com.NokiaBellLabs.LabPackage.MainActivity")

            self.ui.idPaciente.setStyleSheet("QLineEdit{background-color: none}")
            self.ui.nSesion.setStyleSheet("QLineEdit{background-color: none}")

        elif self.ui.idPaciente.text() == "" and self.ui.nSesion.text() != "":
            self.ui.idPaciente.setStyleSheet("QLineEdit{background-color: rgb(255, 196, 196)}")
            self.ui.nSesion.setStyleSheet("QLineEdit{background-color: none}")
        elif self.ui.idPaciente.text() != "" and self.ui.nSesion.text() == "":
            self.ui.idPaciente.setStyleSheet("QLineEdit{background-color: none}")
            self.ui.nSesion.setStyleSheet("QLineEdit{background-color: rgb(255, 196, 196)}")
        else:
            self.ui.idPaciente.setStyleSheet("QLineEdit{background-color: rgb(255, 196, 196)}")
            self.ui.nSesion.setStyleSheet("QLineEdit{background-color: rgb(255, 196, 196)}")

        for button in self.escena_buttons:
            button.setStyleSheet("""
                QPushButton {
                    background-color: none;
                    border: 1px solid gray;
                }
            """)

        self.ui.BarandillaInterioresGrisesBaj_.setChecked(True)
        self.ui.BarandillaEscalerasInterioresGris_.setChecked(True)
        self.ui.BarandillaInterioresNaranjasBaj_.setChecked(True)
        self.ui.BarandillaInterioresNaranjasSub_.setChecked(True)

    def StopApp(self):
        for button in self.escena_buttons:
            button.setStyleSheet("""QPushButton {background-color: none;border: 1px solid gray;}""")

        self.device.shell("am force-stop com.GTI.BehavioralTherapy_stairs_phobia_true")
        self.stopTimer()
        self.guardar_datos()

    def guardar_datos(self):
        remote_logs_dir = "/sdcard/Android/data/datos_sesiones/Logs"
        try:
            self.device.shell(f'mkdir -p "{remote_logs_dir}"')
            print(f"[DEVICE] Asegurada carpeta remota: {remote_logs_dir}")
        except Exception as e:
            print(f"[ERROR] No se pudo crear la carpeta remota {remote_logs_dir}: {e}")

        self.device.shell("cp /sdcard/Android/data/com.GTI.BehavioralTherapy_stairs_phobia_true/files/Result*.txt /sdcard/Android/data/datos_sesiones/Logs/")

        base_dir = os.path.expandvars(
            self.cfg.get('Paths', 'LogsDir', fallback=r'%USERPROFILE%\Documents\Incluverso\Datos_Sesiones')
        )
        dst_evt = os.path.join(base_dir, 'Logs')
        os.makedirs(dst_evt, exist_ok=True)

        root = '/sdcard/Android/data/com.GTI.BehavioralTherapy_stairs_phobia_true/files'
        subprocess.call(f'adb pull "{root}" "{dst_evt}"', shell=True)
        self.device.shell('rm /sdcard/Android/data/com.GTI.BehavioralTherapy_stairs_phobia_true/files/Result*.txt')

    def on_escena_button_clicked(self):
        sender_button = self.sender()

        for button in self.escena_buttons:
            button.setStyleSheet("""QPushButton {background-color: none;border: 1px solid gray;}""")

        sender_button.setStyleSheet("""
            QPushButton {
                background-color: darkgray;
                border: 1px solid gray;
            }
        """)

        if sender_button in [self.ui.Escenario_Playa_,
                             self.ui.EscenarioNeutroMontana,
                             self.ui.EscenarioNeutroSalonCasa_,
                             self.ui.EscenarioNeutroPlaya2_]:
            sender_button.setStyleSheet("""QPushButton {background-color: darkgray;border: 1px solid gray;}""")
            self.ui.EscenariosNeutros_.setStyleSheet("""QPushButton {background-color: darkgray;border: 1px solid gray;}""")

        if sender_button in [self.ui.EscenarioCapturaEscaleras01,
                            self.ui.EscenarioCapturaEscaleras02,
                            self.ui.EscenarioCapturaEscaleras03,
                            self.ui.EscenarioCapturaEscaleras04,
                            self.ui.EscenarioCapturaEscaleras05,
                            self.ui.EscenarioCapturaEscaleras06,
                            self.ui.EscenarioCapturaEscaleras08,
                            self.ui.EscenarioCapturaEscaleras09,
                            #self.ui.EscenarioCapturaEscaleras10,
                            self.ui.EscenarioCapturaEscaleras11,
                            #self.ui.EscenarioCapturaEscaleras12,
                            self.ui.EscenarioCapturaEscaleras13,
                            #self.ui.EscenarioCapturaEscaleras14,
                            #self.ui.EscenarioCapturaEscaleras15,
                            self.ui.CapturasAmigables01,
                            self.ui.CapturasAmigables02,
                            self.ui.CapturasAmigables03,
                            self.ui.CapturasAmigables04,
                            self.ui.CapturasAmigables05]:
            sender_button.setStyleSheet("""
                                    QPushButton {
                                        background-color: darkgray;
                                        border: 1px solid gray;
                                    }
                                """)
            self.ui.Capturas_Escaleras_.setStyleSheet("""
                            QPushButton {
                                background-color: darkgray;
                                border: 1px solid gray;
                            }
                        """)

        if sender_button.objectName() == "EscenariosNeutros_":
            uri = "EscenariosNeutros"
        elif sender_button.objectName() == "Capturas_Escaleras_":
            uri = "CapturasEscaleras"
        elif sender_button.objectName() == "EscalerasInterioresGrises_":
            uri = "EscalerasGrises"
        elif sender_button.objectName() == "EscalerasInterioresGrisesBaj_":
            uri = "EscalerasGrisesBajada"
        elif sender_button.objectName() == "EscalerasInterioresNaranjas_":
            uri = "EscalerasNaranjas"
        elif sender_button.objectName() == "EscalerasInterioresNaranjasBaj_":
            uri = "EscalerasNaranjasBajada"
        elif sender_button.objectName() == "EscalerasMecanicas_":
            uri = "EscalerasMecanicas"
        elif sender_button.objectName() == "EscalerasMecanicasBaj_":
            uri = "EscalerasMecanicasBajada"
        elif sender_button.objectName() == "EscalerasAutobus_":
            uri = "EscalerasBus"
        elif sender_button.objectName() == "EscalerasAutobusBaj_":
            uri = "EscalerasBusBajada"

        self.on_click_button(uri)

    def list_devices(self):
        self.ui.combo_device_.clear()
        items = [i.serial for i in adb.device_list()]
        self.ui.combo_device_.addItems(items)
        return items

    def on_combo_box_select(self, uri, selection):
        self.sio.emit("dr_command", {"group": "oculus1", "uri": ""+uri+selection+"", "tag": "training"})

    def on_click_button(self, uri):
        self.sio.emit("dr_command", {"group": "oculus1", "uri": ""+uri+"", "tag": "training"})
        if uri == "falseVotacion":
            self.ui.VisibilidadRayo.setCheckState(Qt.Checked)


    def on_click_check_box(self, value, uri1, uri2):
        if value == True:
            self.sio.emit("dr_command", {"group": "oculus1", "uri": ""+uri1+"", "tag": "training"})
        else:
            #self.sio.emit(uri2)
            self.sio.emit("dr_command", {"group": "oculus1", "uri": ""+uri2+"", "tag": "training"})

    def on_click_slider(self, slider_value, uri):
        self.sio.emit("dr_command", {"group": "oculus1", "uri": str(slider_value/100) + uri, "tag": "training"})

    def on_init(self):
        self.setWindowTitle(f"Serial: {self.client.device_name}")

    def scrcpy_mirror(self):
        #scrcpy_path = r"C:\Users\Incluverso\Documents\MonitorConductual\py-scrcpy-client\scrcpy-funciona\scrcpy.exe"
        scrcpy_path = r"..\scrcpy-funciona\scrcpy.exe"

        # Argumentos que hacen que funcione la vista de las gafas - Si deja de funcionar, revisar foros
        args = [
            scrcpy_path,
            "--display-id", "0",
            "--crop", "1600:900:68:495"
        ]

        try:
            subprocess.Popen(args)
            print("scrcpy iniciado correctamente con los argumentos.")
        except Exception as e:
            print(f"Error al iniciar scrcpy: {e}")

    def biosensors_mirror(self, timeout=2.0):
        ms = int(timeout * 1000)
        cap = cv2.VideoCapture()

        try:
            cap.setExceptionMode(True)
        except Exception:
            pass

        try:
            opened = cap.open(
                self.SmartPhoneHTTP,
                apiPreference=cv2.CAP_FFMPEG,
                params=[cv2.CAP_PROP_OPEN_TIMEOUT_MSEC, ms],
            )
        except cv2.error as e:
            print("cv2.error al abrir capture:", e)
            try:
                cap.release()
            except Exception:
                pass
            QMessageBox.information(
                self,
                "Móvil no conectado",
                "No se pudo conectar al móvil (error al abrir el stream).\n\n"
                "Asegúrate de que la app de streaming esté abierta y que el teléfono y el PC estén en la misma red Wi-Fi."
            )
            return False

        if not opened and not getattr(cap, "isOpened", lambda: False)():
            try:
                cap.release()
            except Exception:
                pass

            QMessageBox.information(
                self,
                "Móvil no conectado",
                "No se detectó conexión con el móvil (timeout al abrir el stream).\n\n"
                "Asegúrate de que la app de streaming esté abierta y que el teléfono y el PC estén en la misma red Wi-Fi."
            )
            return False

        self.cap = cap

        try:
            ret, frame = self.cap.read()
        except Exception as e:
            print("Error leyendo frame:", e)
            ret = False
            frame = None

        if ret and frame is not None:
            cv2.imshow("Biosensor", frame)
            cv2.waitKey(0)

        # limpieza segura
        try:
            if getattr(self, "cap", None):
                self.cap.release()
        except Exception:
            pass

        return True

    def on_frame2(self, frame):
        app.processEvents() # ANTES COMENTADO
        #print(frame.shape)
        if frame is not None:
            ratio = self.max_width / (1000*1.65)
            #frame =
            image = QImage(
                frame,
                frame.shape[1],
                frame.shape[0],
                frame.shape[1] * 3,
                QImage.Format_BGR888,
            )
            #image = image.copy( 0, 0, 1832, 1920);
            pix = QPixmap(image)
            pix.setDevicePixelRatio(1 / ratio)
            self.ui.label2.setPixmap(pix)
            self.resize(1, 1)


    def on_frame(self, frame):
        app.processEvents()
        if frame is not None:
            ratio = self.max_width / max(self.client.resolution)
            image = QImage(
                frame,
                frame.shape[1],
                frame.shape[0],
                frame.shape[1] * 3,
                QImage.Format_BGR888,
            )
            image = image.copy( 0, 0, 1832, 1920);
            pix = QPixmap(image)
            pix.setDevicePixelRatio(1 / ratio)
            self.ui.label.setPixmap(pix)  # Second QLabel named label2
            self.resize(1, 1)
            if self.frameSmart is not None:
                self.lock.acquire(1)
                self.on_frame2(self.frameSmart)
            self.lock.release()

def main():
    faulthandler.enable()
    parser = ArgumentParser(description="A simple scrcpy client")
    parser.add_argument(
        "-m",
        "--max_width",
        type=int,
        default=800,
        help="Set max width of the window, default 800",
    )
    parser.add_argument(
        "-d",
        "--device",
        type=str,
        help="Select device manually (device serial required)",
    )

    parser.add_argument("--encoder_name", type=str, help="Encoder name to use")
    args = parser.parse_args()

    m = MainWindow(args.max_width, args.device,  args.encoder_name)

    file_ini = os.path.join(os.getcwd(), 'TerapiaEscaleras.ini')

    if os.path.isfile(file_ini):
        import configparser
        configParser = configparser.ConfigParser()
        configFile = configParser.read(file_ini)
        m.ui.idPaciente.setText(configParser['Defaults']['user_id'])
        m.ui.nSesion.setText(configParser['Defaults']['nsession'])
        if (configParser['Defaults']['mano'] == 'mano_izquierda'):
            m.ui.ManoEmpatica.setCurrentIndex(0)
        elif (configParser['Defaults']['mano'] == 'mano_derecha'):
            m.ui.ManoEmpatica.setCurrentIndex(1)
        m.time = m.time.addSecs(int(time.time() - os.path.getctime(file_ini)))
        m.startTimer()

    m.show()

    while m.alive:
        try:
            m.devices = m.list_devices()
            if (len(m.devices) < 1):
                #m.connect_button.setVisible(True)
                #m.ui.label.setText("Gafas no conectadas. Dale al botón y después cierra la interfaz.")
                # QMessageBox.information(m, "HTC XR Elite no encontradas", "Cierra el terminal y repite los pasos de conexión de las gafas al ordenador.")
                app.processEvents()
            else:
                #m.client.start()
                app.processEvents()
            # time.sleep(0.1)
        except Exception as e:
            # print(f"Error: {e}")
            app.processEvents()
            break

    sys.exit(app.exec()) # AÑADIDO POR MI

if __name__ == "__main__":
    main()
