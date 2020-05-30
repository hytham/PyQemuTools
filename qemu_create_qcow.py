import subprocess
import argparse

qcow_file_name='raspbian.qcow' # the qow file name
image_file_name='PiZeroW_withSMBA.img' # the image file name

cmd ="qemu-img convert -f raw -O qcow2 {} raspbian.qcow".format(image_file_name)
subprocess.call(cmd,shell=True)