
from playwright.sync_api import sync_playwright, expect

def run_verification():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("file:///app/HeaderBuilderDefault.html")

        # 1. Verify canvas size change to 1200x1200
        page.click("#canvas-size-button")
        page.click("#canvas-1200")
        preview_area = page.locator("#preview-container > #preview-area")
        expect(preview_area).to_have_css("width", "1200px")
        expect(preview_area).to_have_css("height", "1200px")
        print("✅ Canvas size correctly changed to 1200x1200.")

        # Take a screenshot to show the final state
        page.screenshot(path="verification_screenshot.png")
        print("📸 Screenshot taken as verification_screenshot.png")

        browser.close()

if __name__ == "__main__":
    run_verification()
