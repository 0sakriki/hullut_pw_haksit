
import pyautogui
import time
import keyboard

ehto = input("1: Puhu, 2: Liiku, 3: Autofarm, 4: Hiiren paikka, 5: Hakkaa farmi, 6: Istutus, 7: Keräys, 8: Juokse farmi läpi, 9: Tyhjää maa (ei toimi) ")

lopetaKoodi = False

def lopeta():
    global lopetaKoodi
    lopetaKoodi = True

keyboard.add_hotkey("e", lopeta)

def kavely():
    print(2)
    pyautogui.hotkey("alt", "tab")
    time.sleep(1)
    pyautogui.keyDown("d")
    pyautogui.keyDown("space")
    for i in range(300):
        time.sleep(0.1)
        if lopetaKoodi:
            pyautogui.keyUp("d")
            pyautogui.keyUp("space")
            return
    pyautogui.keyUp("d")
    pyautogui.keyUp("space")

def kirjoitus():
    print(1)
    time.sleep(1)
    #hiiren_paikka = pyautogui.position()
    #print(hiiren_paikka)
    pyautogui.click(1870, 33)
    pyautogui.typewrite("kissa ja koira im so fast writer cant u see super haker man program")
    pyautogui.press('enter')

def autofarm():
    print(3)
    pyautogui.hotkey("alt", "tab")

    for i in range(50):

        pyautogui.click(1036, 1027) # ottaa blokit käteen

        pyautogui.moveTo(820,434) # farmauksen aloituspaikka (vasen yläkulma)
        pyautogui.mouseDown()

        for i in range(5):
            pyautogui.move(270, 0, duration = 1)
            pyautogui.move(-270, 60)
        
        pyautogui.doubleClick(873, 1029) # ottaa nyrkin käteen
      
        pyautogui.moveTo(820,434) # farmauksen aloituspaikka (vasen yläkulma)
        pyautogui.mouseDown()

        for i in range(3):
            pyautogui.move(300, 0, duration = 7)
            pyautogui.move(-300, 60)

        pyautogui.move(110, 0, duration = 3)
        pyautogui.move(70, 0)
        pyautogui.move(110, 0, duration = 3)
        pyautogui.move(-300, 65)
        pyautogui.move(300, 0, duration = 7)

        pyautogui.click(1036, 1027) # ottaa blokit käteen

        print(f"{i}. kierros")

def hiirenpaikka():
    pyautogui.click(873, 1029)
    time.sleep(3)
    print(pyautogui.position())

def farminhakkaus():
    pyautogui.hotkey("alt", "tab")

    kierrosmaara = 0
    for i in range(5):

        if kierrosmaara % 2 == 0:
            nappain = "d" # liiku oikealle
            hiiripainallus = (1861, 662) # riko oikealta alhaalta kaksi blokkia
        else:
            nappain = "a" # liiku vasemmalle
            hiiripainallus = (85, 725) # riko vasemmalta alhaalta kaksi blokkia

        pyautogui.keyDown(nappain)
        pyautogui.keyDown("space")

        for i in range(1000):
            time.sleep(0.1)
            if lopetaKoodi == True:
                pyautogui.keyUp(nappain)
                pyautogui.keyUp("space")
                return

        pyautogui.keyUp(nappain)
        pyautogui.keyUp("space")

        pyautogui.moveTo(hiiripainallus)

        pyautogui.mouseDown()

        for i in range(20):
            time.sleep(0.1)
            if lopetaKoodi == True:
                pyautogui.mouseUp()
                return

        pyautogui.mouseUp()

        kierrosmaara += 1

        """"
        pyautogui.keyDown("a")
        pyautogui.keyDown("space")

        time.sleep(100)

        pyautogui.keyUp("a")
        pyautogui.keyUp("space")

        pyautogui.moveTo(85, 725)

        pyautogui.mouseDown()
        time.sleep(2)
        pyautogui.mouseUp()
        """

def istutus():
    pyautogui.hotkey("alt", "tab")
    pyautogui.click(1036, 1027) # ottaa siemenet käteen

    for i in range(5):
        pyautogui.moveTo(943, 537) # vie hiiren näytön keskelle
        pyautogui.mouseDown()

        pyautogui.keyDown("d")

        for i in range(150):
            time.sleep(0.1)
            if lopetaKoodi == True:
                pyautogui.keyUp("d")
                return
            
        pyautogui.keyUp("d")

        pyautogui.keyDown("a")

        for i in range(150):
                    time.sleep(0.1)
                    if lopetaKoodi == True:
                        pyautogui.keyUp("a")
                        return
               
        pyautogui.keyUp("a")

def kerays():
    pyautogui.hotkey("alt", "tab")
    pyautogui.keyDown("space")
    time.sleep(1)

    for i in range(7):
        for i in range(29):
            if lopetaKoodi == True:
                return
            pyautogui.keyDown("d")
            time.sleep(0.4)
            pyautogui.keyUp("d")
            time.sleep(0.4)

        for i in range(29):
            if lopetaKoodi == True:
                return
            pyautogui.keyDown("a")
            time.sleep(0.4)
            pyautogui.keyUp("a")
            time.sleep(0.5)

def farmin_lapijuoksu():
    pyautogui.hotkey("alt", "tab")
    time.sleep(1)

    for i in range(5):
        pyautogui.keyDown("d")

        for i in range(150):
            time.sleep(0.1)
            if lopetaKoodi == True:
                pyautogui.keyUp("d")
                return
            
        pyautogui.keyUp("d")

        pyautogui.keyDown("a")

        for i in range(150):
            time.sleep(0.1)
            if lopetaKoodi == True:
                pyautogui.keyUp("a")
                return
        
        pyautogui.keyUp("a")

def tyhjaamaa():
    pyautogui.hotkey("alt", "tab")
    time.sleep(1)

"""
    pyautogui.keyDown("space")

    for i in range(20):
        for i in range(29):
            pyautogui.keyDown("d")
            time.sleep(0.4)
            pyautogui.keyUp("d")
            time.sleep(2)

            pyautogui.moveTo(1861, 662)
            pyautogui.mouseDown()
            time.sleep(1)
            pyautogui.mouseUp()

        for i in range(29):
            pyautogui.keyDown("a")
            time.sleep(0.4)
            pyautogui.keyUp("a")
            time.sleep(2)

            pyautogui.moveTo(85, 725)
            pyautogui.mouseDown()
            time.sleep(1)
            pyautogui.mouseUp()
"""

if ehto == "1":
    kirjoitus()
elif ehto == "2":
    kavely()
elif ehto == "3":
    autofarm()
elif ehto == "4":
    hiirenpaikka()
elif ehto == "5":
    farminhakkaus()
elif ehto == "6":
    istutus()
elif ehto == "7":
    kerays()
elif ehto == "8":
    farmin_lapijuoksu()
elif ehto == "9":
    tyhjaamaa()

# tee p poistu nappi mikä keskeyttää skriptin suorittamisen heti
# tee u uudelleensyntymisnappi mikä keskeyttää skriptin suorittamisen ja laittaa minut synytmään uudelleen
# laita printit kuntoon