import os
import platform
import sys

home = os.path.expanduser("~")

macOS, Windows, Linux = "Darwin", "Windows", "Linux"

if platform.system() != Windows and platform.system() == macOS:
    os.system(
        """osascript -e 'tell application (path to frontmost application as text) to display dialog \
    "Please run script on windows" buttons {"OK"} with icon caution'"""
    )
    sys.exit()
