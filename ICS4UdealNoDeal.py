def Deal_Or_No_Deal():
    my_list = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000] # Value of cash in the cases
    print("which case are you going to open?")
    def Cases():
        print("How many cases are you going to open?")
        choice = float(input(" "))
        if (choice == 1):
            remaining_cases = (500+1000+5000+10000+25000+50000+100000+50000+1000000)/9 #case excluding first value
        elif(choice == 2):
            remaining_cases = (1000+5000+10000+25000+50000+100000+50000+1000000)/8 
        elif(choice == 3):
            remaining_cases = (5000+10000+25000+50000+100000+50000+1000000)/7 
        elif(choice == 4):
            remaining_cases = (10000+25000+50000+100000+50000+1000000)/6 
        elif(choice == 5):
            remaining_cases = (25000+50000+100000+50000+1000000)/5
        elif(choice == 6):
            remaining_cases = (50000+100000+50000+1000000)/4
        elif(choice == 7):
            remaining_cases  = (100000+50000+1000000)/3
        elif(choice == 8):
            remaining_cases_value = (50000+1000000)/2
        elif(choice == 9):
            remaining_cases_value = (1000000)/1
        else:
            print("Try again")
            Cases()

    
    #The Bankers offer
    Cases()
    Banker_offer = float(input("The banker is offering: "))
    
    if (remaining_cases > Banker_offer):
        print("Take the deal")
    else:
        print("Don't Take the deal")
        Cases()
    
Deal_Or_No_Deal()
