@echo off
if (pip install . && echo 'successfuly install pywhatkit') else if (easy_install pip && pip install . && echo 'successfuly installed pywhatkit') else (echo 'Unable to install' )
exit
