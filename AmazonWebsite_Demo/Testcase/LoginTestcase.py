import lemoncheesecake.api as lcc
from lemoncheesecake.matching import *
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url="https://www.amazon.in/"
search_tb="//input[@id='twotabsearchtextbox']"
search_btn="//input[@id='nav-search-submit-button']"
path="E:\AmazonWebsite_Demo\Driver\geckodriver.exe"
#path="../Driver/geckodriver.exe"
#relative_path = os.path.relpath(path)


@lcc.test("Login to the page")
def navigatetopage():
	driver = webdriver.Firefox(executable_path=path)
	driver.get(url)
	

@lcc.test("Verify if title is correct or not")
def verifytitle(title):
	assert f"{title}" in driver.title



#as not knowing how to pass the instance of current webdriver in python I have again launch the webdriver for this testcase
@lcc.test("Search for a particular product")
def searchproduct(product):
	driver = webdriver.Firefox(executable_path=path)
	driver.get(url)
	element=driver.find_element_by_xpath(search_tb)
	element.send_keys(product)
	button=driver.find_element_by_xpath(search_btn)
	button.click();

navigatetopage()
#verifytitle("Amazon")
searchproduct("Headphones")



