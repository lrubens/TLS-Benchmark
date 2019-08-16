from scapy.all import *
import matplotlib.pyplot as plt
cipher_list = ["round5_r5n1_1kem_0d", "round5_r5n1_3kem_0d", "round5_r5n1_5kem_0d", "round5_r5nd_1kem_0d", "round5_r5nd_3kem_0d", "round5_r5nd_3kem_5d", "round5_r5nd_5kem_0d", "round5_r5nd_5kem_5d"]
avgList = list()
for cipher in cipher_list:
    with PcapReader('../results/'+ cipher + '.pcap') as pcap_reader:
        synList = list()
        finList = list()
        sum = 0
        for pkt in pcap_reader:
            if TCP in pkt:
                if (pkt[TCP].flags & 0x2) and not (pkt[TCP].flags & 0x10):
                    synList.append(pkt.time)
                if (pkt[TCP].flags & 0x1) and not (pkt[TCP].flags & 0x8):
                    finList.append(pkt.time)
        print(len(finList))
        print(len(synList))
        for i in range(len(finList)):
            sum += finList[i] - synList[i]
        avg = sum/len(synList)
        avgList.append(avg)
    print(cipher + ': ' + str(avg))
plt.bar(cipher_list, avgList)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("graph.png")
plt.clf()
