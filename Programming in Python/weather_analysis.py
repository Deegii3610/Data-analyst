# Assignment 2 /Delgersuren.N/
#question 1
print("Question 1\n")

import random


daily_temperatures = [random.randint(0, 35) for _ in range(30)]

hottestDay = max(daily_temperatures)
print("Hottest temperature is: ", hottestDay)

coldestDay = min(daily_temperatures)
print("Coldest temperature is: ", coldestDay)

averageTemp = sum(daily_temperatures)/len(daily_temperatures)
print("The average temperature is: ", averageTemp)
print("\n")

#question 2
print("Question 2\n")
daily_rainfall = [random.randint(0, 10) for _ in range(30)]

"""import matplotlib.pyplot as plt
plt.plot(range(30), daily_temperatures, label="Daily temperature", color='blue', marker='o')

plt.plot(range(30), daily_rainfall, label="Daily rainfall", color='red', marker='x')


plt.xlabel('Day')
plt.ylabel("Temperature and Rainfall")
plt.legend()
plt.show()
"""

worstTemprature = 35
worstRainfall = 0
WorstDay = 0
for day, (tempera, rainfall) in enumerate(zip(daily_temperatures, daily_rainfall)):
    if tempera <= worstTemprature and rainfall >= worstRainfall:
        worstTemprature = tempera
        worstRainfall = rainfall
        WorstDay = day

        
print(f"Worst day is {WorstDay+1}, temperature is {worstTemprature} and rainfall is {worstRainfall}")
print("\n")

# Question 3
print("Question 3\n")
weekly_temperatures = [[random.randint(-1,10) for _ in range(7)] for _ in range(4)]

for weeks, teweek in enumerate(weekly_temperatures):
    for dt in teweek:
        if dt <= 0:
            print(f"Temperature is freezing {dt} in {weeks} week.")

print("\n")

# Question 4

print("Question 4\n")

def hottest_coldest_average(temperatures):
    hottemp = max(temperatures)
    print("Hottest temperature is: ", hottemp)
    coldtemp = min(temperatures)
    print("Coldest temperature is: ", coldtemp)
    avTemp = sum(temperatures)/len(temperatures)
    print("The average temperature is: ", avTemp)
    

hottest_coldest_average(daily_temperatures)

def worst_day_record(temperatures, rainfall):
    wTemprature = 35
    wRainfall = 0
    WDay = 0
    for woday, (tem, rain) in enumerate(zip(temperatures, rainfall)):
        if tem <= wTemprature and rain >= wRainfall:
            wTemprature = tem
            wRainfall = rain
            WDay = woday     
    print(f"Worst day is {WDay+1}, temperature is {wTemprature} and rainfall is {wRainfall}")

worst_day_record(daily_temperatures, daily_rainfall)
print("\n")

# Question 5

print("Question 5\n")


international_weather = {
    "Ireland": {
        'temperature': [random.randint(0, 30) for _ in range(30)],
        'rainfall': [random.randint(0, 10) for _ in range(30)]
    },
    "France": {
        'temperature': [random.randint(0, 30) for _ in range(30)],
        'rainfall': [random.randint(0, 10) for _ in range(30)]
    },
    "Spain": {
        'temperature': [random.randint(0, 30) for _ in range(30)],
        'rainfall': [random.randint(0, 10) for _ in range(30)]
    }
}


hottest_coldest_average(international_weather["Ireland"]['temperature'])
worst_day_record(international_weather["Ireland"]['temperature'],international_weather["Ireland"]['rainfall'])
print("\n")

# Question 6

print("Question 6\n")
Ask = True

while Ask:
    country = input("Enter the country (Ireland, France, Spain), or type 'Done' to finish: ")

    if country == "Done":
        Ask = False
        continue  

    if country not in international_weather:
        print("Invalid country. Please enter Ireland, France, or Spain.")
    else:
        randtem = international_weather[country]['temperature']
        randrain = international_weather[country]['rainfall']
        print(f"In {country}:")
        hottest_coldest_average(randtem)
        worst_day_record(randtem, randrain)
        print("\n")


