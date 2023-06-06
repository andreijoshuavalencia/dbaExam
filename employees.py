import time

# prompt user for question
def prompt_user(question):
    print(question, end='')
    time.sleep(1)  # Pause for 1 second for effect
    return int(input())

# displays a loading animation
def loadingAnimation():
    for _ in range(5):
        time.sleep(0.5)
        print("=", end='', flush=True)
    print("Calculating", end='')
    for _ in range(5):
        time.sleep(0.5)
        print("=", end='', flush=True)
    print()

# Welcome message
print("Welcome to the Employee Database!")
time.sleep(1)  # Pause for 1 second for effect

# Prompt the user for input
num_male_new_hires = prompt_user("Enter the number of newly hired males: ")
num_female_new_hires = prompt_user("Enter the number of newly hired females: ")
loadingAnimation()

num_male_permanent = prompt_user("Enter the number of permanent position males: ")
num_female_permanent = prompt_user("Enter the number of permanent position females: ")
loadingAnimation()

num_male_resigned = prompt_user("Enter the number of resigned males: ")
num_female_resigned = prompt_user("Enter the number of resigned females: ")
loadingAnimation()

# calculate total
total_new_hires = num_male_new_hires + num_female_new_hires
total_permanent = num_male_permanent + num_female_permanent
total_resigned = num_male_resigned + num_female_resigned

# calculate percentage
percent_male_new_hires = (num_male_new_hires / total_new_hires) * 100
percent_female_new_hires = (num_female_new_hires / total_new_hires) * 100

percent_male_permanent = (num_male_permanent / total_permanent) * 100
percent_female_permanent = (num_female_permanent / total_permanent) * 100

percent_male_resigned = (num_male_resigned / total_resigned) * 100
percent_female_resigned = (num_female_resigned / total_resigned) * 100

# display results
print()
print("Thank you for your input! Here are the results:")
time.sleep(1)
print("Total newly hired employees: {}".format(total_new_hires))
print("Total permanent employees: {}".format(total_permanent))
print("Total resigned employees: {}".format(total_resigned))
print()


print("Percentage of Data")
time.sleep(1) 
loadingAnimation()
print()
print("Percentage of newly hired males: {:.2f}%".format(percent_male_new_hires))
print("Percentage of newly hired females: {:.2f}%".format(percent_female_new_hires))
print()
print("Percentage of males in permanent positions: {:.2f}%".format(percent_male_permanent))
print("Percentage of females in permanent positions: {:.2f}%".format(percent_female_permanent))
print()
print("Percentage of males resigned: {:.2f}%".format(percent_male_resigned))
print("Percentage of females resigned: {:.2f}%".format(percent_female_resigned))
