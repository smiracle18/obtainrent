from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from env import *


driver = webdriver.Chrome("C:\\Users\\susha\\Desktop\\kncChain\\driver\\chromedriver.exe")

driver.get(knc_login_url)

driver.find_element_by_name("account").send_keys(knc_account)
driver.find_element_by_name("password").send_keys(knc_password)
time.sleep(1)
driver.find_element_by_css_selector(".login-submit button").click()
time.sleep(1)
driver.find_element_by_css_selector(".mui-popup-button-bold").click()
time.sleep(1)
driver.get(knc_machine_url)
time.sleep(1)

obtained_number = 0

while(True):
    #try except block
    try:
        #identify element
        obtain_button = driver.find_element_by_css_selector(".homenewshps i button")
        time.sleep(0.5)
        obtain_button.click()  
        time.sleep(1)
        obtained_number += 1
        print("Button exist rent obtained for: "+ str(obtained_number))
        time.sleep(2)
        driver.get(knc_machine_url)



        continue

    #NoSuchElementException thrown if not present
    except NoSuchElementException:
        print("Button not present")
        break



if obtained_number == 0:
    print("No rent obtained")

else:
    # Python code to Send mail once rent is obtained.
    # your Gmail account 
    import smtplib
    from email.message import EmailMessage

    
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()
    
    # Authentication
    s.login(mailer_account, mailer_password)
    

    # msg to be sent
    msg = EmailMessage()
    msg.set_content('Hello There! this is mail for your auto rent obtaining process. Total rent obtained: '+str(obtained_number))
    msg['Subject'] = 'Success: Rent Obtaining'
    msg['From'] = mailer_account
    msg['To'] = recipient_account
    
    # sending the mail
    s.send_message(msg)
    
    # terminating the session
    s.quit()









