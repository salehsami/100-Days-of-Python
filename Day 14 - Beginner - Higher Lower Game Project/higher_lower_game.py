import random
import art
import game_data
print(art.logo)
def format_data(account):
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f" {account_name}, {account_desc}, {account_country}."
account_a = random.choice(game_data.data)
account_b = random.choice(game_data.data)

count = 0
condition = True
while condition is True:
    if account_a == account_b:
        account_b = random.choice(game_data.data)
    print(f"Compare A: {format_data(account_a)}")
    print(art.vs)
    print(f"Compare B: {format_data(account_b)}")
    guess = input("Who has more followers: Type 'A' or 'B':").lower()
    if guess == "a":
        if account_a["follower_count"] > account_b["follower_count"]:
            account_b = random.choice(game_data.data)
            count += 1
            print(f"You are right. You have scored {count}")
            condition = True

        else:
            print(f"You are wrong. You have scored {count}")
            condition = False
    elif guess == "b":
        if account_b["follower_count"] > account_a["follower_count"]:
            account_a = random.choice(game_data.data)
            count += 1
            print(f"You are right. You have scored {count}")
            condition = True
        else:
            print(f"You are wrong. You have scored {count}")
            condition = False
    else:
        print("You have entered wrong data")
