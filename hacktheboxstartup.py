import virtualbox
import os
import time
import sys

vbox = virtualbox.VirtualBox()

for m in vbox.machines:
    print(m.name)
print("opening kali 64 bit VM")
session = virtualbox.Session()
machine = vbox.find_machine("kali 64 bit")
progress = machine.launch_vm_process(session, "gui", [])
progress.wait_for_completion()

file = '\"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe\"'
print(file)
print("opening onenote")
chromecommand = f"{file} onenote.com"
os.system(chromecommand)
print("onenote opened")
print("opening hackthebox.com")
time.sleep(5)
hacktheboxcommand = f"{file} app.hackthebox.com"
os.system(hacktheboxcommand)
print("hackthebox opened")
print("opening notepad++")
time.sleep(5)
os.system('"C:\\Program Files (x86)\\Notepad++\\notepad++"')
print (notepad++ opened)
time.sleep(5)
sys.exit()