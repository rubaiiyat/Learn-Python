list1 = ["Biryani", "Ice Cream", "Pizza", "Pancakes"]
list2 = ["Aromatic", "Cold", "Cheesy", "Fluffy"]


for item, specialty in zip(list1, list2):
    print(f"{item}: {specialty}")
