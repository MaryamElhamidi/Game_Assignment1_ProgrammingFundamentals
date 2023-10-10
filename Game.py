"""
Implementation of the game data and logic.
"""
from App import two_week_pr
from App import one_week_pr
from App import week_of
from App import Engagement
from App import Self_discipline
from App import Stress_Level
from App import Goal_Planning


def intro():
    print("Welcome to 'Academic Weapon' – a text-based game that guides you through the journey of becoming an academic weapon!")
    print("In this simulation, you'll follow the stories of two characters as they navigate the challenges of the academic world.") 
    print("An academic weapon, as defined by Urban Dictionary, is someone who possesses scholarly traits, and that's precisely what we aim to help you become.")
    print("The first weeks of college are crucial, and many students often overlook the importance of available resources, leading to increased stress levels and academic setbacks.")
    print("Academic Weapon will immerse you in real-world scenarios, providing examples of both the right and wrong choices to make during this crucial period.") 
    print("Throughout the game, you'll learn the significance of four essential attributes: engagement, self-discipline/responsibility, goal planning, and stress management.")
    print("These elements are the keys to academic success, and by enhancing these skills, you'll not only excel in your studies but also experience personal growth.")
    print("So, get ready to embark on this academic adventure, make choices, and see how your decisions impact your character's journey. Are you ready to become an academic weapon? Let's begin!")
    welcome = input("Would you like to start the game' (yes/no): ").lower()
    if welcome == "yes":
        print("Awesome. You have two choices between two charachters")
        role = input("It’s time to choose which character you would like to play! It's important to take into account their unique characteristics and potential contributions. There are two students in which you may choose from. Would you like more information? (yes/no): ").lower()
        if role == "yes":
            print ("The choices are:")
            print ("Student 1, Heba Ali, at 19 years old, is a domestic student residing close to the institution and has actively sought out Accessible Learning services, reflecting her determination and commitment to academic success. However, her preparedness in the critical two weeks before classes commence may play a pivotal role in her achievements.")
            print("Student 2, Joseph Bane, aged 20, is an international student from Brampton, demonstrating strong academic focus and resourcefulness despite the challenges of distance. Similarly, his actions in the two weeks leading up to classes could significantly impact his success. The question then arises: which student's journey and preparation align better with the themes and objectives of your game?")
            role_choice = input("Enter yes to play the game as Heba, or enter no to play as Joesph' (yes/no): ").lower()
        if role_choice == "yes":
            print("Congrautulations, you are now play as Heba Ali.")
            return
        else:
            print("Congrautulations, you are now play as Joesph Ali.")
            return
    else:
        print("That's okay! Hope to see you soon!")

'''
This module enters the welcome message and gives the user information about the respected characters given. They get to choose which character they would like to play as as well.
'''
def game_rules():
    total_points = Engagement + Self_discipline + Stress_Level + Goal_Planning  
    if total_points <= -100:
        print(f"Total Points: {total_points}. Critical Loss.Every decision you made greatly impacted all four attributes.")
        print("You need to review the decisions in which you have made during the game, review where you lost cirtical attribute points (10-35). Better luck next time!")
    elif -100 <= total_points <= -50:
        print(f"Total Points: {total_points}. Loss. You made bad decisions and good decisions, and it has impacted your attributes. The majority of your decisions were bad.")
        print("You need to review the decisions in which you have made during the game, review where you lost cirtical attribute points (10-35). Better luck next time!")
    elif -50 <= total_points <= 0:
        print(f"Total Points: {total_points}. Win. You made good  decisions and bad decisions, but overall your attributes are not negatively affected.")
        print("You need to review the decisions in which you have made during the game, review where you lost cirtical attribute points (10-35). Better luck next time!")
    else:
        total_points <= 100
        print(f"Total Points: {total_points}. Critical Win! You made every possible right decision! Congrautlations!")
'''
This module discusses the win or loss criteria for the game Academic Weapon.
'''

print(intro())
#printing the welcome message and letting users choose weather to begin or not, as well as giving them insight on the characters and who they want to play as.

print(two_week_pr())
#printing module 1
print(one_week_pr())
#printing module 2

print(week_of())
#printing module 3
print(game_rules())