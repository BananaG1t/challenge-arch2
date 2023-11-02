# Given guest list
guest_list = [
    "Liam", "Emma", "Noah", "Olivia", "Lucas", "Mila", "Floris", "Sophie", "Levi", "Zwaantje", "Luuk", "Julia", "Sem", "Eva",
    "Daan", "Lynn", "Jayden", "Tess", "Mees", "Sara", "Lars", "Anna", "Bram", "Nora", "Thijs", "Fleur", "Jesse", "Liv",
    "Sam", "Noa", "Max", "Elin", "Thomas", "Roos", "Milan", "Nova", "Finn", "Emily", "Adam", "Isabella", "Daniel", "Lara",
    "Gijs", "Isabel", "Dylan", "Nina", "Stijn", "Evi", "Tijn", "Lotte"
]


def find_friend(guest):
    setguest = set(guest)
    friendlist = []
    for other in guest_list:
        setother = set(other)
        if len(setguest & setother) == 0:
            friendlist.append(other)
    return friendlist


for guest in guest_list:
    friendlist = find_friend(guest)
    if len(friendlist) == 2:
        friends = friendlist
        cnt = 0
        summ = 0
        for friend in friendlist:
            if cnt < 1:
                friendlistone = set(find_friend(friend))
            else:
                friendlisttwo = set(find_friend(friend))
            cnt += 1
        friendmatches = friendlistone & friendlisttwo
        for friendoffriend in friendmatches:
            summ += len(friendoffriend)
        break

print(summ)