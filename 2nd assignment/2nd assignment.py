import csv
import pandas as pd
import matplotlib.pyplot as plt

#######################Question 6############################################## 

def get_all_info():
    
    #Choice Table
    print("Please select what you are interested in finding: \n")
    print("1.To find every athlete that has competed in every Grand Slam Tournament, insert 1.")
    print("2.To find every athlete that has won a Grand Slam Tournament, insert 2.")
    print("3.To find every runner-up that has never won a Grand Slam Tournament. insert 3.")
    print("4.To find the number of Grand Slam tournaments an athlete has won, insert 4.")
    print("5.To find the athletes with most Grand Slam wins, insert 5.")
    print("Type stop to end the program...")
    validchoices = ["1","2","3","4","5"]
    choice = input("Input a choice, from 1 to 5 (integer): ")
    while choice not in validchoices:
      choice = input("Wrong input. Select an integer from 1 to 5: ")
      if choice == 'stop':                      #break the loop in case "stop" is inserted
          print("Program end.")
          break
#######################Question 1##############################################    
#function get_tour_info
    def get_tour_info(filename, tour):
    
        header_list = ["Year", "Tournament", "Winner", "Runner-Up"]
        reader = pd.read_csv(filename, delimiter = ',', quoting = csv.QUOTE_NONE, names = header_list)  #read data into dataframes
        
        #Rows take "true" values wherever the column "Tournament" is equal to the desired tournament
        is_French =  reader['Tournament']=='French Open'
        is_Aupen =  reader['Tournament']=='Australian Open'
        is_US =  reader['Tournament']=='U.S. Open'
        is_Wimb =  reader['Tournament']=='Wimbledon'
    
        #new data with the corresponding tournaments
        French = reader[is_French]
        Aupen = reader[is_Aupen]
        US = reader[is_US]
        Wimb = reader[is_Wimb]
    
        tmd = {}    
        
        #returning a dictionary with "Year" as the key and value ["Winner" vs. "Runner Up"]
        if tour == 'French Open':
            for index, row in French.iterrows():
                tmd[row[0]] = "{} vs. {}".format(row[2],row[3])
        elif tour == 'Australian Open':
            for index, row in Aupen.iterrows():
                tmd[row[0]] = "{} vs. {}".format(row[2],row[3])
        elif tour == 'U.S. Open':
            for index, row in US.iterrows():
                tmd[row[0]] = "{} vs. {}".format(row[2],row[3])
        else:
            for index, row in Wimb.iterrows():
                tmd[row[0]] = "{} vs. {}".format(row[2],row[3])

        return(tmd)
######################################def function end########################################
    
    #variable initialization so that loops "while" and "if" run smoothly
    
    filename = 'none'
    tour = 'none'
    validTours = ['French Open', 'Australian Open', 'U.S. Open', 'Wimbledon']

    counter = 0
    while filename != 'tennis_men.csv':
        if counter == 0:
            filename = input("Insert the filename;(e.g. tennis_men.csv, insert stop to stop the loop): " )
        else:
            filename = input("This filename does not exist in your working directory. Try again (insert stop to stop the loop): " )
    
        if filename == 'stop':
            break
        counter =+ 1
 
    counter = 0
    while tour not in validTours:
        if counter == 0:
            tour = input("What Tournament are you interested in? (Accepted Tournaments: French Open, U.S. Open, Australian Open & Wimbledon - insert stop to break loop): " )
        else:
            tour = input("This Tournament is not valid, try again: (Accepted Tournaments: French Open, U.S. Open, Australian Open & Wimbledon - insert stop to break loop): " )
    
        if tour == 'stop':
            break  
        counter=+1
   
    tennis = get_tour_info(filename,tour)       #final dictionary
    
  
#######################Question 2##############################################

#function get_winner_info
    def get_winner_info(dictionary):
        #dictionary to dataframe
        
        z = pd.DataFrame(list(dictionary.items()), columns=['Year', 'Winner'])
        tempplayers = z.Winner.str.split(' vs.',expand=True) #split column "Winner vs. RunnerUp" into 2 new columns
        tempplayers.columns = ['Winner', 'RunnerUp']
        z = z.Year

        winnerdf = pd.concat([z, tempplayers], axis = 1)    #combine columns "Years" & "Winners"
        wonyears = winnerdf.groupby('Winner')['Year'].apply(list).reset_index(name='Years Won')     #a list containing the years an athlete has won Grand Slam Tournaments

        wpd = {}
        for index, row in wonyears.iterrows():
            wpd[row[0]] = row[1]    #dictionary with "Winner" as key and the years they won in a list

        return(wpd)

    winner_info = get_winner_info(tennis)
######################################def function end########################################      

#######################Question 3##############################################
 
