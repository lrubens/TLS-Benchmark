from scapy.all import *
import matplotlib.pyplot as plt
cipher_list = ['round5_r5nd_5ccakem_5d', 'round5_r5nd_5kem_0d', 'round5_r5nd_1kem_0d', 'round5_r5nd_0kem_2iot', 'round5_r5nd_1kem_4longkey', 'round5_r5n1_3ccakem_0d', 'round5_r5nd_5ccakem_0d', 'round5_r5n1_5kem_0d', 'round5_r5n1_1kem_0d', 'round5_r5n1_3kem_0d', 'round5_r5nd_1kem_5d', 'round5_r5nd_5kem_5d', 'round5_r5nd_3kem_0d', 'round5_r5nd_3kem_5d', 'round5_r5nd_3ccakem_5d', 'round5_r5n1_5ccakem_0d', 'round5_r5nd_1ccakem_0d', 'round5_r5nd_1ccakem_5d', 'round5_r5n1_1ccakem_0d', 'round5_r5nd_3ccakem_0d']
name_list = ['r5nd_5ccakem_5d', 'r5nd_5kem_0d', 'r5nd_1kem_0d', 'r5nd_0kem_2iot', 'r5nd_1kem_4longkey', 'r5n1_3ccakem_0d', 'r5nd_5ccakem_0d', 'r5n1_5kem_0d', 'r5n1_1kem_0d', 'r5n1_3kem_0d', 'r5nd_1kem_5d', 'r5nd_5kem_5d', 'r5nd_3kem_0d', 'r5nd_3kem_5d', 'r5nd_3ccakem_5d', 'r5n1_5ccakem_0d', 'r5nd_1ccakem_0d', 'r5nd_1ccakem_5d', 'r5n1_1ccakem_0d', 'r5nd_3ccakem_0d']
avgList = list()
double_fin = False
for cipher in cipher_list:
    with PcapReader('../results/'+ cipher + '.pcap') as pcap_reader:
        synList = list()
        finList = list()
        sum = 0
        for pkt in pcap_reader:
            if TCP in pkt:
                if (pkt[TCP].flags & 0x2) and not (pkt[TCP].flags & 0x10):
                    synList.append(pkt.time)
                    double_fin = False
                if (pkt[TCP].flags & 0x1) and not (pkt[TCP].flags & 0x8):
                    if(double_fin):
                        finList[len(finList) - 1] = pkt.time
                    else:
                        finList.append(pkt.time)
                        double_fin = True
        print(len(finList))
        print(len(synList))
        #print(cipher + 'Synlist:', synList)
        #print(cipher + 'Finlist:', finList)
        for i in range(len(synList)):
            sum += finList[i] - synList[i]
        avg = sum/len(synList)
        avgList.append(avg * 1000)
    print(cipher + ': ' + str(avg))
plt.bar(name_list, avgList)
plt.ylabel("milliseconds")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("graph2.png")
plt.clf()
