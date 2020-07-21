from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import os

driver = webdriver.Chrome(ChromeDriverManager().install())
url = 'https://web.whatsapp.com/'
driver.get(url)

time.sleep(10)
# Open whatsapp and scan qr by 10 sec

name = input("Enter the receiver's name\n")
#Opening the chat box
search_box = driver.find_element_by_class_name('_3FRCZ')
search_box.send_keys(name)
search_box.send_keys(Keys.ENTER)



#### For simple messages
#message_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
#message_box.send_keys(Keys.ENTER)




# Path is the folder in which the images you want to upload are present.
# In case you want to send only one img, do so by removing the for loop.
path = input('Enter the complete path to the folder\n')
os.chdir(path)         #Change directory
lis_files = os.listdir()       # List files in that directory
time.sleep(2)
# The loop takes all files in folder in the position file
for file in lis_files:
    img_pin = driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]')
    img_pin.click()

    time.sleep(2)

    gallery = driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/span/div/div/ul/li[1]/button/input')

    gallery.send_keys(path + '/' +file)

    time.sleep(10)


    ### Caption for images etc only. If a normal file, cant be used
    #caption = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div[1]/span/div/div[2]/div/div[3]/div[1]/div[2]')
    #caption.send_keys('Automated Send... Enjoy ')



    send = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div')
    send.click()
    time.sleep(5)
