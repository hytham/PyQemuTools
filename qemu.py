import subprocess
import argparse

parser = argparse.ArgumentParser(description='CLI to deal with qemu')

def convertToCow(image_file_path,file_size=16):      
      cmd ="qemu-img convert -f raw -O qcow2 {} raspbian.qcow".format(image_file_path)
      subprocess.call(cmd,shell=True)
      subprocess.call("qemu-img resize raspbian.qcow +{}G".format(file_size),shell=True)

def emulateRASPI():
      
      qemu ="qemu-system-arm -M versatilepb -display gtk -cpu arm1176 -m 256 -hda raspbian.qcow -dtb versatile-pb-buster.dtb -kernel kernel-qemu-4.19.50-buster -append  \"root=/dev/sda2 panic=1 \" -no-reboot"
      
      print('qemu end with exit code {}'.format(subprocess.call(qemu, shell=True)))

#convertToCow('PiZeroW_withSMBA.img')
emulateRASPI()