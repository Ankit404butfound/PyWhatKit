import subprocess
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

