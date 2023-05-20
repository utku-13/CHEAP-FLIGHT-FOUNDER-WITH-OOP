from flight_founder import FlightFounder
from messager import Message
from data_manage import DataManage

ff =FlightFounder()
m = Message()
dm = DataManage()

sheet_data = dm.get_info()

for data in sheet_data:
    sheet_price = data["lowestPrice"]
    price = ff.search_flightt(origincity="LON",cityname=data["iataCode"])
    difference = sheet_price - price
    print(f"sheetPrice:{sheet_price}€\nfoundPrice:{price}€")
    if data["lowestPrice"]>ff.search_flightt(origincity="LON",cityname=data["iataCode"]):
        m.message(f"CHEAP FLIGHT HAS FOUND.\n\nExact cost is {price}.\n It is {difference}€ cheaper. ")
        print("it is cheaper.")
    else:
        print("it is expensive")