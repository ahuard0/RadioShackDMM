from rs22812 import RS22812
from time import strftime, sleep
from sys import argv

def TimeNow():
        return strftime("%d%b%Y-%H:%M:%S")


if __name__ == "__main__":
    rs = RS22812("COM11")
    interval = 0
    if len(argv) > 1:
        interval = abs(float(argv[1]))
    count = 0
    while True:
        count += 1
        r = rs.GetReading()
        print(TimeNow() + " [%d]" % count, r)
        sleep(interval)
