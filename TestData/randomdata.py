import random

def random_number():
    #value = random.uniform(1,25) # floating numbers
    #print(value)
    value_int = random.randint(1,100)
    print(value_int)
    return value_int
random_number()

def random_choice():
   emails=["abc@gmail.com","doe@gmail.com","chary@outlook.com","xyx@gmail.com"]
   value = random.choice(emails)
   print(value)
   return value

random_choice() 

def random_card():
    deck = list(range(1,53))
    random.shuffle(deck)
    hand=random.sample(deck,k=5) # we want 5 random unique cards
    print(hand)

random_card()

def random_Fname():
    fnames=["Caleb","Jarvis","Mack","Vito","Judy","Claud","Glen","Kimberly","Karla","Bret","Carmen","Carly","Leola","Elroy","Rickey"]
    Fname=random.choice(fnames)
    print(Fname)
    return Fname
random_Fname()

def random_Lname():
    lnames=["Parker","Mack","Clarke","Collier","Hartman","Schafner","Beasley","Woods","Patterson","Cherry","Connor","Holland","Walters","Kaiser"]
    Lname=random.choice(lnames)
    print(Lname)
    return Lname
random_Lname()

def random_email():
    fname=random_Fname()
    lname=random_Lname()
    num=random_number()
    email=fname+lname+str(num)+'@gmail.com'
    print(email)
random_email()