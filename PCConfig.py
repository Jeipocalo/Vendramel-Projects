import platform
import socket
import psutil
import cpuinfo
import wmi
from getmac import get_mac_address as gma
import datetime

#Information Collection
osname = platform.system()
osrelease = platform.release()
host_name = socket.gethostname()
ip_address = socket.gethostbyname(host_name)
osfull = osname + " " + osrelease
mac = gma()
memory_info = psutil.virtual_memory()
memory = memory_info.total / (1024 ** 3)
memory = round(memory, 2)
memory = str(memory) + "GB"
info = cpuinfo.get_cpu_info()
cpu_name = info['brand_raw']
cpu_freq = (info['hz_advertised'][0])/(10 ** 9)
cpu_freq = round(cpu_freq, 2)
cpufull = cpu_name + " " + str(cpu_freq) + "GHz"
infoHD = ""

c = wmi.WMI()

for physical_disk in c.Win32_DiskDrive():
    model_name = physical_disk.Model
    infoHD = infoHD + " " + "(" + str(model_name)

    total_disk_size = int(physical_disk.Size)
    total_disk_size_gb = total_disk_size / (1024 ** 3)
    total_disk_size_gb = round(total_disk_size_gb, 2)

    infoHD = infoHD + " | " + str(total_disk_size_gb) + "GB" + ")"

date = str(datetime.datetime.now())
date = date[: -10]
#________________________________________________________________
#Exporting to txt file
output_file = "systeminfo.txt"

with open(output_file, "w") as file:

    file.write("System Info:\n")
    file.write("Operational System: " + osfull + "\n")
    file.write("Host Name: " + host_name + "\n")
    file.write("IP Address: " + ip_address + "\n")
    file.write("MAC Address: " + mac + "\n\n")

    file.write("Hardware Info:\n")
    file.write("CPU: " + cpufull + "\n")
    file.write("RAM Memory: " + memory + "\n")
    file.write("Hard Disk Info: " + infoHD + "\n\n")

    file.write("Last Updated: " + date + "\n")

print("File exported to ", output_file)