from selenium import webdriver

# specify the location of the chrome driver executable
chromedriver = "C:\meticulous\chromedriver.exe"

# Open the website using the Chrome browser
driver = webdriver.Chrome(executable_path=chromedriver)
driver.get("https://chat.openai.com/chat")

# Wait for the page to load
driver.implicitly_wait(10) # seconds

# Keep the browser open
input("Press Enter to close the browser.")

# Close the browser
driver.quit()
