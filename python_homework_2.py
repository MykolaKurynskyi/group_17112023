# Task_1
print('~' * 40)
# Task_2
username = input('Please, enter your username >>> ')
print(username.strip().title())
# Task_3
age_of_users = int(input('Please, enter your age >>> '))
print(age_of_users)
# Task_4
average_monthly_salary_at_the_moment = float(input('Please, enter your salary at the moment >>> '))
print(average_monthly_salary_at_the_moment)
# Task_5
retirement_age = 65
years_left_until_retirement = retirement_age - age_of_users
print(years_left_until_retirement)
# Task_6
months_a_year = 12
total_earnings_before_retirement = years_left_until_retirement * months_a_year * average_monthly_salary_at_the_moment
print(total_earnings_before_retirement)
# Task_7
dollar_exchange_rate = 37.3
total_in_dollars = total_earnings_before_retirement / dollar_exchange_rate
print(total_in_dollars)
# Task_8
cost_of_one_car = 31500
total_cars = total_in_dollars // cost_of_one_car
print(total_cars)
# Task_9
# print( f{'я, Сергій, зможу заробити лише', 'total_in_dollars'})
# # full_name = f'{name} {surname} - {reaction} another text'
full_text = f'я, {username.strip().title()}, зможу заробити лише {total_in_dollars} доларів, що вистачить лише  на {total_cars} тойот, мене це не влаштовує, тому я буду змінювати своє життя і буду завзято вивчати програмування!'
print(full_text)
