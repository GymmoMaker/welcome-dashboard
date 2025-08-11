from datetime import date
from babel.dates import format_date
import datetime
import python_weather
import asyncio
import os

async def main() -> None:
    today = datetime.date.today()
    print("De datum is " + format_date(today, format = 'long', locale='nl'))
    print("Het weeknummer is " + today.strftime("%V"))

    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
        weather = await client.get('Leiden')
        print("De temperatuur is " + str(weather.temperature) + " graden")

if __name__ == "__main__":
    asyncio.run(main())