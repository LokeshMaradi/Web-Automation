from selenium import webdriver
u=input("Enter the username of the person/page:")
url="https://www.instagram.com/"
browser=webdriver.Chrome("C:\\Userschromedriver.exe")
user=url+u
browser.get(user)
try:
	dp=browser.find_element_by_xpath('//*[@class="be6sR"]')
except:
	dp=browser.find_element_by_xpath('//*[@class="_6q-tv"]')
link=dp.get_attribute("src")
import urllib.request
path="D://"+u+".jpg"                                           #Here 'u' is the username 
urllib.request.urlretrieve(link,path)
print("Image has been dowloaded at"+path)
