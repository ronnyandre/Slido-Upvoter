import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

# Set Chrome to Incognito mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

# Slido settings
slido_id = "---"
slido_qid = "---"

# How many votes should the question get?
votes = 3

# How long to wait until Slido loads?
load_delay = 10

# Loop through the voting
for i in range(votes):

    # Create Chrome driver and get URL
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(f'https://app.sli.do/event/{slido_id}/live/questions')

    # Wait for page to load
    try:
        # Find question
        el = WebDriverWait(driver, load_delay).until(EC.presence_of_element_located((By.XPATH, f'//*[@data-qid="{slido_qid}"]')))
        print("Found question!")

        # Find vote button
        btn = el.find_element_by_xpath('.//button')

        # Click the vote button
        btn.click()

        # Get current votes
        current_votes = btn.find_element_by_xpath('.//span').text

        # Print feedback
        print(f"Question upvoted. Votes: {current_votes}")

        # Wait before quitting browser
        time.sleep(2)

        # Quit browser
        driver.quit()

        # Wait before restarting loop
        time.sleep(1)

    # Page load timeout
    except TimeoutException:
        print("Loading took too much time!")