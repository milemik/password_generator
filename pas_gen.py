import random
import string
import json
import logging

from datetime import datetime

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


def mlog(msg: str) -> None:
    logger.info(msg=msg)


def time_to_str() -> str:
    td = datetime.now()
    return f"{td.day}-{td.month}-{td.year}T{td.hour}-{td.minute}-{td.second}"


def ask_imput_pass_length() -> int:
    while True:
        try:
            strong = int(input("How strong would you like your pass to be? (0-30)\n"))
            if 0 < strong < 31:
                mlog(msg="Input ok")
                return strong
            else:
                print("Please enter number betwen 0 and 10")
        except ValueError:
            mlog("Plase enter valid number")


def ask_input_pass_name() -> str:
    return input("Name the password:\n")


class Password_gen:
    LOVER_LETTERS = string.ascii_lowercase
    UPPER_LETTERS = string.ascii_uppercase
    NUMBERS = [x for x in range(0, 30)]

    def __init__(self, strength: int) -> None:
        # objects
        self.name: str = ask_input_pass_name()
        self.when_time: str = time_to_str()
        self.strong: int = strength

    # GET RANDOM DATA
    def random(self) -> str:
        password = ""
        strong_check: int = 0
        while True:
            add = random.choice([self.random_ll, self.random_ul, self.random_num])
            password += add()
            strong_check += 1
            if strong_check == self.strong:
                break
        mlog(msg=f"GENERATED PASS: {password}")
        return password

    # random lower letter
    def random_ll(self):
        return random.choice(self.LOVER_LETTERS)

    # random UPPER LETTER
    def random_ul(self):
        return random.choice(self.UPPER_LETTERS)

    # radnom number
    def random_num(self):
        return str(random.choice(self.NUMBERS))

    # Write to json file
    def write_to_file(self, password: str) -> None:
        data = {"name": self.name, "time": self.when_time, "password": password}
        with open(f"PASSWORD {self.when_time}.json", "w") as f:
            f.write(json.dumps(data, indent=2))

    def run(self):
        password: str = self.random()
        self.write_to_file(password=password)


def main():
    user_input: int = ask_imput_pass_length()
    Password_gen(strength=user_input).run()


if __name__ == "__main__":
    main()
