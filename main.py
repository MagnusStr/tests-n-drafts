import time
import os
import wget
from storage import Storage
from webmodule import Webmodule
 
web = Webmodule()
files = Storage()        
if(files.checar_links() == False):
    files.criar_lista()


print("Baixando programas\n")
web.download_apps() 
if (web.checar_winget() == True):
    print("Winget instalado na máquina!\n")
    print("Ao fim das instalações o winget atualizará todos os pacotes ;)")
    time.sleep(390)
    os.system('cmd /k"winget upgrade --all"')
    print("Todos os pacotes foram atualizados")
else:
    print("Winget não instalado na máquina\n")
    print("Baixando winget!\n")
    url = "https://github.com/microsoft/winget-cli/releases/download/v1.4.10173/Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle"
    wget.download(url)
   

