cars=[
    {"id":1,"name":"fronx","price":1200000,"brand":"nexa","colors":["red","blue","white"],"transmissions":["manuel","amt","cvt"]},
    
    {"id":2,"name":"baleno","price":1100000,"brand":"nexa","colors":["grey","blue","white"],"transmissions":["manuel","amt","cvt"]},
    
    {"id":3,"name":"3xo","price":900000,"brand":"mahindra","colors":["red","white","black"],"transmissions":["amt","cvt"]},
    
    {"id":4,"name":"punch","price":700000,"brand":"tata","colors":["red","blue","white","green"],"transmissions":["manuel","cvt"]},
    
    {"id":5,"name":"nexon","price":1400000,"brand":"tata","colors":["red","white"],"transmissions":["manuel","amt","cvt"]},
       
    {"id":6,"name":"kiger","price":1000000,"brand":"renault","colors":["blue","white"],"transmissions":["manuel","cvt"]},
    
    {"id":7,"name":"taigun","price":2300000,"brand":"volkswagon","colors":["red","blue","white"],"transmissions":["manuel","cvt"]},
]

# print("total cars=",len(cars))

#print(avaliable colors of baleno)
# print(cars.index[1])

# baleno_color=[c.get("colors")for c in cars if c.get("name")=="baleno"]

# print(baleno_color[0])
#   or 

# for c in cars:
    
#     if c.get("name")=="baleno":
#         colors=c.get("colors")
#         print(colors)
        
# all_brands={c.get("brand") for c in cars}

# print(all_brands)
# #or

# all=[c.get("brand") for c in cars ]
# print(set(all))

# amt_transmission=[c.get("names") for c in cars if "amt" in  c.get("transmissions")]
# print(amt_transmission)




# costly_car=max(cars,key=lambda d:d.get("price"))
# print(costly_car.get("name"))


# low_cost=min(cars,key=lambda d :d.get("price"))

# print(low_cost.get("name"))

# sorted_car=sorted(cars,key=lambda d :d.get("price"),reverse=True)

# sorted_cars={name.get("name"):[name.get("price"),name.get("brand")] for name in sorted_car}

# print(sorted_cars)

#rpint(all brands

# brand={c.get("brand") for c in cars }
# print(brand)

#print cars names availbable in amt transmission

cars_in_amttran=[c.get("name") for c in cars if "amt" in c.get("transmissions")]
# print(cars_in_amttran)

#cars available n blue color

blue_cars=[c.get("name") for c in cars if "blue" in c.get("colors")]
print(blue_cars)

#printall tarnsmissions

all_transmisions={t for c in cars for t in c.get("transmissions")}
# print(all_transmisions)

#print(all colors



all_colors={color for c in cars for color in c.get("colors")}

# print(all_colors)

#most popular color

# popular_color=[for c in cars for k,v in c.get("color") ]

costly_car=max(cars,key=lambda d:d.get("price"))
print(costly_car.get("name"))

low_cost=min(cars,key=lambda d :d.get("price"))
print(low_cost.get("name"))

sorted_car=sorted(cars,key=lambda d :d.get("price"),reverse=True)
sorted_car_name=[c.get("name") for c in sorted_car ]
print(sorted_car_name)
