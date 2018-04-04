# coding=utf-8
my_variable = "hello"
grades = [77, 80, 90]
tuple_grades = (77, 80, 90)
set_grades = {77, 80, 90}

set_grades.add(60)
set_grades.add(60)

your_lottery_numbers = {1, 2, 3, 4, 5}
winning_numbers = {1, 3, 5, 7, 9, 11}

# print(your_lottery_numbers.intersection(winning_numbers))
# print(your_lottery_numbers.union(winning_numbers))
# print({1, 2, 3, 4}.difference({1, 2}))

# for character in my_variable:
#     print(character)
#
# my_list = [1, 3, 5, 7, 9]
#
# for number in my_list:
#     print(number ** 2)

user_wants_number = True
while user_wants_number:
    print(10)
    user_input = raw_input("should we print again? (y/n)\n")
    if user_input == 'n':
        user_wants_number = False