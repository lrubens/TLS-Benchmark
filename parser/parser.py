#this file generates a graph using the data from results

from scapy.all import *
import matplotlib.pyplot as plt
kem_list = ['r5nd_1kem_0d', 'r5nd_0kem_2iot', 'r5nd_1kem_5d', 'r5nd_5kem_0d', 'r5nd_1kem_4longkey', 'r5nd_3kem_5d', 'r5n1_3kem_0d', 'r5n1_1kem_0d', 'r5n1_5kem_0d', 'r5nd_3kem_0d', 'r5nd_5kem_5d']
ccakem_list = ['r5nd_5ccakem_0d', 'r5nd_3ccakem_0d', 'r5nd_5ccakem_5d', 'r5nd_1ccakem_5d', 'r5nd_1ccakem_0d', 'r5n1_3ccakem_0d', 'r5nd_3ccakem_5d', 'r5n1_5ccakem_0d', 'r5n1_1ccakem_0d']
avgList = list()
double_fin = False
list_list = [kem_list, ccakem_list]
list_list1 = ['kem_list', 'ccakem_list']
count = 0
for ciphers in list_list:
    avgList = list()
    for cipher in ciphers:
        cipher = 'round5_' + cipher	
        with PcapReader('./results/'+ cipher + '.pcap') as pcap_reader:
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
    plt.barh(list_list[count], avgList, align='center')
    plt.xlabel("milliseconds")
    # plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig(list_list1[count] + "1.png")
    count += 1
    plt.clf()
