""" implements the interactivity with the user.
"""

# Three Attrivutes
Engagement = 0
Self_discipline = 0
Stress_Level = 0
Goal_Planning = 0
'''
The four attributes—engagement, self-discipline/responsibility, stress levels, 
and goal planning—are integral to the academic success of the charachter in the game (Heba, and Joseph).
Engagement, reflected in Heba's proactive approach and Joseph's academic focus, 
fosters active participation and deeper understanding. Both students exhibit 
self-discipline and responsibility, with Heba's dedication to accessible resources
and Joseph's self-reliance contributing to their success. Goal planning plays a vital role, 
with Heba's proactive resource use and Joseph's determination influencing
their journey. Stress management varies, with Heba's Accessible Learning registration 
potentially mitigating stress, and Joseph potentially experiencing stress as an international 
student. The point system indicates the importance of each attribute, with 35 points representing 
high importance, and 5 being holding the least value.
'''
#Module 1

def two_week_pr():
    oritentation_kickoff = input("2 weeks prior: Do you want to attend Orrientation Kickoff. It is a virtual event. (yes/no): ").lower()
    if oritentation_kickoff == "yes":
        Engagement = +10
        Self_discipline = +10
        Stress_Level = +35
        Goal_Planning = +35
        print("Congratulations, you've gained 10 points across all three attributes, and a special 35 points for stress levels!")
        print("You have met with upper year students, leaders, and alumni and learned about their experience and what it means to be a Sheridan Bruin. You additionally learned about how you can ‘Dare 2 Care’ about yourself, your classmates and the Sheridan community.")
        print("By making the choice to attend oritentation kickoff, you were additionally able to download your first year guide and plan accordingly!")
    else:
        Engagement = -5
        Self_discipline = -5
        Stress_Level = -35
        Goal_Planning = -35
        print("Oh no! You've lost 5 points across the board and a significant 35 points for your stress level and goal planning. You will have the oppuruntity to make a different choice in the following week regarding an orientation event!")
        print("Your stress levels decrrased and you lost a major oppurunity to meet peers and learn what to expect from Sheridan. This is addtionally a bad reflection on your goal planning skills.")
    '''
    Within the 2_weeks_pr module, the 'oritentation_kickoff' parameter prompts users to 
    decide whether they wish to attend the orientation kickoff, which is a virtual event 
    welcoming them alongside upper year students, leaders, and alumni who share their 
    experiences and the essence of being a Sheridan Bruin. Participation in this event presents an 
    opportunity to establish connections with upperclassmen, alumni, and even professors, fostering valuable 
    networking prospects. Agreeing to attend earns users 10 points each in Engagement 
    and Self Discipline, signifying the gain of an enriching experience. Notably, opting
    out of this event does not have an irrevocable impact on these attributes, as there 
    are subsequent opportunities for networking. However, declining participation results 
    in a 5-point loss, as this unique experience cannot be revisited. Saying yes to the 
    orientation kickoff yields a substantial boost of 35 points in Stress Level and Goal
    Planning, enhancing stress management and providing clarity about expectations and 
    peer interactions at Sheridan. It is crucial to note that stress level losses at 
    this event cannot be reversed during upcoming orientation activities.
    '''
    alc = input("2 weeks prior: Are you in need of accomindations (yes/no): ").lower()
    '''
    Within the 2_weeks_pr module, the ALC (Accessible Learning Centre) plays a crucial role in
      ensuring equal opportunities for all students, regardless of their background, socioeconomic 
      status, or disabilities. Its mission is to provide every student with the chance to acquire 
      the knowledge, skills, and competencies necessary for academic success. If a student does not
        require support from the ALC, their attributes remain unaffected by this parameter. 
        However, for those in need of accommodations who delay contacting the ALC in the initial 
        weeks before classes, there is a substantial impact on stress levels and other in-game attributes. 
        Delaying contact with an ALC coordinator makes it increasingly challenging to access ALC services, 
        potentially leading to an unfavorable situation. Therefore, timely planning is crucial. 
        If accommodations are not needed, there is no impact on points. In contrast, for students requiring 
        accommodations who do not seek help, there is a severe loss of 35 points across all attributes, with 
        no opportunity for recovery. Conversely, seeking help results in a 35-point gain across all attributes, 
        except for engagement, where a neutral 10-point increase is awarded. This reflects the acknowledgment of 
        responsible decision-making, alleviates future stress related to ALC support, and strengthens planning skills.
    '''
    if alc == "no":
        print("No worries, your score won't be affected by this!")
    else:
        alc_choice = input("Would you like to sign up for accessible learning' (yes/no): ").lower()
        if alc_choice == "yes":
            Engagement = +10
            Self_discipline = +35
            Stress_Level = +35
            Goal_Planning = +35
            print("Congratulations, you've gained 35 points in the goal planning, stress level, and self discipline attributes! You have gained 10 points under engagement.")
            print("You're all set up and you no longer need to worry about signing up with ALC!")
        else:
            Engagement = -35
            Self_discipline = -35
            Stress_Level = -35
            Goal_Planning = -35
            print("Oh no! You've lost 10 points across the board. You will immensely be affected by this in the following weeks.")
    
    
    sheridan_central = input("2 weeks prior: Would you like to login to Sheridan Central (it's like the Google of Sheridan) with your Sheridan username and password? (yes/no): ").lower()
    if sheridan_central == "no":
            Engagement = -10
            Self_discipline = -10
            Stress_Level = -10
            Goal_Planning = -10
            print("Oh no! You've lost 10 points across the board. You will immensely be affected by this in the following weeks.")
    else:
        input("Would you like to update your contact information and set up multifactor authentication (MFA)' (yes/no): ").lower()
        if sheridan_central == "yes":
            Engagement = +35
            Self_discipline = +35
            Stress_Level = +35
            Goal_Planning = +35
            print("Congratulations, you've gained 10 points across all three attributes!")
        else:
            Engagement = +10
            Self_discipline = +10
            Stress_Level = +10
            Goal_Planning = +10
            print("Oh no! You've lost 10 points across the board. Unfortunately, you will not be able to redo this action in following weeks.")
    '''
    Within the 2_weeks_pr module, the parameter of logging into Sheridan Central holds considerable significance. By accessing this platform, 
    students familiarize themselves with its interface, enabling them to update essential personal information, access their timetables, 
    course details, financial information, and various resources offered by Sheridan. The act of logging in and actively seeking to update 
    personal information and activate MFA not only showcases self-discipline but also strengthens planning skills. Moreover, this early access
    affords students the advantage of familiarizing themselves with the platform and its resources two weeks prior to the start of classes, 
    saving valuable time. Failing to do so results in a notable but not overwhelming loss of 10 points across all attributes. Conversely, 
    actively engaging with Sheridan Central, including updating contact information and configuring MFA, yields a substantial reward of 
    35 points across all attributes, reflecting the initiative taken to excel in these essential areas.
    '''

    payments = input("2 weeks prior: Would you like to learn about student fees, how to pay them, and financial aid options' (yes/no): ").lower()
    if payments == "no":
            Engagement = -35
            Self_discipline = -35
            Stress_Level = -35
            Goal_Planning = -35
            print("Oh no! You've lost 35 points across the board. You can NOT redo this action...")
    else:
        Engagement = +35
        Self_discipline = +35
        Stress_Level = +35
        Goal_Planning = +35
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
    '''
    Within the 2_weeks_pr module, users are presented with an option to delve into understanding payments, a crucial aspect of their academic journey.
    This knowledge holds particular significance for domestic students, as it equips them with the tools to effectively navigate the financial intricacies
    of their education. Domestic students benefit from comprehending student fees, payment methods, and available financial aid options, such as OSAP 
    (Ontario Student Assistance Program), which can significantly alleviate financial burdens. Moreover, domestic students may have the option to opt 
    out of specific fees, like dental plans, based on their individual circumstances and preferences. Conversely, international students face similar 
    financial challenges but may encounter variations in accessing financial aid due to their residency status. Therefore, it is imperative for both 
    domestic and international students to actively seek information regarding fees, payment procedures, and financial aid to ensure a seamless and 
    financially manageable academic journey. Failing to recognize the importance of payments in the initial two weeks before the commencement of classes 
    could potentially lead to severe consequences, resulting in a substantial loss of 35 points across all attributes. This is because neglecting to 
    acquire concrete information about the significance of payments may lead to oversights in crucial financial responsibilities, including entrance 
    fees and tuition payment deadlines. On the other hand, users who conscientiously review payment deadlines and information can mitigate such risks,
    earning a reward of 35 points across all attributes. Furthermore, domestic students gain an additional 10 points, as they become aware of the 
    option to opt out of dental plans, offering potential cost savings.
    '''
