#===================================================Imported Modules==========================================
#==============================Coded By Dimzy Boy, <Ukwedje Taiwo Goodness>===================================
from bs4 import BeautifulSoup
from collections import Counter
import sqlite3
from sqlite3 import Error
import random

#==================================================Variables==================================================
days = []
colors = []


# Assign numeric values to colors
rgb_values = {
    'GREEN': (0, 128, 0),
    'YELLOW': (255, 255, 0),
    'BROWN': (165, 42, 42),
    'BLUE': (0, 0, 255),
    'PINK': (255, 192, 203),
    'ORANGE': (255, 165, 0),
    'RED': (255, 0, 0),
    'WHITE': (255, 255, 255),
    'BLACK': (0, 0, 0),
    'CREAM': (255, 253, 208),
    'ARSH': (50, 205, 50),
    'BLEW': (0, 0, 255),
}

#==================================================Main Code==================================================
with open("python_class_question.html") as html_content:
    soup = BeautifulSoup(html_content, 'html.parser')

table = soup.find_all('td')
for day_num in range(0, len(table), 2):
    days.append(table[day_num].text)
    colors.extend(table[day_num + 1].text.split(', '))

unique_colors = list(set(colors))
color_frequency = Counter(colors)

mean_rgb = tuple(sum(color[i] for color in rgb_values.values()) // len(rgb_values) for i in range(3))

# Find the closest color in terms of RGB values
def closest_color(rgb):
    min_distance = float('inf')
    closest = None
    for color, value in rgb_values.items():
        distance = sum(abs(rgb[i] - value[i]) for i in range(3))
        if distance < min_distance:
            min_distance = distance
            closest = color
    return closest

mean_color = closest_color(mean_rgb)
most_frequent_color = color_frequency.most_common(1)[0][0]
sorted_colors = sorted(colors, key=lambda x: color_frequency[x], reverse=True)
median_index = len(sorted_colors) // 2
median_color = sorted_colors[median_index]
total_frequency = sum(color_frequency.values())

#Calculate the Variance
variance = sum(sum((rgb_values[color][i] - mean_rgb[i]) ** 2 for i in range(3)) for color in rgb_values) / len(rgb_values)

#probabilty of picking all the color
for x in unique_colors:
#    print(x)
    probability = color_frequency[x] / total_frequency
    probability_percentage = round(probability * 100)
#    print(probability_percentage, '%')

#Calculate the probability of choosing red as a percentage
probability_red = color_frequency['RED'] / total_frequency
probability_red_percentage = probability_red * 100

#==========================================================Database===========================================

conn = sqlite3.connect('colors.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS colors
             (color TEXT, frequency INTEGER)''')
for color, frequency in color_frequency.items():
    c.execute("INSERT INTO colors (color, frequency) VALUES (?, ?)", (color, frequency))
conn.commit()
conn.close()


# Generate a random 4-digit binary number
binary_number = ''.join(random.choice(['0', '1']) for _ in range(4))

# Convert the binary number to base 10
decimal_number = int(binary_number, 2)

def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Generate the first 50 Fibonacci numbers
fib_numbers = fibonacci(50)

# Sum the Fibonacci numbers
fib_sum = sum(fib_numbers)

print("Days:", days)
print("Unique Colors:", unique_colors)
#print(color_frequency)
print("Mean Color:", mean_color, f'rgb{mean_rgb}')
print("Most frequent Color Worn is:", most_frequent_color )
print("Variance of Color:", variance)
print(f"Probability of choosing red as a percentage: {round(probability_red_percentage)}%")


print("Colors and frequencies saved to SQLite database successfully!")


print(f"Generated binary number: {binary_number}")
print(f"Equivalent decimal number: {decimal_number}")
print(f"The sum of the first 50 Fibonacci numbers is: {fib_sum}")


