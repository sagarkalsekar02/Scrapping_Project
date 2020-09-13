import App
from selenium import webdriver
import time
import pdb
from dbconn import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#platform links Xpath
start="https://www.itv.com/hub/categories/children"
URL ='http://www.itv.com/hub/categories/'
cookies="//*[@id='cookie-message-accept']"
categories="//div[@class='nav-secondary__wrapper js-nav-secondary-wrapper']/ul/li/a"
titlelist="//*[@id='categories-list']/ul[@class='grid-list list-reset']/li[@class='grid-list__item width--one-half width--custard--one-third js-lazy is-lazy-processed']/a"
title="//div[@id='categories-list']/ul[@class='grid-list list-reset']/li[@class='grid-list__item width--one-half width--custard--one-third js-lazy is-lazy-processed'][{}]/a[@class='complex-link']/article/div[@class='media__body tout__body']/header/h3[@class='tout__title complex-link__target theme__target']"
cate="//*[@id='skip_to_main_content']/section[@class='block']/div[@class='block__wrapper']/div[@class='categories module module--under-nav js-categories']/h1[@class='module__heading']"
catlist=[]
status_dict={}


def platformlinks():
	driver = webdriver.Firefox()
	driver.get(URL)
	driver.maximize_window()
	d1.update_status('ScrappingStatus','Running')
	#time.sleep(10)
	#driver.close()
	ele = driver.find_element_by_xpath(cookies)
	ele.click()
	driver.get(start)
	cat = driver.find_elements_by_xpath(categories)
	count=0
	for elem in cat:
	    #pdb.set_trace()
	    catlist.append(elem.get_attribute("href"))

	for el1 in catlist:
		#pdb.set_trace()
		driver.get(el1)
		elems = driver.find_elements_by_xpath(titlelist)
		time.sleep(5)
		print(el1)
		for els in range(0,len(elems)):
			elink=elems[els].get_attribute("href")
			#elstitle=driver.find_element_by_xpath(title.replace("raw",str(els))).text
			target = driver.find_element_by_xpath(title.format(str(els+1)))
			driver.execute_script('arguments[0].scrollIntoView(true);', target)
			#elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, target)))
			time.sleep(0.5)
			driver.execute_script("window.scrollBy(0,-280)","") 
			elstitle=driver.find_element_by_xpath(title.format(str(els+1))).text
			categ=driver.find_element_by_xpath(cate).text
			d1.insert_platformlinks(str(el1),str(elink),str(elstitle),str(categ))
			count+=1
	d1.update_status('ProgramLinkScrapping','No')
	print(count)





def chk_status():
	op=d1.Scrapping_Status()
	if op.get('ProgramLinkScrapping') == 'Yes':
		platformlinks()
	elif op.get('DataScrapping') == 'Yes':
		print("DataScrapping")
	elif op.get('ProgramLinkScrapping') == 'No':
		print("No ProgramLinkScrapping")
	elif op.get('DataScrapping') == 'No':
		print("DataScrapping")






def main():
	#driver = webdriver.Firefox(executable_path="D:/python_practice/Selproj/geckodriver.exe")
	chk_status()
	
	#for elem in cat:
	#	catlist.append(elem.get_attribute("href"))
		#print(elem.get_attribute("href"))
	#print(catlist)
	




if __name__ == '__main__':
	main()


