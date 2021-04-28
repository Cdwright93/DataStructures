from random import randint

months = {"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
          "December"}
for key in months:
    if key == "March":
        print(key)

places = ["Georgia", "Florida", "Illinois", "Connecticut", ]
places.append("Hawaii")
places.append("Australia")
places.append("Bahamas")

for key in places:
    print(key)


class People:
    def __init__(self):
        self.name = ''
        self.first_name = ''
        self.last_name = ''
        self.winner = False
        self.relationship = ''


person_one = People()
person_one.name = "john doe"
person_one.first_name = "john"
person_one.last_name = "doe"
person_one.relationship = 'dad'
person_two = People()
person_two.name = "jane doe"
person_two.first_name = "jane"
person_two.last_name = "doe"
person_two.relationship = "mom"
person_three = People()
person_three.name = "Mark doe"
person_three.first_name = 'Mark'
person_three.last_name = "doe"
person_three.relationship = 'brother'
person_four = People()
person_four.name = "Steve doe"
person_four.first_name = 'Steve'
person_four.last_name = 'doe'
person_four.relationship = 'brother'
person_five = People()
person_five.name = "Richard doe"
person_five.first_name = "Richard"
person_five.last_name = "doe"
person_five.relationship = 'brother'

participants = [person_one, person_two, person_three, person_four, person_five]


def get_winner(participants):
    x = 0
    j = 1
    while x < j:
        i = randint(0, len(participants) - 1)
        participants[i].winner = True
        print("The winner of the sweepstakes is " + participants[i].name + '!')
        x = 1


get_winner(participants)

family = [person_one, person_two, person_three, person_four, person_five]