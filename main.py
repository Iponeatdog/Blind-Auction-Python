# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

from art import logo
print(logo)
print("Welcome to the secret auction program.")

continue_or_not = True
bid_dict = {}

while continue_or_not:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

    if name in bid_dict:
        print("Already have a bidder of that name")
    else:
        bid_dict[name] = bid

    continue_or_not = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if continue_or_not == "yes":
        print("\n" * 20)
        continue_or_not = True
    else:
        continue_or_not = False

for key in bid_dict:
    print(f"{key} bid ${bid_dict[key]}")
max_bid_amount = 0
max_bid_person = None
for key in bid_dict:
    if bid_dict[key] > max_bid_amount:
        max_bid_amount = bid_dict[key]
        max_bid_person = key

print(f"{max_bid_person} won by the bid of ${max_bid_amount}")

winner = max(bid_dict, key=lambda k: bid_dict[k])
print(f"{winner} won with a bid of ${bid_dict[winner]}")


print(max(bid_dict.values()))