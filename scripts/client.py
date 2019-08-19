#!/usr/bin/env python3

# Import of python system library.
import os
import subprocess
import shutil
import time
import pip

num_attempts = 200

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

try:
            from scapy.all import *
except:
            install("scapy")

def run_client():
    try:
        os.mkdir('../openssl/results')
    except:
        pass
    cipher_lst = ['round5_r5nd_5ccakem_5d', 'round5_r5nd_5kem_0d', 'round5_r5nd_1kem_0d', 'round5_r5nd_0kem_2iot', 'round5_r5nd_1kem_4longkey', 'round5_r5n1_3ccakem_0d', 'round5_r5nd_5ccakem_0d', 'round5_r5n1_5kem_0d', 'round5_r5n1_1kem_0d', 'round5_r5n1_3kem_0d', 'round5_r5nd_1kem_5d', 'round5_r5nd_5kem_5d', 'round5_r5nd_3kem_0d', 'round5_r5nd_3kem_5d', 'round5_r5nd_3ccakem_5d', 'round5_r5n1_5ccakem_0d', 'round5_r5nd_1ccakem_0d', 'round5_r5nd_1ccakem_5d', 'round5_r5n1_1ccakem_0d', 'round5_r5nd_3ccakem_0d']
    for cipher in cipher_lst:
        tcpdump = subprocess.Popen(['tcpdump', '--time-stamp-precision', 'nano', '-i', 'eth0', '-w', '../openssl/results/{}.pcap'.format(cipher)], stdout=subprocess.PIPE)
        time.sleep(2)
        print("Running measurements...")
        for i in range(num_attempts):
            os.system('echo hi | ../openssl/apps/openssl s_client -connect server:4433 -curves {} -tls1_3'.format(cipher))
        time.sleep(5)
        tcpdump.terminate()

def main():
    run_client()

if __name__ == "__main__":
    main()
