read -n 1 -s -r -p "Please, CONNECT the HMD using the USB. Once connected press any key to continue"
adb tcpip 5555
adb connect 192.168.1.250:5555
read -n 1 -s -r -p "Please, DISCONNECT the HMD using the USB. Once disconnected press any key to continue"
./scrcpy.exe --tcpip=192.168.1.250:5555 -n --video-bit-rate 5M --crop 2000:2100:1864:100 --max-fps=50

