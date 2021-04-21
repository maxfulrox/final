# python package
import csv
import time
import random
import sys
import subprocess
import time
import mysql.connector 

# subprocess package
from subprocess import Popen

# selenium package
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import WebDriverException

# connection sql
try:
    conn = mysql.connector.connect(
        user="fulrox",
        password="Maximum-34",
        host="54.37.157.139",
        port=3306,
        database="RTX",
    )

except mysql.connector.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

# configurer webdriver
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"
driver = webdriver.Chrome(executable_path='./drivers/chromedriver')
wait = WebDriverWait(driver, 20)

# argument
url = ( sys.argv[1] )

# variable
mail = ( sys.argv[2] )
mdp = ( sys.argv[3] )
paypalmail = ( sys.argv[4] )
paypalmdp = ( sys.argv[5] )
credit = ( sys.argv[6] )
iduser = ( sys.argv[7] )

# ouverture + cookies
driver.get(url)
wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='rgpd-btn-index-accept']")))
driver.find_element_by_xpath("//*[@id='rgpd-btn-index-accept']").click()

# panier

driver.find_element_by_xpath("//*[@id='add-product']").click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='popup-add']/div[1]/p[3]/a[1]/i")))
driver.find_element_by_xpath("//*[@id='popup-add']/div[1]/p[3]/a[1]/i").click()
time.sleep(2)
wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='to-order']/a")))
driver.find_element_by_xpath("//*[@id='to-order']/a").click()

# connexion
wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='login']")))
driver.find_element_by_xpath("//*[@id='login']").send_keys(mail)
driver.find_element_by_xpath("//*[@id='login_pass']").send_keys(mdp)
driver.find_element_by_xpath("//*[@id='form_login']/div/button").click()
time.sleep(2)
wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='cart-delivery-content']/div/div[5]/a")))
driver.find_element_by_xpath("//*[@id='cart-delivery-content']/div/div[5]/a").click()

# payement
wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='cart-payment-content']/div[1]/div[1]/table/tbody/tr[4]/td[1]/input")))
driver.find_element_by_xpath("//*[@id='cart-payment-content']/div[1]/div[1]/table/tbody/tr[4]/td[1]/input").click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='order_submit']")))
driver.find_element_by_xpath("//*[@id='order_submit']").click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='pl-pm-paypal_3-payBtn']")))
driver.find_element_by_xpath("//*[@id='pl-pm-paypal_3-payBtn']").click()

# paypal
#wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='email']")))
#driver.find_element_by_xpath("//*[@id='email']").send_keys(paypalmail)
#driver.find_element_by_xpath("//*[@id='btnNext']").click()
#wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='password']")))
#driver.find_element_by_xpath("//*[@id='password']").send_keys(paypalmdp)
#driver.find_element_by_xpath("//*[@id='btnLogin']").click()
#wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='acceptAllButton']")))
#driver.find_element_by_xpath("//*[@id='acceptAllButton']").click()
#wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='payment-submit-btn']")))

#driver.find_element_by_xpath("//*[@id='payment-submit-btn']").click()
driver.close()

print("GG +1")

credit = int(credit)
credit = credit - 1
cur.execute("UPDATE info SET CREDIT = (%s) where ID = (%s)", (credit, iduser))
conn.commit()

f = open("url.txt", "a")
f.write("\n")
f.write(url)
f.close()