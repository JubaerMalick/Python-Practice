#Can you change the self-parameter inside a class to something else(say "jubaer"). Try changing self to "slf" of "jubaer" and see the effects.

from random import randint

class Train:

    def __init__(jubaer,trainNo):
        jubaer.trainNo = trainNo

    def book(jubaer, fro, to):
        print(f"Ticket is booked in train no: {jubaer.trainNo} from {fro} to {to}")
           
    def getStatus(jubaer):
        print(f"Ticket no: {jubaer.trainNo} is running on time")

    def getFare(jubaer, fro, to):
        print(f"Ticket fare in train no: {jubaer.trainNo} from {fro} to {to} is {randint(222, 5555)}")


t = Train(788)
t.book("Dhaka", "Chuadanga")
t.getStatus()
t.getFare("Dhaka", "Chuadanga")