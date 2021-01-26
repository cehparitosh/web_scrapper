import requests
from bs4 import BeautifulSoup
import pandas
import sql_connect
url = "https://www.oyorooms.com/hotels-in-delhi/"
req = requests.get(url)
scrapped_info_list = []
sql_connect.connect()
content = req.content
soup = BeautifulSoup(content,"html.parser")
all_hotels = soup.find_all("div", {"class": "hotelCardListing"})
for hotel in all_hotels:
    hotel_dict = {}
    hotel_dict["name"] = hotel.find("h3",{"class":"listingHotelDescription__hotelName"}).text
    hotel_dict["add"] = hotel.find("span",{"itemprop":"streetAddress"}).text
    hotel_dict["price"] = hotel.find("span",{"class":"listingPrice__finalPrice"}).text
    try:
        hotel_dict["rate"] = hotel.find("span",{"class":"hotelRating__ratingSummary"}).text
    except AttributeError:
        pass
    parent_amenities_element = hotel.find("div", {"class": "amenityWrapper"})
    amenities_list = []
    for amenity in parent_amenities_element.find_all("div", {"class": "amenityWrapper__amenity"}):
        amenities_list.append(amenity.find("span", {"class": "d-body-sm"}).text.strip())
    hotel_dict["amenities"] = ', '.join(amenities_list[:-1])
    scrapped_info_list.append(hotel_dict)
    sql_connect.insert(tuple(hotel_dict.values()))
sql_connect.show()