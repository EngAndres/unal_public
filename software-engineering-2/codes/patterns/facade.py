class CreditCard:
    def make_payment(self, amount: int):
        print(f'Payment by {amount}$ successful')

    def generate_report(self, ):
        print('Report generate.')



class SavingAccount:
    def get_cash(self, amount: int):
        print(f'Providing {amount}$ cash.')

    def reload(self, amount):
        print(f'Adding {amount}$.')


#============================
import sys
class Facade():
    def __init__(self):
        self.saving_acount = SavingAccount()
        self.credit_card = CreditCard()

    def interaction(self):
        menu: str = "\n\nBIENVENIDO AL BANCO UN\nEscoja  una de nuestras opciones.\n\
1. Get Cash\n2. Deposit money\n3.Make CCard Payment\n4. Generate CCard Report\n5. Exit\n"
        
        print(menu)
        input_ = int( input() )
        if input_ == 1:
            amount = input("How many money?")
            self.saving_acount.get_cash(amount)
        elif input_ == 2:
            amount = input("How many money?")
            self.saving_acount.reload(amount)
        elif input_ == 3: 
            amount = input("How many money?")
            self.credit_card.make_payment(amount)
        elif input_ == 4:
            self.credit_card.generate_report()
        elif input_ == 5:
            print("Thanks. Exiting...")
            sys.exit()
        else:
            print("Choose a valid option...")

#==== CLIENT

test = Facade()
while True:
    test.interaction()
