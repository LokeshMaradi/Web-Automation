from selenium import webdriver
url="https://www.instagram.com/"
user=input("Enter the username of the id:")
user_id=url+user
browser=webdriver.Chrome("C:\\Users\\chromedriver.exe")
browser.get(user_id)
try:
	bio=browser.find_element_by_xpath('//*[@class="-vDIg"]/span[1]').get_attribute('textContent')
	path='C:\\Users\\'+user+'bio.txt'
	fp=open(path,'a')
	fp.write(bio)
	fp.close()
except:
	print("Bio not found")


