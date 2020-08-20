#!/usr/bin/python
import ctypes
import os
import subprocess
import sys

'''
Virtualbox and WSL2 can not be run together this 
script will allow to switch between running virtualbox and wsl2  
by running all the necessary commands for you. Only works on windows.

Does not check if your computer currently meets minimum requirements for wsl
'''


def reboot_windows():
    print('Rebooting...')
    os.system('shutdown -t 0 -r -f')


def enable_virtualbox():
    subprocess.call('powershell.exe bcdedit /set hypervisorlaunchtype off', shell=True)
    subprocess.call(
        'powershell.exe dism.exe /online /disable-feature /featurename:Microsoft-Windows-Subsystem-Linux /norestart',
        shell=True)
    subprocess.call('powershell.exe dism.exe /online /disable-feature /featurename:VirtualMachinePlatform /norestart',
                    shell=True)
    reboot_windows()


def enable_wsl2():
    subprocess.call('powershell.exe bcdedit /set hypervisorlaunchtype auto', shell=True)
    subprocess.call(
        'powershell.exe dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart',
        shell=True)
    subprocess.call(
        'powershell.exe dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart',
        shell=True)
    subprocess.call('powershell.exe wsl --set-default-version 2', shell=True)
    reboot_windows()


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def main():
    if is_admin():
        answer = input('VirtualBox or WSL2?: ')
        if 'vi' in answer.lower():
            print('enabling virtualbox')
            enable_virtualbox()
        elif 'wsl' in answer.lower():
            print('enabling wsl2')
            enable_wsl2()
        else:
            print('Unknown Command')
    else:
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)


if __name__ == '__main__':
    if sys.platform == 'win32':
        main()
