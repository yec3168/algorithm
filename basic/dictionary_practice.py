# dictionary은 set과 생성이 아주 비슷함

# key : value 
country = {"korea" : "seoul", 
           "usa" : "washington DC", 
           "japan" : "tokyo"}


print(country["korea"]) # key값을 가져와야함.


#get == 위에꺼랑 같은 의미?
print(country.get('usa'))

# keys
print(country.keys())


# values
print(country.values())

#items.
print(country.items())


for key, value in country.items():
    print(key, value)


# update

country.update({"중국" : "베이징"})
for key, value in country.items():
    print(key, value)


country.update({"중국" : "Beijing"})
for key, value in country.items():
    print(key, value)


#pop
country.pop("중국")
for key, value in country.items():
    print(key, value)