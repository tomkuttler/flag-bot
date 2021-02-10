# Flag bot

# This is a python bot that can solve the flag quiz on geo-quiz.net faster than a human
# by automatically detecting the color of the top left pixel of the flag and clicking 
# on the correct answer on the screen.

# Limitations: This bot uses absolute screen coordinates, so it can only be used on 
# a 1920 x 1080 pixel resolution screen using Firefox browser. 
# Alternatively, you can manually adjust the coordinates in the script to match your 
# screen resolution. Additionally, the bot is sometimes too fast for the anti-cheat 
# mechanisms, so you might need to adjust the delays in the script.

from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

# flag coords: (919,271,250,167)
# flag top left: (919,271)
# flag bottom right: (1150, 420)
# answers coords: (900,460,280,330)

# flags(top left rgb values):
# Same rgb values have same tag assigned

##Aegypten.png (255,0,0)                red
##Aequatorialguinea.png (64,155,100)
##Aethiopien.png (0,113,69)
##Afghanistan.png (0,0,0)               black
##Albanien (113,4,13)
##Algerien.png (87,182,120)
##Andorra.png (6,29,141)
##Angola.png (207,8,33)                 red_dark
##Argentinien.png (118,172,220)
##Armenien.png (255,0,0)                red
##Aserbaidschan.png (0,147,200)
##Australien.png (255,61,61)
##Bahamas.png (0,3,12)
##Bahrain.png (141,141,141)
##Bangladesch.png (0,106,77)            green_dark
##Barbados.png (0,33,128)
##Belgien.png (0,0,0)                   black
##Belize.png (117,12,23)
##Benin.png (0,136,80)                  green
##Bhutan.png (127,95,22)
##Bolivien.png (217,24,0)
##BosnienHerzogowina.png (53,57,125)
##Botswana.png (238,238,238)            gray
##Brasilien.png (0,157,56)
##Bulgarien.png (255,255,255)           white
##BurkinaFaso.png (122,5,17)
##Burudi.png (255,255,255)              white
##Chile.png (238,238,238)               gray
##China.png (255,0,0)                   red
##Cookinseln.png (216,61,61)
##CostaRica.png (238,238,238)           gray
##Daenemark.png (207,37,71)
##demrepkongo.png (0,128,255)
##Deutschland.png (0,0,0)               black
##Dominikanische.png (4,43,83)
##Dschibuti.png (213,234,248)
##Ecuador.png (158,150,41)
##Elfenbeinkueste.png (0,156,98)
##Eritrea.png (127,14,27)
##Estland.png (238,238,238)             gray
##Fidschi.png (112,16,25)
##Finnland.png (238,238,238)            gray
##Frankreich.png (0,30,150)
##Gabun.png (0,159,96)
##Gambia.png (207,8,33)                 red_dark
##Georgien.png (255,255,255)            white
##Ghana.png (207,8,33)                  red_dark
##Griechenland.png (5,94,176)
##Guatemala.png (135,200,228)
##Guinea.png (207,8,33)                 red_dark
##Guyana.png (49,70,58)
##Haiti.png (0,26,160)                  blue
##Honduras.png (2,124,207)
##Indien.png (147,91,27)
##Indonesien.png (232,0,8)
##Irak.png (207,8,33)                   red_dark
##Iran.png (29,160,62)
##Irland.png (0,156,70)
##Island.png (0,53,152)
##Israel.png (255,255,255)              white
##Italien.png (0,147,68)
##Jamaika.png (249,219,0)
##Japan.png (255,255,255)               white
##Jemen.png (207,8,33)                  red_dark
##Jordanien.png (146,4,20)
##Kambodscha.png (0,42,162)
##Kamerun.png (0,123,94)
##Kanada.png (219,34,31)
##Kasachstan.png (111,221,255)
##Katar.png(255,255,255)                white
##Kenia.png (0,0,0)                     black
##Kirgisistan.png (233,8,41)
##Kiribati.png (255,3,3)
##Kolumbien.png (252,210,14)
##Komoren.png (120,161,41)
##Kongo.png (0,150,65)
##Kosovo.png (31,73,166)
##Kroatien.png (215,13,16)
##Kuba.png (94,5,18)
##Kuwait.png (0,68,51)
##Laos.png (207,8,33)                   red_dark
##Lesotho.png (0,26,160)                blue
##Lettland.png (159,44,54)
##Libanon.png (238,22,31)               red2
##Liberia.png (0,35,104)
##Libyen.png (232,0,12)
##Lichtenstein.png (35,68,145)
##Litauen.png (253,186,11)
##Luxemburg.png (239,39,41)             Rot4
##Madagaskar.png (255,255,255)          white
##Malawi.png (0,0,0)                    black
##Malaysia.png (0,1,138)
##Malediven.png (211,8,49)              red3
##Mali.png (12,182,55)
##Malta.png (255,255,255)               white
##Marokko.png (236,0,11)
##Marshallinseln.png (0,53,148)
##Mauretanien.png (0,98,48)             green_dark2
##Mauritius.png (255,0,0)               rot
##Mexiko.png (3,115,33)
##Moldawien.png (29,94,186)
##Monaco.png (207,8,33)                 red_dark
##Mongolei.png (215,13,16)
##Montenegro.png (213,177,55)
##Mosambik.png (138,48,69)
##Namibia.png (0,50,129)
##Neuseeland.png (220,91,106)
##Nicaragua.png (0,103,199)
##Niederlande.png (211,56,48)
##Niger.png (225,81,1)
##Nigeria.png (0,136,80)               green
##Nordkorea.png (12,25,174)
##Nordmazedonien.png (221,55,0)
##Norwegen.png (239,39,41)             red4
##Oesterreich.png (238,238,238)        gray
##Oman.png (233,215,214)
##Pakistan.png (255,255,255)           white
##Panama.png (255,255,255)             white
##Papua.png (68,1,5)
##Paraguay.png (220,69,58)
##Peru.png (224,42,61)
##Philippinen.png (0,4,51)
##Polen.png (255,255,255)              white
##Portugal.png (0,98,48)               green_dark2
##Ruanda.png (0,155,244)
##Rumaenien.png (0,45,147)
##Russland.png (255,255,255)           white
##Salomonen.png (0,73,171)
##Sambia.png (18,139,0)
##Samoa.png (0,39,128)
##SanMarino.png (255,255,255)          white
##SaudiArabien.png (0,108,50)
##Schweden.png (35,126,180)
##Schweiz.png (183,12,9)
##Senegal.png (0,134,61)
##Serbien.png (221,25,33)
##Seychellen.png (0,61,136)
##SierraLeone.png (24,182,55)
##Simbabwe.png (137,135,139)
##Slowakei.png (255,255,255)           white
##Slowenien.png (255,255,255)          white
##Somalia.png (63,138,222)
##Spanien.png (199,3,24)
##SriLanka.png (255,205,0)
##StLucia.png (3,80,162)
##Sudan.png (110,63,43)
##Suedafrika.png (0,123,76)
##Suedkorea.png (249,249,249)
##Suriname.png (0,115,36)
##Swasiland.png (60,94,186)
##Syrien.png (214,45,65)
##Tadschikistan.png (205,0,0)
##Taiwan.png (2,0,50)
##Tansania.png (0,129,0)
##Thailand.png (223,8,17)
##TimorLeste.png (121,50,10)
##Togo.png (211,8,49)                  red3
##Tonga.png (255,255,255)              white
##TrinidadTobago.png (229,129,138)
##Tschad.png (8,36,82)
##Tschechien.png (52,48,195)
##Tuerkei.png (238,22,31)              rot2
##Tunesien.png (232,0,11)
##Turkmenistan.png (0,106,77)          green_dark
##Uganda.png (0,0,0)                   black
##Ukraine.png (55,118,196)
##Ungarn.png (214,56,22)
##Uruguay.png (255,255,255)            white
##USA.png (6,40,100)
##Usbekistan.png (0,154,182)
##Vanuatu.png (57,0,6)
##Vatikan.png (196,182,2)
##Venezuela.png (247,210,16)
##Vereinigtearab.png (255,0,0)         red
##Vereinigtes.png (255,74,74)
##Vietnam.png (237,0,13)
##whiterussland.png (173,8,18)
##Zentralafrikanische.png (29,74,147)

