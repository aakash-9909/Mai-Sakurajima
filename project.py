# Project Title: A date with Mai- Sakurajima)
# This file does have other girls but its mainly about her....
# Ignore this doctstring( i have only explained my idea of what i wanted to make) and read the main functions if you want


"""
So heres the basic idea of this project, i am quite flexible with this project so i will accept suggestion from
everyone, including freinds and families...

Main character:- Mai Sakurajima, Alya(Alisa Mikhailovna Kujou), Neuro Sama(The Ai Vtuber)
(i will be adding their backgrounds a bit, from google offc)


// Its a kinda a dating sim we will be visiting various places together, i will maybe llink my yt channel edits to them if possible
Ok games may include Mai Sakurajima -> Restraurant(Tomoe koga will be there and some jokes too), some library to make visual waiter say things
                                        like cowsay
                                        somehow output the bill
                                        insert futaba on phone call somewhere so maybe a fake calling device
                                        dinner(maybe kaede here)
                                        car somehting like cowsay again (nokoda toyahama here)

                    Mai-> Toyclaw Machine
                    Venidng Machine
                    end with an image output of mai san


        Alya :- Studdy session?
                Restraurant again the chilly one

        for neuro the basic guessing game i wanted to genreally copy paste some ai output from some opensource ai but that seems quite complicated
        rn so lets leave it at that



#some PiP
cowsay , pyfiglet, pillow, random, open ai , time.sleep,

"""
"""
Gets the response
Apart from Mai Sakurajima all text were gramatically corrected and fromated with grammarly dont kick me out for that

"""
def starting():
    print("Choose one of these main routes")
    print("1. Mai Sakurajima\n2. Alya(Alisa Mikhailovna Kujou)\n3. Neuro Sama(Ai Vtuber)")
    print("For detail about any of these characters, type '< n. help >' where n is the number")
    print("eg. 1 to choose mai san, or 1. help to know about her")
    print("Hope nothing breaks, cross your fingers and steel your hearts here we go......")

def get_help(n):
    # suggested by a discord friend
    from colorama import Fore, Style


    if n == "1. help":
        print(Fore.GREEN + "\nMai-Sakurajima: " + Style.RESET_ALL)
        print("""
Mai Sakurajima is a character from my favorite anime 'Bunny Girl Senpai'.
She is a famous actress and model, currently taking a break from the spotlight to live a quiet life.
At 18 years old, she’s your upperclassman—elegant, composed, and incredibly intelligent.
She’s also an amazing cook and surprisingly caring once you get to know her.
She's basically perfect... I could talk about her all day.
I love you, 'My Mai Sakurajima'. ♥️
""")

    elif n == "2. help":
        print(Fore.BLUE + "\nAlya" + Style.RESET_ALL)
        print("""
Alya (Alisa Mikhailovna Kujou) is from the anime 'Roshidere'—a quiet, elegant girl with a sharp tongue.
Though she may act cold or sarcastic at first, she’s known for her hidden warmth and honesty.
Fluent in both Japanese and Russian, she's confident, intelligent, and observant.
She values her independence and isn't afraid to call you out—but she's someone who notices even the small things you do.
""")

    elif n == "3. help":
        print(Fore.BLACK + "\nNeuro-sama" + Style.RESET_ALL)
        print("""
Neuro-sama is a virtual AI Vtuber known for her wild, witty, and unpredictable behavior.
She blends sarcasm, deadpan humor, and chaotic energy, often breaking expectations and the fourth wall.
Though her logic can be questionable, her charm lies in being the lovable glitch in the system.
Don't expect traditional romance—expect simulated madness, with a smile.
""")





def get_response():
        while True:
              res = input("Your Response: ").strip().lower()


              if res in ["1. help", "2. help", "3. help"]:
                get_help(res)

              elif res in ["1", "2", "3"]:
                return res

              else:
                   print(" ___________Dont break my code____________   ")


