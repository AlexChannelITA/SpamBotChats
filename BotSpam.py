import time,pyautogui, pyperclip
#spero che avete tutte le librerie di cui avete bisogno per il progetto altrimenti scaricatevele
#if you dont'have the reposotories donwload them
time.sleep(5)
f = open("spam","r")

for char in f:
    pyperclip.copy(char)
    pyautogui.hotkey('ctrl', 'v', interval=0.02)#se avete mac os dovete sostituire "ctrl" con "command"/ if you have whidnows write "ctrl", whit mac os write "command"
    pyautogui.typewrite("\n")
