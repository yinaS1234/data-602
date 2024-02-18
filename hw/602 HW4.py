# %%
class BankAccount:
    def __init__(self,bankname, firstname, lastname, balance=0 ):
        self.bankname=bankname
        self.firstname=firstname
        self.lastname=lastname
        self.balance=balance
    def deposit(self, amount):
        self.balance+=amount
        print(f'Deposited: {amount}. New balance: {self.balance}')

    def withdrawal(self, amount):
        if amount<=self.balance:
            self.balance -=amount
            print(f'Withdrew {amount}. New balance: {self.balance}')
        else:
            print('Insufficient balance')

    def __str__(self):
        return f'Bank: {self.bankname}\n Owner: {self.firstname} {self.lastname}\n Balance: {self.balance}'

# Testing
    
account=BankAccount('Bank of America','John', 'Doe')
account.deposit(105)
account.withdrawal(106)
account.withdrawal(102)
print(account)


#%%
class Box():
    def __init__(self, length, width):
        self.length=length
        self.width=width

    def render(self):
        for i in range(self.width):
            print('*' * self.length)

    def invert(self):
        self.length, self.width = self.width, self.length

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.length + self.width)
    
    def double(self):
        self.width *=2
        self.length *=2
    def __eq__(self, other):
        return self.length==other.length and self.width==other.width
    
    def print_dim(self):
        print(f'Length: {self.length}. Width: {self.width}')

    def get_dim(self):
        return (self.length, self.width)
    
    def combine(self, other):
        self.length += other.length
        self.width  += other.width

    def get_hypot(self):
        return (self.length**2 + self.width**2)**0.5
    
# Testing
    
box1=Box(5,10)
box2=Box(3,4)
box3=Box(5,10)

box1.print_dim()
box2.print_dim()
box3.print_dim()

print('box1==box2:', box1==box2)
print('box1==box3:', box1==box3)

box1.combine(box3)
box1.print_dim()

box2.double()
box2.print_dim()

box1.combine(box2)
box1.print_dim()
