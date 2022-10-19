##Jonathan Zhou jaz978
#Homework 6
#October 16th, 2022
#Apple Stock Price Data Summary Tool

#function to retrieve start and end week from user while validating their input
def get_input():
    check = True
    check1 = True

#while loop validates start week
    while check:
        week_start = input('Please enter the start week: ')
        if week_start == "":
            week_start = 1
            check = False
        else:
            try:
                week_start = int(week_start)
                if week_start < 1 or week_start > 52:
                    print('Please enter a number between 1 - 52.')
                else:
                    check = False
            except:
                print('Please enter a valid integer.')

#while loop validates end week
    while check1:
        week_end = input('Please enter the end week: ')
        if week_end == "":
            week_end = 52
            check1 = False
        else:
            try:
                week_end = int(week_end)
                if week_end > 52:
                    print('Please enter a week between start and 52.')
                elif week_end < week_start:
                    print('The ending week cannot be before the starting week.')
                else:
                    check1 = False
            except:
                print('Please enter a valid integer.')

    return week_start, week_end

#function to retrieve data from file within the ranges of start and end week and put it into list
def read_data(start, end):
    file_temp = open('ApplePrices.txt', 'r')
    prices_list = []

#loop to skip past any weeks before our start date
    for skip in range(1 , start):
        line = file_temp.readline()

#loop to retrieve prices from specified start and end week
    for store in range(start, end + 1):
        line = file_temp.readline()
        line = float(line.rstrip('\n'))
        prices_list.append(line)
    
    return prices_list

#function to create week and change list
def make_lists(start,end,values):
    week_list = []
    change_list = []
    point1 = 0
    point2 = 1

    for i in range(start, end + 1):
        week_list.append(i)
    
    change_list.append(0)

    if len(values) != 1:
        for i in range(0,end-start):
            change = values[point2] - values[point1]
            change_list.append(change)
            point1 += 1
            point2 += 1
    
    return week_list, change_list

#function to analyze best and worst changes along with corresponding week
def analyze_data(week, change):
    avg = sum(change)/len(change)

    worst = min(change)
    worst_week_index = change.index(worst)
    worst_week = week[worst_week_index]

    best = max(change)
    best_week_index = change.index(best)
    best_week = week[best_week_index]
    
    return avg, worst, worst_week, best, best_week

#function to display data summary
def display_output(avg, worst, worst_week, best, best_week):
    print(f'The average change is {avg:.2f}')
    print(f'The week with the highest growth is week {best_week} with a change of {best:.2f}')
    print(f'The week with the lowest growth is week {worst_week} with a change of {worst:.2f}')

#main function along with creation of nested list in main
def main():
    nested_list = []

    start, end = get_input()
    prices = read_data(start, end)

    nested_list.append(prices)

    week, change = make_lists(start, end, nested_list[0])
    
    nested_list.append(week)
    nested_list.append(change)

    avg, worst, worst_week, best, best_week = analyze_data(nested_list[1], nested_list[2])

    display_output(avg, worst, worst_week, best, best_week)

main()
