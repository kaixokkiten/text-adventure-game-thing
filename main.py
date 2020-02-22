def main():
    print("You awaken in your dorm room to the clarion sound of your haphazard tower of styrofoam noodle cups and pizza boxes collapsing. There is no apparent cause, so presumably structural fatigue. Your roommate is nowhere to be seen. You are tired and have a headache. You need a shower.\n\nYou are standing next to your bed. You see your desk and the garbage pile. To the East lies your roommate's area. To the South lies the door to the hallway (and showers).")

    command = input("> ") # need to take 2 paramters, separated by a space. probably have to split up the input and lint by space ughhhh

    checkCommand(command)

def checkCommand(command):
    x = command.split()

    if x[1] == "look":
        print(x[1])

if __name__ == '__main__':
    main()
