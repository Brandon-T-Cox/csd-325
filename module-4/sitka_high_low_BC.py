#Brandon Cox July 5th module 4 assignment 4.2

import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []

    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6]) #feature added- new row called for to add data

        dates.append(current_date)
        highs.append(high)
        lows.append(low)

print("Welcome to the Sitka Weather Program!")
print("Use the menu to view High temperatures, Low temperatures, or Exit the program.")

#feature added- new menu loop with highs, lows, and exit
while True:
    print("\nMenu:")
    print("1. Highs")
    print("2. Lows")
    print("3. Exit")

    choice = input("Enter Highs, Lows, or Exit: ").lower()

    if choice == "highs":
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red')

        plt.title("Daily High Temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)

        plt.show()
#feature added- low temp with blue graph
    elif choice == "lows":
        fig, ax = plt.subplots()
        ax.plot(dates, lows, c='blue')

        plt.title("Daily Low Temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)

        plt.show()
#feature added- exit message
    elif choice == "exit":
        print("Thank you for using the Sitka Weather Program. Goodbye!")
        break
#feature added- else feature requiring specific input or error message shown
    else:
        print("Invalid choice. Please enter Highs, Lows, or Exit.")
