from playwright.sync_api import sync_playwright

def run(playwright):
    #chromium = playwright.chromium() # or "firefox" or "webkit".
    browser = playwright.chromium.launch(channel="chrome")
    page = browser.new_page()
    page.goto("http://google.com")
    # other actions...
    #browser.close()

with sync_playwright() as playwright:
    run(playwright)

