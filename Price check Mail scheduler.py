from selenium import webdriver
import smtplib as s
import schedule
browser=webdriver.Chrome('C:\\Users\\chromedriver.exe')

def flipkart():
	browser.get('https://www.flipkart.com/oneplus-7-mirror-grey-256-gb/p/itmdbcd3dd156000')  #example site
	x=browser.find_element_by_xpath('//*[@class="_1vC4OE _3qQ9m1"]').text
	x=x[1:].split(',')
	p=""
	for i in x:
		p+=i
	return float(p)
a=flipkart()
p=32000
def mail():
	G=s.SMTP('smpt.gmail.com','587')
	G.starttls()
	e=input('Enter mail:')
	p=input('Password:')
	G.login(e,p)
	msg='You can buy now'
	sender=e
	dest='yourmail@gmail.com'
	G.sendmail(sender,dest,msg)
	G.quit()
def d():
	if(a<p):
		mail()
		print('Mail sent')
	else:
		print('Not yet')
#schedule.every().day.at('12:35').do(d)
schedule.every(10).seconds.do(d)
while True:
	schedule.run_pending()
