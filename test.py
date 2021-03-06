'''
This is a test file to check if
every module works.

This file prints some useful system
information for DEBUGGING purposes only
and it would help the author in fixing
specific problems with the code...

This information will not individually identify
the user and will cannot be used for any other
purpose other than fixing errors and mistakes.
'''
from __future__ import print_function
import platform
import proxy_conf
print()


# Python 2.x incompatibility
if int(platform.python_version_tuple()[0]) < 3:
    print("This script is NOT compatible with Python 2.x")
    print("Use this command to run the script:\n")
    print("python3 test.py\n")
    print("*"*30 + "\n" + "\tTEST FAILED" + "\n" + "*"*30)
    quit()

if platform.system() not in ['Linux', 'Darwin']:
    print("Looks like you are not running on GNU/Linux or a Mac")
    print("If this test is successful then you can run: ")
    print("\npython3 sci_hub.py\n")

try:
    import argparse
    import os
    import re
    import time
    import webbrowser
except(ImportError):
    print("Either argparse, os platform, time, webbrowser"
          + "or re could not be imported")
    quit()

try:
    from bs4 import BeautifulSoup as bs
    import requests
except(ImportError):
    print("Either requests or BeautifulSoup could not be imported")
    quit()

print('''
This file prints some useful system
information for DEBUGGING purposes only
and it would help the author in fixing
specific problems with the code...

This information will not individually identify
the user and will not be used for any other
purpose other than fixing errors and mistakes.

By choosing to share the output of this
program, the user explicitly consents the
author to use the output of this program
for fixing errors and understands that the
information will not be used for any other
purpose other than what is said.
''')

time.sleep(15)


parser = argparse.ArgumentParser(description="The most useless python script \
                                              written by me")
parser.add_argument("target", help="enter any random URL")
args = parser.parse_args()

print("\n" + "*"*50 + "\n" + "YOUR TEST IS ALREADY SUCCESSFUL")
print("The next output is for debugging purposes :/\n")
print("You can safely ignore it if you don't have problems\n" + "*"*50 + "\n")
time.sleep(5)

print(proxy_conf.proxies)
print()

print(os.listdir("./"))
print()
print(platform.uname())
print()

print(args)
response = requests.get(args.target)
if response.status_code == requests.codes.ok:
    try:
        soup = bs(response.content, "lxml")
    except Exception:
        print("Check is lxml parser is installed")
    print(soup.title.text)
else:
    print("Something happened")

if re.match("oir", "air"):
    print("yes")

print("\nNow your default web browser will open")
print("Don't be scared, I haven't hacked your computer :P\n")
print("If it doesn't then try setting a default browser"
      + " for the script to work properly")
time.sleep(2)
print(webbrowser.open_new("https://google.com"))
