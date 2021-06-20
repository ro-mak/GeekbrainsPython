from lesson6.task1.TrafficLight import TrafficLight

traffic_light = TrafficLight()
traffic_light.launch_traffic_light()


def are_you_dead(color):
    if color == "RED":
        return True
    else:
        return False


attempts = 5

while True:
    print()
    answer = input("Should I walk? \n")
    if answer.lower() == "yes":
        is_dead = are_you_dead(traffic_light.check_light())
        if is_dead:
            print("WASTED")
            traffic_light.stop_traffic_light()
            break
        else:
            print("Congratulations, you live another day!")
            traffic_light.stop_traffic_light()
            break
    else:
        if attempts <= 0:
            print("You died of starvation...")
            traffic_light.stop_traffic_light()
            break
        else:
            print("Try once again")
            attempts -= 1
