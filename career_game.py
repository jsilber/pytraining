#Learn Python the Hard Way Python 3: Lesson 36 Designing and Debugging p126


from sys import exit

def weather():
    #options if you choose meterology as career
    print ("You are swept away by a tornado during the first field trip. You die but still have to pay back your student loans in purgatory. Game over.")
    dead()

def coding():
    #options if you choose programing as a career
    print ("You realize programming is REALLY hard. Do you change majors, quit school or stick with it?")
    coding_choice = input(">")

    if "change majors" in coding_choice:
        print ("Would you like to be a Meterologist or a GIS Specialist?")
        change_choice = input(">")

        if "Meterologist" in change_choice:
            weather()
        elif "GIS" in change_choice:
            gis()
        else:
            print ("Learn to type dude! Type either Meterologist, GIS, or quit.")
            coding()
    elif "stick with it" in coding_choice:
        print ("You graduate with honors, but the job market is saturated. You lose. Game over.")
        dead()

    elif "quit" in coding_choice:
        print ("Of course programming is hard. Oh well. Game over.")
        dead()
    else:
        print ("Learn to type dude!")
        coding()

def gis():
    #options if you choose GIS as a career
    print ("You choose GIS as a career. You are super smart and there are plenty of jobs upon graduation. You win!")
    exit(0)


def dead():
    exit(0)


def start():
    #introduction to game
    print ("It's your first day in college.")
    print ("You must declare a major, but since this is a small school there are only three options.")
    print ("Do you choose Meterology, Programming, or GIS? Or give up and quit.")
    user_choice = input(">")

    if "Meterology" in user_choice: #checks to see if the word meterology is anywhere in the user's input statement
        weather()
    elif "Programming" in user_choice:
        coding()
    elif "GIS" in user_choice:
        gis()
    elif "quit" in user_choice:
        print ("You didn't even try! Game over.")
        dead()
    else:
        print ("You gotta pick something man! Start over.")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        start()


start()
