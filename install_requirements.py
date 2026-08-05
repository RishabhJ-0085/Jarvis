import subprocess
import sys
import os

FLAG_FILE = ".requirements_installed"

# Agar pehle install ho chuki hain to dobara install mat karo
if os.path.exists(FLAG_FILE):
    with open("Install_requirements.txt",'r') as New_lib:
        New_lib = New_lib.read().splitlines()
        with open("requirements.txt",'r') as old_lib:
            Old_lib = old_lib.read().splitlines()
            New_set = set(New_lib)         
            Old_set = set(Old_lib)
            missing = New_set - Old_set
            for i in missing:
                print("Installing required libraries...")
                subprocess.check_call([
                    sys.executable,
                    "-m",
                    "pip",
                    "install",
                    i
                ])
                with open("requirements.txt",'a') as old_lib:
                    old_lib.write(i+'\n')
    print("All libraries installed.")
else:
    print("Installing required libraries...")
    subprocess.check_call([
        sys.executable,
        "-m",
        "pip",
        "install",
        "-r",
        "install_requirements.txt"
    ])
    with open(FLAG_FILE, "w") as f:
        f.write("Installed")
    with open("Install_requirements.txt",'r') as New_lib:
        New_lib = New_lib.read().splitlines()
        with open('requirements.txt', 'w') as fill:
            for i in New_lib:
                fill.write(i+'\n')
    print("All libraries installed.")