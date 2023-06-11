import asyncio
import aiohttp
import time, random

websites = ['http://davidreynon.com', 'https://cnn.com']


"""
-await for each website
    -await request/response website, get response text
    -await 
        -await parse each line, process
        -await store in db
    

"""
async def request(site):
    print('request()' + site)
    await asyncio.sleep(random.randint(1,3))
    print ('response from ', site)
    return 'response ' + site

async def etl(line, site):
    print('etl()' + line + site)
    await asyncio.sleep(random.randint(1,3))
    print ('completed etl for ', line, site)
    return 'etl ' + site

async def write_to_db(data, site):
    print('write_to_db()' + data + site)
    await asyncio.sleep(random.randint(1,3))
    print ('write_to_db() complete', data, site)
    return 'write_to_db' + site

async def site_process(site):
    response = await request(site)
    etl_status = await etl(response, site)
    db_write_status = await write_to_db('fake data', site)
    return

async def main():
    websites_group = await asyncio.gather(
        *[site_process(site) for site in websites]
    )


main = asyncio.run(main())



