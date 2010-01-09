import random
import os
import hashlib

if __name__ == '__main__':
    n = raw_input('Name: ')
    e = raw_input('Email: ')
    c = raw_input('Signer Server URL: ')
    h = raw_input('(Optional) Phrase: ')
    random.seed(hash(random.getrandbits(20))+hash(h)+hash(os.urandom(random.randint(1, 30))))
    i = random.randint(1, 99999999999)
    print "Unqiue ID:"
    print i
    s = n + e + str(i) + c
    print "Hashed string: "
    print s
    print "Line to put in XML pycard:"
    print "<hash>" + hashlib.sha1(s).hexdigest() + "</hash>"
