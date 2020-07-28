import os
import platform
import sys

home = os.path.expanduser('~')

if platform.system() != 'Windows':
    os.system("""osascript -e 'tell application (path to frontmost application as text) to display dialog "Please run script on windows" buttons {"OK"} with icon caution'""")
    sys.exit()
