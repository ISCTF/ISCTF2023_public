import random
from gmpy2 import invert,sqrt,gcd

class P:
	def __init__(self, data):
		if type(data) is int:
			self.size = data
			self._list = [i+1 for i in range(self.size)]
			self._initialize()			
		elif type(data) is list:
			self._list = data
			self.size = len(self._list)

	def __mul__(self, other):
		return self._iterList(self.getList(),other.getList())

	def __repr__(self):
		return str(self._list)

	def __len__(self):
		return len(self._list)

	def __pow__(self, other):
		for _ in range(1,other):
			self._list = self._iterList(self._list, self._list)
		return self._list

	def __str__(self):
		return str(self._list)

	def getList(self):
		return self._list

	def _initialize(self):
		for i in range(10):
			random.shuffle(self._list)

	def _iterList(self, List1,List2):
		new_list = []
		for elem in List1:
			new_list.append(List2[elem - 1])
		return new_list

pass

class Block():
	def __init__(self):
		while True:
			self.q = random.getrandbits(2048)
			self.f = random.randint(1, sqrt(self.q // 2))
			self.g = random.randint(sqrt(self.q // 4), sqrt(self.q // 2))
			if gcd(self.f, self.q * self.g) == 1:
				break

		self.h = invert(self.f, self.q) * self.g % self.q
		
	def getPublicKey(self):
		return (int(self.q), int(self.h))
	
	def enc(self, m):
		assert m < sqrt(self.q//4)
		r = random.randint(1, sqrt(self.q // 2))
		e = (r * self.h + m) % self.q
		
		return int(e)

	def dec(self, e):
		a = self.f * e % self.q
		b = invert(self.f, self.g) * a % self.g
		return b