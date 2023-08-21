import time

from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common .by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--headless=new')

check_in = input("Enter Check In Date as mmddyyyy")
check_out = input("Enter Check Out Date as mmddyyyy")

driver = webdriver.Chrome(options=options)
driver.get(f"https://www.makemytrip.com/hotels/hotel-listing/?_uCurrency=INR&checkin={check_in}&checkout={check_out}&city=CTXMY&country=IN&locusId=CTXMY&locusType=city&regionNearByExp=3&roomStayQualifier=1e0e&rsc=1e1e0e&searchText=Mysore&sort=reviewRating-desc")
last_height = driver.execute_script("return document.body.scrollHeight")
itemTargetCount = int(driver.find_element(By.XPATH, '//*[@id="seoH1DontRemoveContainer"]').text.split(" ")[0])

# print(itemTargetCount)

cost = []
hotel_name = []
rating_text = []
ratings = []
location = []

while itemTargetCount > len(cost):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height == last_height:
        break

    last_height = new_height

    elements = driver.find_elements(By.ID, 'hlistpg_hotel_shown_price')
    names = driver.find_elements(By.CSS_SELECTOR, '#hlistpg_hotel_name .wordBreak')
    rat_text = driver.find_elements(By.CLASS_NAME, 'ratingText')
    rat = driver.find_elements(By.ID, 'hlistpg_hotel_user_rating')
    loc = driver.find_elements(By.CSS_SELECTOR, '.addrContainer span')
    textElements = []
    textNames = []
    textRatings = []
    textRatingsName = []
    textLocation = []
    for i in range(len(elements)):
        textElements.append(elements[i].text)
    for i in range(len(names)):
        textNames.append(names[i].text)
    for i in range(len(rat)):
        textRatings.append(rat[i].text)
    for i in range(len(rat_text)):
        textRatingsName.append(rat_text[i].text)
    for i in range(len(loc)):
        textLocation.append(loc[i].text)

    cost = textElements
    hotel_name = textNames
    rating_text = textRatingsName
    ratings = textRatings
    location = textLocation

total = len(cost)
while len(rating_text) != total:
    rating_text.append('None')
    ratings.append('-')

for i in range(len(hotel_name)):
    driver.get('https://docs.google.com/forms/d/e/1FAIpQLSdWsqEQ1Wok53dt4CkmdJ8adWpFQS6qO139fqIA9RQzb0WHKQ/viewform?vc=0&c=0&w=1&flr=0')
    time.sleep(1)
    form_cost = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    form_name = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    form_text = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    form_ratings = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
    form_location = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')

    form_cost.send_keys(cost[i])
    form_name.send_keys(hotel_name[i])
    form_text.send_keys(rating_text[i])
    form_ratings.send_keys(ratings[i])
    form_location.send_keys(location[i])
    submit_button.click()