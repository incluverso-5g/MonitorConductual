#!/bin/bash
#ipHMD='138.4.33.61'

#.ini file
iniFile='../TemplateterapiaEscaleras.ini'

#ip HMD
ipHMD=$(awk -F'=' '/\[TCP\]/{flag=1;next}/\[/{flag=0}flag && /hmd_ip/{gsub(/ /,"",$2);print $2}' "$iniFile")

#Conectar gafas a ordenador por adb
read -n 1 -s -r -p "Porfavor, CONECTA las Meta Quest 2 con el cable USB al ordenador. Una vez conectadas, presiona cualquier tecla"
echo -e "\n"

adb tcpip 5555
adb connect $ipHMD:5555

echo "Gafas conectadas"
sleep 5
