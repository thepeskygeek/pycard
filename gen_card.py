import random
import os
import hashlib
import base64

def warning():
    print
    print "*** ATTENTION"
    print "This utilty will generate a self-signed identity card."
    print "Please verify your card with a service provider."
    print
    print "Please enter true details faithfully."
    print

def gen_hash(name, email):
    random.seed(hash(random.getrandbits(20))+hash(os.urandom(20))+6+hash(name))
    i = random.randrange(1, 999999999)
    s = name + email
    # welcome to hackville
    s.format(s+"{0}".format(i))
    # whew
    s = s + "selfsigned"
    return hashlib.sha1(base64.b64encode(s)).hexdigest()

def create_xml(has, email, name):
    x = "<?xml version='1.0'><card v='1.0'><identity><person><name>" + name + "</name><email>" + email + "</email></person><verification><trust level='3'/><hash>" + has + "</hash><server>selfsigned</server></verification></identity></card>"
    file('identity.crd', 'w').write(x)

if __name__ == "__main__":
    warning()

    print "You need to feel out this form. Please answer the questions."
    print "== REQUIRED"
    name = raw_input("Your name: ")
    email = raw_input("Your email: ")
    c = raw_input("Is this all correct? ")
    if c == "yes":
        h = gen_hash(name, email)
        create_xml(h, email, name)
    else:
        print "Quiting. Please rerun."