##-----------------------------------------------

## Bottom Right (1150, 420)

## white:

##Bulgarien.png (255,255,255) (215,33,10)
##Burudi.png (255,255,255) (255,255,255) (1150,400: 24,182,55)
##Georgien.png (255,255,255) (255,255,255) (1116,418: 205,0,0)
##Israel.png (255,255,255) (0,53,185)
##Japan.png (255,255,255) (255,255,255) (1040,350: 212,0,0)
##Katar.png(255,255,255) (113,18,58)
##Madagaskar.png (255,255,255) (0,205,35)
##Malta.png (255,255,255) (208,12,39)
##Pakistan.png (255,255,255) (0,102,0)          
##Panama.png (255,255,255) (255,255,255) (1107,390: 217,0,0)
##Polen.png (255,255,255) (255,255,255) (1130,344: 255,135,135)
##Russland.png (255,255,255) (254,0,0)
##SanMarino.png (255,255,255) (0,131,196)
##Slowakei.png (255,255,255) (255,0,0)
##Slowenien.png (255,255,255) (255,255,255) (970,299: 137,163,155)
##Tonga.png (255,255,255) (194,0,0)
##Uruguay.png (255,255,255) (255,255,255) (965,325: 224,179,32)

## red_dark

##Angola.png (207,8,33) (0,0,0) (1045,338: 249,215,14)
##Guinea.png (207,8,33) (0,149,96)
##Irak.png (207,8,33) (0,0,0) (1088,363: 0,159,96)
##Jemen.png (207,8,33) (0,0,0) (1141,325: 207,8,33)
##Laos.png (207,8,33) (207,8,33)
##Monaco.png (207,8,33) (255,255,255)
##Gambia.png (207,8,33) (55,120,35)             
##Ghana.png (207,8,33) (0,107,61)

