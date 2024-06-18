import time


class OPS:

    def __init__(self):
        self.seconds = {}
        pass

    def add(self):
        sec = int(round(time.time()))

        if sec in self.seconds:
            self.seconds[sec] = self.seconds[sec]+1
        else:
            self.seconds[sec] = 1

    def print(self):
        print(self.seconds)


o = OPS()
i = 0
# try for 20,000,000 basic operators
while i < 20000000:
    i = i + 1
    o.add()

o.print()
# prints {1544912424: 769, 1544912425: 2648, 1544912426: 2578, 1544912427: 2599, 1544912428: 1406}
# the result shows, the number of seconds counted from epoch, and the number of operators in a second.
