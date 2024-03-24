# import subprocess
# def get_default_browser():
#     command = 'powershell -Command "$defaultBrowser = (Get-ItemProperty \'HKCU:\\Software\\Microsoft\\Windows\\Shell\\Associations\\UrlAssociations\\http\\UserChoice\').ProgId; switch ($defaultBrowser) { \'FirefoxURL\' { \'Firefox\' }; \'ChromeHTML\' { \'Google Chrome\' };{ \'Google Chrome\' }; default { \'Unknown\' } }"'
#     result = subprocess.run(command, stdout=subprocess.PIPE, shell=True)
#     print(result.stdout.decode('utf-8').strip())
#     return result.stdout.decode('utf-8').strip()
# get_default_browser()
# import subprocess

# def get_default_browser():
#     command = 'powershell -Command "$defaultBrowser = (Get-ItemProperty \'HKCU:\\Software\\Microsoft\\Windows\\Shell\\Associations\\UrlAssociations\\http\\UserChoice\').ProgId; switch ($defaultBrowser) { \'FirefoxURL\' { \'Firefox\' }; \'ChromeHTML\' { \'Google Chrome\' }; \'MSEdgeHTM\' { \'Microsoft Edge\' }; default { \'Unknown\' } }"'
#     result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    
#     if result.returncode != 0:
#         print("Error executing PowerShell command:")
#         print(result.stderr.decode('utf-8').strip())
#         return None
    
#     output = result.stdout.decode('utf-8').strip()
#     print(output)
#     return output
# def set_frontmost_process(app_name):
#     applescript = f'tell application "System Events" to set frontmost of process "{app_name}" to true'
#     subprocess.run(['osascript', '-e', applescript])
# # Test the function
# default_browser=get_default_browser()
# set_frontmost_process(default_browser)

# import subprocess

# def get_default_browser():
#     command = 'powershell -Command "$defaultBrowser = (Get-ItemProperty \'HKCU:\\Software\\Microsoft\\Windows\\Shell\\Associations\\UrlAssociations\\http\\UserChoice\').ProgId; Write-Output $defaultBrowser;"'
#     result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    
#     if result.returncode != 0:
#         print("Error executing PowerShell command:")
#         print(result.stderr.decode('utf-8').strip())
#         return None
    
#     output = result.stdout.decode('utf-8').strip()
#     print("Output:", output)
#     return output

# # Test the function
# get_default_browser()




# import subprocess
# import win32gui

# def get_default_browser():
#     command = 'powershell -Command "$defaultBrowser = (Get-ItemProperty \'HKCU:\\Software\\Microsoft\\Windows\\Shell\\Associations\\UrlAssociations\\http\\UserChoice\').ProgId; switch ($defaultBrowser) { \'FirefoxURL\' { \'Firefox\' }; \'ChromeHTML\' { \'Google Chrome\' }; \'MSEdgeHTM\' { \'Microsoft Edge\' }; default { \'Unknown\' } }"'
#     result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    
#     if result.returncode != 0:
#         print("Error executing PowerShell command:")
#         print(result.stderr.decode('utf-8').strip())
#         return None
    
#     output = result.stdout.decode('utf-8').strip()
#     return output

# def set_frontmost_process(app_name='chrome'):
#     # Find the window handle of the application
#     handle = win32gui.FindWindow(None, app_name)
    
#     if handle == 0:
#         print(f"Error: {app_name} not found.")
#         return
    
#     # Bring the window to the foreground
#     win32gui.SetForegroundWindow(handle)

# # Test the function
# default_browser = get_default_browser()
# set_frontmost_process()




import subprocess
import win32gui

def get_default_browser():
    command = 'powershell -Command "$defaultBrowser = (Get-ItemProperty \'HKCU:\\Software\\Microsoft\\Windows\\Shell\\Associations\\UrlAssociations\\http\\UserChoice\').ProgId; echo $defaultBrowser"'
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
    
    if result.returncode != 0:
        print("Error executing PowerShell command:")
        print(result.stderr.strip())
        return None
    
    output = result.stdout.strip()
    return output

def set_frontmost_process(browser_name):
    if browser_name.lower() == 'microsoft edge':
        # For Microsoft Edge, let's try a different approach to bring it to the foreground
        subprocess.run('start microsoft-edge:', shell=True)
        return
    
    # Find the window handle of the application
    handle = win32gui.FindWindow(None, browser_name)
    
    if handle == 0:
        print(f"Error: {browser_name} window not found.")
        return
    
    # Bring the window to the foreground
    win32gui.SetForegroundWindow(handle)

# Test the function
default_browser = get_default_browser()
if default_browser:
    browser_mapping = {
        'FirefoxURL': 'Firefox',
        'ChromeHTML': 'Google Chrome',
        'MSEdgeHTM': 'Microsoft Edge'
    }
    
    get_default_browser()
    browser_name = browser_mapping.get(default_browser, 'Unknown')
    print(f"The default browser is: {browser_name}")
    set_frontmost_process(browser_name)