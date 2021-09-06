import asyncio

async def main():

    loop = asyncio.get_event_loop()
    print(loop)
    await asyncio.sleep(5)


if __name__ == '__main__':
    asyncio.run(main())