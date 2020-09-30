import selenium
import sys
import os
import codecs
from bs4 import BeautifulSoup
import re
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import pyperclip
import mechanize
import cookielib
import xml.etree.ElementTree
import requests
#declarar navegador



br = mechanize.Browser(factory=mechanize.RobustFactory())

cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

chromedriver = 'C:\\chromedriver.exe'
browser = webdriver.Chrome(chromedriver)




paginas = codecs.open('pages.txt', encoding='iso-8859-1')

br.set_handle_robots(False)
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_debug_responses(True)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
requests.packages.urllib3.disable_warnings()
jar = cookielib.CookieJar()
url='https://accounts.google.com/ServiceLogin?sacu=1&continue=https%3A%2F%2Fwww.blogger.com%2Fblogger.g%3FblogID%3D1145570540015990153&hl=es&service=blogger#identifier'




browser.set_page_load_timeout(30)

browser.get(url)
time.sleep(28)

    
    
   
   
    
  


for p in paginas.read().split('\n'):
    r = br.open(p)
    respuesta=br.response().read()
    soup = BeautifulSoup(respuesta)
   

    for title in soup.find_all("h2", {"class":"post-title entry-title blogpost-title"}):
        avtitle=title.get_text()
        avs=avtitle.encode('utf-8')
        tits=re.sub('<[A-Za-z\/][^>]*>', '', avs)
        print ''.join(tits)
        time.sleep(2.6)

        for node in soup.find_all("div", {"class":"post-body entry-content post_content"}):
            pyperclip.copy(tits)
            browser.execute_script('location.href="javascript: window.alert = function(x) {console.log(x)}; window.confirm = function(){return true;};";')
            time.sleep(0.3)
            
            browser.get('https://www.blogger.com/blogger.g?blogID=1962518881400773159')
            time.sleep(3)
            browser.execute_script("var field = document.getElementsByClassName('blogg-button blogg-primary');field[0].click() ;")
            time.sleep(5.6)
        
          
            
           
                                                                 
            browser.find_element_by_xpath("//input[@class='OAVLIQC-F-b titleField textField OAVLIQC-F-a']").send_keys(Keys.CONTROL, 'v')
            
            time.sleep(2.4)
            xd=node.encode('iso-8859-1')
            pyperclip.copy(xd)
            time.sleep(2.6)
            browser.execute_script("var field = document.getElementsByClassName('blogg-button blogg-collapse-left selected');field[0].click() ;")
            time.sleep(0.9)
            inputtt=browser.find_element_by_xpath("//textarea[@class='htmlBox']").send_keys(Keys.CONTROL, 'v')
            time.sleep(2.3)
                    
               
            browser.execute_script("var inputs = document.getElementsByClassName('blogg-button OAVLIQC-U-s'); for(var i=0; i<inputs.length;i++) { inputs[i].click(); }")
            time.sleep(2.4)
           # browser.execute_script("javascript:document.getElementsByTagName('a')[31].click();")
            #time.sleep(3.2)
            #browser.execute_script("javascript:document.getElementsByTagName('a')[32].click();")
            #time.sleep(1.2)
            #browser.execute_script("javascript:document.getElementsByTagName('a')[31].click();")
            #time.sleep(2)
            #browser.execute_script("javascript:document.getElementsByTagName('a')[32].click();")
            #time.sleep(1.6)
            browser.execute_script("var field = document.getElementsByClassName('blogg-button blogg-primary');field[0].click() ;")
            time.sleep(2.9)
            try:
                time.sleep(0.4)
                alert = browser.switch_to_alert()
                time.sleep(0.6)
                alert.accept()
            except:pass
            
            time.sleep(0.8)
            browser.get('https://www.google.com.mx/?gws_rd=ssl')
            time.sleep(1.2)
           

            






            
        
