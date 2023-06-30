import asyncio
import aiohttp
import time, random


class ScrapeSites:

    def __init__(self, websites=None):
        if websites is None:
            self.websites = ['http://davidreynon.com', 'https://cnn.com']
        else:
            self.websites = websites

    """
    -await for each website
        -await request/response website, get response text
        -await 
            -await parse each line, process
            -await store in db
        

    """
    async def request(self, site):
        print('request()' + site)
        await asyncio.sleep(random.randint(1,3))
        print ('response from ', site)
        return 'response ' + site

    async def etl(self, line, site):
        print('etl()' + line + site)
        await asyncio.sleep(random.randint(1,3))
        print ('completed etl for ', line, site)
        return 'etl ' + site

    async def write_to_db(self, data, site):
        print('write_to_db()' + data + site)
        await asyncio.sleep(random.randint(1,3))
        print ('write_to_db() complete', data, site)
        return 'write_to_db' + site

    async def site_process(self, site):
        response = await self.request(site)
        etl_status = await self.etl(response, site)
        db_write_status = await self.write_to_db('fake data', site)
        return

    async def scrape(self):
        websites_group = await asyncio.gather(
            *[self.site_process(site) for site in self.websites]
        )

    def main(self):
        asyncio.run(self.scrape())

