from datetime import datetime as dt
from decimal import Decimal
from custom_module import generate_time_travel_message
import random
#current dates and times
date_now = dt.today().date()
time = dt.now().time()
print("Current date is " + str(date_now) + " " + str(time))
#year_arrive it will take to arrive
year_arrive = random.randint(2025,10001)
print("year generated is {}".format(year_arrive))
formatted_date = f"{date_now.month}-{date_now.day}-{year_arrive}"
print("year arrive is {}".format(formatted_date))
#cost of trip
base = Decimal('200000.00')
#total of trip
total_cost = base * Decimal(year_arrive - date_now.year)
destination = ["Tokyo (Japan)","Great Wall of China (China)","Taj Mahal (India)","Mount Everest (Nepal/Tibet)"]
final_destination = random.choice(destination)
print("random destination is {}".format(final_destination))
trip_final = generate_time_travel_message(year_arrive, final_destination, total_cost)
print(trip_final)
