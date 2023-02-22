@echo off
pip install pyinstaller
pip install sockets
pip install requests
pip install pillow
pip install discord.py
pyinstaller -F -w -i Jusky_logo.ico rdp_s_discord.py

rmdir /s /q __pycache__
rmdir /s /q build

:cmd
pause null