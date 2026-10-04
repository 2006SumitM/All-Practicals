# table = {
#     ("Red", "Obstacle"): "Stop",
#     ("Green", "Clear"): "Move Forward",
#     ("Yellow", "Clear"): "Slow Down",
#     ("Red", "Clear"): "Stop",
#     ("Green", "Obstacle"): "Brake"
# }

# print("Autonomous Taxi Agent")
# print("---------------------")

# signal = input("Enter traffic signal (Red/Yellow/Green): ")
# road = input("Enter road condition (Clear/Obstacle): ")

# percept = (signal, road)
# action = table.get(percept)

# print("Action to perform:", action)

table = {
    ("red","clear") : "stop",
    ("red","obstacle") : "stop",
    ("green","clear") : "move forward",
    ("green","obstacle") : "stop and horn!",
    ("yellow","clear") : "slow down",
    ("yellow","stop") : "stop"
}


print("this is an automatic taxi agent")
print("---------------------------------------------------------------------")


signal_color = input("enter the color of signal (red,green,yello) : ")
disturbance = input("enter whethear any obstacle is there or not : ")

action_detailes = (signal_color,disturbance)
action = table.get(action_detailes)

print("action to perform : ",action)





