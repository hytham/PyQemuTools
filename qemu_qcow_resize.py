import subprocess
import argparse

file_size = 16

subprocess.call("qemu-img resize raspbian.qcow +{}G".format(file_size),shell=True)