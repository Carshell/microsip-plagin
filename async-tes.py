import asyncio

async def funcc():
    print("Hello1")
    await asyncio.sleep(5)
    print("Secondd helo1")

async def funcc2():
    print("Hello2")
    await asyncio.sleep(1)
    print("Secondd helo2")

async def main():
    await asyncio.gather(funcc(), funcc2())  

asyncio.run(main())