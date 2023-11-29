import re
import time


class LogTail:
    def __init__(self, file):
        self.f = file
        self.buffer = ""

    def read_line(self):
        temp = self.f.readline()
        if temp != "":
            self.buffer += temp
            if self.buffer.endswith("\n"):
                line_out = self.buffer
                self.buffer = ""
                return line_out
            else:
                return None

    def read(self, pred=None):
        temp = ""
        if pred is not None:
            while line := self.read_line():
                if pred(line):
                    temp += line
        else:
            while line := self.read_line():
                temp += line
        return temp


def is_kill(line):
    return re.match(
        """\d\d\/\d\d\/\d\d\d\d - \d\d:\d\d:\d\d: ([^\n]{0,32}) killed ([^\n]{0,32}) with (\w+)(\.|(\. \(crit\)))""",
        line) is not None


if __name__ == '__main__':
    with open("E:\\Programs\\Steam\\steamapps\\common\\Team Fortress 2\\tf\\console.log", 'r') as file:
        log = LogTail(file)
        while True:
            while line := log.read(is_kill):
                print(line, end='')
            time.sleep(0.5)
