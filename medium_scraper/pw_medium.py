import asyncio
from playwright.async_api import async_playwright


async def get_site_meta(url: str):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(url)
        await page.screenshot(path="medium.index.png")
        print(await page.title())
        await browser.close()


