from selenium import webdriver
import pandas as pd,time
browser=webdriver.Chrome('C:\\Users\\chromedriver.exe')
browser.get('https://twitter.com/explore/tabs/trending')
time.sleep(15)
span_list=browser.find_elements_by_tag_name('span')
t=[]
for i in span_list:
	tex=i.text
	if tex.startswith('#') and tex not in t:
		t.append(tex)

urls=[]
for i in t:
	url='https://twitter.com/search?q=%23'+i[1:]+'&src=trend_click'
	urls.append(url)

dic={'trend':t,'Url':urls}
df=pd.DataFrame(dic)
df.to_csv('C:\\Users\\twitter.csv',index=False)
print("Done")
