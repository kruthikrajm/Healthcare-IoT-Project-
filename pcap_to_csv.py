# from scapy.all import rdpcap, IP, TCP, UDP
# import pandas as pd


# pcap_file = "captures/live_simulation.pcap"

# print("Reading PCAP file...")

# packets = rdpcap(pcap_file)

# data = []


# for pkt in packets:

#     if IP in pkt:

#         row = {}

#         row["src_ip"] = pkt[IP].src
#         row["dst_ip"] = pkt[IP].dst
#         row["length"] = len(pkt)
#         row["protocol"] = pkt[IP].proto


#         if TCP in pkt:
#             row["src_port"] = pkt[TCP].sport
#             row["dst_port"] = pkt[TCP].dport


#         elif UDP in pkt:
#             row["src_port"] = pkt[UDP].sport
#             row["dst_port"] = pkt[UDP].dport


#         else:
#             row["src_port"] = 0
#             row["dst_port"] = 0


#         data.append(row)



# df = pd.DataFrame(data)


# output_file = "captures/live_simulation1.csv"

# df.to_csv(
#     output_file,
#     index=False
# )


# print("PCAP converted successfully")
# print("Saved:", output_file)
# print(df.head())
# print("Shape:", df.shape)
#------------------------------------------------final
from scapy.all import rdpcap, IP, TCP, UDP
import pandas as pd


pcap_file = "/home/vboxuser/captures/hiot.pcap"

output_file = "/home/vboxuser/captures/packet_data.csv"


print("Reading PCAP...")

packets = rdpcap(pcap_file)


data = []


for pkt in packets:


    if IP not in pkt:
        continue


    row = {}

    row["time"] = float(pkt.time)

    row["src_ip"] = pkt[IP].src

    row["dst_ip"] = pkt[IP].dst

    row["length"] = len(pkt)

    row["protocol"] = pkt[IP].proto



    # TCP

    if TCP in pkt:

        row["src_port"] = pkt[TCP].sport

        row["dst_port"] = pkt[TCP].dport



    # UDP

    elif UDP in pkt:

        row["src_port"] = pkt[UDP].sport

        row["dst_port"] = pkt[UDP].dport



    # ICMP

    else:

        row["src_port"] = 0

        row["dst_port"] = 0



    data.append(row)



df = pd.DataFrame(data)



df.to_csv(
    output_file,
    index=False
)



print("\nPacket CSV generated")

print("Location:")
print(output_file)

print("\nShape:")
print(df.shape)

print(df.head())