import re
from playwright.sync_api import Page, expect


def test_add_product_successfully_to_cart(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.locator(".radiotextsty", has_text="Admin").check()
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.locator("#signInBtn").click()
    expect(page.get_by_text("ProtoCommerce Home", exact=True)).to_be_visible()
    samsungProduct = page.locator("app-card").filter(has_text="Samsung Note 8")
    samsungProduct.get_by_role("button").click()
    blackberryProduct = page.locator("app-card").filter(has_text="Blackberry")
    blackberryProduct.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    expect(page.get_by_text("Quantity")).to_be_visible()
    page.screenshot(path="products.png", full_page=True)
    expect(page.locator(".media-body")).to_have_count(2)