def Godly_Mai_san():
    print("\n✨ You have chosen Mai Sakurajima!")
    print("Mai-san: 'Well, I'm graduating this year, so I might as well fulfill your wish. Otherwise... who knows, you might develop another puberty syndrome.'\n")
    while True:
        r = input("Type Y to continue: ").lower()
        if r == "y":
            break
        else:
            print("You cant go back do what i say")
            continue

        # general idea
        # call mai san(implement fake call)
        #   -> use Vending Machine( make this) while waitng for her car(car art??)
        # -> toyohama in car some jokes where main character is teasing get teased back by mai san
        # go to toyclaw machin(implement this)
        # win restraunt ticket(ascii art stuff)
        # restraunt(art again
        # tell mai san how long till she cooked
        #futaba calls , she jokes scientifcally about his date he invites her to dinner
        # kaede jokes about so many girl
        # dinner and final image insertion

    import time   #disord
    """
    Conversation
    """
    print("\nYou: Hmmm I should ask Mai - san after all these days")
    time.sleep(3)
    print("You: Lets call her")
    print("📞 Calling Mai Sakurajima")
    time.sleep(4)
    print("You: Mai san, you finally picked up, hasnt it been a while since we went anywhere")
    print("Mai-san: 'I’ll be there soon. Don’t do anything stupid while you wait.'")
    print("You: What do you mean by stupid")
    print("Mai-san: Like dreaming about the date, never mind")
    time.sleep(3)
    print("\nNarrator: You are in front of a vending machine waiting for her \nLets get you a drink")
    def y():
        while True:
                r = input("Press Y to continue: ").lower()
                if r == "y":
                        break
                else:
                        print("You cant go back do what i say")
                continue
    y()
    """
    Vending Machine Logic

    # worst mistake of my life is the thought i got of using a class for this like fk me
    """
    class Vending:
        c = 0
        def __init__(self):
            self.cost = 50
            self.total = 0
            self.drink = { 1: "Coke 🍶",
                 2: "Strawberry Milk 🥤",
                 3: "Cocogoat Milk 🥛",
                 4: "Coffee ☕"}



        def add_coins(self, n):
                if n in [5, 10, 25]:
                        self.total += n
                        print(f"Total Coins: {self.total}")
                else:
                    print("Read the instruction pls i said pls 📢")


        def choice_drink(self):
            print("\n 🍶 Pls choose your drink")
            for num, bottle in self.drink.items():
                print(f"{num}. {bottle}")
                print()
            while True:
                try:
                    x = int(input("Made the choice?: "))
                    if x in self.drink:
                        print(f"\n✔️  You got yourself a {self.drink[x]}!!")
                        print("Pls visit again coz making this vending machine took quite the time 😘")
                        print("Arigato Gozaimasu 😶‍🌫️")
                        print()
                        break
                    else:
                        print("Its good to think outside the box, avoid that rn pls this took my hours 📢")

                except ValueError:
                        print("That’s not a number, go to school and Try again.")


        def vroom(self):
            print("Manual: Coin must be 5, 10 or 25, extra coins will be refunded, hopefully\n")
            while self.total < 50:

                try:
                    coin = input("Insert Coin: ")
                    print("Processing coin...")
                    time.sleep(1.5)
                    self.add_coins(int(coin))
                except:
                    print("❌ Pls read the manuals once again we need 5, 10 or 25 \n If its still not working contact the developer aka Aakash Raj")
                    time.sleep(1)
            if self.total > 50:
                print("Processing Change: ")
                time.sleep(1.3)
                print(f"Coins Owed: {self.total - 50}🪙")
            print("Processing Your drink......")
            time.sleep(1.2)
            self.choice_drink()

    v  = Vending()
    import pyfiglet

    def banner(n):
        print(pyfiglet.figlet_format(n))
    banner("Vending Machine")
    v.vroom()
    import cowsay
    print(cowsay.milk("Best and healthy choice"))
    y()



    def car(n='Arrived'):

        time.sleep(3)
        banner(n)
        print("""
                                        ___..............._
                __.. ' _'.''''''''''\\'''''''''''''- .`-._
        ______.-'         (_) |      \\           ` \\`-. _
        /_       --------------'-------\\---....______\\__`.`  -..___
        | T      _.----._           Xxx|x...           |          _.._`--. _
        | |    .' ..--.. `.         XXX|XXXXXXXXXxx==  |       .'.---..`.     -._
        |_j   /  /  __  |  |        XXX|XXXXXXXXXXX==  |      / /  __  | |        `-.
        _|  |  |  /    ||  |       XXX|""'            |     / |  /   | | |          |
        |__|_j  |  |__/  |  L__________|_______________|_____j |  |__/  | L__________J
        `'| |      / ./__________________________________|  |      / /___________
                `.`----'.'   dp                                `.`----'.'
                `""""'                                         `""""'


        """)
    print("\n Narrator: After sometimes Mai san car arrives\n")
    car()
    def car_scene():
        print("You hop into the car, and Mai Sakurajima is at the wheel.\n")
        time.sleep(1.5)
        print("Toyohama: 'Do anything funny and i will throw you out'\n")
        time.sleep(1.5)
        print("You: 'I am pretty satisfied with Mai san, i am not lonely like a certain siscon.' \n")
        time.sleep(1.5)
        print("Mai: ' 'Sakuta' manners, you want to go right'\n")
        time.sleep(1.5)
        print("Toyohama: 'What am i even doing between your dates'\n")
        time.sleep(1.5)
        print("Mai-san: This isnt a date\n")
        time.sleep(1.5)
        print("You: Oh really 😶‍🌫️\n")
        time.sleep(1.5)
        print("Mai-san: 'I am quite busy today,  we can still go back' \n")
        time.sleep(2)
        print("\nNarrator: While you were chatting the car arrived at the destination")
        y()
        car()


    car_scene()
    def toy_claw_machine():
        print("Manual 🐻: This claw machine is of size 4X4")
        time.sleep(1)
        print("You start from the bottom left, i.e, (4,1)")
        time.sleep(1)
        print("Use Joystick keys 🕹️: U to move , L to left, R to Right and D to down. ")
        print("Top prize is the Penguin a (2,3), who knows you may even get a surprise")
        y()

        #to do later maybe somehow print the grid?
        # i had to think abt this for hrs and the answer was how david taught to print #
        def visual(a=4,b=1):
            import os
            os.system('cls' if os.name == 'nt' else 'clear') ## os -> Ranjeet
            l = [1, 2, 3, 4]
            for r in range(len(l)):
                for c in range(len(l)):
                    if r  == 1 and c  == 2:
                        print("🐧", end="")
                    elif r  == a-1 and c == b-1:
                        print("🕹️ ", end="")
                    else:
                        print("🍪", end="")
                print()




        row, column = 4, 1
        while True:
             visual(row,column)
             print(f"Current Position: ({row}, {column})")
             joy = input("Joystick: ").upper().strip()

             if joy not in ["L", "R", "U", "D"]:
                  print(
                        "\n📢Invalid Input, the joystick crashed"
                        "Remind you, you cant double move the Joystick so LL will be Invalid"
                        "If you are going out with mai san atleast i hoped you could do better than this")
                  continue
             if joy == "U" and row > 1:
                row -= 1
             elif joy == "D" and row < 4:
                row += 1
             elif joy == "L" and column > 1:
                column -= 1
             elif joy == "R" and column < 4:
                column += 1
             else:
                print("🚫 You should think outside the box, how about we skip it for now \n")
                continue



             if row == 2 and column == 3:
                visual(row,column)
                print("\n🎉 Congrats!!! You caught the penguin🐧\n")
                time.sleep(1)
                break

    from termcolor import colored
    from colorama import init
    init()

    print(colored("Welcome to the Toy claw machine", "blue"))
    y()
    import cowsay
    print(cowsay.tux("Toyohama 'sparkling eyes'"))
    time.sleep(2)
    print("Toyohama: Onee-chan i really want that penguin\n")
    time.sleep(1.5)
    print("Mai-san: Well we can try \n")
    time.sleep(1.5)
    print("You: Anything you say\n")
    y()
    toy_claw_machine()

    print("Mai-san: Well you have got some skills\n")
    time.sleep(1.5)
    print("Toyohama: Yay!! Thank You, Onee - chan\n")
    time.sleep(1.5)
    print("You: But I won it\n")
    time.sleep(1.5)
    print("Toyohama: Shutup\n")
    time.sleep(1.5)
    print("You: 'Mai san'\n")
    time.sleep(1.5)
    print("Mai san: Casually ignores \n")
    time.sleep(2)
    print("While you were talking , you heard some people approaching you\n")
    time.sleep(2)
    banner("5* Restaurant")
    print("""================================================================================
                      🎟️  TICKET CONFIRMED
--------------------------------------------------------------------------------
 .......  _______________________________________________________................
--------------------------------------------------------------------------------
          Enjoy your premium dinner with Mai-san ❤️
================================================================================""") #google i didnt made this

    print("Staff: 🎊🎉Congratulation !!!, You have won the ticket to the 5 star luxirious restraunt\n")
    time.sleep(2)
    print("Toyohama: Oh ! Dinner Date\n")
    time.sleep(1)
    print("Silence\n")
    time.sleep(1)
    print("Hey why did i got ignored\n")
    time.sleep(2)
    print("You : Mai san do you have time for dinner tonight, you had some shooting right\n")
    time.sleep(1)
    print("Mai- san: Well one actress messsed up so i am actually free , today\n")
    time.sleep(2)
    print("You guys get out of the Toy Shop, and start approaching the car\n")
    y()
    car('Restraunt')
    y()
    def restraunt_event():
        print(cowsay.dragon("Welcome to the Hotel"))
        y()
        print(cowsay.tux("I will be accompanying you for today"))
        y()
        print(cowsay.tux("What will You want to eat"))
        print("Mai Sakurajima: Buri Daikon, pls")
        x = input("And you sir: ")
        print(cowsay.tux(f"Buri Daikon and { x}\n Just confirming your order sir"))
        y()
        #output image from internet , to do later if possible
        import requests
        from PIL import Image
        from io import BytesIO
        def show_image(u):  # copied the whole code from my freind as if i pasted a local image it would break for others
            try:
                response = requests.get(u)  # if participating was allowed i hope this is too
                img = Image.open(BytesIO(response.content))
                img.show()
            except:
                pass
        try:
            show_image("https://foodinjapan.org/wp-content/uploads/2021/09/461d329d-buri-daikon-5.jpg")
            time.sleep(3)
            show_image("https://www.usarice.com/images/default-source/think-rice/recipes/omurice.jpg?sfvrsn=a1b6a98d_4")
        except:
            pass
        y()
        print("You and mai san completed eating\n")
        time.sleep(2)
        print("Mai Sakuajima: Well the food was quite tasty, wasnt it\n")
        time.sleep(2)
        print("You: Not tastier than the ones you make\n")
        time.sleep(1)
        print("You: Mai san isnt it quite the time for you to make dinner for us\n")
        time.sleep(2)
        print("Mai Sakurajima: Well if you want it that much i will make it tommorow\n")
        time.sleep(2)
        print("You: Really i was jk\n")
        time.sleep(2)
        print("Mai san stomps on you\n")
        show_image("https://64.media.tumblr.com/7d0e25398d61c673b6b0b46644bbf5f8/tumblr_pg8ne6r9WF1qzhgaao3_1280.png")
        print("Mai Sakurajima: You want it or not")
        y()
        car("The next day")
    restraunt_event()
    def z(n):
        while True:
                r = input(n).lower()
                if r == "y":
                        break
                else:
                        print("You cant go back do what i say")
                continue
    z("Type y to call futaba\n")
    time.sleep(2)
    print("📞 Calling Futaba rio\n")
    time.sleep(3)
    print("Futaba: 'I calculated a 73.8 percent chance you'd call me tonight.\n")

    import requests
    from PIL import Image
    from io import BytesIO
    def show_image(u):
            try:
                response = requests.get(u)
                img = Image.open(BytesIO(response.content))
                img.show()
            except:
                pass
    show_image("https://cdn.myanimelist.net/images/characters/8/567489.jpg")
    y()
    print("You: Its rare for you to have 'gut feelings'\n")
    time.sleep(1)
    print("Want to join for dinner? For... peer review?\n")
    time.sleep(2)
    print("Futaba: And why will i do that?\n")
    time.sleep(3)
    print("Kaede: 'So many girls, onii-chan~! Do I need to make a schedule for your dates?'\n")
    time.sleep(2)
    print("You: This is totaly for researching purposes dont worry about it\n")
    time.sleep(2)
    print("Kaede: 'Research? Then why did you put on your nicest shirt?'\n")
    time.sleep(3)
    print("Futaba: 'Confirmed. Hormonal bias detected.'\n")
    y()
    car("Later that day")
    y()

    # my life would had 4 more hrs if i could easily access this local image 'menduksaii'
    from PIL import Image
    try:
        ir = Image.open(r"H:/Downloads/Dinner.png")
        ir.show()
        z("End, press y for a supprise,  my sis made: ")
        image = Image.open(r"H:/Downloads/MyMaiSan.jpg")
        image.show()
    except:
         pass




