# Given guest list
guest_list = [
    "Liam", "Emma", "Noah", "Olivia", "Lucas", "Mila", "Floris", "Sophie", "Levi", "Zwaantje", "Luuk", "Julia", "Sem", "Eva",
    "Daan", "Lynn", "Jayden", "Tess", "Mees", "Sara", "Lars", "Anna", "Bram", "Nora", "Thijs", "Fleur", "Jesse", "Liv",
    "Sam", "Noa", "Max", "Elin", "Thomas", "Roos", "Milan", "Nova", "Finn", "Emily", "Adam", "Isabella", "Daniel", "Lara",
    "Gijs", "Isabel", "Dylan", "Nina", "Stijn", "Evi", "Tijn", "Lotte"
]

# Function to check if two names have common letters
def have_common_letters(name1, name2):
    for letter in name1:
        if letter in name2:
            return False
    return True

# Create an empty dictionary to store the number of friends for each guest
friends_count = {}

# Initialize the dictionary with a count of 0 for each guest
for guest in guest_list:
    friends_count[guest] = 0

# Determine the number of friends for each guest
for guest1 in guest_list:
    for guest2 in guest_list:
        if guest1 != guest2 and have_common_letters(guest1, guest2):
            friends_count[guest1] += 1

# Find the guest with only 2 friends
guest_with_2_friends = None  # Initialize the variable to store the guest with 2 friends

for guest, count in friends_count.items():
    if count == 2:
        guest_with_2_friends = guest
        break  # Exit the loop when the guest is found

# Check if there is exactly one guest with 2 friends
if guest_with_2_friends is not None:
    # Determine the friends of the guest with 2 friends
    common_friends = [guest for guest in guest_list if have_common_letters(guest, guest_with_2_friends)]

    # Calculate the sum of the lengths of the names of the common friends
    sum_of_name_lengths = sum(len(name) for name in common_friends)

    print(f"The two friends had {len(common_friends)} different friends in common, and the sum of their name lengths is {sum_of_name_lengths}.")
else:
    print("There is not exactly one guest with 2 friends.")
