import random
import string


class Password_gen():

    def __init__(self):
        # objects
        self.lower_letters = string.ascii_lowercase
        self.upper_letters = string.ascii_uppercase
        self.numbers = [x for x in range(0, 30)]
        self.strong_check = 0
        while True:
            try:
                self.strong = int(input("How strong would you like your pass to be? (0-30)\n"))
                if 0 < self.strong < 31:
                    print("Input ok")
                    break
                else:
                    print("Please enter number betwen 0 and 10")
            except ValueError:
                print("Plase enter valid number")
        self.password = ""


    # GET RANDOM DATA
    def random(self):
        while True:
            add = random.choice([self.random_ll, self.random_ul, self.random_num])
            #print(add())
            self.password += add()
            self.strong_check += 1
            if self.strong_check == self.strong:
                break
        return self.password
    
    #random lower letter
    def random_ll(self):
        return random.choice(self.lower_letters)
        
    # random UPPER LETTER
    def random_ul(self):
        return random.choice(self.upper_letters)

    # radnom number
    def random_num(self):
        return str(random.choice(self.numbers))

    def __str__(self):
        return f"Your pass is: {self.password}"

def main():
    s = Password_gen()
    s.random()
    print(s)


if __name__ == "__main__":
    main()
