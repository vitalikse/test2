import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_open_page(driver):
    driver.get('https://openweathermap.org/')
    print(driver.current_url)
    assert 'openweathermap' in driver.current_url
    driver.maximize_window()

def test_check_title(driver):
    driver.get('https://openweathermap.org/')
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'

def test_search_city(driver):
    driver.get('https://openweathermap.org')
    search_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search city']")
    search_field.send_keys('New York')
    time.sleep(5)
    search_button = driver.find_element(By.CSS_SELECTOR, "button[class='button-round dark']")
    search_button.click()
    time.sleep(5)
    search_option = driver.find_element(By.CSS_SELECTOR, 'ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)')
    search_option.click()
    time.sleep(10)
    expected_city = 'New York City, US'
    displayed_city = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.grid-container.grid-4-5 h2')))
    # driver.find_element(By.CSS_SELECTOR, '.grid-container.grid-4-5 h2')
    assert expected_city == displayed_city.text
#ererer
print('ffffff')


# def test_open_page():
#     browser.get('https://suninjuly.github.io/xpath_examples')

# def test_open_page():
#     browser.get('https://suninjuly.github.io/cats.html')
# def open_page():
#     browser.get('http://suninjuly.github.io/cats.html')
#     bullet_cat = browser.find_element(By.XPATH, "//*[contains(text(), 'Bullet cat')]")
#
#     # print(bullet_cat.text)
#     view_buttons = browser.find_elements(By.XPATH, "//*[contains(text(), 'View')]")
#     # print(len(view_buttons))
#     assert len(view_buttons) == 5, 'Wrong length'
#
# def test_open_page():
#     open_page()