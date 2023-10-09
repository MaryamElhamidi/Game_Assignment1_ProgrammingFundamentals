""" implements the interactivity with the user.
"""

# Three Attrivutes
Engagement = 0
Self_discipline = 0
Stress_Level = 0
Goal_Planning = 0

#Module 1

def two_week_pr():
    print("2 WEEK BEFOOOREEE college:")
    print("☑️ Read Succeeding @ Sheridan: A guide for your first year.")
    print("☑️ Review the Sheridan Student Housing Guide")
    print("☑️ Register with Accessible Learning if you have a learning disability, medical condition, mental illness, or disability.")
    print("   Are you with accessible learning / need accommodations? Talk to your professors in the first week")
    print("☑️ Login to Sheridan Central (it's like the Google of Sheridan) with your Sheridan username and password.")
    print("☑️ Update your contact information.")
    print("☑️ Set up multifactor authentication (MFA) with the Microsoft Authenticator App")
    print("   Look at upcoming events, go to one of them?")
    print("   💻 Accessing Supports:  July 5 at 10:00 A.M. EDT")
    print("   💻 Attending Classes on Campus: July 11 at 11 A.M. EDT")
    print("   💻 Housing Options: July 13 at 10 A.M. EDT")
    print("   💻 Getting Online 101: The Basics: July 20 at 1 P.M. EDT")
    print("   These are the options. Choose one or pass?")
    
    # Week 2
    choice = input("Week 2: Do you want to attend orientation? (yes/no): ").lower()
    if choice == "yes":
        print("Attend orientation")
    
    print("Submit your Sheridan One Card photo.")
    print("☑️ Learn about your student fees, how to pay them, and financial aid options.")
    print("☑️ Apply for a credit transfer if you've taken courses at a college or university.")
    print("☑️ Download your first year guide.")
    print("☑️ Register with Accessible Learning if you have a learning disability, medical condition, mental illness, or disability.")
    print("Connect With Us")
    print("Meet with a Peer Mentor.👋")
    print("See how you can get involved.🏆")
    print("Have a question? Ask us! 🤔")
    print("Pay entrance fee - are you international or domestic. Paying with OSAP or not.")

# Call the function to execute the checklist
two_week_pr()
