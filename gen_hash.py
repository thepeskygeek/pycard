import random
import os
import hashlib
import base64

if __name__ == '__main__':
    n = raw_input('Name: ')
    e = raw_input('Email: ')
    c = raw_input('Signer Server URL: ')
    random.seed(hash(random.getrandbits(20))+hash(os.urandom(20))+6+hash(n))
    i = random.randrange(1, 999999999)
    print "Unqiue ID:"
    print i
    s = n + e
    # welcome to hackville
    s.format(s+"{0}".format(i))
    # whew
    s = s + c
    print s
    print "<hash>" + hashlib.sha1(base64.b64encode(s)).hexdigest() + "</hash>"
