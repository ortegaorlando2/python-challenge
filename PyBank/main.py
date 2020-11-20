
import os #imports operating system peculiarities
import csv #imports special group of functions that handles csv files


#Assigns to variable a string with the location of the original data
Myfileis = "C:\\Users\\oorte\\Documents\\RICE-CLASS-MATERIAL\\python-challenge\\python-challenge\\PyBank\\Resources\\budget_data.csv"

#opens the file located in "Myfileis" and assigns a reference called Finances
with open(Myfileis) as Finances: #Finances is a long string with the whole csv file
    #We are going to split the csv file in its components
    #We create an iterator called "Financesreader" that will contain 
    #the csv file structure line by line
    
    Financesreader=csv.reader(Finances)
    
    #next() advances the iterator one row, that is to the first line of the csv
    Finances_header=next(Financesreader)
#    print(Finances_header)
    
#variables declaration
    currentdate=[]
    previousprofitloss=[]
    currentprofitloss=[]
    change=[0]
    monthsnumber=0
    sumofchanges=0
    greatestincrease=0
    greatestdecrease=0
    datemaxincrease=''
    datemaxdecrease=''

# we call each line (addline) by advancing Financesreader through Finances and
# assigning the line to a list. 
# 
# Then we create lists for each column in Finances
    
    for addline in Financesreader:

        currentdate.append(addline[0])
        previousprofitloss.append(int(addline[1]))
        currentprofitloss.append(int(addline[1]))      

# Initialize a variable that contains the previous profit/loss
    previous=previousprofitloss[0]

# Starting in the second line of the list, we can calculate the change
# of profit loss for each month. The first change is cero.
    for i in range(1,len(currentdate)):
        change.append(currentprofitloss[i]-previous) #creates a list for change
        previous=currentprofitloss[i] #reassigns the previous profit/loss

# Next, we investigate which are the maximum and minimum profit/losses and when
# we can use if statements for that

        if change[i] >= greatestincrease:
            greatestincrease=change[i]
            datemaxincrease=currentdate[i]
    
        if change[i] <= greatestdecrease:
            greatestdecrease=change[i]
            datemaxdecrease=currentdate[i]
        
# Preparing a report similar to the example in the homework
print('\n'*3)
print('EL CHAPARRO COLORADO LLC')
print('Below is a balance report for the period: \n',  
    '**Jan-2010 to Feb-2017**')
print('\n')

print('Financial Analysis')
print('-'*25)
print(f'Number of months in dataset= {len(currentdate)}')
print(f'Net total amount profits/losses over the period  ${sum(previousprofitloss)}')
average= sum(change)/(len(change)-1) #the average does not include the first element in the list
ave2decimals="{:.2f}".format(average) #this formats average to two decimals
print(f'Average of profits/losses over the period=  ${ave2decimals}')
print(f'The greatest increase in profits was  (${greatestincrease}) in {datemaxincrease}')
print(f'The greatest decrease in profits was  (${greatestdecrease}) in {datemaxdecrease}')
print('\n')

#Writing results to a text file with the name of the ficticious company
output= os.path.join('Analysis','ChaparroColorado.txt') 
output=open(output,'w')
output.write('EL CHAPARRO COLORADO LLC\n')
output.write('Below is a balance report for the period:\n')
output.write('**Jan-2010 to Feb-2017**\n')
output.write('-'*25)
output.write('\n')
output.write(f'Number of months in dataset= {len(currentdate)} \n')
output.write(f'Net total amount profits/losses over the period  ${sum(previousprofitloss)} \n')
output.write(f'Average of profits/losses over the period=  ${ave2decimals} \n')
output.write(f'The greatest increase in profits was  (${greatestincrease}) in {datemaxincrease} \n')
output.write(f'The greatest decrease in profits was  (${greatestdecrease}) in {datemaxdecrease} \n')
output.write('\n')

output.close()

