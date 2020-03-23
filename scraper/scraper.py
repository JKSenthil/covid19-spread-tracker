#!/usr/bin/env python3
import pickle

from extract import extract_counties_and_cases

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

    m[state] = extract_counties_and_cases(data, m[state])

    driver.execute_script("arguments[0].click();", span)

pickle.dump(m, open("scraped.p", "wb"))