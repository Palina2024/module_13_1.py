import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')

    for n in range(1, 6):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {n}-й шар')

    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Harry', 10))
    task2 = asyncio.create_task(start_strongman('Ron', 6))
    task3 = asyncio.create_task(start_strongman('Hermione', 8))
    await task1
    await task2
    await task3

if __name__ == '__main__':
    asyncio.run(start_tournament())