'''
The "two_week_pr" module encompasses several choices and outcomes related to crucial aspects of
student preparation. It begins with an option to attend the orientation kickoff, where students 
can gain significant engagement, self-discipline, stress level, and goal planning points, reflecting
the importance of this event in their academic journey. The module also addresses the Accessible Learning Centre (ALC),
emphasizing the significance of timely contact for students in need of accommodations. Logging into Sheridan Central 
is another pivotal choice, with positive consequences for self-discipline, planning, and stress management. Learning 
about student fees, payment methods, and financial aid options is highlighted, particularly for domestic students,
who can potentially opt out of certain fees like dental plans and apply for OSAP. The point system underscores the 
importance of these decisions, with 35 points representing high significance. These choices significantly impact the
attributes, emphasizing their role in shaping the students' academic path.
'''
# two_week_pr() 

def one_week_pr():
    laptop_reqs = input("1 week prior: Would you like to check your program laptop requirements' (yes/no): ").lower()
    if laptop_reqs == "yes":
         Engagement = +35
         Self_discipline = +35
         Stress_Level = +35
         Goal_Planning = +35 
         print("Awesome! You have now gained 35 points across the board.")
         print("Because of your action, you now know what laptop you need for school and are able to exchange or buy a new one before classes are in session!")
    else:
        Engagement = -35
        Self_discipline = -35
        Stress_Level = -35
        Goal_Planning = -35
        print("You have lost 35 points across the board...Better luck next time!")

    oritentation_choice = input("1 week prior: Do you want to attend orientation? (yes/no): ").lower()
    if oritentation_choice == "yes":
        Engagement = +10
        Self_discipline = +10
        Goal_Planning = +35
        print("Congratulations, you've gained 10 points across all three attributes!")
        event_type = int("Would you like to learn about the three events hosted at orientation (yes/no): ").lower()
        if event_type == "yes":
             print("Program sessions. Meet your professors and classmates. Learn about how to succeed in your program.")
             print("Services. Check out the Marketplace to meet our services, student organizations, and supports. They'll be happy to answer any of your questions and let you know of any other events going on! (You might even get some Sheridan swag!)")
             print("Social activities. There are two events, Art Hive, and Light Lunch. In Art Hive, you unleash your creativity, relax, and connect with other students. During Light lunch, you get a chance to enjoy a light complimentary lunch. It's the perfect opportunity to hang out with other new students.")
             event_choice1 = int("Would you like to go to all three events (yes/no): ").lower()
             if event_choice1 == "no":
                Engagement = +35
                Self_discipline = +35
                Stress_Level = +35
                Goal_Planning = +35
                print("Congratulations, you've gained 35 points across the board.")
             else:
                Engagement = +10
                Self_discipline = +10
                Stress_Level = +10
                Goal_Planning = +10
                print("You are doing decently and will make it through fine through the semester. You have went to the events you believe will benefit you and that will not affect you.")
                print("No worries! You still have decided to go to at least one event. That will suffice.")
    else:
        Engagement = -35
        Self_discipline = -35
        Stress_Level = -35
        Goal_Planning = -35
        print("Oh no! You've lost 35 points across the board. You can not make up the lost points. All orientation events have ended.")
    '''
    Within the context of the 1_week_pr module, a parameter is presented that prompts the user to
    decide whether to attend orientation events and provides information on the various types of events
    available. Users have the option to select attending all, some, or none of these events. Opting for
    attendance at all three events maximizes attributes, facilitating a deeper understanding of classes,
    professors, peers, and the institution. Attendance at one or two events yields decent results, impacting
    attributes positively without significant detriment. However, missing all events results in the permanent
    loss of points, as orientation events conclude. Simply confirming attendance at any event earns the user
    10 engagement and self-discipline points for their initiative, and 35 goal planning points for strategic
    event selection. Attending all three events grants a substantial 35-point boost across all attributes, 
    while attendance at only one or two events provides a 10-point increment across the board. 
    Conversely, failing to attend any event constitutes a significant error, leading to a 
    substantial loss of 35 points across all attributes.
   ''' 
    one_card = input("1 week prior: Do you want submit your Sheridan One Card Photo? (yes/no): ").lower()
    if one_card == "yes":
        Engagement = +10
        Self_discipline = +10
        Stress_Level = +10
        Goal_Planning = +10
        print("Congratulations, you've gained 10 points across all three attributes!")
    else:
        Engagement = -5
        Self_discipline = -5
        Stress_Level = -35
        Goal_Planning = -5
        print("Oh no! You've lost 5 points across the board, except for stress levels. You have lost 35 in that category. You can not recover these points.")

    find_classes = int("1 week prior: Would you like to walk around campus and find your classes (yes/no): ").lower()
    if find_classes == "yes":
        Engagement = +10
        Self_discipline = +10
        Stress_Level = +35
        Goal_Planning = +10
        print("Congratulations, you've gained 10 points across all three attributes, and a special 35 points for stress levels!")
    else:
        Engagement = -5
        Self_discipline = -5
        Stress_Level = -35
        Goal_Planning = -5
        print("Oh no! You've lost 5 points across the board but lost 35 for stress levels")
