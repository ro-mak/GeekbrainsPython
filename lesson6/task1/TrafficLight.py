import time
import threading

colors = {1: "RED", 2: "YELLOW", 3: "GREEN"}

CRED = '\033[101m'
CGREEN = '\033[102m'
CYELLOW = '\033[103m'
CEND = '\033[0m'


class TrafficLight:

    def __init__(self):
        self.__is_running = True
        self.__color = colors[1]
        self.__color_lock = threading.Lock()
        self.__traffic_thread = threading.Thread(target=self.running, args=())

    def running(self):
        while self.__is_running:
            self.change_color(1)
            time.sleep(7)
            self.change_color(2)
            time.sleep(2)
            self.change_color(3)
            time.sleep(5)

    def change_color(self, color_pos):
        self.__color_lock.acquire()
        self.__color = colors[color_pos]
        start_color = CRED
        if color_pos == 2:
            start_color = CYELLOW
        elif color_pos == 3:
            start_color = CGREEN
        print(f"\n{start_color}{self.__color}{CEND}")
        self.__color_lock.release()

    def launch_traffic_light(self):
        print(f"\nStarting thread {self.__traffic_thread}")
        self.__traffic_thread.start()

    def stop_traffic_light(self):
        print("\nTraffic light will be turned off on the next iteration...")
        self.__is_running = False

    def check_light(self):
        if not self.__color_lock.locked():
            self.__color_lock.acquire()
            result = self.__color
            self.__color_lock.release()
            return result
