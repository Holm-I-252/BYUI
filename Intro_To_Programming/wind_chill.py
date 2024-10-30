temp = float(input("Enter the temperature: "))
unit = input("Enter 'C' for Celsius or 'F' for Fahrenheit: ").upper()

def calculate_wind_chill(temp, unit):
    wind_chill = 0

    for i in range(1, 13):
        if unit == "F":
            wind_chill = 35.74 + (0.6215 * temp) - (35.75 * ((i * 5) ** 0.16)) + (0.4275 * temp * ((i * 5) ** 0.16))
        elif unit == "C":
            wind_chill = 13.12 + (0.6215 * temp) - (11.37 * ((i * 5) ** 0.16)) + (0.3965 * temp * ((i * 5) ** 0.16))
        print(f"At tempurature {temp} {unit} and wind speed {i * 5} mph, the wind chill is {wind_chill:.2f} degrees.")

calculate_wind_chill(temp, unit)