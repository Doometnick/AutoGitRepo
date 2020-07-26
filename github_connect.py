import sys
from time import sleep
from decouple import config
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


GITHUB_LOGIN_LINK = "https://github.com/login"


class Xpaths:

    """Stores xpaths required for navigating on https://www.github.com"""

    LOGIN_NAME = "/html/body/div[3]/main/div/form/div[4]/input[1]"
    LOGIN_PASSWORD = "/html/body/div[3]/main/div/form/div[4]/input[2]"
    SIGNIN_BTN = "/html/body/div[3]/main/div/form/div[4]/input[9]"
    NEWREPO = "/html/body/div[4]/div/aside[1]/div[2]/div[1]/div/h2/a"
    REPONAME = "/html/body/div[4]/main/div/form/div[2]/auto-check/dl/dd/input"
    CREATE_BTN = "/html/body/div[4]/main/div/form/div[4]/button"


def click_button(driver: webdriver, xpath: str, wait_post_click: float=0.0):
    element = driver.find_element_by_xpath(xpath)
    element.click()
    sleep(abs(wait_post_click))


def write_to_textfield(driver: webdriver, xpath: str, text: str):
    element = driver.find_element_by_xpath(xpath)
    element.clear()
    element.send_keys(text)


def create_repo(repo_name: str):
    driver = webdriver.Chrome()
    driver.get(GITHUB_LOGIN_LINK)

    write_to_textfield(driver, Xpaths.LOGIN_NAME, config("GIT_USER"))
    write_to_textfield(driver, Xpaths.LOGIN_PASSWORD, config("GIT_PW"))
    click_button(driver, Xpaths.SIGNIN_BTN)
    click_button(driver, Xpaths.NEWREPO, 1)
    write_to_textfield(driver, Xpaths.REPONAME, repo_name)
    # Wait one second for git to validate your git repository name.
    sleep(1)
    click_button(driver, Xpaths.CREATE_BTN, 1)


if __name__ == "__main__":

    try:
        repo_name = sys.argv[1]
    except IndexError:
        print("Argument for repository name expected.")
    else:
        create_repo(repo_name)
