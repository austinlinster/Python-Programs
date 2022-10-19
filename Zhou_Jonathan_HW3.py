answer1 = False
answer2 = False
answer3 = False
answer4 = False
answer5 = False

while answer1 is False:
    annual_saving = int(input("What is your annual savings amount?: "))
    if annual_saving < 0:
        print("Please input non-negative number")
    else:
        answer1 = True

while answer2 is False:
    start_year = int(input("What year do you want to start saving: "))
    if start_year < 2021 or start_year > 2050:
        print("Please enter a year between 2021 to 2050")
    else:
        answer2 = True

while answer3 is False:
    stop_year = int(input("What year do you want to stop saving: "))
    if stop_year < start_year or stop_year > 2100:
        print("Please enter a year between your start year and 2100")
    else:
        answer3 = True

while answer4 is False:
    retirement = int(input("What year do you want to retire: "))
    if retirement < stop_year or retirement > 2100:
        print("Please enter a year between the year you stop saving and 2100")
    else:
        answer4 = True

while answer5 is False:
    interest_rate = float(input("What is the interest rate: "))
    if interest_rate < .5 or interest_rate > 15:
        print("Please enter an interest rate between .5 to 15 percent")
    else:
        answer5 = True
        interest_rate = (interest_rate / 100) 

header1 = "Year"
header2 = "Savings"
header3 = "Interest"
header4 = "Total"
total_saving = 0

print(f'{header1:25}{header2:25}{header3:25}{header4:25}')
print(80 * "-")

for ele in range(start_year,retirement + 1):
    if ele <= stop_year:
        savings = annual_saving
    else:
        savings = 0
    interest_earned = (total_saving + savings) * interest_rate
    total_saving = total_saving + interest_earned + savings
    print(f'{ele}{savings:25,.0f}{interest_earned:25,.0f}{total_saving:25,.0f}')