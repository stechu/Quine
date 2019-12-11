#!/usr/bin/env python3

qe = chr(34)
c = chr(44)
s = chr(32)

def quine():
    p = ["#!/usr/bin/env python3",
         "",
         "qe = chr(34)",
         "c = chr(44)",
         "s = chr(32)",
         "",
         "def quine():",
         "p = [",
         "    for e in p[:7]:",
         "        print(e)",
         "    print(s + s + s + s+ p[7] + qe + p[0] + qe + c)",
         "    for e in p[1:-1]:",
         "        print(s + s + s + s + s + s + s + s + s + qe + e + qe + c)",
         "    print(s + s + s + s + s + s + s + s + s + qe + p[-1] + qe + p[-1])",
         "    for e in p[8:-4]:",
         "        print(e)",
         "    print(p[1])",
         "    print(p[-4] + qe + p[-3] + qe + chr(58))",
         "    print(p[-2])",
         "if __name__ == ",
         "__main__",
         "    quine()",
         "]"]
    for e in p[:7]:
        print(e)
    print(s + s + s + s+ p[7] + qe + p[0] + qe + c)
    for e in p[1:-1]:
        print(s + s + s + s + s + s + s + s + s + qe + e + qe + c)
    print(s + s + s + s + s + s + s + s + s + qe + p[-1] + qe + p[-1])
    for e in p[8:-4]:
        print(e)
    print(p[1])
    print(p[-4] + qe + p[-3] + qe + chr(58))
    print(p[-2])

if __name__ == "__main__":
    quine()
