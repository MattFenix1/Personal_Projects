
def Menu():
    print("Choose an Option:")
    print("1. Show List")
    print("2. Add to the List")
    ans=int(input("Pick an Option Here: "))
    while ans == 1 or ans == 2:
        if ans == 1:
            List(t,wtw,a,wa)
        elif ans == 2:
            Append()
        else:
            print("Pick another option.")
            

def Sort(t,wtw,a,wa):
    size = len(t)
    for k in range(0, size-1):
        for i in range(0, size-1):
            if t[i] > t[i+1]:
                temp = t[i]
                t[i] = t[i+1]
                t[i+1] = temp

                temp = wtw[i]
                wtw[i] = wtw[i+1]
                wtw[i+1] = temp
                
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp
                
                temp = wa[i]
                wa[i] = wa[i+1]
                wa[i+1] = temp

def List(t,wtw,a,wa):
    h1 = "Title"
    h2 = "Where to Watch"
    h3 = "Additional People?"
    h4 = "Watched?"

    Sort(t,wtw,a,wa)
    size=len(t)
    print(f"{h1:45} {h2:18} {h3:18} {h4:8}")
    print("---------------------------------------------------------------------------------------------")
    for i in range(0, size):
        if i<size:
            print(f"{t[i]:46}{wtw[i]:19}{a[i]:19}{wa[i]:8}")
    print("\n")
    Menu()
            
def Append():
    t=input("What is the title? ")
    wtw=input("Where can this be watched? ")
    a=input("Does anyone else need to attend? ")
    wa=input("Have you watched this yet? ")
    fields=[t, wtw, a, wa]
    with open(r"C:\Users\Tyler\Desktop\Personal Folder\Personal_Projects\MovieList\MovieList.csv", 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(fields)
    print("\n")
    Menu()
        
########################Main Program#############################################
import os    
import csv

t=[]
wtw=[]
a=[]
wa=[]

with open(r"C:\Users\Tyler\Desktop\Personal Folder\Personal_Projects\MovieList\MovieList.csv") as csvfile:
    file=csv.reader(csvfile)
    for row in file:
        t.append(row[0])
        wtw.append(row[1])
        a.append(row[2])
        wa.append(row[3])

Menu()