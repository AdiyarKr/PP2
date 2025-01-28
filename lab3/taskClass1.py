class String():
    def getString(self):
        self.s = str(input())
    def printString(self):
        print(self.s.upper())

ans = String()
ans.getString()
ans.printString()