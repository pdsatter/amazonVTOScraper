from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tkinter as tk
from selenium.webdriver.common.action_chains import ActionChains
from flask import Flask, request, render_template
import Application

#  app = Flask('Amazon Time Web-Scraper')


#  @app.route('/')
#  def homepage():
#      return render_template('homepage.html')


if __name__ == '__main__':
    #  app.run()
    print('done')


'''
NOTES: 

Commands:

driver.get('link')                                          Opens website
driver.close() / driver.quit()                              closes website
driver.title                                                gets title

search = driver.find_element_by_name("name of object")      Finds Object
objects = search.find_elements_by_...("Type of Object")     Finds Stuff by type
    Search:
    first: id (unique), then: name, worst: class

search.send_keys("text")                                    Uses Object and sends text
search.send_keys(Keys.RETURN)                               Hits enter after inputting text

time.sleep(10)                                              Does nothing for this time
driver.page_source)                                         Entire source code for page

link.Click()                                                Clicks on object
driver.back()                                               goes back a page

driver.back()                                               goes back a page

Made By: pdsatter https://github.com/pdsatter
'''

''' Before click on opportunity
<div id="7/11/2021"> </div>      # date displayed, use this to find correct day
<div class="time-display">18:30 - 22:30</div>
<a class="list-group-item "data-omniture-link="View NEW_VET - Click" href="/time/extra/amzn.ls.opportunityid1125bde9-133b-47c3-a25f-380c575afa20">
    <div class ="container">
        <div class="status-action status-left">
            <div class="hidden" wfd-invisible="true"></div>
'''
''' After click, then button accept
    <button class="btn btn-primary btn-half-block" data-omniture-link="Accept NEW_VET - Click">Accept</button> # ACCEPTS VET

'''

'''
<div class="list-group">
<div><li class="list-group-item full">
<div class="container">

<body>
    <div class ="employees




SHOWS STATUS OF TOP (FULL)
<div class="row-eq-height">                     (flex) ACTION?
    <div class="status-action status-left">
    <div class="row-eq-height">
    <div class="shift-sprite stop-secondary-sm">
    </div>
    <div class="status-display">Full</div>       CHECKS IF FULL OR (AVAILABLE)
    </div>
    </div>
    <div class="drop-row-display"></div>
</div>

SHOWS TIME
<div class="row-eq-height">
    <div class="col col-xs-8">
        <div class="time-display">03:00 - 07:00</div>                             TIME OF SHIFT!!!!!!!!!!!!!!
        <div class="duration-display"> (4 hrs)</div>
        <div class="workgroup-display">Amtran Sortation</div>
    </div>
    <div class="col right col-xs-4">
        <div class="pull-right status-action">
            <div>
            <div class="hidden" data-omniture-link=""></div>
            <div class="hidden"></div>
        </div>
    </div>
</div></div></div></li><div></div></div></div>


'''
