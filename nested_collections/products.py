

mobiles=[
    {"id":1,"title":"s23ultra","brand":"samsung","price":78000},
    {"id":2,"title":"a17","brand":"samsung","price":18000},
    {"id":3,"title":"m50","brand":"samsung","price":16000},
    {"id":4,"title":"pocom3","brand":"poco","price":15000},
    {"id":7,"title":"vivov50","brand":"vivo","price":25000},
    {"id":5,"title":"oppof19pro","brand":"oppo","price":27000},
    {"id":6,"title":"iphone16pro","brand":"apple","price":150000},
    {"id":8,"title":"nokia105","brand":"nokia","price":150000}

]

# total number of mobiles

# print(len(products))

# print mobile titles

# moblie_title=[m.get("title") for m in products]

# # print(moblie_title)

# # print samsung mobiles

# sam_mob =[m.get("title") for m in products if m.get("brand")=="samsung"]
# # print(sam_mob)

# # print(max(products,key=lambda m:m.get("price")))
# # print(min(products,key=lambda d :d.get("price")))


# costly_mobile=max(products,key=lambda d:d.get("price"))

# print(costly_mobile)

# max_price=costly_mobile.get("price")

# print(max_price)

# costly_mob_name=[m.get("title") for m in products if m.get("price")==max_price]
# print(costly_mob_name)

# samsung_mobile=[mobiles.count(m) for m in mobiles if m.get("brand")=="samsung"]
# print(len(samsung_mobile))


all_brand=[m.get("brand") for m in mobiles ]
print(all_brand)

count_allbrand={b:all_brand.count(b) for b in all_brand }
print(count_allbrand)