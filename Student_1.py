"""
implements the data and logic associated with the first role
"""
from App import two_week_pr
from App import one_week_pr
from App import week_of
from App import Engagement
from App import Self_discipline
from App import Stress_Level
from App import Goal_Planning
from Game import intro
from Game import game_rules

#About student 1, implementation through the game.py file.
print ("Student 1, Heba Ali, at 19 years old, is a domestic student residing close to the institution and has actively sought out Accessible Learning services, reflecting her determination and commitment to academic success. However, her preparedness in the critical two weeks before classes commence may play a pivotal role in her achievements.")
print(two_week_pr())
#printing module 1
print(one_week_pr())
#printing module 2

print(week_of())
#printing module 3

print(game_rules())