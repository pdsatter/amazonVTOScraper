from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def startScraper(shift_choice, start_time, day):
    type_shift = shift_choice
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get('https://atoz.amazon.work/login')
    print('start scraper')

    # Task 1: Log in for user:  NEEDS VERIFICATION SO USER HAS TO DO THIS
    # if password is wrong, let user try again.

    # inputs:
    # Enter Password:
    # Enter User:

    # selenium: input password in box
    # go to username
    # input username in box
    # hit enter

    # Task 2:

    # Check if page is past password page
    # redirect user to VTO page
    # Ask user to input:
    #   Day and time to VTO
    try:
        element = WebDriverWait(driver, 120).until(EC.url_contains('atoz.amazon.work'))
        print('Now logged in')
    except:
        print('2 minutes passed: Timed out. Restart program if needed')

    # redirect user to VTO/VET page
    if type_shift == 'VTO':
        driver.get('https://atoz.amazon.work/time/optional')
    elif type_shift == 'VET':
        driver.get('https://atoz.amazon.work/time/extra')

    # Task 3:
    # run loop until VTO is taken

    # In loop:
    #   click page every 10 seconds to prevent logout
    #   check if VTO is available, if it is then accept it
    #   if VTO is taken, close program

    # xpath of no VET //*[@id="atoz-time-page-root"]/div/div/div[2]/div
    # xpath of no VTO //*[@id="atoz-time-page-root"]/div/div/div[2]/div/div[1]/div[2]

    # BLOCk
    # full xpath: /html/body/div[1]/div[2]/div/div/div/div[2]/div[2]/ul/div/a/div/div[2]
    # xpath: //*[@id="7/12/2021"]/ul/div/a/div/div[2]
    # outer html: <div class="row-eq-height"><div class="col col-xs-8"><div class="time-display">18:30 - 22:30</div><div class="duration-display"> (4 hrs)</div><div class="workgroup-display">Amtran Sortation</div></div><div class="col right col-xs-4"><div class="pull-right status-action"><div class="st-sprite st-button-arrow-icon active-arrow"></div></div></div></div>
    # selector: #\37 \/12\/2021 > ul > div > a > div > div:nth-child(2)

    # LINK:
    # xpath: //*[@id="7/12/2021"]/ul/div/a
    # full xpath: /html/body/div[1]/div[2]/div/div/div/div[2]/div[2]/ul/div/a
    # outer html: <a class="list-group-item " data-omniture-link="View NEW_VET - Click" href="/time/extra/amzn.ls.opportunityide7804896-1213-454b-a2ab-48032dd31100"><div class="container"><div class="row-eq-height"><div class="status-action status-left"><div class="row-eq-height"><div class="hidden"></div><div class="status-display"></div></div></div><div class="drop-row-display"></div></div><div class="row-eq-height"><div class="col col-xs-8"><div class="time-display">18:30 - 22:30</div><div class="duration-display"> (4 hrs)</div><div class="workgroup-display">Amtran Sortation</div></div><div class="col right col-xs-4"><div class="pull-right status-action"><div class="st-sprite st-button-arrow-icon active-arrow"></div></div></div></div></div></a>
    if type_shift == 'VET':
        while True:
            try:
                xpathVET = "//*[contains(text(), {})".format(day)  # TODO: put in xpath
                # element2VET = driver.find_elements_by_xpath(xpathVET)  # finds path with time

                # element = WebDriverWait(driver, 20).until(driver.find_element_by_xpath(xpathVET))
                # wait for option to pop up
                assert WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.XPATH, xpathVET))).click()
                # causes exception if not true, else breaks and continues
                break

            except:
                driver.refresh()  # prevent time out by server by refreshing page

    if type_shift == 'VTO':
        while True:
            try:
                xpathVTO = "//*[contains(text(), {})".format(day)  # TODO: put in xpath
                # element2VTO = driver.find_elements_by_xpath(xpathVTO)  # finds path with time
                # wait for option to pop up
                assert WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.XPATH, xpathVTO))).click()
                # causes exception if not true, else breaks and continues
                break
            except:
                driver.refresh()  # prevent time out by refreshing page

    # Task 4
    # click accept button

    # ACCEPT BUTTON
    # xpath: //*[@id="atoz-time-page-root"]/div/div/div/div[3]/div/div[5]/div/button
    # full xpath: /html/body/div[1]/div[2]/div/div/div/div/div[3]/div/div[5]/div/button
    # outer html: <button class="btn btn-primary btn-half-block" data-omniture-link="Accept NEW_VET - Click">Accept</button>
    # JS path: document.querySelector("#atoz-time-page-root > div > div > div > div.center-block.centered-page.opportunity-detail > div > div.button-footer > div > button")

    if type_shift == 'VET':
        idVET = ''  # TODO: insert ID
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, idVET))).click()
        print('VET accepted')
        driver.close()
    elif type_shift == 'VTO':
        idVTO = ''  # TODO: insert ID
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, idVTO))).click()
        print('VET accepted')
        driver.close()
