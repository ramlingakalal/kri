import math
def hlf(a,b):
    hcf=math.gcd(a,b)
    lcm=abs(a*b)//hcf
    return hcf,lcm


if __name__=="__main__":
    print(hlf(12,18))
