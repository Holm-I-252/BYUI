import csv

with open("Intro_To_Programming/life-expectancy.csv", "r") as file:
    data = csv.reader(file)

    lowest_life_ex = 100
    lowest_result = ""

    highest_life_ex = 0
    highest_result = ""

    user_year = int(input("Enter a year to learn about it: "))

    year_list = []
    year_data = []

    user_country = input("Enter a country to learn about it: ").title()

    country_list = []
    country_data = []


    for i in data:
        if i[3] == "Life expectancy (years)":
            continue
        if float(i[3]) < lowest_life_ex:
            lowest_life_ex = float(i[3])
            lowest_result = i
        if float(i[3]) > highest_life_ex:
            highest_life_ex = float(i[3])
            highest_result = i
        
        if int(i[2]) == user_year:
            year_list.append(float(i[3]))
            year_data.append(i)

        if i[0] == user_country:
            country_list.append(float(i[3]))
            country_data.append(i)

    print(f"\nThe country with the lowest life expectancy overal was {lowest_result[0]} in {lowest_result[2]} with a life expectancy of {lowest_result[3]} years.")
    print(f"The country with the highest life expectancy overal was {highest_result[0]} in {highest_result[2]} with a life expectancy of {highest_result[3]} years. \n")

    if len(year_list) == 0:
        print("There is no data for that year.")
    else:
        average = sum(year_list) / len(year_list)

        print(f"For {user_year}:")
        print(f"The average life expectancy in {user_year} was {average} years.")

        highest_year = 0
        highest_year_result = ""
        lowest_year = 100
        lowest_year_result = ""

        for i in year_data:
            if float(i[3]) < lowest_year:
                lowest_year = float(i[3])
                lowest_year_result = i
            if float(i[3]) > highest_year:
                highest_year = float(i[3])
                highest_year_result = i



        print(f"The country with the lowest life expectancy in {user_year} was {lowest_year_result[0]} with a life expectancy of {lowest_year_result[3]} years.")
        print(f"The country with the highest life expectancy in {user_year} was {highest_year_result[0]} with a life expectancy of {highest_year_result[3]} years.")

    if len(country_list) == 0:
        print("There is no data for that country.")
    else:
        average = sum(country_list) / len(country_list)

        print(f"\nFor {user_country}:")
        print(f"The average life expectancy in {user_country} was {average} years.")

        highest_country = 0
        highest_country_result = ""
        lowest_country = 100
        lowest_country_result = ""

        for i in country_data:
            if float(i[3]) < lowest_country:
                lowest_country = float(i[3])
                lowest_country_result = i
            if float(i[3]) > highest_country:
                highest_country = float(i[3])
                highest_country_result = i

        print(f"The lowest life expectancy in {user_country} was {lowest_country_result[3]} years in {lowest_country_result[2]}.")
        print(f"The highest life expectancy in {user_country} was {highest_country_result[3]} years in {highest_country_result[2]}.")








            
