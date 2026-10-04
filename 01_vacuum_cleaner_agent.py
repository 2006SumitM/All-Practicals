table = {
    ("A", "Dirty"): "Suck",
    ("A", "Clean"): "Move Right",
    ("B", "Dirty"): "Suck",
    ("B", "Clean"): "Move Left"
}

print("Vacuum Cleaner Agent")
print("--------------------")

location = input("Enter location (A/B): ")
status = input("Enter status (Dirty/Clean): ")

percept = (location, status)
action = table.get(percept)

print("Action to perform:", action)
