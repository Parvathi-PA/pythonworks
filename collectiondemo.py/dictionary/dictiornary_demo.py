

#dictionary - it is defined using key value pair .eg: key:value,"name":"anu"

#indexing not supported

product={"id":"cd234","title":"phone","price":10000,"brand":"realme"}

# print(product["id"])
# print(product["price"])
print(product["brand"])

#update  product= product["orice"]=34

#add to dictionary

product["date"]="12-3-2024"

# product["offer"]=5

# print(product)

#chek key is present

if "id" in product:
    print("exist")
    
else:
    print("not exist")
    
#add offer as 10 if offer is exist else add oofer as 20

if "offer" in product:
    product["offer"]=10
else:
    product["offer"]=20
print(product)