class LoadWallet:
    name = ""
    mobile_number = ""
    total_balance = 0.0
    
    def __init__(self, name, number, starting_balance):
        self.name = name
        self.mobile_number = number
        self.total_balance = starting_balance
        
    def top_up(self, amount):
        self.total_balance += amount
        print("Top-up successful!")
        print(f"New balance: ₱{self.total_balance}")
    
    def send_load(self, recipient, amount):
        if self.total_balance >= amount:
            self.total_balance -= amount
            recipient.total_balance += amount
            print(f"Successfully sent ₱{amount} to {recipient.name}.")
            print(f"New balance: ₱{self.total_balance}")
        else:
            print("Insufficient balance to send load.")
            
    def send_with_fee(self, recipient, amount):
        fee = 2
        if self.total_balance >= amount + fee:
            self.total_balance -= amount + fee
            recipient.total_balance += amount
            print(f"Successfully sent ₱{amount} to {recipient.name} (other network).")
            print(f"₱{fee} fee charged.")
            print(f"New balance: ₱{self.total_balance}")
        else:
            print("Insufficient balance to send load.")
            
    def show_balance(self):
        print(f"{self.name}'s current balance:")
        print(f"₱{self.total_balance}")