from tabulate import tabulate
import time, sys, os, datetime
from termcolor import cprint
cprint ("Priority Calculator", 'green')
time.sleep(2)
os.system("clear")
name = input("Enter your name here: ")
os.system("clear")
print ("Hey "+name+", this tool is meant to help you \nprioritize your tasks in a given amount of time. \nI will start by asking some questions.")
time.sleep(5)
os.system('clear')
totalTime = int(input("Type the number of hours you have \ntoday STRICTLY for working. \nOnly write the number: "))
os.system('clear')
task_log = {}
date_log = {}
importance_log = {}
today = datetime.date.today()
task_number = 1
while True:
	task = input('Enter a task here: ')
	task_log[task_number] = task
	os.system('clear')
	
	due = input("What day does this task have to be completed by? \nEnter the date in format YYYY MM DD:  ")
	due_list = due.split(' ')
	dates = tuple(due_list)
	year, month, day = dates
	os.system('clear')
	due_date = datetime.date(int(year), int(month), int(day))
	date_log[task_number] = due_date
		
			
	importance = int(input('How important is this task? Enter a number between 1-3, \n1 being not important and 3 being very important: '))
	
	importance_log[task_number] = importance
	os.system('clear')
	while True:
		yesORno = input('Another Task? y/n: ')
		if yesORno == 'y':
			os.system('clear')
			break
		elif yesORno == 'n':
			os.system('clear')
			break
		else:
			print('Invalid input! Type only y/n!')
			os.system('clear')
			continue
	if yesORno == 'y':
		task_number += 1
		continue
	else:
		break
days = []
for i in date_log:
	delta = date_log[i] - today
	days.append(delta.days)
priority_order = sorted(days)
numbers_needed = len(priority_order)
priority_numbers = []
found_keys = []
for i in priority_order:
	found = days.index(i)
	found_keys.append(task_log[found + 1])
for i in task_log:
	task_log[i] = found_keys[i-1]
tasks = []
for task in task_log:
	tasks.append([task_log[task]])
for i in range(1, numbers_needed + 1):
	priority_numbers.append(i)
mins_available = totalTime * 60
numerators = sorted(days, reverse=True)
denominator = 0
for i in numerators:
	denominator += i
timeAllotted90 = []
timeAllotted10 = []
for i in numerators:
	ratiodecimal = i / denominator
	Time = ratiodecimal * mins_available
	whole_time = round(Time)
	minus10 = Time * 0.9
	timeAllotted90.append(minus10)
	minus90 = Time * 0.1
	timeAllotted10.append(minus90)
tenpercentsum = 0
for i in timeAllotted10:
	tenpercentsum += i
importancenumber = 0
for i in importance_log:
	importancenumber += importance_log[i]
importancechunks = tenpercentsum / importancenumber
timeAllotted = []
index = 1
for x in timeAllotted90:
	if importance_log[index] == 1:
		time1 = x + importancechunks
		realtime1 = round(time1)
		timeAllotted.append(realtime1)
	if importance_log[index] == 2:
		time2 = x + (importancechunks * 2)
		realtime2 = round(time2)
		timeAllotted.append(realtime2)
	if importance_log[index] == 3:
		time3 = x + (importancechunks * 3)
		realtime3 = round(time3)
		timeAllotted.append(realtime3)
	index += 1
datadict = {}
for x in range(1, len(tasks)+1):
	datadict[x] = [tasks[x-1], priority_numbers[x-1], timeAllotted[x-1]]
data = []
for i in datadict:
	data.append(datadict[i])
headers = ["Activity","Priority Level","Time Alotted (Minutes)"]
print(tabulate(data, headers, tablefmt="fancy_grid"))
headers = ["Priority Level", "Activity", "Time Alotted"]
