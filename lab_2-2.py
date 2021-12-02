# Author: RTS 12/01/21

def party_inv(lst):
    for name in lst:
        print("Hi {0}, You're invited to my party").format(int(name))

invites(["Michael", "Jake", "Steve"])
