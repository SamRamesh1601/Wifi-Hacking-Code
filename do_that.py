import subprocess as s
import ctypes , os , sys
from subprocess import Popen  ,DEVNULL 

# # s.check_call([sys.executable,"net","user","administrator","/active:yes"])
# # s.check_call([sys.executable,"net","user","administrator","/active:no"])
# s.call("netsh.exe advfirewall set publicprofile state off")

def check_Admin():
    try:
        ctypes.windll.shell32.isUserAnAdmin()
    except AttributeError:
        isAdmin = False
    if not isAdmin:
        ctypes.windll.shell32.ShellExecuteW(None,"runas",sys.executable,__file__,None,1)

def addRule(rule_name, file_path):
    s.check_call('netsh advfirewall add rule name='+rule_name+" dir=out action=block enable=no program="+file_path,shell = True ,  stdout = DEVNULL ,  stderr= DEVNULL)

def modifyRule(rule_name , state):
    if state:
        # s.call()
        s.check_call("netsh.exe advfirewall set rule name="+rule_name+" new enable=yes ",shell = True ,  stdout = DEVNULL ,  stderr= DEVNULL)
        print("Rule ",rule_name,"Enabled ")
    else:
        s.check_call("netsh.exe advfirewall set rule name="+rule_name+" new enable=no ",shell = True ,  stdout = DEVNULL ,  stderr= DEVNULL)
        print("Rule ",rule_name," Disabled ")

check_Admin()
addRule("Rule Name","path to file ")
modifyRule("Rule Name",1)