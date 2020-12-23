"""Example usage of pytracktry."""
import asyncio
import aiohttp
from pytracktry.tracker import Tracking

API_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXX'


async def example():
    """Get pending packages."""
    async with aiohttp.ClientSession() as session:
        pytracktry = Tracking(LOOP, session, API_KEY)
        packages = await pytracktry.get_trackings()
        print("Pending packages:", packages)
        await pytracktry.remove_package_tracking('dsv', 'SCGN0076436')
        

LOOP = asyncio.get_event_loop()
LOOP.run_until_complete(example())