from selenium import webdriver
import time

driver = webdriver.Chrome("C:\\Users\\bhoom\\Downloads\\chromedriver_win32\\chromedriver")
driver.get("http://127.0.0.1:5000/")
driver.execute_script("window.scrollTo(0, 200)") 
gender=driver.find_element("id","gender")
gender.send_keys("0")
age=driver.find_element("id","age")
age.send_keys("80")
hypertension=driver.find_element("id","hypertension")
hypertension.send_keys("0")
heart_disease=driver.find_element("id","heart_disease")
heart_disease.send_keys("0")
ever_married=driver.find_element("id","ever_married")
ever_married.send_keys("1")
work_type=driver.find_element("id","work_type")
work_type.send_keys("3")
Residence_type=driver.find_element("id","Residence_type")
Residence_type.send_keys("1")
avg_glucose_level=driver.find_element("id","avg_glucose_level")
avg_glucose_level.send_keys("105.92")
bmi=driver.find_element("id","bmi")
bmi.send_keys("23.7")
smoking_status=driver.find_element("id","smoking_status")
smoking_status.send_keys("3")
time.sleep(5)
driver.find_element("id","submit").click()
time.sleep(5)
driver.quit()