import numpy as np
import random as rm

states = ["Sleep","Icecream","Run"]

transitionName = [["SS","SR","SI"],["RS","RR","RI"],["IS","IR","II"]]

transitionMatrix = [[0.2,0.6,0.2],[0.1,0.6,0.3],[0.2,0.7,0.1]]

if sum(transitionMatrix[0])+sum(transitionMatrix[1])+sum(transitionMatrix[1]) != 3:
    print("Somewhere, something went wrong. Transition matrix, perhaps?")
else: print("All is gonna be okay, you should move on!! ;)")

def activity_forecast(days, initial):
    activityToday = initial
    activityList = [activityToday]
    i = 0
    prob = 1
    while i != days:
        if activityToday == "Sleep":
            change = np.random.choice(transitionName[0],replace=True,p=transitionMatrix[0])
            if change == "SS":
                prob = prob * 0.2
                activityList.append("Sleep")
                pass
            elif change == "SR":
                prob = prob * 0.6
                activityToday = "Run"
                activityList.append("Run")
            else:
                prob = prob * 0.2
                activityToday = "Icecream"
                activityList.append("Icecream")
        elif activityToday == "Run":
            change = np.random.choice(transitionName[1],replace=True,p=transitionMatrix[1])
            if change == "RR":
                prob = prob * 0.5
                activityList.append("Run")
                pass
            elif change == "RS":
                prob = prob * 0.2
                activityToday = "Sleep"
                activityList.append("Sleep")
            else:
                prob = prob * 0.3
                activityToday = "Icecream"
                activityList.append("Icecream")
        elif activityToday == "Icecream":
            change = np.random.choice(transitionName[2],replace=True,p=transitionMatrix[2])
            if change == "II":
                prob = prob * 0.1
                activityList.append("Icecream")
                pass
            elif change == "IS":
                prob = prob * 0.2
                activityToday = "Sleep"
                activityList.append("Sleep")
            else:
                prob = prob * 0.7
                activityToday = "Run"
                activityList.append("Run")
        i += 1    
    return activityList

list_activity = []
count = 0

for iterations in range(1,10000):
        list_activity.append(activity_forecast(2, "Sleep"))


for smaller_list in list_activity:
    if(smaller_list[2] == "Run"):
        count += 1

percentage = (count/10000) * 100
print("The probability of starting at state:'Sleep' and ending at state:'Run'= " + str(percentage) + "%")

list_activity_RI = []
count_RI = 0

for iterations in range(1,10000):
        list_activity_RI.append(activity_forecast(2, "Run"))


for smaller_list in list_activity_RI:
    if(smaller_list[2] == "Icecream"):
        count_RI += 1

percentage = (count_RI/10000) * 100
print("The probability of starting at state:'Run' and ending at state:'Icecream'= " + str(percentage) + "%")