names_of_cities = (
    "6..58київ\nоДеса     Львів\tжитоМИР      уЖгОрОд ХарКІВ       слАвУтИч74$:?$"
)
corrected_names_of_cities = names_of_cities.strip("6..5874$:?$").title().split()
print(corrected_names_of_cities)
reaction = "\U00002764"
first_city = corrected_names_of_cities[0]
print(f"Я {reaction} {first_city}")
second_city = corrected_names_of_cities[1]
print(f"Я {reaction} {second_city}")
third_city = corrected_names_of_cities[2]
print(f"Я {reaction} {third_city}")
fourth_city = corrected_names_of_cities[3]
print(f"Я {reaction} {fourth_city}")
fifth_city = corrected_names_of_cities[4]
print(f"Я {reaction} {fifth_city}")
sixth_city = corrected_names_of_cities[5]
print(f"Я {reaction} {sixth_city}")
seventh_city = corrected_names_of_cities[6]
print(f"Я {reaction} {seventh_city}")