## black:

##Afghanistan.png (0,0,0) (0,154,0)
##Belgien.png (0,0,0) (255,6,27)  
##Deutschland.png (0,0,0) (255,205,0)
##Kenia.png (0,0,0) (0,102,0)
##Malawi.png (0,0,0) (47,159,50)
##Uganda.png (0,0,0) (223,54,2)

## gray:

##Botswana.png (238,238,238) (169,215,243)
##Chile.png (238,238,238) (237,17,40)
##CostaRica.png (238,238,238) (20,66,142)
##Estland.png (238,238,238) (255,255,255) (1100,300: 34,122,201)           
##Finnland.png (238,238,238) (255,255,255) (1010,347: 13,84,157)
##Oesterreich.png (238,238,238) (255,255,255) (1150,400: 237,21,30)

## red:

##Aegypten.png (255,0,0) (0,0,0) (1059,356: 217,186,0)
##Armenien.png (255,0,0) (255,179,0)
##China.png (255,0,0) (255,0,0)
##Mauritius.png (255,0,0) (0,155,0)
##Vereinigtearab.png (255,0,0) (0,0,0) (1115,350: 255,255,255)

## red2

##Libanon.png (238,22,31) (238,22,31) (1039,376: 0,168,80)
##Tuerkei.png (238,22,31) (238,22,31) (975,343: 255,255,255)

## red3

##Malediven.png (211,8,49) (211,8,49)
##Togo.png (211,8,49) (0,106,77)

## red4

##Norwegen.png (239,39,41) (239,39,41)
##Luxemburg.png (239,39,41) (0,165,222)

## green

##Benin.png (0,136,80) (233,8,41)                 
##Nigeria.png (0,136,80) (0,136,80)

## green_dark

##Bangladesch.png (0,106,77) (0,106,77) (1050,335: 244,37,63)           
##Turkmenistan.png (0,106,77) (0,106,77) (971,425: 181,20,49)

## green_dark2

##Mauretanien.png (0,98,48) (0,98,48)             
##Portugal.png (0,98,48) (221,31,25)

## blue

##Haiti.png (0,26,160) (211,8,49)
##Lesotho.png (0,26,160) (0,150,65)                              

#-----------------------------------------------

# fast click function:
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

# Start the game:
time.sleep(3)
click(1043,787)
time.sleep(0.3)

