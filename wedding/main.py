# Marshall and Lily are getting married! They sent wedding invitations to all their friends.
# Each invitation can be noted +one — it means that the friend wants to come with his
# non-invited partner. All friends have responded to the invitations, and now Lily
# wants to know for how many guests to organize a dinner in a restaurant.
# All guests will sit at one large table. Marshall is very superstitious, so if there
# will be exactly 13 people at the table (including Marshall and Lily), then Lily will
# ask restaurant staff to put a dummy and serve it along with all. How much will young
# couple spend on this dinner, if the service of one person (or dummy) is worth $100?
# Input
# The first line contains a single integer n that is a number of friends of Marshall and Lily,
# that have responded to the invitations (1 ≤ n ≤ 20).
# The next n lines describe the responses. Each response has the form name[+one].
# This is the name of the friend and +one if the friend has chosen this option.
# It is guaranteed that the length of each name does not exceed 20, and each name
# consists of Latin letters.
# Output
# Output the cost of dinner in dollars.

i = 0
price = 100
guests = 0
dinner = 0

while i == 0:
    g = int(input("Enter a number of invitations: "))
    p = int(input("Enter a number of guests with partner: "))
    if g <= 0 or p > g:
        print("Wrong number.")
    else:
        i = 1
        guests = g + p
        if guests == 13:
            guests = guests + 1
dinner = guests * price
print("Dinner costs ", dinner, "$")
