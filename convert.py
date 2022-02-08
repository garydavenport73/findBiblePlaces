from datetime import datetime, timedelta

# infile = open('Full Reading Plan w_Prayers.fodg', 'r')
# contents = infile.read()
# infile.close()

myDictionary = {}

quitProgram = False

while quitProgram==False:
    try:
        print("\nEnter q to quit.")
        shift_days=input("Enter a number to shift reading schedule by: ")
        
        if shift_days.lower().strip()=="q":
            print("Bye.")
            quitProgram=True
        else:
            shift_days=int(shift_days) #should break here and go to except if doesn't int
            
            for day_count in range(0, 365) : 
                curr_date_object = datetime.strptime('2015-01-01', '%Y-%m-%d') + timedelta(days=day_count)
                #print("Day "  +str(day_count+1).zfill(3) + "-----" + curr_date_object.strftime("%b %d") )
                myDictionary[str("Day "  +str((day_count+shift_days)%365 +1).zfill(3))]=str(curr_date_object.strftime("%b %d"))
            
            for word in myDictionary:
                print(word,myDictionary[word])
                #contents=contents.replace(word,myDictionary[word])

            # outfile = open('newplan.fodg','w')
            # outfile.write(contents)
            # outfile.close()

    except:
        print("Please enter only an integer.")