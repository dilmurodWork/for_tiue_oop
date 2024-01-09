class Client:
    name: str
    surname: str

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.surname} {self.name}'


class BankCard:
    bank_name: str
    card_holder: Client
    card_number: str
    limit_date: str
    __balance: float = 0.0
    __pin: str

    def __init__(self, bank_name, name, surname, card_number, limit_date):
        self.bank_name = bank_name
        self.card_holder = Client(name, surname)
        self.card_number = card_number
        self.limit_date = limit_date
        self.__pin = '0000'

    def __str__(self):
        return f'{self.bank_name}\n{self.card_number}\n\t\t\t  {self.limit_date}\n{self.card_holder}\n'

    def check_pin(self, pin):
        return self.__pin == pin

    def set_pin(self, old_pin, new_pin):
        if old_pin is self.__pin:
            self.__pin = new_pin

    def get_balance(self, pin):
        if self.check_pin(pin):
            return f'Your current balance: {self.__balance}'
        else:
            return 'Incorrect pin'

    def income(self, money):
        if money > 0:
            self.__balance += money

    def outcome(self, pin, money):
        if self.check_pin(pin) and 0 < money <= self.__balance:
            self.__balance -= money


bc = BankCard('Ipoteka Bank', 'Dilmurod', 'Normurodov', '8600 1234 4321 4999', '10/26')

print('************************TERMINAL***************************')
ans = 1

while True:
    pin = input('Enter your pin code: ')
    if bc.check_pin(pin):
        break

while ans:
    ans = int(input('1-Card info\n2-Balance\n3-Income\n4-Outcome\n0-exit\n'))

    match ans:
        case 1:
            print(bc)
        case 2:
            print(bc.get_balance(pin))
        case 3:
            inc = float(input('Amount of money: '))
            bc.income(inc)
        case 4:
            ouc = float(input('Amount of money you want outcome: '))
            bc.outcome(pin, ouc)
        case 0:
            break
