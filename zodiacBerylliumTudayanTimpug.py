def chinese_zodiac(year):
    animals = ["Monkey (猴 / Hóu)", "Rooster (鸡 / Jī)", "Dog (狗 / Gǒu)",
               "Pig (猪 / Zhū)", "Rat (鼠 / Shǔ)", "Ox (牛 / Niú)",
               "Tiger (虎 / Hǔ)", "Rabbit (兔 / Tù)", "Dragon (龙 / Lóng)",
               "Snake (蛇 / Shé)", "Horse (马 / Mǎ)", "Goat (羊 / Yáng)"]
    return animals[year % 12]

year_of_birth = int(input("Enter your birth year: "))
if year_of_birth < 1900:
    print("Invalid year, it should not be earlier than 1900")
else:
    print("Your Chinese Zodiac Sign is: ", chinese_zodiac(year_of_birth))