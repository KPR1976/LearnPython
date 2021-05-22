"""
The new "Avengers" movie has just been released!
There are a lot of people at the cinema box office standing in a huge line.
Each of them has a single 100, 50 or 25 dollars bill. An "Avengers" ticket costs 25 dollars.
Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.
Can Vasya sell a ticket to each person and give the change if he initially has no money and sells the
tickets strictly in the order people follow in the line?
Return YES, if Vasya can sell a ticket to each person and give the change with the bills he has at hand
at that moment. Otherwise return NO.

Examples:
tickets([25, 25, 50]) # => YES
tickets([25, 100]) # => NO. Vasya will not have enough money to give change to 100 dollars
tickets([25, 25, 50, 50, 100]) # => NO. Vasya will not have the right bills to give 75 dollars of change (you can't make two bills of 25 from one of 50)
"""
def tickets(people):
    cash = []
    result = 'YES'
    for t in people:
        if t == 25:
            cash.append(t)
        elif t == 50 and cash.count(25) > 0:
            cash.append(t)
            cash.pop(cash.index(25))
        elif t == 100 and cash.count(25) > 0 and cash.count(50) > 0:
            cash.append(t)
            cash.pop(cash.index(25))
            cash.pop(cash.index(50))
        elif t == 100 and cash.count(25) > 2:
            cash.append(t)
            for i in range(3):
                cash.pop(cash.index(25))
        else:
            result = 'NO'
    #print(cash)
    return result

print(tickets([25, 25, 25,50,100]))
