from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time 
from PIL import Image
while True:
# Set up the options for the Chrome webdriver
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # run Chrome in headless mode

    # Initialize the Chrome webdriver
    driver = webdriver.Chrome(options=chrome_options)


    driver.get('https://www.varzesh3.com/football/league/3/%D9%84%DB%8C%DA%AF-%D8%A8%D8%B1%D8%AA%D8%B1-%D8%A7%D9%86%DA%AF%D9%84%DB%8C%D8%B3')




    # Navigate to the Premier League homepage and zoom out to ensure the entire page is visible

    driver.execute_script("document.body.style.zoom='80%'")
    # Take a screenshot of the entire page
    driver.save_screenshot('premier_league.png')

    driver.set_window_size(310, 600)
    driver.get('https://www.varzesh3.com/livescore')

    driver.save_screenshot('live.png')

    # Navigate to the Premier League homepage and zoom out to ensure the entire page is visible

    # Quit the webdriver
    driver.quit()




    # Load the image file
    image_file = 'premier_league.png'
    img = Image.open(image_file)

    # Get the dimensions of the image
    width, height = img.size

    # Define the crop area
    left = int(width * 0.75)
    top = int(height * 0.33)
    right = int(width * 0.975)
    bottom = int(height * 0.92)

    # Crop the image
    img_crop = img.crop((left, top, right, bottom))

    # Save the cropped image
    img_crop.save('premier_league_cropped.png')

    # Load the image file
    image_file = 'live.png'
    img = Image.open(image_file)

    # Get the dimensions of the image
    width, height = img.size

    # Define the crop area
    left = int(width * 0.0)
    top = int(height * 0.255)
    right = int(width * 0.975)
    bottom = int(height * 1)

    # Crop the image
    img_crop = img.crop((left, top, right, bottom))

    # Save the cropped image
    img_crop.save('live_cropped.png')
    time.sleep(14400)
