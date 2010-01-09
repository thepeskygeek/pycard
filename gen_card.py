import random
import os
import hashlib
import base64

def warning():
    print
    print "*** ATTENTION"
    print "This utilty will generate a self-signed identity card."
    print "Nobody can verify it."
    print
    print "Please enter true details faithfully."
    print

def gen_hash(name, email, rand):
    s = name + email + rand + "selfsigned"
    return hashlib.sha1(base64.b64encode(s)).hexdigest()

def create_xml(has, email, name, i):
    x = "<?xml version='1.0'?><card v='1.0'><identity><person><name>" + name + "</name><email>" + email + "</email></person><verification><id>" + i + "</id><hash>" + has + "</hash><server>selfsigned</server></verification></identity></card>"
    file('identity.crd', 'w').write(x)

if __name__ == "__main__":
    warning()

    print "You need to fill out this form. Please answer the questions."
    print "== REQUIRED"
    name = raw_input("Your name: ")
    email = raw_input("Your email: ")
    c = raw_input("Is this all correct? ")
    if c == "yes":
        p = raw_input("(Optional) Enter a phrase: ")
        if p:
            ti = os.urandom(20) + p + os.urandom(20)
        else:
            i = os.urandom(20) + random.randint(1, random.randint(100000000, 999999999)) + random.getrandbits(10)
            ti = str(i)
        t = hashlib.sha1(ti).hexdigest()
        h = gen_hash(name, email, t)
        create_xml(h, email, name, t)
        print 'Identity card created as identity.crd.'
        
    else:
        print "Quiting. Please rerun."
