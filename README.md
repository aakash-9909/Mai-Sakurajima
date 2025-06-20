# A date with Mai - Sakurajima
An interactive dating sim which has 3 girls but revolves around mai sakurajima. Why?? Ofc cause she is the best...
#### Video Demo:  <https://youtu.be/iSc1n1-84oE?si=TscD8SczIhBMgxK5>
#### Description:
This is my final project for **CS50 Python** .
With some **mini games , ASCII arts**, **image popups**, i also have implemented some **ai featrue** in *neuro sama* and tons of **dialogues** most of them are handmade and there are many gramaticall errors or spelling errors despite of what i said about using grammarly.

Isnt it the perfect timing as in july we are finally getting
>*** Rascal Does Not Dream of Santa Clause ***

After all those movies...(which i ofc  loved but finally yay!! )

#### Yapping:
I made this whole project alone but i got some ideas from freinds
for eg. the clean os idea was from ranjit

Delay / animation feature or time.sleep was implemented with the help of another discord freind and so on but i have mentioned this in comments so worry not

***The AI feature will wont work for you , because of privacy reasons i cant submit this with my api so you can get the chat gpt api and paste it in the <ins> api key </ins> place in **neuro_sama()*****
>Check the requirements.txt to download the necessary PIP
using PIP install <ins>name</ins>

## Features
### Routes
There are three main routes you can choose from:
> Godly_Mai_San (): Recommended

>alya()

>neuro_sama(): For ai feature

#### Mai san route:
>I wont spoil the game for you
Basically, this is the main routes with games like **vending machine, toy claw, some ascii arts like cars and image popups** ...

>I really hope you will enjoy this one

#### Alya (from Roshidere aka Alya hides her feelings in Russian):

>Yuki came to save the sleep deprived overworked author. Arigatto

#### Neuro (The famous vtuber neuro, channel the owned by this turtle guy aka vedal):
> Ai feature is here, i wanted to implement bunch of other features, but i dont have time, for now its postponed

## Characters details
#### Mai Sakurajima:
Mai Sakurajima is a character from my favorite anime 'Bunny Girl Senpai'.
She is a famous actress and model, currently taking a break from the spotlight to live a quiet life.
At 18 years old, she’s your upperclassman—elegant, composed, and incredibly intelligent.
She’s also an amazing cook and surprisingly caring once you get to know her.
She's basically perfect... I could talk about her all day.
I love you, 'My Mai Sakurajima'. ♥️

#### Alya (Basically the cool smart and tsundere girl ):
Alya (Alisa Mikhailovna Kujou) is from the anime 'Roshidere'—a quiet, elegant girl with a sharp tongue.
Though she may act cold or sarcastic at first, she’s known for her hidden warmth and honesty.
Fluent in both Japanese and Russian, she's confident, intelligent, and observant.
She values her independence and isn't afraid to call you out—but she's someone who notices even the small things you do.

#### Neuro Sama:
Neuro-sama is a virtual AI Vtuber known for her wild, witty, and unpredictable behavior.
She blends sarcasm, deadpan humor, and chaotic energy, often breaking expectations and the fourth wall.
Though her logic can be questionable, her charm lies in being the lovable glitch in the system.
Don't expect traditional romance—expect simulated madness, with a smile.

##  Explaining Functions ():
### starting():
Starts the game and gives the manual
eg. 1 to choose the route or 1. help to know about the character

### get_help(n):
Takes n parameter to print the character details of the specific string

eg. n = "1. help"

### get_response():
Prompts the user for response and calls get_help if needed

### main():
initiate starting ( ) and get_response ( ) and calls one of the main routes if prompted

### Godly_Mai_san():
Get called by main and start the main routes

### alya():
Get called by main and start the shortest route

### neuro_sama():
Get called by main and start the AI featured route

## Repeated Functions:

### y():
Prompt the user if they want to continue or not.
Rejects other input , here some may argue that i could just add sys.exit() to quit the programm and i agree but at this point i havent used any file I/O method to save the file so they will have to restart , if thats the case they can manually exist if they want knowing, this wont be saved.

### banner(n):
Take string arhument to output text in ascii art.

### car():
Print ascii art car

### car_scene():
Triggers the car scene ( one of the main events)

### restraunt_event():
Similar

# Some main and big functions
## v  = Vending()
> Calls the vending machine class

### v.vroom():
Activates the vending maching

Some may argue that a function would be easy instead of a class and i agree but i made it hard too much hard

## toy_claw_machine()
> Calls the toy claw machine function.
>
>
> Not the hardest but most fun and best working function hardest was making the vending machine....

## restraunt_event():
> Triggers the **restaurant event**

## show_image(n):
> Paste the image url and it will make it popup


## Thanks for reading see you next time , I hope atleast...

