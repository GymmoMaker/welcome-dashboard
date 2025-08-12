#!/home/gymmo/Documenten/GymmoMaker/welcome-dashboard/venv/bin/python

from babel.dates import format_date
import datetime
import python_weather
import asyncio

LABEL_WIDTH = 20
VALUE_WIDTH = 10
LOCATION = 'Katwijk'

def get_current_date(date):
    return format_date(date, format = 'long', locale='nl')

def get_week_number(date):
    return date.strftime("%V")

async def get_temperature():
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
        return (await client.get(LOCATION)).temperature

def f_to_c(degrees):
    #Convert Fahrenheit to Celsius
    return (degrees - 32) / 1.8

async def main():
    today = datetime.date.today()
    temp = await get_temperature()

    print(f"{'Datum:':{LABEL_WIDTH}} {get_current_date(today):<{VALUE_WIDTH}}")
    print(f"{'Weeknummer:':{LABEL_WIDTH}} {get_week_number(today):<{VALUE_WIDTH}}")
    print(f"{'Temperatuur(F):':{LABEL_WIDTH}} {round(temp):<{VALUE_WIDTH}}")
    print(f"{'Temperatuur(C):':{LABEL_WIDTH}} {round(f_to_c(temp)):<{VALUE_WIDTH}}")

if __name__ == "__main__":
    asyncio.run(main())