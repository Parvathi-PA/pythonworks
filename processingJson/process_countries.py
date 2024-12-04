from json import load

f=open("C:\\Users\\parva\\OneDrive\\Desktop\\pythonworks\\dataset\\countries.json",encoding="utf-8")

data=load(f)

# print(len(data))

all_country_name=[country.get("name") for country in data]

# print(all_country_name)

# print all regions

all_regions=[country.get("region") for country in data]
# print(set(all_regions))

# cpunt of regions wise countries

region_count={region:all_regions.count(region) for region in all_regions}

# print(region_count)

max_region_count=max(region_count,key=lambda k:region_count.get(k))

# print(max_region_count,region_count.get(max_region_count))

# capital of a specific country

country_capital=[country.get("capital") for country in data if country.get("name")=="India"]

# print(country_capital)

country_borders={country.get("name"):len(country.get("borders",[])) for country in data}
#  bnm,print(country_borders)

max_border_country=max(data,key=lambda country:len(country.get("borders",[]))).get("name")

# print(max_border_country)

max_border_count=max(data,key=lambda country:len(country.get("borders",[]))).get("name")
# print(max_border_count)

# most populateed country


population={country.get("name"):country.get("population") for country in data }
most_populate_country=max(data,key=lambda country:country.get("population")).get("name")
# print(most_populate_country,population.get(most_populate_country))


indian_border=[country.get("borders") for country in data if country.get("name")=="India"][0]
# print(indian_border)


alpha_3_code=[country.get("borders") for country in data if country.get("name")=="Afghanistan"][0]

for code in alpha_3_code:
    
    for country in data:
        
        if country.get("alpha3Code")==code:
            
            print(country.get("name"))