import asyncio
import random

async def fetch(url):
    delay = random.uniform(0.5, 2)
    await asyncio.sleep(delay)
    print(f"Fetched {url} in {delay:.2f}s")
    return url

async def main():
    urls = [f"https://example.com/{i}" for i in range(5)]
    results = await asyncio.gather(*(fetch(u) for u in urls))
    print("All fetched:", results)

asyncio.run(main())