# one_week_pr()

def week_of():
    one_card_pickup = int("Week of: Would you like to pick up your card (yes/no): ").lower()
    if one_card_pickup == "no":
        Engagement = +10
        Self_discipline = +10
        Stress_Level = +35
        Goal_Planning = +10
        print("Congratulations, you've gained 10 points across all three attributes, and a special 35 points for stress levels! (yes/no): ").lower()
    else:
        Engagement = -5
        Self_discipline = -5
        Stress_Level = -35
        Goal_Planning = -5
        print("Oh no! You've lost 5 points across the board but lost 35 for stress levels")

# week_of()

def intro():
    welcome = 


    role = input("It’s time to choose which character you would like to play! It's important to take into account their unique characteristics and potential contributions. There are two students in which you may choose from. Would you like more information? (yes/no): ").lower()
    if role == "yes":
        print ("The choices are:")
        print ("Student 1, Heba Ali, at 19 years old, is a domestic student residing close to the institution and has actively sought out Accessible Learning services, reflecting her determination and commitment to academic success. However, her preparedness in the critical two weeks before classes commence may play a pivotal role in her achievements.")
        print("Student 2, Joseph Bane, aged 20, is an international student from Brampton, demonstrating strong academic focus and resourcefulness despite the challenges of distance. Similarly, his actions in the two weeks leading up to classes could significantly impact his success. The question then arises: which student's journey and preparation align better with the themes and objectives of your game?")
        role_choice = input("Enter yes to play the game as Heba, or enter no to play as Joesph' (yes/no): ").lower()
        if role_choice == "yes":
            print("Congrautulations, you are now play as Heba Ali.")
        else:
            print("Congrautulations, you are now play as Joesph Ali.")
