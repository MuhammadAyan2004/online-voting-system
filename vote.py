from users import User

class votingSystem:
    parties = {"MQM":0, "PTI":0, "PPL":0}
    def vote(self):
        username = input("Enter your username to vote:")
        password = input("Enter your password to vote:")
        user = User.authenticate(username,password)
        if user:
            if user.has_voted:
                print("you already voted.")
                return
            print("Parties: MQM, PTI, PPL")
            choice = input("enter the party name you want to vote for. ").upper()
            if choice in self.parties:
                self.parties[choice] +=1
                user.has_voted = True
                print("vote cast successfully.")
            else:
                print("invalid party choice.")
    def view_result(self):
        print("\n voting results: ")
        for party, vote in self.parties.items():
            print(f"party {party}: {vote} votes.")

