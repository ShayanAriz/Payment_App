import random

question = ("Who is Prime minister of india", "Who is president of india", "Fullform of WHO")

#Account of the person
accema = input("Your email: ")
vc = input("Varification code: ")
if vc == '9815' or vc == '5467' or vc == '6666' or vc == '1111' or vc == '0001':
    accusername = input("Your username: ")

    #password
    passw = input("Your password(it is in the notepad file with nammed password): ")
    #the ballance
    ball = 0
    print("Your ballance is: 0")

    #the play
    while True:
        sugg = input("If you want to earn type play to check ballance type ball to send type send and to recive type rec type buy to buy: ")
        if sugg == 'play' or sugg == 'Play':
            qwe = random.choice(question)
            print(qwe)
            ans = input("Your answer ")
            if qwe == 'Who is Prime minister of india':
                if ans == 'Modi' or ans == 'Narendra Modi':
                    ball = ball + 10
                    print(ball)
                else:
                    ball = ball - 10
            if qwe == 'Who is president of india':
                if ans == 'Ram Nath Kovind':
                    ball = ball + 50
                    print(ball)
                else:
                    ball = ball - 10
            if qwe == 'Fullform of WHO':
                if ans == 'World Health Organisation':
                    ball = ball + 10000
                    print(ball)
                else:
                    ball = ball - 10
        if sugg == 'ball':
            print(ball)
        if sugg == 'send':
            txt = input("To whome? ")
            if ball > 10:
                ball = ball - 10
                print(txt + ": Thanks!!!")
                print(ball)
            elif ball <= 10:
                print("Can't Send")
        if sugg == 'rec':
            ball = ball + 5
            print(ball)
        if sugg == 'buy':
            if ball > 100:
                buyy = input("What you want to buy? a laptop an ipad a phone or a clock ")
                if buyy == 'laptop':
                    print('$25')
                    ball = ball - 25000
                if buyy == 'ipad':
                    print('$25')
                    ball = bal - 18000
                if buyy == 'phone':
                    print('$25')
                    ball = ball - 9000
                if buyy == 'clock':
                    print('$25')
                    ball = ball - 6000
            elif ball <= 100:
                print("Can't buy")
