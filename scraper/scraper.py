import pickle
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('./driver/chromedriver')
driver.get('https://web.archive.org/web/20200315053301/https://coronavirus.1point3acres.com/en')

sleep(30)

states = ["New York", "Washington", "California", "Massachusetts",
          "Florida", "New Jersey", "Louisiana", "Colorado ", "Georgia",
          "Illinois", "Texas", "Pennsylvania", "Maryland", "Michigan",
          "Minnesota", "Tennessee", "Virginia", "Oregon", "Ohio",
          "Wisconsin", "Nevada", "Utah", "Connecticut", "North Carolina",
          "South Carolina", "Indiana", "Alabama", "Kentucky", "Iowa",
          "Arkansas", "Rhode Island", "New Mexico", "Arizona",
          "Nebraska", "New Hampshire", "Maine", "Vermont", "Mississippi",
          "Kansas", "Oklahoma", "Hawaii", "South Dakota", "Wyoming",
          "Missouri", "Montana", "Delaware", "Idaho", "Alaska", "North Dakota"]

m = {}

for state in states:
    m[state] = {}
    try:
        span = driver.find_element_by_xpath("//span[text()='{}']".format(state))
    except:
        continue
    driver.execute_script("arguments[0].click();", span)
    counties = driver.find_element_by_class_name("counties")
    text = counties.text
    data = text.split("\n")

    for i in range(0, len(data), 4):
        county = data[i]
        cases = data[i + 1].split("+")[0]
        m[state][county] = int(cases)

    driver.execute_script("arguments[0].click();", span)

pickle.dump(m, open("scraped.p", "wb"))