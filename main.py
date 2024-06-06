import selenium
from webdriver_manager.firefox import GeckoDriverManager

# Check Selenium and WebDriver Manager versions
print("Selenium version:", selenium.__version__)
print("WebDriver Manager version:", GeckoDriverManager().get_driver_version())

# Check Firefox version
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
binary = FirefoxBinary()
firefox_version = binary.capabilities['browserVersion']
print("Firefox version:", firefox_version)

# Check geckodriver version
geckodriver_version = GeckoDriverManager().get_driver_latest_release_version()
print("Geckodriver version:", geckodriver_version)

# Verify compatibility
if selenium.__version__ >= "4.0":
    print("Selenium 4.x is compatible with geckodriver", geckodriver_version)
else:
    print("Selenium", selenium.__version__, "may require geckodriver", geckodriver_version)

# Add more compatibility checks if needed

# Initialize Firefox WebDriver using WebDriver Manager
from selenium.webdriver import Firefox
driver = Firefox(executable_path=GeckoDriverManager().install())

# Proceed with your Selenium script




website_url = "https://ifazility.com/Optdesk/Account/Login"


driver.implicitly_wait(5)

# Open the website
driver.get(website_url)
# Find the login form elements and fill them in


time.sleep(50)
# Close the browser
driver.quit()
