como lo ves como un readme?
# Interfaz de Control - Terapia Conductual

Interfaz para el control y monitoreo de sesiones de terapia conductual.

---

## Requisitos

- **Python**: 3.8.10  ([Descargar Python 3.8.10](https://www.python.org/downloads/release/python-3810/))
- **Dispositivos**: 
    - Meta Quest 2
    - Dispositivo móvil Android (En este caso se ha usado un Samsung Galaxy A8)
- **Aplicación en el móvil**: 
    - [ScreenStream](https://play.google.com/store/apps/details?id=info.dvkr.screenstream&hl=es)
    - [Empática Care](https://play.google.com/store/apps/details?id=com.empatica.healthmonitor.lab&hl=es_419)
    
---

## Instalación

1. Clonar o descargar este repositorio:

```shell
git clone https://git.gti.ssr.upm.es/mgm/monitorconductual
cd py-scrcpy-client
```

2. Instalar los requirements
```shell
pip install -r requirements.txt
```

---

## Fichero de configuración

**Asegúrate de editar este archivo antes de iniciar la aplicación.**

../TemplateTerapiaEscaleras.ini

Hay que incluir: 
- [TCP] hmd_ip: Dirección IP de las gafas XR (puedes obtenerla con: *adb shell ip route*)
- [Biosensors] phone_ip: Dirección IP del móvil al que están conectados los biosensores
- [Offloading] ip: Dirección IP del ordenador
- [Paths] LogsDir: Path donde se quieran guardar los datos de las sesiones

---

## Inicio de la app

Dos posibles formas

1. Con el script

```shell
Open_app.sh
```

1. Con línea de comandos

```shell
cd scrcpy_ui #Si no entras dentro de este directorio no va a funcionar la interfaz
python main.py
```
---

## Control interfaz

1. Incluir ID del paciente y Nº de sesión y pulsar botón *EMPEZAR APLICACIÓN*
2. Una vez inicializada la aplicación se puede controlar
    - Lanzamiento audio
    - Lanzamiento vídeo 360º
    - Lanzamiento de escenas virtuales
    - Control de parámetros dentro de las escenas virtuales (El control es una vez que se haya lanzado)
    - Lanzamiento de escena de votación
3. Cuando la sesión esté finalizada, pulsar botón *PARAR APLICACIÓN*

---

## Vista HMD

### Conexión del HMD al ordenador

**HMD y ordenador están en el mismo Wi-Fi.**

Dos posibles formas:

1. Con el script

```shell
Connect_HMD_adb.sh
```

2. Con línea de comandos
```shell
adb tcpip 5555
adb connect ipHMD:5555 #ipHMD es del estilo: xxx.xx.xx.xx
```

### Vista en la interfaz

En la aplicación pulsar el botón **Ver vista gafas (HMD)**

---

## Vista bio-sensores

*En nuestro caso Empatica Embrace Plus*

### Inicializar bio-sensores

1. Instalar aplicación Empatica Care en el móvil
2. Seguir las instrucciones para emparejar la pulsera de este [link](https://support.empatica.com/hc/en-us/articles/13681477919261-Pairing-your-Empatica-Wearable)

### Inicio aplicación ScreenStream en el móvil

1. Habilitar Modo local (MJPEG)
2. Guardar IP del móvil, en la aplicación es *Wi-Fi (IPv4 pública)*
3. Dar al botón de *Iniciar transmisión*
4. Abrir la aplicación Empática Care y transmite los datos de la pulsera

### Vista en la interfaz

En la aplicación pulsar el botón **Ver vista biosensores (móvil)**

