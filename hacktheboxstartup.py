import virtualbox
import os

vbox = virtualbox.VirtualBox()

for m in vbox.machines:
    print(m.name)

session = virtualbox.Session()
machine = vbox.find_machine("kali 64 bit")
progress = machine.launch_vm_process(session, "gui", [])
progress.wait_for_completion()

file = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
os.system('"' + file + '"' + ' ' + 'onenote.com')
os.system('"' + file + '"' + ' ' + 'app.hackthebox.com')
file2 = "C:\\Program Files (x86)\\Notepad++\\notepad++.exe"
os.system('"' + file2 + '"')