bids = {}
bidding_finished = False
def biding_auction(amount_of_bids):
    global bidding_finished
    while not bidding_finished:
        name = input("Enter bidder name")
        price = input("Enter your final price $")
        bids[name] = price
        count = input("More bidders yes or no")
        if count == "no":
            bidding_finished = True

    for key in bids:
        maxi = ""
        highest_bidder = 0
        if bids[key] > maxi:
            maxi = bids[key]
            highest_bidder = key
        print(f"The winner is {highest_bidder} with a highest bid of {maxi}")

biding_auction(bids)
