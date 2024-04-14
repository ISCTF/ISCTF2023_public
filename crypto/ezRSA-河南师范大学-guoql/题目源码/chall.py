from secret import flag,key
from Crypto.Util.number import *
from random import randint,getrandbits
from sympy import factorial as factor
from gmpy2 import is_prime as is_strongPrime
from gmpy2 import gcd
from libnum import s2n

def step1(m):
	p,q = getPrime(1024),getPrime(1024)
	n=p*q
	e=getPrime(512)
	phi = (p-1)*(q-1)
	while gcd(e,phi) != 1:
		e=getPrime(512)
	d = pow(e,-1,phi)
	k = randint(800,1500)
	f = factor(k)
	leak = (pow(e, 2) + (e*d - 1)*f)*getPrime(256) + k
	print(f"{n=}")
	print(f"{leak=}")
	e = 65537
	c = pow(m,e,n)
	return c


def step2(m):
	#the key number is three part 
	assert key < 10**9
	assert (is_prime(key) and not is_strongPrime(key))

	p,q = getPrime(512),getPrime(512)
	n=p*q
	leak1 = pow(p,q,n) + pow(q,p,n)
	print(f"{n=}")
	print(f"{leak1=}")
	e=0x10001
	c = pow(m,e,n)
	seed = getrandbits(64)
	a = getPrime(256)
	b = getPrime(256)
	leak2 = []
	for i in range(10):
		leak2.append(seed := (seed * a + b) % p)
	print(f"{leak2 = }")
	seed = (seed * a + b) % p
	base = key ^ seed
	final = []
	while c > 0:
		final.append(c % base)
		c //= base

	return final


# def most(lis):
# 	return lis.count(True) > lis.count(False)

def is_prime(p):
	check = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
	return all([pow(i,p-1,p)==1 for i in check])


def main():
	assert len(flag) == 2
	print("step1:")
	print("c =",step1(s2n(flag[0])))
	print("step2:")
	print("final =",step2(s2n(flag[1])))


if __name__ == "__main__":
	main()