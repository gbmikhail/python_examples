import asyncio

import aiohttp


async def get_pokemon(pokemon_id: int) -> str:
    url = f'http://pokeapi.co/api/v2/pokemon/{pokemon_id}'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            pokemon = await response.json()
            return pokemon['name']


async def create_tasks(count):
    tasks = [asyncio.create_task(get_pokemon(i)) for i in range(1, count)]
    return await asyncio.gather(*tasks)


async def main():
    result = await create_tasks(10)
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
