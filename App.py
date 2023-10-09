""" implements the interactivity with the user.
"""

# Three Attrivutes
Engagement = 0
Self_discipline = 0
Stress_Level = 0
Goal_Planning = 0

#Module 1

def two_week_pr():
    oritentation_choice = input("Week 2: Do you want to attend orientation? (yes/no): ").lower()
    if oritentation_choice == "yes":
        Engagement = +10
        Self_discipline = +10
        Stress_Level = +10
        Goal_Planning = +10
        print("Congratulations, you've gained 10 points across all three attributes!")
    else:
        Engagement = -5
        Self_discipline = -5
        Stress_Level = -5
        Goal_Planning = -5
        print("Oh no! You've lost 5 points across the board, but no worries. You will have the oppuruntity to make a different choice in the following week!")

    firstyr_guide = input("Week 2: Do you want to read 'Succeeding @ Sheridan: A guide for your first years' (yes/no): ").lower()
    if firstyr_guide == "yes":
        Engagement = +10
        Self_discipline = +10
        Stress_Level = +10
        Goal_Planning = +10
        print("Congratulations, you've gained 10 points across all three attributes!")
    else:
        Engagement = -5
        Self_discipline = -5
        Stress_Level = -5
        Goal_Planning = -5
        print("Oh no! You've lost 5 points across the board, but no worries. You will have the oppuruntity to make a different choice in the following week!")
  
    acl = input("Week 2: Are you in need of accomindations (yes/no): ").lower()
    if acl == "no":
        print("No worries, your score won't be affected by this!")
    else:
        input("Week 2: Would you like to sign up for accessible learning' (yes/no): ").lower()
        if firstyr_guide == "yes":
            Engagement = +10
            Self_discipline = +10
            Stress_Level = +10
            Goal_Planning = +10
            print("Congratulations, you've gained 10 points across all three attributes!")
        else:
            Engagement = -10
            Self_discipline = -10
            Stress_Level = -10
            Goal_Planning = -10
            print("Oh no! You've lost 10 points across the board. You will immensely be affected by this in the following weeks.")
    
    
    sheridan_central = input("Week 2: Would you like to login to Sheridan Central (it's like the Google of Sheridan) with your Sheridan username and password? (yes/no): ").lower()
    if sheridan_central == "no":
            Engagement = -10
            Self_discipline = -10
            Stress_Level = -10
            Goal_Planning = -10
            print("Oh no! You've lost 10 points across the board. You will immensely be affected by this in the following weeks.")
    else:
        input("Week 2: Would you like to Update your contact information and Set up multifactor authentication (MFA)' (yes/no): ").lower()
        if sheridan_central == "yes":
            Engagement = +10
            Self_discipline = +10
            Stress_Level = +10
            Goal_Planning = +10
            print("Congratulations, you've gained 10 points across all three attributes!")
        else:
            Engagement = -10
            Self_discipline = -10
            Stress_Level = -10
            Goal_Planning = -10
            print("Oh no! You've lost 10 points across the board. Unfortunately, you will not be able to redo this action in following weeks.")
   
    upcoming_event = input("Week 2: There are a couple of upcoming events, would you like to see the options (yes/no): ").lower()
    if upcoming_event == "no":
            Engagement = -10
            Self_discipline = -10
            Stress_Level = -10
            Goal_Planning = -10
            print("Oh no! You've lost 10 points across the board, and unfortunately you will not be able to redo this action.")
    else:
        print("These are the following options; Accessing Supports:  July 5 at 10:00 A.M. EDT, Attending Classes on Campus: July 11 at 11 A.M. EDT, Housing Options: July 13 at 10 A.M. EDT, and Getting Online 101: The Basics: July 20 at 1 P.M. EDT")
        event_option = input("These are the options. Would you like to attend one' (yes/no): ").lower()
        if event_option == "yes":
            Engagement = +10
            Self_discipline = +10
            Stress_Level = +10
            Goal_Planning = +10
            print("Congratulations, you've gained 10 points across all three attributes!")
        else:
            Engagement = -5
            Self_discipline = -10
            Stress_Level = -5
            Goal_Planning = -10
            print("Oh no! Your stress level's and engagement have decreased by 5, but all your other attributes have decreased by 10")

    one_card = input("Week 2: Do you want submit your Sheridan One Card Photo? (yes/no): ").lower()
    if one_card == "yes":
        Engagement = +10
        Self_discipline = +10
        Stress_Level = +10
        Goal_Planning = +10
        print("Congratulations, you've gained 10 points across all three attributes!")
    else:
        Engagement = -5
        Self_discipline = -5
        Stress_Level = -5
        Goal_Planning = -5
        print("Oh no! You've lost 5 points across the board. However, you can not recover these points.")

    payments = input("Week 2: Would you like to learn about student fees, how to pay them, and financial aid options' (yes/no): ").lower()
    if payments == "no":
            Engagement = -10
            Self_discipline = -10
            Stress_Level = -10
            Goal_Planning = -10
            print("Oh no! You've lost 10 points across the board. You can NOT redo this action.")
    else:
        print("Congratulations! You are now aware that you must pay an entrance fee to attend school for the first couple of weeks with no issues!")
        dom_v_int = input("Are you a domestic or international student. If you're domestic, enter yes, if international, enter no: ").lower()
        if dom_v_int == "no":
            print("No worries, your score won't be affected by this!")
        else:
            print("Because you are a domestic student, you have the option to opt out of the dental plan, as well as apply for OSAP")
            print("You have gained 10 points across the board!")
            Engagement = +10
            Self_discipline = +10
            Stress_Level = +10
            Goal_Planning = +10

    peer_mentor = input("Week 2: Would you like to connect with a Peer mentor' (yes/no): ").lower()
    if peer_mentor == "yes":
         Engagement = +35
         Self_discipline = +35
         Stress_Level = +35
         Goal_Planning = +35 
         print("Awesome! You have now gained 35 points across the board.")
         print("Because of your action, you now know how to get involved at Sheridan, as well as have an extensive list of resource")
    else:
         Engagement = -35
         Self_discipline = -35
         Stress_Level = -35
         Goal_Planning = -35
         print("You have lost 35 points across the board...Better luck next time!")

two_week_pr()