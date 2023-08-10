import sys
import time

from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pynput.keyboard import Key, Controller


class TestOne:

    def test_e2e(self):
        # driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get('https://staging.localnewbusiness.com/auth/registration')
        driver.maximize_window()
        driver.implicitly_wait(5)

        wait = WebDriverWait(driver, 30)
        """Registration starts here"""

        driver.find_element(By.NAME, "firstname").send_keys('Zahed')
        driver.find_element(By.NAME, "lastname").send_keys('Alam')
        driver.find_element(By.NAME, "email").send_keys('zahedalam1002@gmail.com')
        driver.find_element(By.XPATH, "//input[@type='tel']").send_keys('767567564544')
        driver.find_element(By.XPATH, "(//div[@id=':Rklaj6:'])[1]").click()
        driver.find_element(By.XPATH, "//li[@role='option']").click()
        driver.find_element(By.XPATH, "//div[@id=':R14laj6:']").click()
        driver.find_element(By.XPATH, "//li[@role='option']").click()
        driver.find_element(By.XPATH, "//input[@id='city-options']").send_keys('London')
        # wait = WebDriverWait(driver, 10)
        # wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "li  # city-options-option-1")))
        # driver.find_element(By.CSS_SELECTOR, "li  # city-options-option-1").click()
        driver.find_element(By.XPATH, "//input[@placeholder='Post Code']").send_keys(4444)
        driver.find_element(By.NAME, "address").send_keys('Dhaka, Bangladesh')
        driver.find_element(By.XPATH, "//button[text()='Next']").click()
        driver.find_element(By.NAME, "userName").send_keys('Zahed7675')
        driver.find_element(By.NAME, "companyWebsite").send_keys("https://localnewbusiness.com")
        driver.find_element(By.NAME, "companyName").send_keys("fkdjfdgjldfjf")
        driver.find_element(By.NAME, "companyType").send_keys("fgjdfghgf")
        driver.find_element(By.XPATH, "//input[@autocomplete='new-password']").send_keys("Bangladesh@1")
        driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
        driver.find_element(By.XPATH, "//button[text()='Create Account']").click()
        # success_text = driver.find_element(By.XPATH, "//div[@id='notistack-snackbar']").text
        # assert success_text in "There is an user found with same email or username"
        """Registration ends here"""

        '''Forget Password section'''
        # driver.find_element(By.CSS_SELECTOR, "form[name='SigninForm'] > span").click()
        # driver.find_element(By.NAME, "email").send_keys("zahedalam1001@gmail.com")
        # driver.find_element(By.CSS_SELECTOR, 'form[name="forgotPasswordForm"] > button[type="submit"]').click()
        # time.sleep(2)

        """Login Start"""
        driver.find_element(By.XPATH, "//span[@class='formbottomlink']").click()
        driver.find_element(By.NAME, "usernameOremail").send_keys('Zahed9275')
        driver.find_element(By.NAME, "password").send_keys('Bangladesh1#')
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        try:
            login_text_element = driver.find_element(By.XPATH, "(//div[@id='notistack-snackbar'])[1]")
            login_text = login_text_element.text

            if login_text == "Login successful":
                assert login_text == "Login successful"
            elif login_text == "Network Error":
                print("Getting Network Error")
                driver.save_screenshot("network_error_screenshot.png")
                sys.exit("Test stopped due to network error")
        except Exception as e:
            print("An error occurred:", e)
            driver.save_screenshot("error_screenshot.png")
        """Login ends here"""

        """Search Functionality starts here"""
        driver.find_element(By.CSS_SELECTOR, ".bannerinputclass").send_keys('LE1')
        # driver.find_element(By.XPATH, "//button[@title='Open']//*[name()='svg']").click()
        # driver.find_element(By.CSS_SELECTOR, "li#combo-box-demo-option-0 > div").click()
        driver.find_element(By.CSS_SELECTOR, ".bannersubmitbutton").click()
        wait.until(EC.presence_of_element_located((By.XPATH, "(//p[@class='opacity-40'])[1]")))
        text = driver.find_element(By.XPATH, "(//p[@class='opacity-40'])[1]").text
        print(text)

        """Search starts here"""
        driver.find_element(By.XPATH, "//button[normalize-space()='Continue To Next Step']").click()

        """Clicking on the checkboxes"""
        driver.find_element(By.XPATH, "(//input[@aria-label='Select row'])[2]").click()
        driver.find_element(By.XPATH, "(//input[@aria-label='Select row'])[8]").click()
        driver.find_element(By.XPATH, "(//input[@aria-label='Select row'])[12]").click()
        """Go to Next step"""
        driver.find_element(By.XPATH, "(//button[normalize-space()='Continue To Next Step'])[1]").click()

        # wait = WebDriverWait(driver, 10)
        # wait.until(EC.visibility_of_element_located((By.XPATH, "//p[@class='opacity-40']")))
        driver.find_element(By.XPATH,
                            "//button[@class=' w-full bg-grey-light hover:bg-grey text-grey-darkest font-bold py-6 sm:py-12 px-4 rounded inline-flex items-center justify-center']").click()
        driver.find_element(By.NAME, "subject").click()
        driver.find_element(By.NAME, "subject").send_keys("HelloTemplate")

        """upload section"""
        driver.find_element(By.XPATH, "//button[normalize-space()='Upload']").click()
        driver.find_element(By.ID, "outlined-basic").click()
        driver.find_element(By.ID, "outlined-basic").send_keys("Hellw_pdf")

        """File Upload Using Actions"""
        driver.find_element(By.XPATH, "//label[@id='label-file-upload']").click()
        time.sleep(2)
        keyboard = Controller()
        keyboard.type("C:\\Users\\sabbir mamud\\Desktop\\new-pdf.pdf")
        time.sleep(2)
        keyboard.press(Key.right)
        time.sleep(1)
        keyboard.press(Key.enter)
        time.sleep(1)
        keyboard.release(Key.enter)

        # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, 'drop_area')))
        # action_chains = ActionChains(driver)

        # action_chains.drag_and_drop(file_path, drop_area).build().perform()
        driver.find_element(By.XPATH, "(//span[@class='mr-2'])[2]").click()
        upload_text = driver.find_element(By.XPATH, "(//div[@id='notistack-snackbar'])[1]").text
        assert upload_text in "Template uploaded successfully"
        time.sleep(3)
        #         Checking the delete functionality
        driver.find_element(By.XPATH, "(//*[name()='path'])[4]").click()
        # delete_msg = driver.find_element(By.XPATH, "(//div[@id='notistack-snackbar'])[1]").text
        # assert delete_msg in "Deleted Successfully"
        time.sleep(2)

        """Add sender Information part"""

        # driver.find_element(By.XPATH, "(//span[@class='mx-2 text-[#23A3FF] cursor-pointer'])[1]").click()
        # time.sleep(5)
        # parent_window = driver.current_window_handle
        # popup_window = None
        # wait = WebDriverWait(driver, 10)
        # for window_handle in driver.window_handles:
        #     if window_handle != parent_window:
        #         popup_window = window_handle
        #         break
        # if popup_window:
        #     driver.switch_to.window(popup_window)
        #     wait.until(EC.element_to_be_clickable((By.XPATH, "//div/input[@name='logo']")))
        #     driver.find_element(By.XPATH, "//div/input[@name='logo']").click()
        #     time.sleep(2)
        #     keyboard.type("C:\\Users\\zahed\\Desktop\\new.jpg")
        #     time.sleep(2)
        #     keyboard.press(Key.right)
        #     time.sleep(1)
        #     keyboard.press(Key.enter)
        #     time.sleep(1)
        #     keyboard.release(Key.enter)
        #     driver.switch_to.window(parent_window)
        #
        # driver.find_element(By.NAME, "firstName").send_keys("Rana")
        # driver.find_element(By.NAME, "lastName").send_keys("Jamshed")
        # driver.find_element(By.NAME, "email").send_keys("Jamshed@gmail.com")
        # driver.find_element(By.NAME, "companyName").send_keys("AMZ Company LTD")
        # driver.find_element(By.XPATH, "//input[@type='tel']").send_keys("01846899956")
        # driver.find_element(By.XPATH, "(//div[@id=':r6j:'])[1]").click()
        # driver.find_element(By.XPATH, "//li[@role='option']").click()
        #
        # driver.find_element(By.XPATH, "(//input[@id=':r6k:'])[1]").send_keys("London")
        # driver.find_element(By.XPATH, "(//div[@id=':r6m:'])[1]").click()
        # driver.find_element(By.XPATH, "//li[@role='option']").click()
        # driver.find_element(By.NAME, "postCode").send_keys(464564)
        # driver.find_element(By.XPATH, "(//div[@class='MuiInputBase-root MuiOutlinedInput-root MuiInputBase-colorPrimary MuiInputBase-fullWidth MuiInputBase-formControl MuiInputBase-multiline css-15kq27i'])[1]").send_keys("Leicester, UK")
        # driver.find_element(By.XPATH, "(//button[normalize-space()='Save'])[1]").click()
        # time.sleep(2)

        driver.find_element(By.XPATH,
                            "(//div[@class='p-3 rounded-md my-2 cursor-pointer flex items-center justify-between mr-1 border-2 border-gray-300'])[1]").click()
        time.sleep(2)
        # driver.find_element(By.XPATH, "").click()
        combobox = driver.find_element(By.XPATH, "//input[@placeholder='Search Sender']")
        actions = ActionChains(driver)
        actions.click(combobox).perform()
        # options_locator = driver.find_element(By.XPATH, "//input[@area-activedescendent='combo-box-demo-option-0']")
        wait = WebDriverWait(driver, 10)
        option = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='presentation']")))
        option.click()

        # for option in options:
        #     # Hover over the option
        #     actions.move_to_element(option).perform()
        #     print(option)
        #     # Generate the locator based on the dynamically generated attribute value
        #     option_attribute_value = option.get_attribute("area-activedescendant")
        #     print(option_attribute_value)
        #     option_locator = (By.XPATH, f"//input[@area-activedescendant='{option_attribute_value}']")
        #     try:
        #         option_element = wait.until(EC.presence_of_element_located(option_locator))
        #         option_element.click()  # Example interaction
        #     except NoSuchElementException:
        #         print("Option not found or interactable")
        #         continue

        # Use the generated locator to interact with the option
        # option_element = driver.find_element(*option_locator)
        # option_element.click()

        # wait.until(EC.visibility_of_element_located(()))
        # action.move_to_element(driver.find_element(By.XPATH, "//input[@area-activedescendent='combo-box-demo-option-0']")).perform()

        # driver.find_element(By.XPATH, "//input[@area-activedescendent='combo-box-demo-option-0']").click()
        driver.find_element(By.XPATH, "//button[@value='Send']").click()
        time.sleep(3)

        """Checkout Page"""
        driver.find_element(By.CSS_SELECTOR, "div#__next span > button").click()

        # wait.until(EC.visibility_of_element_located((By.ID, "email")))
        driver.find_element(By.XPATH, "//input[@id='email']").send_keys("Zahedalam1001@gmail.com")
        driver.find_element(By.XPATH, "//input[@id='shipping-name']").send_keys("Zahed")
        driver.find_element(By.ID, "shipping-street").send_keys("Dhaka, Bangladesh")
        driver.find_element(By.ID, "shipping-zip").send_keys("1212")
        time.sleep(2)
        driver.find_element(By.ID, "submitButton").click()

        driver.find_element(By.ID, "card_number").send_keys(4242424242424242)
        driver.find_element(By.ID, "cc-csc").send_keys(375)
        driver.find_element(By.ID, "submitButton").click()

        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='shadow-lg py-20 text-center']/h2")))
        text = driver.find_element(By.XPATH, "//div[@class='shadow-lg py-20 text-center']/h2").text

        assert "Payment Successfully Completed" in text

        driver.find_element(By.XPATH, "section button").click()
        time.sleep(2)

        """Assertion of Total company and Amount"""
        # Assert Total Number of Company and Prices
        # total_company_element = driver.find_element(By.XPATH, "//p[normalize-space()='2']")
        # net_price_element = driver.find_element(By.XPATH, "(//p[normalize-space()='£ 1 * 2'])[1]")
        # vat_element = driver.find_element(By.XPATH, "//p[normalize-space()='£ 0']")
        # total_price_element = driver.find_element(By.XPATH, "//p[normalize-space()='£ 2']")
        #
        # total_company = total_company_element.text
        # net_price = net_price_element.text
        # vat = vat_element.text
        # total_price = total_price_element.text
        #
        # expected_total_company = "2"
        # expected_net_price = "£ 1 * 2"
        # expected_vat = "£ 0"
        # expected_total_price = "£ 2"
        #
        # assert total_company == expected_total_company, f"Total company assertion failed: Expected {expected_total_company}, but got {total_company}"
        # assert net_price == expected_net_price, f"Net price assertion failed: Expected {expected_net_price}, but got {net_price}"
        # assert vat == expected_vat, f"VAT assertion failed: Expected {expected_vat}, but got {vat}"
        # assert total_price == expected_total_price, f"Total price assertion failed: Expected {expected_total_price}, but got {total_price}"






