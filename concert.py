from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import re

# Windows users need to specify the path to chrome driver you just downloaded.
# You need to unzip the zipfile first and move the .exe file to any folder you want.
# driver = webdriver.Chrome(r'path\to\where\you\download\the\chromedriver.exe')
driver = webdriver.Chrome()

driver.get("http://www.espn.com/nba/statistics/rpm/_/sort/RPM")

# Windows users need to open the file using 'wb'
# csv_file = open('reviews.csv', 'wb')
csv_file = open('nba.csv', 'w')
writer = csv.writer(csv_file)
# Page index used to keep track of where we are.
index = 1
while True and index < 5:
# first check 5 pages
	try:
		print("Scraping Page number " + str(index))
		index = index + 1
		# Find all the reviews on the page
		wait_event = WebDriverWait(driver, 10)
		players = wait_event.until(EC.presence_of_all_elements_located((By.XPATH,
									'//tr[@class="oddrow"]')))

		for player in players:
			# Initialize an empty dictionary for each review
			man = player.find_elements_by_tag_name('td')
			player_dict = {}
			# Use relative xpath to locate the title, text, username, date.
			# Once you locate the element, you can use 'element.text' to return its string.
			# To get the attribute instead of the text of each element, use 'element.get_attribute()'
			name = man[2].text

			# text = player.find_element_by_xpath('.//span[@itemprop="reviewBody"]').text
			# username = player.find_element_by_xpath('.//span[@itemprop="author"]').text
			# date_published = player.find_element_by_xpath('.//meta[@itemprop="datePublished"]').get_attribute('content')
			# rating = player.find_element_by_xpath('.//span[@itemprop="ratingValue"]').text

			player_dict['player'] = name
			# player_dict['content'] = text
			# player_dict['username'] = username
			# player_dict['date_published'] = date_published
			# player_dict['rating'] = rating
			writer.writerow(player_dict.values())

		players = wait_event.until(EC.presence_of_all_elements_located((By.XPATH,
									'//table[@tr="evenrow"]')))			
		for player in players:
			# Initialize an empty dictionary for each review
			man = player.find_elements_by_tag_name('td')
			player_dict = {}
			# Use relative xpath to locate the title, text, username, date.
			# Once you locate the element, you can use 'element.text' to return its string.
			# To get the attribute instead of the text of each element, use 'element.get_attribute()'
			name = man[2].text

			# text = player.find_element_by_xpath('.//span[@itemprop="reviewBody"]').text
			# username = player.find_element_by_xpath('.//span[@itemprop="author"]').text
			# date_published = player.find_element_by_xpath('.//meta[@itemprop="datePublished"]').get_attribute('content')
			# rating = player.find_element_by_xpath('.//span[@itemprop="ratingValue"]').text

			player_dict['player'] = name
			# player_dict['content'] = text
			# player_dict['username'] = username
			# player_dict['date_published'] = date_published
			# player_dict['rating'] = rating
			writer.writerow(player_dict.values())

		# Locate the next button on the page.
		wait_button = WebDriverWait(driver, 10)
		next_button = wait_button.until(EC.element_to_be_clickable((By.XPATH,
									'.//div[@class = "jcarousel-next"]')))
		
		next_button.click()

	except Exception as e:
		print(e)
		csv_file.close()
		driver.close()
		break
