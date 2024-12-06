import asyncio
import time


async def FryEggs():
    print("Started frying eggs")
    await asyncio.sleep(3)
    print("Finished frying eggs")

    return "Fried Eggs"


async def CutTomatoes():
    print("Started cutting tomatoes")
    await asyncio.sleep(2)
    print("Finished cutting tomatoes")

    return "Cut Tomatoes"


async def main():

    starttime = time.time()

    batch = asyncio.gather(FryEggs(), CutTomatoes())

    await batch

    endtime = time.time()

    print("Execution time: " + str(endtime - starttime))

    return

if "__init__" == "__init__":
    asyncio.run(main())
