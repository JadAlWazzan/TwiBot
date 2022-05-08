import requests

url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/3hourly"

querystring = {"lat":"35.5","lon":"-78.5"}

headers = {
	"X-RapidAPI-Host": "weatherbit-v1-mashape.p.rapidapi.com",
	"X-RapidAPI-Key": "c3efd3a460msh47e29fad6939edbp1659edjsn93b4e066eebc"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)