import pyautogui
import pyperclip
import keyboard
import difflib
import time

width, height = pyautogui.size()
pyautogui.moveTo(width/4, height/2)


prev_string = ""

print("#####################################")
print("")
print(" kakaotalk logging macro(Kakaotalk Anti deleting) by hyoom")
print(" Date Created : 2019.02.21")
print(" Version : v1.0")
print(" Developer Blog : hyoom1024.github.io")
print("")
print("#####################################")

print("")
print("[*] 삭제 된 메시지 목록")
wait_key = 0
try:
    while(1):
        if keyboard.is_pressed('ctrl') and keyboard.is_pressed('f10'):
            break        
        if wait_key == 1:
            if keyboard.is_pressed('ctrl') and keyboard.is_pressed('f9'):
                print("[!] 5초 후 재개합니다.")
                time.sleep(5)
                wait_key = 0
                prev_string = ""
                print("[*] 삭제 된 메시지 목록")
                
        elif keyboard.is_pressed('ctrl') and keyboard.is_pressed('f9'):
            print("[!] 일시정지")
            time.sleep(5)
            wait_key = 1
        else:
            pyautogui.moveTo(width/4, height/2)
            pyautogui.click()
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(0.5)
            if prev_string == "":
                prev_string = pyperclip.paste()
            else:
                new_string = pyperclip.paste()
                if not prev_string == "":
                    diff = difflib.ndiff(prev_string.splitlines(keepends=True), new_string.splitlines(keepends=True))
                    asdf = ''.join(diff)
                    for i in asdf.split("\n"):
                        if i[:2] == "- ":
                            pyautogui.moveTo(width/4, height/20 * 18)
                            pyautogui.click()
                            pyperclip.copy('[!]삭제 메시지 감지 ' + i)
                            pyautogui.hotkey('ctrl', 'v')
                            pyautogui.press('enter')  
                            print(i)
                        else:
                            f = ""
                    prev_string = new_string
                    
except:
    print("알 수 없는 에러입니다.")
        
print("finish program")
