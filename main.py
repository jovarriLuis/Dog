from load_wallet import LoadWallet


wallets = {
    "09110000001": LoadWallet("Ana Reyes", "09110000001", 100),
    "09110000002": LoadWallet("Ben Santos", "09110000002", 250),
    "09110000003": LoadWallet("Chris Cruz", "09110000003", 300),
    "09110000004": LoadWallet("Dina Lopez", "09110000004", 150),
    "09110000005": LoadWallet("Eli Ramos", "09110000005", 400),
}


def top_up_wallet():
    mobile_number = input("Enter your mobile number: ")
    wallet = wallets.get(mobile_number)

    if wallet is None:
        print("Wallet not found.")
        return

    amount = float(input("Enter top-up amount: "))
    wallet.top_up(amount)


def send_load(same_network=True):
    sender_number = input("Enter sender mobile number: ")
    sender = wallets.get(sender_number)
    if sender is None:
        print("Sender mobile number not found.")
        return

    recipient_number = input("Enter recipient mobile number: ")
    recipient = wallets.get(recipient_number)
    if recipient is None:
        print("Recipient mobile number not found.")
        return

    amount = float(input("Enter amount to send: "))

    if same_network:
        sender.send_load(recipient, amount)
    else:
        sender.send_with_fee(recipient, amount)


def check_balance():
    mobile_number = input("Enter mobile number to check balance: ")
    wallet = wallets.get(mobile_number)

    if wallet is None:
        print("Wallet not found.")
        return

    print(f"Balance for {wallet.name} ({wallet.mobile_number}):")
    print(f"₱{wallet.total_balance}")


def ask_to_continue():
    answer = input("Do you want to continue? (Y/N): ").strip().lower()
    if answer == "n" or answer == "no":
        print("Thank you for using LoadWallet!")
        return False
    return True


def main():
    while True:
        print("\n===== LoadWallet Menu =====")
        print("1. Top up wallet")
        print("2. Send load (same network)")
        print("3. Send load with ₱2 fee (other network)")
        print("4. Check balance")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            top_up_wallet()
            if not ask_to_continue():
                break
        elif choice == "2":
            send_load(True)
            if not ask_to_continue():
                break
        elif choice == "3":
            send_load(False)
            if not ask_to_continue():
                break
        elif choice == "4":
            check_balance()
            if not ask_to_continue():
                break
        elif choice == "5":
            print("Thank you for using LoadWallet!")
            break
        else:
            print("Invalid option. Please choose from 1-5.")


if __name__ == "__main__":
    main()