from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import JavascriptException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import PIL
import pickle
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import os



def storeVar():
    global base_url
    base_url= E3.get()
    global email
    email=E1.get()
    global Pss_word
    Pss_word=E2.get()
    Tk.destroy(top)

top = tk.Tk()
top.geometry("568x294")
top.title("Connect-Me.In")
top.iconbitmap('C:\Users\walmart\PycharmProjects\connect_me\handshake_LvS_icon.ico')
image = Image.open('C:/Users/walmart/PycharmProjects/connect_me/business_photo.gif')
photo = ImageTk.PhotoImage(image)
L0 = Label(top, image=photo)
L0.place(x=0, y=0, relwidth=1, relheight=1)

l1 = Label(top, text="Make sure to watch tutorial for best results",).grid(row=1, column=2)
L2 = Label(top, text="EMAIL",).grid(row=1,column=0)
L3 = Label(top, text="PASSWORD",).grid(row=2,column=0)
L4 = Label(top, text="URL",).grid(row=3,column=0)

E1 = Entry(top, bd =5)
E1.grid(row=1,column=1)

E2 = Entry(top, bd =5)
E2.grid(row=2,column=1)

E3 = Entry(top, bd =5)
E3.grid(row=3,column=1)



submit = Button(top, text= "Let's Connect!", command = storeVar)
submit.grid(row=4, column=1)

top.mainloop()
RelPath = os.path.dirname(__file__)
driver = webdriver.Chrome(executable_path=RelPath +"\chromedriver.exe")

driver.maximize_window()



driver.get("https://www.linkedin.com/uas/login")
time.sleep(5)

driver.find_element_by_name('session_key').send_keys(email)
driver.find_element_by_class_name('password').send_keys(Pss_word)
driver.find_element_by_name('signin').click()


time.sleep(10)

driver.get(base_url)


time.sleep(10)
def connect_me():
    sendNow = driver.find_element_by_css_selector(".button-primary-large.ml1")
    driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", sendNow)
    time.sleep(4)
    return

def the_script():
    try:
        driver.execute_script("document.getElementsByClassName('search-result__actions--primary button-secondary-medium m5')[0].click();")
        connect_me()

    except (NoSuchElementException, JavascriptException) as e:
        pass

    try:
        driver.execute_script("document.getElementsByClassName('search-result__actions--primary button-secondary-medium m5')[1].click();")
        connect_me()
    except (NoSuchElementException, JavascriptException) as e:
        pass
    try:
        driver.execute_script("document.getElementsByClassName('search-result__actions--primary button-secondary-medium m5')[2].click();")
        connect_me()
    except (NoSuchElementException, JavascriptException) as e:

        pass
    try:
        driver.execute_script("document.getElementsByClassName('search-result__actions--primary button-secondary-medium m5')[3].click();")
        connect_me()

    except (NoSuchElementException, JavascriptException) as e:

        pass
    time.sleep(5)

    driver.execute_script("window.scrollTo(0, 750)")
    time.sleep(5)
    try:
        driver.execute_script(
            "document.getElementsByClassName('search-result__actions--primary button-secondary-medium m5')[4].click();")
        connect_me()
    except (NoSuchElementException, JavascriptException) as e:

        pass
    try:
        driver.execute_script(
            "document.getElementsByClassName('search-result__actions--primary button-secondary-medium m5')[5].click();")
        connect_me()
    except (NoSuchElementException, JavascriptException) as e:

        pass
    try:
        driver.execute_script(
            "document.getElementsByClassName('search-result__actions--primary button-secondary-medium m5')[6].click();")
        connect_me()

    except (NoSuchElementException, JavascriptException) as e:

        pass
    time.sleep(5)
    driver.execute_script("window.scrollTo(0, 1500)")
    time.sleep(5)

    try:
        driver.execute_script(
            "document.getElementsByClassName('search-result__actions--primary button-secondary-medium m5')[7].click();")
        connect_me()
    except (NoSuchElementException, JavascriptException) as e:

        pass
    try:
        driver.execute_script(
            "document.getElementsByClassName('search-result__actions--primary button-secondary-medium m5')[8].click();")
        connect_me()
    except (NoSuchElementException, JavascriptException) as e:

        pass
    try:
        driver.execute_script(
            "document.getElementsByClassName('search-result__actions--primary button-secondary-medium m5')[9].click();")
        connect_me()

    except (NoSuchElementException, JavascriptException) as e:

        pass
    time.sleep(5)
    return
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '2')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)

time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '3')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '4')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '5')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '6')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)
the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '7')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '8')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '9')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '10')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '11')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '12')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '13')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '14')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '15')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '16')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '17')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '18')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '19')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '20')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '21')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '22')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '23')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '24')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '25')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '26')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '27')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '28')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '29')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '30')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '31')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '32')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '33')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '34')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '35')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '36')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '37')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '38')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '39')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '40')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '41')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '42')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '43')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '44')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '45')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '46')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '47')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '48')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '49')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

nextPage = driver.find_element_by_xpath("//button[contains(text(), '51')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '52')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '53')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '54')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '55')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)


the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '56')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '57')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '58')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '59')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '60')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '61')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '62')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '63')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '64')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '65')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '66')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '67')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '68')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '69')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '70')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '71')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '72')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '73')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '74')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '75')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '76')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '77')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '78')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '79')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '80')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '81')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '82')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '83')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '84')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '85')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '86')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '87')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '88')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '89')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '90')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '91')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '92')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '93')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '94')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '95')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '96')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '97')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '98')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)

the_script()

nextPage = driver.find_element_by_xpath("//button[contains(text(), '99')]")
driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].click();", nextPage)
time.sleep(5)