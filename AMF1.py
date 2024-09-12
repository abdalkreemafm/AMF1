import os
def menu():
    print("""                               
=======================================                             Today we will prove the basics in termux
=======================================
=======================================
Telegram:@Professionaltermux
=======================================                          Choose a number
_______________________________________________
1.The basics Termux
_______________________________________________
00.Exit 
_______________________________________________""")

loop = True
while loop:
    menu()
    what = input("AMF#: ")
    if what == "1":
        print("===================================")
        print("----------------")
        hm = input("[?] Do you want to continue? (y/n): ")
        print("================================")
        if hm == "y":
            print("========================================================")
            print("[+] Please put down you android and go to the toilet...")
            print("Because this will take a long time.")
            print("========================================================")
            os.system("apt-get update -y")
            os.system("apt-get upgrade -y")
            os.system("apt-get install python -y")
            os.system("apt-get install python2 -y")
            os.system("apt-get install python3 -y")
            os.system("apt-get install ruby -y")
            os.system("apt-get install git -y")
            os.system("apt-get install php -y")
            os.system("apt-get install nano -y")
            os.system("apt-get install nmap -y")
            os.system("apt-get install perl -y")
            os.system("termux-setup-storage -y")
            os.system("apt-get install golang -y")
            os.system("apt-get install host -y")
            os.system("apt-get install havij -y")
            os.system("apt-get install hydra -y")
            os.system("apt install wireshark -y")
            os.system("apt-get install cmatrix -y")
            os.system("apr-get install figlet -y")
            os.system("apt-get install wget -y")
            os.system("apt-get install wget -y")
            os.system("apt-get install python2 -y")
            os.system("apt-geg install python2-dev -y")
            os.system("apt install wireshark -y")
            os.system("apt-get install cowsay -y")
            os.system("apt-get install toilet -y")
            os.system("apt-get install curlinstall wgetrc -y")
            os.system("apt-get install ruby -y")
            os.system("apt-get install help -y")
            os.system("apt-get install net-tools -y")
            os.system("apt-get install w3m -y")
            os.system("apt-get install unrar -y")
            os.system("apt-get install clang -y")
            os.system("apt-get install openssh -y")
            os.system("apt-get install tor -y")
            os.system("apt-get install tar -y")
            os.system("apt-get install zip -y")
            os.system("apt-get install proot -y")
            os.system("pip2 install wget -y")
            os.system("pip2 install requests -y")
            os.system("gem install lolcat -y")
            os.system("apt update -y && apt upgrade -y")
            os.system("clear")
            print("====================================")
            print("[+] routersploit installed successfully :)")
            print("[+] Go to routersploit folder and type 'python2 rsf.py' to start.")
            print("====================================")
            print("====================================")
            print("[+] Useful commands in Termux:")
            print("   - `pkg update` and `pkg upgrade`: Keep your system updated.")
            print("   - `ls`: List files and directories.")
            print("   - `cd`: Change directory.")
            print("   - `mkdir`: Create a new directory.")
            print("   - `rm`: Remove files or directories.")
            print("   - `mv`: Move or rename files or directories.")
            print("   - `cp`: Copy files or directories.")
            print("   - `clear`: Clear the screen.")
            print("   - `pwd`: Show the current working directory.")
            print("   - `exit`: Exit the Termux session.")
            print("====================================")
            print("[+] Additional Useful commands in Termux:")
            print("   - `apt-get install <package>`: Install a package.")
            print("   - `apt-get remove <package>`: Uninstall a package.")
            print("   - `apt-get search <keyword>`: Search for packages.")
            print("   - `apt-get list`: List all installed packages.")
            print("   - `termux-setup-storage`: Configure storage access.")
            print("   - `termux-info`: Display information about Termux.")
            print("====================================")
            print("[+] Install RouterSploit and it's requirements:")
            print("   - `cd routersploit`")
            print("   - `pip2 install -r requirements-dev.txt`")
            print("   - `pip2 install -r requirements.txt`")
            print("   - `pip2 install requests`")
            print("   - `python2 rsf.py`")
            rmenu = input("[?] Back to Menu? (y/n): ")
            if rmenu == "y":
                menu()
            else:
                break
    elif what == "00":
        break
