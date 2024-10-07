from duckduckgo_search import AsyncDDGS
import asyncio

async def main():
    # async
    results = await AsyncDDGS().achat('vitamins in orange')
    print(results)

if __name__ == "__main__":
    asyncio.run(main())
