import csv
#import pandas as PD
title = ['TYPE','CONTENT','PRIORITY','INDENT','AUTHOR','RESPONSIBLE','DATE','DATE_LANG','TIMEZONE']
task = ["task","","4","1","","","","",""]
emptyline = ['','','','','','','','','']
mylines = []    
mytodolist = []
mytodolist.append(title)
with open ('/Users/ftucci/Downloads/todoist/shoppingweekend.txt', 'rt') as myfile:  # Open lorem.txt for reading text.
    for line in myfile:                   # For each line of text,
        
#        print(">>>>>")
#        print(task)
        
        holdings = line.strip('❏').replace("\u2002", " ").strip('✔')
        
        task[1] = holdings.rstrip().strip()
        
        if "✔" or "❏" in holdings:
           task[3] = "2"    
        else:
           task[3] = "1" 

        task[1] = holdings.strip().strip('✔').strip('❏').strip() 

        mytodolist.append(task.copy())
        mytodolist.append(emptyline)

#        print("<<<<<")             

#for todo in mytodolist:
#    print(todo)


#write the csv file
with open('/Users/ftucci/Downloads/todoist/shopppping.csv', 'w') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    writer.writerows(mytodolist)

#df = PD.read_fwf('/Users/ftucci/Downloads/todoist/testinput.txt')
#df.to_csv('/Users/ftucci/Downloads/todoist/testinput.csv')