#function get_runnerups_info
    def get_runnerups_info(dictionary):
    
        z = pd.DataFrame(list(dictionary.items()), columns=['Year', 'Winner'])      #dictionary to dataframe
        tempplayers = z.Winner.str.split(' vs. ',expand=True)                       #create 2 new columns, Winner and RunnerUp to replace old "Winner" column
        tempplayers.columns = ['Winner', 'RunnerUp']                                #add column names

        RunnerUps = list(set(tempplayers['RunnerUp']).difference(tempplayers['Winner']))    #a list with the difference of "RunnerUp" and "Winner" sets
     
        return(RunnerUps)
######################################def function end########################################  
    
    rups = get_runnerups_info(tennis)
    
#######################Question 4##############################################

#function get_tour_info
    def get_tour_info(dictionary, name):
        
        #dictionary to dataframe
        z = pd.DataFrame(winner_info.items())
        z.columns = ['Winner','Years']
        
        is_Player = list(z.Winner==name)    #column with Trues values in the rows with the desired athlete name 
        idx = is_Player.index(True)         #corresponding indices

        numberoftours = len(z)*[0]          #zero list
        for row in range(len(z)):
            numberoftours[row] = len(z.Years[row])  #the column with the Tournament finals each athlete won
        
        result = numberoftours[idx]         #the number of Grand Slam finals won by the desired athlete

        return(result)
######################################def function end########################################   
    
    if choice == "4":
        winner_names = pd.DataFrame(list(tennis.items()), columns=['Year', 'Winner'])       #the set of winners to check for valid inputs
        winner_names = winner_names.Winner.str.split(' vs. ',expand=True)                   
        winner_names.columns = ['Winner', 'RunnerUp']
        winner_names = winner_names['Winner']
    

        print("\nGive athlete name, to check the number of",tour,"finals she/he has won: ")
        name = input()
        while name not in winner_names.values:
            name = input('This name is either not valid, or has never won a Grand Slam Tournament! Try again (insert stop to stop the loop): ')
            if name == 'stop':
                print('Function stopped.')
                break
    
        tour_info = get_tour_info(winner_info, name)
    
    else:
        tour_info = 'No info'
#######################Question 5##############################################
        
    if choice == "5":
        n = -1
        l = len(winner_info)

        while n not in range(0,l):
            print('Insert the number of n top players that have won', tour, 'finals: \n(only positive integers, smaller than', l,')')
            n = int(input())
 
#function get_wins_info
        def get_wins_info(dictionary, n):
            
            #using the same method as in function get_tour_info to start with
            z = pd.DataFrame(dictionary.items())    
            z.columns = ['Winner','Years']

            numberoftours = len(z)*[0]

            for row in range(len(z)):
                numberoftours[row] = len(z.Years[row])  
                
            #then, I sort by wins number to find n top athletes
            numberoftours = pd.DataFrame(numberoftours)
            number_per_winner = pd.concat([z.Winner, numberoftours], axis=1)
            number_per_winner.columns = ['Athlete','Wins']
            number_per_winner = number_per_winner.sort_values('Wins', ascending=False)

            result = pd.DataFrame.head(number_per_winner, n)
            return(result)
    
        get_wins = get_wins_info(winner_info, n)
#####################BONUS Question############################ 
#function get_top5_info
        def get_top5_info():
        
            top5 = get_wins_info(winner_info, 5)    #top 5 athletes for the desired tournament
            ind = [0,1,2,3,4]
            x = top5.Athlete
            y = top5.Wins
            plot = plt.style.use('ggplot')
            plt.bar(x,y)
            plt.xlabel('Athletes',fontsize=7)
            plt.xticks(ind, x, fontsize=5, rotation=30)
            plt.ylabel('Number of wins', fontsize=7)
            plt.title('Top 5 athletes with most Grand Slam wins')

            return(plot)
        
    else:
        get_wins = "No info"
        
################################# def function end######################################## 

#Print result based on the choice the user selected at the start of the program
    if choice == "1":
        for k,v in tennis.items():
            print( k, v,)
    elif choice == "2":
            print("\nThe following athletes have won a", tour, "final the following year(s) \n", winner_info, '\n')
    elif choice == "3":
            print("\nThe following athletes played a final but never won a",tour,"final:\n", rups, '\n')
    elif choice == "4":
            print("\nAthlete",name,"has won",tour_info, tour,"finals! \n")
    elif choice == "5":
            print("\nThe top", n, "athletes with most", tour, "Grand Slam finals are: \n", get_wins)
            print("\nIn case of equal wins the print is random! \n")
            
            #print το bonus ερώτημα, σε περίπτωση που επιθυμεί ο user
            top5print = input("Do you wish to print top 5 athletes with most wins? (Yes to print, anything else to continue) ")
            
            if top5print == "Yes":
                top5plot = get_top5_info()
                #print(top5plot)
                plt.show()
            
    return(tennis, winner_info, rups, tour_info, get_wins)
######################Question 6##############################################

#loop until user select "stop"
breaker = "No"
while breaker != "Yes":
    get_all_info()
    breaker = input("Do you wish to stop; (Yes to stop program, anything else to continue): ")

##############################################BONUS##################################

