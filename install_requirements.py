import os
import subprocess
import sys

FLAG_FILE = ".requirements_installed"

# Agar pehle install ho chuki hain to dobara install mat karo
if not os.path.exists(FLAG_FILE):

    print("Installing required libraries...")

    subprocess.check_call([
        sys.executable,
        "-m",
        "pip",
        "install",
        "-r",
        "requirements.txt"
    ])

    # Flag file bana do
    with open(FLAG_FILE, "w") as f:
        f.write("Installed")

    print("All libraries installed.")