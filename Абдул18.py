import time
import keyboard
import pyautogui
while True:
    print("Ведите пароль:")
    par=input("")
    if par=="Ёлки иголки":
       print("Доступ разрешён.")
       print("Добро пожаловать")
       time.sleep(1)
       print("-А на каком я сайте?")
       time.sleep(1)
       print("Por...")
       time.sleep(1)
       print("-Я понел.")
       time.sleep(1)
       print("*Выход*")
       time.sleep(1)
    elif par=="Лололошка топ":
       print("Это да, но это не пароль")
       print("Доступ отклонён")
    if par=="Я незнаю":
       print("Блин я теперь забыл его(")
    elif par=="Смешарики топ":
       print("Согласен тебе разрешён доступ.")
       print("Добро пожаловать")
    if par=="Снег":
       print("...")
       print("Неа лёд")
       print("Доступ отклонён")
    elif par=="Скибиди доп ес":
       print("Туалет, чтоли?")
       print("Ща камеру достану")
       print("Доступ отклонён")
    if par=="Новогодняя песня":
       print("Окей ща будет")
       pyautogui.moveTo(1750,5)
       time.sleep(1)
       pyautoguipg.click(button="left")
       time.sleep(1)
       pyautogui.moveTo(10,900)
       time.sleep(1)
       pyautogui.doubleClick()
       pyautogui.moveTo(500,910)
       time.sleep(1)
       pyautogui.click(button="left")
       time.sleep(1)
       keyboard.write("https://www.youtube.com/watch?v=DWG74q_LjLs")
       pyautogui.press("enter")