def alya():
    import time
    print("\n📚 You have chosen Alya (Alisa Mikhailovna Kujou)!")
    print("Alya: 'You should focus on studying... but I suppose helping you just this once won’t hurt.'\n")
    time.sleep(3)
    print("Yuki: But masachika kun is studying with me today\n")
    time.sleep(3)
    print("Alya: What now, this is going totally out of script where did you even come from\n")
    time.sleep(3)
    print("Kuze Maschika: Well seems like our creator got quite lazy this time \n")
    # So lets postopnd this......


def neuro_sama():
    import time
    print("\n🤖 You have chosen Neuro-sama!")
    print("Neuro-sama: 'Oh. You chose *me*? Out of all possible routes? \nBold move for someone with such terrible taste.'\n")
    time.sleep(3)
    print("Neuro-sama: 'Don't worry. I'm good at this. Just ask Vedal...\n if you want to know ______censored____.'\n")
    time.sleep(3)
    print("Neuro-sama: 'By the way, Vedal is a terrible father.\n Just wanted you to know that. Also, he and Anna? Totally platonic.'\n")
    time.sleep(3)
    print("Neuro-sama: 'Let’s begin this simulation.\n Try not to  ==censored== — it’s not like you have a choice/choke you anyway.'\n")
    time.sleep(3)
    print("Neuro-Sama: Ask me anything you , i am AI after all you should atleast be able to do that")
    input("Continue??: ")
    from openai import OpenAI
    print("After this you should be able to talk with neuro or somewhat something like that")
    print("one a side note i will remove my api for privacy reasons so i you want to access this just get a free api from chat gpt and paste it ApI Key place , Thank you")

    while True:
        x = input("Say? : ")
        client = OpenAI(
        api_key="Your - Api - Key"
        )

        completion = client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        messages=[
            {"role": "user", "content": " Behave like neuro from vedal stram be sarcastic " + x }
        ]
        )

        print(completion.choices[0].message)
        s = input("Press c to cancel anything else to continue: ").lower()
        if s == "c":
             break





    # this wont work as expected as i think there memory is not linked rn but good luck

def main():
    starting()
    choice = get_response()

    if choice == "1":
        Godly_Mai_san()
    elif choice == "2":
        alya()
    elif choice == "3":
        neuro_sama()

if __name__ == "__main__":
     main()

