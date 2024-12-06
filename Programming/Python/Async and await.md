Python uses [[Concurrency vs Parallelism|concurrency]] for running coroutines.

```python
import asyncio

async def func():
    # this function does something
    return result
```

When creating a concurrently running batch of tasks, the usage of `async` and `await` are essential
## Async 
The `async def` defines a [[Coroutines|coroutine]].

> Functions defined with async def syntax are always coroutine functions, even if they do not contain await or async keywords

\- Python Compound Statements

`async def` returns a coroutine object, that can be ran using `asyncio.run()`

```python
async def main():
    asyncio.run(func()) # where func is defined with async def
    return
```

## Await
`await` is keyword used within a coroutine that suspends its execution until the "awaited" task is completed. 

Key aspects of `await` :
1. Suspension: `await` suspends the execution of a coroutine, allowing other coroutines to run.
2. Awaitability: `await` can only be applied to task that are awaitable.
3. Event loop: the event loop schedules the other coroutines run, while the awaited task is being processed.
4. Resume: after the awaited task is finished, the execution of the coroutine continues by the event loop from where the coroutine was left off.

## Example 
```python
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
```
