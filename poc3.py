import csv
#import pandas as PD
title = ['TYPE','CONTENT','PRIORITY','INDENT','AUTHOR','RESPONSIBLE','DATE','DATE_LANG','TIMEZONE']
task = ["task","","4","1","","","","",""]
emptyline = ['','','','','','','','','']
mylines = []    
mytodolist = []
mytodolist.append(title)
with open ('/Users/ftucci/Downloads/todoist/home.txt', 'rt') as myfile:  # Open lorem.txt for reading text.
    for line in myfile:                   # For each line of text,
        
        print(">>>>>")
        print(line)
        
        #holdings = line.strip()   # strip spaces
        holdings = line
#        print(holdings)

        holdings = holdings.strip('❏').strip('✔')
#        print(holdings)
#        print(holdings[0])
#        print(holdings[1])
        
        index = 0
        count = 0 
        
        for a in holdings: 
            index+=1
            if (a.isspace()) == True and index < 3: 
                count+=1
        
        if count == 2:
            task[3] = "2"
        else: 
            task[3] = "1"

        task[1] = holdings.strip()

        task[1] = holdings.strip().strip('✔').strip('❏').strip() 

        mytodolist.append(task.copy())
        mytodolist.append(emptyline)

#        print("<<<<<")             

#for todo in mytodolist:
#    print(todo)

#write the csv file
with open('/Users/ftucci/Downloads/todoist/home.csv', 'w') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    writer.writerows(mytodolist)