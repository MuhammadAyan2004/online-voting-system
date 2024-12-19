from users import User, register_user, login_user
from vote import votingSystem

def main():
    voting = votingSystem()
    while True:
        print("1. Register")
        print("2. Login")
        print("3. vote")
        print("4. view Results")
        print("5. Exit")
        choice = input("Enter Your Choice: ")
        if choice == "1":
            register_user()
        elif choice == "2":
            login_user()
        elif choice == "3":
            voting.vote()
        elif choice == "4":
            voting.view_result()
        elif choice == "5":
            print("Exiting the system.")
            break
        else:
            print("invalid choice please try again.")

if __name__ == "__main__":
    main()
