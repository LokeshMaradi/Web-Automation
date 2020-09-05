from selenium import webdriver
browser=webdriver.Chrome("C:\\Users\\chromedriver.exe")
user_name=input("Enter you user_name:")
password=input("Enter your password")
browser.get(https://www.facebook.com/"")
e=browser.find_element_by_id("email")
e.send_keys(user_name)
p=browser.find_element_by_id("pass")
p.send_keys(password)
log=browser.find_element_by_id("u_0_b")
p.click()

xp=browser.find_element_by_xpath('//*[@id="home_birthdays"]/div/div/div/div/a/div/div/span/span[2]').get_attribute("textContent")
xp=int(xp[0])
browser.get("https://www.facebook.com/events/birthdays/")
bday_list=browser.find_elements_by_xpath("//*[@class ='enter_submit uiTextareaNoResize uiTextareaAutogrow uiStreamInlineTextarea inlineReplyTextArea mentionsTextarea textInput']") 
c=0
for i in bday_list:
	idb=str(i.get_attribute("id"))
	x=browser.find_element_by_xpath('//*[id="'+idb+'"]')
	x.send_keys("Happy Birthdayyy")
	x.send_keys(Keys.RETURN)
	c=c+1
	if(c>xp):
		break;
