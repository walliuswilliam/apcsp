import requests, datetime
from operator import itemgetter

data = requests.get("https://sheetdb.io/api/v1/1v47x51g4h3b0").json()

today = [datetime.datetime.now().strftime("%x")]
today.append(int(input("How many minutes do you have to do homework today?\n")))

tomorrow = [(datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%x")]
tomorrow.append(int(input("How many minutes do you have to do homework tomorrow?\n")))

dayafter = [(datetime.datetime.now() + datetime.timedelta(days=2)).strftime("%x")]
dayafter.append(int(input("How many minutes do you have to do homework the day after?\n")))

# ASSIGNMENT STARTS HERE

# FIRST WRITE A COMMENT DESCRIBING YOUR ALGORITHM
# HOW WILL YOUR ALGORITHM WORK? WHAT IS THE HEURISTIC YOU ARE USING? WHAT HAPPENS WHEN YOU HAVE TOO MUCH HOMEWORK AND NOT ENOUGH MINUTES? WHAT HAPPENS WHEN YOU HAVE ENOUGH MINUTES TO COMPLETE AN ASSIGNMENT HALFWAY, BUT NOT COMPLETELY? WALK ME THROUGH AN EXAMPLE WITH A FEW ASSIGNMENTS.  
'''
The algorithm will check for the assignments due first. Then, out of those, those worth the most points will be done second. After, the proprity will be taken into account.
Once this is sorted, assignments will be added to a certain day's agaenda based on how much time is availble, and its order in the queue.
'''
# NEXT WRITE YOUR ALGORITHM OUT IN PSEUDOCODE

#FINALLY - IMPLEMENT YOUR ALGORITHM! IF YOU FINISH, THINK ABOUT HOW TO OPTIMIZE YOUR ALGORITHM! MAYBE ADD A "I DONT WANT TO" OPTION TO PUSH YOUR HOMEWORK TO THE NEXT DAY OR A "STAY UP LATE" TO FINISH A PRIORITY ASSIGNMENT

sorted_data = sorted(data, key=itemgetter('Due Date', 'Points', 'Priority'))

def organize_assignments(assignment_list):
    totals = {'today': 0, 'tomorrow': 0, 'dayafter': 0}
    assignments = {'today': [], 'tomorrow': [], 'dayafter': []}
    used_assignments = []

    for day in totals.keys():
        for assignment in assignment_list:
            assignment_time = int(assignment['Time'])

            if totals[day] + assignment_time <= globals()[day][1] and assignment not in used_assignments:
                totals[day] += assignment_time
                assignments[day].append(assignment['Name'])
                used_assignments.append(assignment)
    return assignments


print(organize_assignments(sorted_data))
