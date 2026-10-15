city= [
	"Taipei", "Taichung", "Tainan", "Kaohsiung", "Hsinchu",
	"Chiayi", "Miaoli", "Nantou", "Yunlin", "Pingtung"
]
code = [63, 66, 67, 64, 10004, 10010, 10005, 10008, 10009, 100013]

city.append("Hualian")
code.append(10015)
code[city.index("Pingtung")] = 10013

city_name = input("Please input a city name: ").strip()

if city_name in city:
	city_index = city.index(city_name)
	print(f"{city_name} code: {code[city_index]}")
else:
	print(f"{city_name} was not found.")

city_tuple = tuple(city)
code_tuple = tuple(code)

if city_name in city_tuple:
	city_index = city_tuple.index(city_name)
	print(f"Tuple: {city_name} code: {code_tuple[city_index]}")
else:
	print(f"Tuple: {city_name} was not found.")