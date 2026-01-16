import re
import time
from tkinter.font import names

from playwright.sync_api import Page, expect

## Verifies that a user can log in successfully using valid credentials
def test_login_successfully_with_valid_credentials(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
 #   page.get_by_label("Admin").check()
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.locator("#signInBtn").click()
    expect(page.get_by_text("ProtoCommerce Home", exact=True)).to_be_visible()

## // Verifies that a user cannot log in using invalid credentials
def test_login_successfully_with_invalid_credentials(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning1")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.locator("#signInBtn").click()
    expect(page.get_by_text("Incorrect username/password.", exact=True)).to_be_visible()