# press 'q' to end loop:
while keyboard.is_pressed('q') == False:

    if pyautogui.pixelMatchesColor(1057,287, (51,122,183)):

        click(1050,300)

    if pyautogui.pixelMatchesColor(919,271, (64,155,100)):

        x, y = pyautogui.locateCenterOnScreen('ansAequatorialguinea.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (0,113,69)):

        x, y = pyautogui.locateCenterOnScreen('ansAethiopien.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (113,4,13)):

        x, y = pyautogui.locateCenterOnScreen('ansAlbanien.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (87,182,120)):

        x, y = pyautogui.locateCenterOnScreen('ansAlgerien.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (6,29,141)):

        x, y = pyautogui.locateCenterOnScreen('ansAndorra.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (118,172,220)):

        x, y = pyautogui.locateCenterOnScreen('ansArgentinien.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (0,147,200)):

        x, y = pyautogui.locateCenterOnScreen('ansAserbaidschan.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (255,61,61)):

        x, y = pyautogui.locateCenterOnScreen('ansAustralien.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (0,3,12)):

        x, y = pyautogui.locateCenterOnScreen('ansBahamas.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (141,141,141)):

        x, y = pyautogui.locateCenterOnScreen('ansBahrain.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (0,33,128)):

        x, y = pyautogui.locateCenterOnScreen('ansBarbados.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (117,12,23)):

        x, y = pyautogui.locateCenterOnScreen('ansBelize.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (127,95,22)):

        x, y = pyautogui.locateCenterOnScreen('ansBhutan.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (217,24,0)):

        x, y = pyautogui.locateCenterOnScreen('ansBolivien.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (58,62,137)):

        x, y = pyautogui.locateCenterOnScreen('ansBosnienHerzogowina.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (0,157,56)):

        x, y = pyautogui.locateCenterOnScreen('ansBrasilien.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (122,5,17)):

        x, y = pyautogui.locateCenterOnScreen('ansBurkinaFaso.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (216,61,61)):

        x, y = pyautogui.locateCenterOnScreen('ansCookinseln.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (207,37,71)):

        x, y = pyautogui.locateCenterOnScreen('ansDaenemark.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (0,128,255)):

        x, y = pyautogui.locateCenterOnScreen('ansdemrepkongo.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (4,43,83)):

        x, y = pyautogui.locateCenterOnScreen('ansDominikanische.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (213,234,248)):

        x, y = pyautogui.locateCenterOnScreen('ansDschibuti.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (158,150,41)):

        x, y = pyautogui.locateCenterOnScreen('ansEcuador.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (0,156,98)):

        x, y = pyautogui.locateCenterOnScreen('ansElfenbeinkueste.png', region=(900,440,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (127,14,27)):

        x, y = pyautogui.locateCenterOnScreen('ansEritrea.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (112,16,25)):

        x, y = pyautogui.locateCenterOnScreen('ansFidschi.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (0,30,150)):

        x, y = pyautogui.locateCenterOnScreen('ansFrankreich.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (0,159,96)):

        x, y = pyautogui.locateCenterOnScreen('ansGabun.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (5,94,176)):

        x, y = pyautogui.locateCenterOnScreen('ansGriechenland.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (135,200,228)):

        x, y = pyautogui.locateCenterOnScreen('ansGuatemala.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (49,70,58)):

        x, y = pyautogui.locateCenterOnScreen('ansGuyana.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (2,124,207)):

        x, y = pyautogui.locateCenterOnScreen('ansHonduras.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (147,91,27)):

        x, y = pyautogui.locateCenterOnScreen('ansIndien.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (232,0,8)):

        x, y = pyautogui.locateCenterOnScreen('ansIndonesien.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)


    if pyautogui.pixelMatchesColor(919,271, (29,160,62)):

        x, y = pyautogui.locateCenterOnScreen('ansIran.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (0,156,70)):

        x, y = pyautogui.locateCenterOnScreen('ansIrland.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (0,53,152)):

        x, y = pyautogui.locateCenterOnScreen('ansIsland.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (0,147,68)):

        x, y = pyautogui.locateCenterOnScreen('ansItalien.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (249,219,0)):

        x, y = pyautogui.locateCenterOnScreen('ansJamaika.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (146,4,20)):

        x, y = pyautogui.locateCenterOnScreen('ansJordanien.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (0,42,162)):

        x, y = pyautogui.locateCenterOnScreen('ansKambodscha.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (0,123,94)):

        x, y = pyautogui.locateCenterOnScreen('ansKamerun.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (219,34,31)):

        x, y = pyautogui.locateCenterOnScreen('ansKanada.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (111,221,255)):

        x, y = pyautogui.locateCenterOnScreen('ansKasachstan.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (233,8,41)):

        x, y = pyautogui.locateCenterOnScreen('ansKirgisistan.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (255,3,3)):

        x, y = pyautogui.locateCenterOnScreen('ansKiribati.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (252,210,14)):

        x, y = pyautogui.locateCenterOnScreen('ansKolumbien.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (120,161,41)):

        x, y = pyautogui.locateCenterOnScreen('ansKomoren.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (0,150,65)):

        x, y = pyautogui.locateCenterOnScreen('ansKongo.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (31,73,166)):

        x, y = pyautogui.locateCenterOnScreen('ansKosovo.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (215,13,16)):

        x, y = pyautogui.locateCenterOnScreen('ansKroatien.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (94,5,18)):

        x, y = pyautogui.locateCenterOnScreen('ansKuba.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (0,68,51)):

        x, y = pyautogui.locateCenterOnScreen('ansKuwait.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (159,44,54)):

        x, y = pyautogui.locateCenterOnScreen('ansLettland.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (0,35,104)):

        x, y = pyautogui.locateCenterOnScreen('ansLiberia.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (232,0,12)):

        x, y = pyautogui.locateCenterOnScreen('ansLibyen.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (35,68,145)):

        x, y = pyautogui.locateCenterOnScreen('ansLichtenstein.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (253,186,11)):

        x, y = pyautogui.locateCenterOnScreen('ansLitauen.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (0,1,138)):

        x, y = pyautogui.locateCenterOnScreen('ansMalaysia.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (12,182,55)):

        x, y = pyautogui.locateCenterOnScreen('ansMali.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (236,0,11)):

        x, y = pyautogui.locateCenterOnScreen('ansMarokko.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (0,53,148)):

        x, y = pyautogui.locateCenterOnScreen('ansMarshallinseln.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (3,115,33)):

        x, y = pyautogui.locateCenterOnScreen('ansMexiko.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (29,94,186)):

        x, y = pyautogui.locateCenterOnScreen('ansMoldawien.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (215,13,16)):

        x, y = pyautogui.locateCenterOnScreen('ansMongolei.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (213,177,55)):

        x, y = pyautogui.locateCenterOnScreen('ansMontenegro.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (138,48,69)):

        x, y = pyautogui.locateCenterOnScreen('ansMosambik.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (0,50,129)):

        x, y = pyautogui.locateCenterOnScreen('ansNamibia.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (220,91,106)):

        x, y = pyautogui.locateCenterOnScreen('ansNeuseeland.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (0,103,199)):

        x, y = pyautogui.locateCenterOnScreen('ansNicaragua.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (211,56,48)):

        x, y = pyautogui.locateCenterOnScreen('ansNiederlande.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (225,81,1)):

        x, y = pyautogui.locateCenterOnScreen('ansNiger.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (12,25,174)):

        x, y = pyautogui.locateCenterOnScreen('ansNordkorea.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (221,55,0)):

        x, y = pyautogui.locateCenterOnScreen('ansNordmazedonien.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (255,236,235)):

        x, y = pyautogui.locateCenterOnScreen('ansOman.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (68,1,5)):

        x, y = pyautogui.locateCenterOnScreen('ansPapua.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (220,69,58)):

        x, y = pyautogui.locateCenterOnScreen('ansParaguay.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (224,42,61)):

        x, y = pyautogui.locateCenterOnScreen('ansPeru.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (0,4,51)):

        x, y = pyautogui.locateCenterOnScreen('ansPhilippinen.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (0,155,244)):

        x, y = pyautogui.locateCenterOnScreen('ansRuanda.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (0,45,157)):

        x, y = pyautogui.locateCenterOnScreen('ansRumaenien.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (0,80,187)):

        x, y = pyautogui.locateCenterOnScreen('ansSalomonen.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (18,139,0)):

        x, y = pyautogui.locateCenterOnScreen('ansSambia.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (0,39,128)):

        x, y = pyautogui.locateCenterOnScreen('ansSamoa.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (0,108,50)):

        x, y = pyautogui.locateCenterOnScreen('ansSaudiArabien.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (35,126,180)):

        x, y = pyautogui.locateCenterOnScreen('ansSchweden.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (183,12,9)):

        x, y = pyautogui.locateCenterOnScreen('ansSchweiz.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (0,134,61)):

        x, y = pyautogui.locateCenterOnScreen('ansSenegal.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (221,25,33)):

        x, y = pyautogui.locateCenterOnScreen('ansSerbien.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (0,61,136)):

        x, y = pyautogui.locateCenterOnScreen('ansSeychellen.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (24,182,55)):

        x, y = pyautogui.locateCenterOnScreen('ansSierraLeone.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (137,135,139)):

        x, y = pyautogui.locateCenterOnScreen('ansSimbabwe.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (63,138,222)):

        x, y = pyautogui.locateCenterOnScreen('ansSomalia.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (199,3,24)):

        x, y = pyautogui.locateCenterOnScreen('ansSpanien.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (255,205,0)):

        x, y = pyautogui.locateCenterOnScreen('ansSriLanka.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (3,80,162)):

        x, y = pyautogui.locateCenterOnScreen('ansStLucia.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (110,63,43)):

        x, y = pyautogui.locateCenterOnScreen('ansSudan.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (0,123,76)):

        x, y = pyautogui.locateCenterOnScreen('ansSuedafrika.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (249,249,249)):

        x, y = pyautogui.locateCenterOnScreen('ansSuedkorea.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (0,115,36)):

        x, y = pyautogui.locateCenterOnScreen('ansSuriname.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (60,94,186)):

        x, y = pyautogui.locateCenterOnScreen('ansSwasiland.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (214,45,65)):

        x, y = pyautogui.locateCenterOnScreen('ansSyrien.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (205,0,0)):

        x, y = pyautogui.locateCenterOnScreen('ansTadschikistan.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (2,0,50)):

        x, y = pyautogui.locateCenterOnScreen('ansTaiwan.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (0,129,0)):

        x, y = pyautogui.locateCenterOnScreen('ansTansania.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (223,8,17)):

        x, y = pyautogui.locateCenterOnScreen('ansThailand.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (121,50,10)):

        x, y = pyautogui.locateCenterOnScreen('ansTimorLeste.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (229,129,138)):

        x, y = pyautogui.locateCenterOnScreen('ansTrinidadTobago.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (8,36,82)):

        x, y = pyautogui.locateCenterOnScreen('ansTschad.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (52,48,195)):

        x, y = pyautogui.locateCenterOnScreen('ansTschechien.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (232,0,11)):

        x, y = pyautogui.locateCenterOnScreen('ansTunesien.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (55,118,196)):

        x, y = pyautogui.locateCenterOnScreen('ansUkraine.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (214,56,22)):

        x, y = pyautogui.locateCenterOnScreen('ansUngarn.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (6,40,100)):

        x, y = pyautogui.locateCenterOnScreen('ansUSA.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (0,154,182)):

        x, y = pyautogui.locateCenterOnScreen('ansUsbekistan.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (57,0,6)):

        x, y = pyautogui.locateCenterOnScreen('ansVanuatu.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (196,182,2)):

        x, y = pyautogui.locateCenterOnScreen('ansVatikan.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (247,210,16)):

        x, y = pyautogui.locateCenterOnScreen('ansVenezuela.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (255,74,74)):

        x, y = pyautogui.locateCenterOnScreen('ansVereinigtes.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (237,0,13)):

        x, y = pyautogui.locateCenterOnScreen('ansVietnam.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (173,8,18)):

        x, y = pyautogui.locateCenterOnScreen('answhiterussland.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

    if pyautogui.pixelMatchesColor(919,271, (29,74,147)):

        x, y = pyautogui.locateCenterOnScreen('ansZentralafrikanische.png', region=(900,460,280,330), confidence=0.8)

        time.sleep(np.random.uniform(0.2,0.5))

        click(x,y)

#----------------------------------------------------------------------------------------------------------------------

## white
        
    if pyautogui.pixelMatchesColor(919,271, (255,255,255)):
        
        if pyautogui.pixelMatchesColor(1150,420, (215,33,10)):
            
            x, y = pyautogui.locateCenterOnScreen('ansBulgarien.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

        if pyautogui.pixelMatchesColor(1150,400, (24,182,55)):
            
            x, y = pyautogui.locateCenterOnScreen('ansBurudi.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

        if pyautogui.pixelMatchesColor(1116,418, (205,0,0)):
            
            x, y = pyautogui.locateCenterOnScreen('ansGeorgien.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

        if pyautogui.pixelMatchesColor(1150,420, (0,53,185)):
            
            x, y = pyautogui.locateCenterOnScreen('ansIsrael.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

        if pyautogui.pixelMatchesColor(1040,350, (212,0,0)):
            
            x, y = pyautogui.locateCenterOnScreen('ansJapan.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

        if pyautogui.pixelMatchesColor(1150,420, (113,18,58)):
            
            x, y = pyautogui.locateCenterOnScreen('ansKatar.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

        if pyautogui.pixelMatchesColor(1150,420, (0,205,35)):
            
            x, y = pyautogui.locateCenterOnScreen('ansMadagaskar.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

        if pyautogui.pixelMatchesColor(1150,420, (208,12,39)):
            
            x, y = pyautogui.locateCenterOnScreen('ansMalta.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

        if pyautogui.pixelMatchesColor(1150,420, (0,102,0)):
            
            x, y = pyautogui.locateCenterOnScreen('ansPakistan.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

        if pyautogui.pixelMatchesColor(1107,390, (217,0,0)):
            
            x, y = pyautogui.locateCenterOnScreen('ansPanama.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

        if pyautogui.pixelMatchesColor(1130,344, (255,135,135)):
            
            x, y = pyautogui.locateCenterOnScreen('ansPolen.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

        if pyautogui.pixelMatchesColor(1150,420, (254,0,0)):
            
            x, y = pyautogui.locateCenterOnScreen('ansRussland.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

        if pyautogui.pixelMatchesColor(1150,420, (0,131,196)):
            
            x, y = pyautogui.locateCenterOnScreen('ansSanMarino.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

        if pyautogui.pixelMatchesColor(1150,420, (255,0,0)):
            
            x, y = pyautogui.locateCenterOnScreen('ansSlowakei.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

        if pyautogui.pixelMatchesColor(970,299, (137,163,155)):
            
            x, y = pyautogui.locateCenterOnScreen('ansSlowenien.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

        if pyautogui.pixelMatchesColor(1150,420, (194,0,0)):
            
            x, y = pyautogui.locateCenterOnScreen('ansTonga.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

        if pyautogui.pixelMatchesColor(965,325, (224,179,32)):
            
            x, y = pyautogui.locateCenterOnScreen('ansUruguay.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

#----------------------------------------------------------------------------------------------------------------------

## red_dark
        
    if pyautogui.pixelMatchesColor(919,271, (207,8,33)):
        
        if pyautogui.pixelMatchesColor(1045,338, (249,215,14)):
            
            x, y = pyautogui.locateCenterOnScreen('ansAngola.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

        if pyautogui.pixelMatchesColor(1150,420, (0,149,96)):
            
            x, y = pyautogui.locateCenterOnScreen('ansGuinea.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

        if pyautogui.pixelMatchesColor(1088,363, (0,159,96)):
            
            x, y = pyautogui.locateCenterOnScreen('ansIrak.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

        if pyautogui.pixelMatchesColor(1141,325, (207,8,33)):
            
            x, y = pyautogui.locateCenterOnScreen('ansJemen.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

        if pyautogui.pixelMatchesColor(1150,420, (207,8,33)):
            
            x, y = pyautogui.locateCenterOnScreen('ansLaos.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

        if pyautogui.pixelMatchesColor(1150,420, (255,255,255)):
            
            x, y = pyautogui.locateCenterOnScreen('ansMonaco.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

        if pyautogui.pixelMatchesColor(1150,420, (55,120,35)):
            
            x, y = pyautogui.locateCenterOnScreen('ansGambia.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

        if pyautogui.pixelMatchesColor(1150,420, (0,107,61)):
            
            x, y = pyautogui.locateCenterOnScreen('ansGhana.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

#----------------------------------------------------------------------------------------------------------------------

## black
        
    if pyautogui.pixelMatchesColor(919,271, (0,0,0)):
        
        if pyautogui.pixelMatchesColor(1150,420, (0,154,0)):
            
            x, y = pyautogui.locateCenterOnScreen('ansAfghanistan.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

        if pyautogui.pixelMatchesColor(1150,420, (255,6,27)):
            
            x, y = pyautogui.locateCenterOnScreen('ansBelgien.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

        if pyautogui.pixelMatchesColor(1150,420, (255,205,0)):
            
            x, y = pyautogui.locateCenterOnScreen('ansDeutschland.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

        if pyautogui.pixelMatchesColor(1150,420, (0,102,0)):
            
            x, y = pyautogui.locateCenterOnScreen('ansKenia.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

        if pyautogui.pixelMatchesColor(1150,420, (47,159,50)):
            
            x, y = pyautogui.locateCenterOnScreen('ansMalawi.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

        if pyautogui.pixelMatchesColor(1150,420, (223,54,2)):
            
            x, y = pyautogui.locateCenterOnScreen('ansUganda.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

#----------------------------------------------------------------------------------------------------------------------

## gray
        
    if pyautogui.pixelMatchesColor(919,271, (238,238,238)):
        
        if pyautogui.pixelMatchesColor(1150,420, (169,215,243)):
            
            x, y = pyautogui.locateCenterOnScreen('ansBotswana.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

        if pyautogui.pixelMatchesColor(1150,420, (237,17,40)):
            
            x, y = pyautogui.locateCenterOnScreen('ansChile.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

        if pyautogui.pixelMatchesColor(1150,410, (20,66,142)):
            
            x, y = pyautogui.locateCenterOnScreen('ansCostaRica.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

        if pyautogui.pixelMatchesColor(1100,300, (34,122,201)):
            
            x, y = pyautogui.locateCenterOnScreen('ansEstland.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

        if pyautogui.pixelMatchesColor(1010,347, (13,84,157)):
            
            x, y = pyautogui.locateCenterOnScreen('ansFinnland.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

        if pyautogui.pixelMatchesColor(1150,400, (237,21,30)):
            
            x, y = pyautogui.locateCenterOnScreen('ansOesterreich.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

#----------------------------------------------------------------------------------------------------------------------

## red
        
    if pyautogui.pixelMatchesColor(919,271, (255,0,0)):
        
        if pyautogui.pixelMatchesColor(1059,356, (217,186,0)):
            
            x, y = pyautogui.locateCenterOnScreen('ansAegypten.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

        if pyautogui.pixelMatchesColor(1150,420, (255,179,0)):
            
            x, y = pyautogui.locateCenterOnScreen('ansArmenien.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

        if pyautogui.pixelMatchesColor(1150,420, (255,0,0)):
            
            x, y = pyautogui.locateCenterOnScreen('ansChina.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

        if pyautogui.pixelMatchesColor(1150,420, (0,155,0)):
            
            x, y = pyautogui.locateCenterOnScreen('ansMauritius.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

        if pyautogui.pixelMatchesColor(1115,350, (255,255,255)):
            
            x, y = pyautogui.locateCenterOnScreen('ansVereinigtearab.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

#----------------------------------------------------------------------------------------------------------------------

## red2
        
    if pyautogui.pixelMatchesColor(919,271, (238,22,31)):
        
        if pyautogui.pixelMatchesColor(1039,376, (0,168,80)):
            
            x, y = pyautogui.locateCenterOnScreen('ansLibanon.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

        if pyautogui.pixelMatchesColor(975,343, (255,255,255)):
            
            x, y = pyautogui.locateCenterOnScreen('ansTuerkei.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

#----------------------------------------------------------------------------------------------------------------------

## red3
        
    if pyautogui.pixelMatchesColor(919,271, (211,8,49)):
        
        if pyautogui.pixelMatchesColor(1150,420, (211,8,49)):
            
            x, y = pyautogui.locateCenterOnScreen('ansMalediven.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

        if pyautogui.pixelMatchesColor(1150,420, (0,106,77)):
            
            x, y = pyautogui.locateCenterOnScreen('ansTogo.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

#----------------------------------------------------------------------------------------------------------------------

## red4
        
    if pyautogui.pixelMatchesColor(919,271, (239,39,41)):
        
        if pyautogui.pixelMatchesColor(1150,420, (239,39,41)):
            
            x, y = pyautogui.locateCenterOnScreen('ansNorwegen.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

        if pyautogui.pixelMatchesColor(1150,420, (0,165,222)):
            
            x, y = pyautogui.locateCenterOnScreen('ansLuxemburg.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

#----------------------------------------------------------------------------------------------------------------------

## green
        
    if pyautogui.pixelMatchesColor(919,271, (0,136,80)):
        
        if pyautogui.pixelMatchesColor(1150,420, (233,8,41)):
            
            x, y = pyautogui.locateCenterOnScreen('ansBenin.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

        if pyautogui.pixelMatchesColor(1150,420, (0,136,80)):
            
            x, y = pyautogui.locateCenterOnScreen('ansNigeria.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

#----------------------------------------------------------------------------------------------------------------------

## green_dark
        
    if pyautogui.pixelMatchesColor(919,271, (0,106,77)):  

        if pyautogui.pixelMatchesColor(971,425, (181,20,49)):
            
            x, y = pyautogui.locateCenterOnScreen('ansTurkmenistan.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

        if pyautogui.pixelMatchesColor(1050,335, (244,37,63)):
            
            x, y = pyautogui.locateCenterOnScreen('ansBangladesch.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

#----------------------------------------------------------------------------------------------------------------------

## green_dark2
        
    if pyautogui.pixelMatchesColor(919,271, (0,98,48)):
        
        if pyautogui.pixelMatchesColor(1150,420, (0,98,48)):
            
            x, y = pyautogui.locateCenterOnScreen('ansMauretanien.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

        if pyautogui.pixelMatchesColor(1150,420, (221,31,25)):
            
            x, y = pyautogui.locateCenterOnScreen('ansPortugal.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

#----------------------------------------------------------------------------------------------------------------------

## blue
        
    if pyautogui.pixelMatchesColor(919,271, (0,26,160)):
        
        if pyautogui.pixelMatchesColor(1150,420, (211,8,49)):
            
            x, y = pyautogui.locateCenterOnScreen('ansHaiti.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)

        if pyautogui.pixelMatchesColor(1150,420, (0,150,65)):
            
            x, y = pyautogui.locateCenterOnScreen('ansLesotho.png', region=(900,460,280,330), confidence=0.8)

            time.sleep(np.random.uniform(0.2,0.5))

            click(x,y)
            
#----------------------------------------------------------------------------------------------------------------------
