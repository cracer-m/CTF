# -*- coding: utf-8 -*-

class CLEMENCY(object):
    def __init__(self,binary):
        self.binary = binary
        self.bitstream = ""
        self.current = 0
        self.plain = []
        while True:
            x = self.get_1_byte()
            if x == None: break
            self.plain.append(x)
    def __len__(self):
        return len(self.plain)
    def __getitem__(self,key):
        return self.plain[key]
    def get_1_byte(self):
        while self.current < len(self.binary) and len(self.bitstream) < 9:
            self.bitstream += "{:08b}".format(ord(self.binary[self.current]))
            self.current += 1
        if len(self.bitstream) < 9: return None
        ans = int(self.bitstream[:9],2)
        self.bitstream = self.bitstream[9:]
        return ans
    def get_bytes(self,n):
        ans = []
        for i in xrange(n):
            ans.append(self.get_1_byte())
        if len(ans) != n: print "file is drained..."
        return ans

with open('rubix.bin') as data:
    binary = data.read()

C = CLEMENCY(binary)

for i in xrange(len(C)-3):
    if C[i:i+3] == [3, 328, 384]:
        print i

