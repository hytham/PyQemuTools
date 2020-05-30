import subprocess
import argparse

qemu = "qemu-system-arm -M versatilepb -display gtk -cpu arm1176 -m 256 -hda raspbian.qcow -dtb versatile-pb-buster.dtb -kernel kernel-qemu-4.19.50-buster -append  \"root=/dev/sda2 panic=1 \" -no-reboot"

print('qemu end with exit code {}'.format(subprocess.call(qemu, shell=True)))