a = int(input())
b = int(input())
c = int(input())
d = int(input())
def simple(d):
    a = d['molecule']
    b = d['denominator']
    while a%b != 0:
        tmp=a%b
        a = b
        b = tmp
    d['molecule'] /= b
    d['denominator'] /= b
dict = {'molecule':a*d+b*c, 'denominator':b*d}
simple(dict)
print("("+str(a)+"/"+str(b)+")"+"+("+str(c)+"/"+str(d)+")"+"="+str(int(dict['molecule']))+"/" + str(int(dict['denominator'])))
dict['molecule'] = a*d-b*c
simple(dict)
print("("+str(a)+"/"+str(b)+")"+"-("+str(c)+"/"+str(d)+")"+"="+str(int(dict['molecule']))+"/" + str(int(dict['denominator'])))
dict['molecule'] = a*c
simple(dict)
print("("+str(a)+"/"+str(b)+")"+"*("+str(c)+"/"+str(d)+")"+"="+str(int(dict['molecule']))+"/" + str(int(dict['denominator'])))
dict['molecule'] = a*d
dict['denominator'] = b*c
simple(dict)
print("("+str(a)+"/"+str(b)+")"+"/("+str(c)+"/"+str(d)+")"+"="+str(int(dict['molecule']))+"/" + str(int(dict['denominator'])))



    
molecule = a*d+b*c
denominator = b*d
print("("+str(a)+"/"+str(b)+")"+"+("+str(c)+"/"+str(d)+")"+"="+str(molecule)+"/" + str(denominator))
molecule = a*d-b*c
print("("+str(a)+"/"+str(b)+")"+"-("+str(c)+"/"+str(d)+")"+"="+str(molecule)+"/" + str(denominator))
molecule = a*c
print("("+str(a)+"/"+str(b)+")"+"*("+str(c)+"/"+str(d)+")"+"="+str(molecule)+"/" + str(denominator))
molecule = a*d
denominator = b*c
print("("+str(a)+"/"+str(b)+")"+"/("+str(c)+"/"+str(d)+")"+"="+str(molecule)+"/" + str(denominator))
