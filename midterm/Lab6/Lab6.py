country_code = {'America':1, 'Korea':82, 'China':86}
country_code['Japan'] = 81

print(country_code)

print("key=", country_code.keys())
print(list(country_code.keys()))

print("value =", country_code.values())
print(list(country_code.values()))

for k,v in country_code.items():
    print(k,v)

print(country_code['Korea'])
print(country_code)

print(country_code.pop('Korea'))
print(country_code)

print(country_code.get('Korea', '없음'))

country_code.clear()
print(country_code)