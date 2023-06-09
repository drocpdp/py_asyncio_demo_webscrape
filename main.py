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
    time.sleep(random.randint(1,3))
    print ('response from ', site)
    return 'response ' + site

async def etl(line, site):
    print('etl()' + line + site)
    time.sleep(random.randint(1,3))
    print ('completed etl for ', line, site)
    return 'etl ' + site

async def write_to_db(data, site):
    print('write_to_db()' + data + site)
    time.sleep(random.randint(1,3))
    print ('write_to_db() complete', data, site)
    return 'write_to_db' + site

async def main():
    for website in websites:
        response = await request(website)
        etl_status = await etl(response, website)
        db_write_status = await write_to_db('fake data', website)


main = asyncio.run(main())
print(main)


