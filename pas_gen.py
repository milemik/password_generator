import random
import string
import json
from datetime import datetime


class Password_gen:

    def __init__(self):
        # objects
        self.name = input("Name the password:\n")
        self.lower_letters = string.ascii_lowercase
        self.upper_letters = string.ascii_uppercase
        self.numbers = [x for x in range(0, 30)]
        self.strong_check = 0
        td = datetime.now()
        self.when_time = (
            f"{td.day} {td.month} {td.year}T{td.hour}-{td.minute}-{td.second}"
        )
        while True:
            try:
                self.strong = int(
                    input("How strong would you like your pass to be? (0-30)\n")
                )
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
            # print(add())
            self.password += add()
            self.strong_check += 1
            if self.strong_check == self.strong:
                break
        return self.password

    # random lower letter
    def random_ll(self):
        return random.choice(self.lower_letters)

    # random UPPER LETTER
    def random_ul(self):
        return random.choice(self.upper_letters)

    # radnom number
    def random_num(self):
        """Will return random number as string"""
        return str(random.choice(self.numbers))

    # Write to json file
    def write_to_file(self):
        """Will write generate JSON file with password info"""
        data = {"name": self.name, "time": self.when_time, "password": self.password}
        with open(f"PASSWORD {self.when_time}.json", "w") as f:
            f.write(json.dumps(data, indent=2))

    def __str__(self):
        return f"Your pass is: {self.password}"


def main():
    """Main function to execute generating password"""
    s = Password_gen()
    s.random()
    s.write_to_file()
    print(s)


if __name__ == "__main__":
    main()
