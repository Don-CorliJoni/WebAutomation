from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException

from logging_helper import get_logger

logger = get_logger(__name__)


def resolve(driver, wait, xpath):
    """

    :param wait:
    :param driver: selenium.webdriver.chrome.webdriver.WebDriver
    :param xpath: The xpath of the HTML element
    :return: An ... object, that is provide functionality to interact with the HTML element
    """

    try:
        wait.until(ec.presence_of_element_located((By.XPATH, xpath)))
        return driver.find_element("xpath", xpath)
    except Exception as e:
        logger.exception(f"The element with x-path='{xpath}' could not be found!", e)

def resolve_many(driver, wait, xpath):
    """

    :param wait:
    :param driver: selenium.webdriver.chrome.webdriver.WebDriver
    :param xpath: The xpath of the HTML elements
    :return: An ... object, that is provide functionality to interact with the HTML element
    """

    try:
        wait.until(ec.presence_of_all_elements_located((By.XPATH, xpath)))
        return driver.find_elements("xpath", xpath)
    except TimeoutException:
        print(f"Timeout: The requested element with x-path='{xpath} could not be found! "
              f"If not necessary, remove this request for performance!")                                                                                                                                                           #logging hier
        return []
    except Exception as e:
        logger.exception(f"The element(s) with x-path='{xpath}' could not be found!", e)
