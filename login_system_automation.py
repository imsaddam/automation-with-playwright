import re
import time
from tkinter.font import names

from playwright.sync_api import Page, expect


def test_loginIntoToSystem(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
 #   page.get_by_label("Admin").check()
    page.get_by_role("combobox").select_option("teach")
    page.get_by_label("terms and conditions").check()
    page.get_by_role("button", name="Sign In").click()
    page.wait_for_timeout(1)




