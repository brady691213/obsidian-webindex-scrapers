import asyncio

from medium_scraper.pw_medium import get_site_meta


asyncio.run(get_site_meta("https://medium.com"))
