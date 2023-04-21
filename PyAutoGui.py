#Laboratorio com robo via interface

#Biblioteca
import pyautogui

#Esse foi um texte para realizar uma pesquisa no chatGPt 
#Lembre-se que é possivél passar a posição para uma variável:
#Ex.: posicao_9 = pyautogui.position() 
pyautogui.moveTo(x=81, y=119); pyautogui.click()
pyautogui.PAUSE = 2
pyautogui.moveTo(x=97, y=222); pyautogui.doubleClick()
pyautogui.moveTo(x=769, y=952); pyautogui.click()
pyautogui.typewrite("Você acredita que Maria Madalena engravidou por meio de um espirito?   ")
pyautogui.moveTo(x=1128, y=942); pyautogui.click()

pyautogui.alert('Pesquisa realizada!')


