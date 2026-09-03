import csv
import requests
try:
    zapros =  requests.get("https://dummyjson.com/products/category/smartphones")
    data = zapros.json()
    products = data["products"]
    zapros.raise_for_status()
except requests.RequestException:
    print(("сайт не ответил"))
with open("smartphones_promo.csv","w",encoding="utf-8-sig",newline="")as sfile:
    writer = csv.writer(sfile,delimiter=";")
    writer.writerow(["Title","Price","Rating","Stock status"])
    for i in products:
        Title = i.get("title","Without title")
        Price = i.get("price","witout price")
        Rating = f'★{i.get("rating","without rating")}'
        s = i.get("stock","Not avaible")
        if Price > 500:
            Price *= 0.9
        if s > 10:
            ss = "в наличии"
        else:
            ss = "заканчивается"
        writer.writerow([Title.upper(),f'{Price}$',Rating,ss])
print("все сделано!")

