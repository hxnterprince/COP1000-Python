import dice_tools

sides = int(input("How many sides should each die have? "))
num_dice = int(input("How many dice should be rolled? "))

for i in range(num_dice):
    result = dice_tools.roll_die(sides)
    print(f"Die {i + 1}: {result}")
