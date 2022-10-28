from urllib import response
import requests

# copy c URL for bash from Network Tab of Chrome Dev Tools for a GET request after auth and paste it in
# curl.trillworks.com and receive Python code

cookies = {
    'prism_225691203': 'ed66a66b-0a1d-4189-809a-ea1141129db3',
    '_fbp': 'fb.1.1664489140605.1780877914',
    'WidgetTrackerCookie': 'e822cc56-3b03-4c8e-b0f0-ae73bd20636d',
    'screen': '{%22width%22:1366}',
    '_gid': 'GA1.2.1728934854.1666757594',
    'cebs': '1',
    '_ce.s': 'v~2cb55605bd4d2e54e4a56ce826141d66c97a659d~vpv~2',
    'user': '{%22id%22:%22729899%22%2C%22firstName%22:%22Sairam%22%2C%22lastName%22:%22Udayshankar%22%2C%22email%22:%22sairamgunner@gmail.com%22%2C%22newsletter%22:false%2C%22homePhone%22:%22647-236-5054%22%2C%22jwt%22:%22eyJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2NjY3NjI4MDksInVzZXJfaWQiOjcyOTg5OX0.aVXMWqZcaf5fjbdJ_OtqmquuZdTTp9jr7dxFLzrdePM%22}',
    'jwt': 'eyJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2NjY3NjI4MDksInVzZXJfaWQiOjcyOTg5OX0.aVXMWqZcaf5fjbdJ_OtqmquuZdTTp9jr7dxFLzrdePM',
    'listing-params': '{%22sort%22:%22date%22%2C%22filter%22:{%22rental%22:false%2C%22status%22:%22available%22%2C%22slug%22:%22toronto-on%22%2C%22latitude%22:43.653226%2C%22longitude%22:-79.3831843%2C%22zoom%22:14%2C%22homeType%22:{%22houseDetached%22:true%2C%22houseSemidetached%22:true%2C%22houseAttached%22:true%2C%22townhouse%22:true%2C%22condo%22:true}%2C%22priceMin%22:null%2C%22priceMax%22:null%2C%22listedSince%22:null%2C%22listedTo%22:null%2C%22bedrooms%22:%220+%22%2C%22sqftMin%22:null%2C%22sqftMax%22:null%2C%22bathrooms%22:%221+%22%2C%22parkingSpaces%22:%220+%22%2C%22openHouse%22:false%2C%22garage%22:false%2C%22pool%22:false%2C%22fireplace%22:false%2C%22waterfront%22:false%2C%22additional%22:{%22house%22:{%22singleFamily%22:false%2C%22basementApartment%22:false%2C%22duplex%22:false%2C%22triplex%22:false%2C%22fourplex+%22:false}%2C%22condoOrTownhouse%22:{%22locker%22:%22any%22%2C%22maintenanceFee%22:null}}%2C%22areaName%22:%22Toronto%2C%20ON%22%2C%22boundary%22:null}}',
    '_bazooka_app_session': 'YjBiem5JMS9GUXBDTXEvZWMyYVlubmlGY3lLQ09zcDg0akUrdVhRZ0hWdHRHcUhScmtyZFRlMzJ6eFJIOEdZaGpDZDh6OUIwNkU3UU1JYnZ6N2FwSFVGZGc3cngxeW9rRHhyRGt5VlJIQkRpT3YwNi8wQmhRRjlzd3ZTWXRrQmEtLVVzMFBSTFRxTHA2MEhvb0IwWStsYXc9PQ%3D%3D--f65f19affed5ebdc123106e0175606a1a4003ec7',
    '_ga_K7EQ5W60XF': 'GS1.1.1666795754.5.1.1666795797.0.0.0',
    'cebsp': '7',
    '_ga': 'GA1.2.587731144.1664489140',
}

headers = {
    'authority': 'www.zoocasa.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'prism_225691203=ed66a66b-0a1d-4189-809a-ea1141129db3; _fbp=fb.1.1664489140605.1780877914; WidgetTrackerCookie=e822cc56-3b03-4c8e-b0f0-ae73bd20636d; screen={%22width%22:1366}; _gid=GA1.2.1728934854.1666757594; cebs=1; _ce.s=v~2cb55605bd4d2e54e4a56ce826141d66c97a659d~vpv~2; user={%22id%22:%22729899%22%2C%22firstName%22:%22Sairam%22%2C%22lastName%22:%22Udayshankar%22%2C%22email%22:%22sairamgunner@gmail.com%22%2C%22newsletter%22:false%2C%22homePhone%22:%22647-236-5054%22%2C%22jwt%22:%22eyJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2NjY3NjI4MDksInVzZXJfaWQiOjcyOTg5OX0.aVXMWqZcaf5fjbdJ_OtqmquuZdTTp9jr7dxFLzrdePM%22}; jwt=eyJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2NjY3NjI4MDksInVzZXJfaWQiOjcyOTg5OX0.aVXMWqZcaf5fjbdJ_OtqmquuZdTTp9jr7dxFLzrdePM; listing-params={%22sort%22:%22date%22%2C%22filter%22:{%22rental%22:false%2C%22status%22:%22available%22%2C%22slug%22:%22toronto-on%22%2C%22latitude%22:43.653226%2C%22longitude%22:-79.3831843%2C%22zoom%22:14%2C%22homeType%22:{%22houseDetached%22:true%2C%22houseSemidetached%22:true%2C%22houseAttached%22:true%2C%22townhouse%22:true%2C%22condo%22:true}%2C%22priceMin%22:null%2C%22priceMax%22:null%2C%22listedSince%22:null%2C%22listedTo%22:null%2C%22bedrooms%22:%220+%22%2C%22sqftMin%22:null%2C%22sqftMax%22:null%2C%22bathrooms%22:%221+%22%2C%22parkingSpaces%22:%220+%22%2C%22openHouse%22:false%2C%22garage%22:false%2C%22pool%22:false%2C%22fireplace%22:false%2C%22waterfront%22:false%2C%22additional%22:{%22house%22:{%22singleFamily%22:false%2C%22basementApartment%22:false%2C%22duplex%22:false%2C%22triplex%22:false%2C%22fourplex+%22:false}%2C%22condoOrTownhouse%22:{%22locker%22:%22any%22%2C%22maintenanceFee%22:null}}%2C%22areaName%22:%22Toronto%2C%20ON%22%2C%22boundary%22:null}}; _bazooka_app_session=YjBiem5JMS9GUXBDTXEvZWMyYVlubmlGY3lLQ09zcDg0akUrdVhRZ0hWdHRHcUhScmtyZFRlMzJ6eFJIOEdZaGpDZDh6OUIwNkU3UU1JYnZ6N2FwSFVGZGc3cngxeW9rRHhyRGt5VlJIQkRpT3YwNi8wQmhRRjlzd3ZTWXRrQmEtLVVzMFBSTFRxTHA2MEhvb0IwWStsYXc9PQ%3D%3D--f65f19affed5ebdc123106e0175606a1a4003ec7; _ga_K7EQ5W60XF=GS1.1.1666795754.5.1.1666795797.0.0.0; cebsp=7; _ga=GA1.2.587731144.1664489140',
    'referer': 'https://www.zoocasa.com/toronto-on-real-estate',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'x-nextjs-data': '1',
}

response = requests.get('https://www.zoocasa.com/vancouver-bc-real-estate/25-w-king-edward-ave', headers=headers, cookies=cookies)
print(response.content)