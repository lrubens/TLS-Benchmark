#!/usr/bin/env python3

# Import of python system library.
import os
import subprocess
import shutil
import time
try:
	from scapy.all import *
except:
	os.system('pip3 install scapy')

num_attempts = 50


def run_client():
    try:
        os.mkdir('../openssl/results')
    except:
        pass
    cipher_lst = ["round5_r5n1_1kem_0d", "round5_r5n1_3kem_0d", "round5_r5n1_5kem_0d", "round5_r5nd_1kem_0d", "round5_r5nd_3kem_0d", "round5_r5nd_3kem_5d", "round5_r5nd_5kem_0d", "round5_r5nd_5kem_5d"]
    for cipher in cipher_lst:
        open('../openssl/results/{}.pcap'.format(cipher), 'a').close()
        tcpdump = subprocess.Popen(['tcpdump', '--time-stamp-precision', 'nano', '-i', 'eth0', '-w', '../openssl/results/{}.pcap'.format(cipher)], stdout=subprocess.PIPE)
        time.sleep(2)
        print("Running measurements...")
        for i in range(num_attempts):
            print("Attempt # {}".format(i))
            os.system('echo hi | ../openssl/apps/openssl s_client -connect server:4433 -curves {} -tls1_3'.format(cipher))
        #os.system("tshark -F pcap -r " + cipher + ".pcap"  + " -w " + cipher + ".pcap")
        time.sleep(1)
        tcpdump.terminate()

def main():
    run_client()

if __name__ == "__main__":
    main()

        

