class Account():

    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def withdraw(self,withdrawn_amount):

        if self.balance >= withdrawn_amount:
            self.balance = self.balance - withdrawn_amount
            print('Amount {} is withdrawn from {} Account is -'.format(withdrawn_amount,self.owner))
            print('Amount left in Account is {}'.format(self.balance))

        else:
            print("Insufficent Amount in your Account !!!")

    def deposit(self,deposit_amount):
        self.balance = self.balance + deposit_amount
        print('Amount {} is Deposited in {} Account is -'.format(deposit_amount,self.owner))
        print('Amount left in Account is {}'.format(self.balance))

    def __str__(self):
        return '-> Total amount in {} account is {}'.format(self.owner,self.balance)


