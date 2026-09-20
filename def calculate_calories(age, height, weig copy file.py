def calculate_calories(age, height, weight, gender):
    if gender == "male":
        return (10 * weight) + (6 * height) - (5 * age)
    else:
        return (10 * weight) + (6 * height) - (5 * age) - 150

def show_items(data):
    for item in data:
        print(item)

age = int(input("Enter age: "))
height = int(input("Enter height in cm: "))
weight = int(input("Enter weight in kg: "))
gender = input("Enter gender (male/female): ")
goal = input("Enter goal (fatloss/gain): ")

daily_calories = calculate_calories(age, height, weight, gender)

diet_plans = {
    "fatloss": [
        "Boiled Eggs",
        "Salad",
        "Fruits",
        "Vegetables",
        "Grilled Chicken"
    ],
    "gain": [
        "Rice",
        "Milk",
        "Banana",
        "Eggs",
        "Peanut Butter"
    ]
}

workout_plans = {
    "fatloss": (
        "Jumping Jacks",
        "Squats",
        "Plank",
        "High Knees",
        "Mountain Climbers"
    ),
    "gain": (
        "Push Ups",
        "Pull Ups",
        "Lunges",
        "Sit Ups",
        "Bodyweight Squats"
    )
}

week_schedule = {
    "Monday": workout_plans[goal],
    "Tuesday": workout_plans[goal],
    "Wednesday": workout_plans[goal],
    "Thursday": workout_plans[goal],
    "Friday": workout_plans[goal],
    "Saturday": workout_plans[goal],
    "Sunday": workout_plans[goal]
}

print("Fitness 360")
print("Budget Diet Planning System")

print("User Information")
print("Age:", age)
print("Height:", height)
print("Weight:", weight)
print("Gender:", gender)
print("Goal:", goal)

print("Daily Calories Needed")
print(daily_calories)

print("Diet Plan")
show_items(diet_plans[goal])

print("Workout Plan")
show_items(workout_plans[goal])

print("Weekly Workout Schedule")
for day in week_schedule:
    print(day)
    for exercise in week_schedule[day]:
        print(exercise)

file = open("fitness360.txt", "a")

file.write("Fitness 360\n")
file.write("Budget Diet Planning System\n")
file.write("User Information\n")
file.write("Age: " + str(age) + "\n")
file.write("Height: " + str(height) + "\n")
file.write("Weight: " + str(weight) + "\n")
file.write("Gender: " + gender + "\n")
file.write("Goal: " + goal + "\n")
file.write("Calories: " + str(daily_calories) + "\n")

file.write("Diet Plan\n")
for food in diet_plans[goal]:
    file.write(food + "\n")

file.write("Workout Plan\n")
for exercise in workout_plans[goal]:
    file.write(exercise + "\n")

file.write("Weekly Workout Schedule\n")
for day in week_schedule:
    file.write(day + "\n")
    for exercise in week_schedule[day]:
        file.write(exercise + "\n")

file.close()

print("Plan Saved Successfully")
print("Thank You")
print("Stay Fit")
print("Stay Healthy")
