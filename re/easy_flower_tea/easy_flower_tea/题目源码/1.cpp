#include<stdio.h>
#include<string.h>
#include<iostream>
#include<stdint.h> 


void encrypt(uint32_t* v, uint32_t* k) {
	uint32_t v0 = v[0], v1 = v[1], sum = 0, i;           /* set up */
	uint32_t delta = 0x9e3779b9;                     /* a key schedule constant */
	uint32_t k0 = k[0], k1 = k[1], k2 = k[2], k3 = k[3];   /* cache key */
	for (i = 0; i < 32; i++) {                       /* basic cycle start */
		sum += delta;
		v0 += ((v1 << 4) + k0) ^ (v1 + sum) ^ ((v1 >> 5) + k1);
		v1 += ((v0 << 4) + k2) ^ (v0 + sum) ^ ((v0 >> 5) + k3);
	}                                              /* end cycle */
	v[0] = v0;
	v[1] = v1;
}

int main()
{
	uint32_t v[2]= {0}, k[4] = {12,34,56,78};
	__asm {
		xor eax, eax
		test eax, eax
		je code1
		jne code2
		code2 :
		__asm _emit 0x5e
		and eax, ebx
			__asm _emit 0x50
		xor eax, ebx
			__asm _emit 0x74
		add eax, edx
			code1 :
	}
	std::cout << "Please enter your number 1:\n" << std::endl;
	std::cin >> v[0];
	std::cout << "Please enter your number 2:\n" << std::endl;
	std::cin >> v[1];
	encrypt(v, k);
	std::cout << "Encryption succeeded!\n" << std::endl;
	if (v[0]==1115126522)
	{
		if (v[1]==2014982346)
		{
			std::cout << "Congrtulation!" << std::endl;
			return 0;
		}
	}
	else
	{
		std::cout << "error" << std::endl;
	}
	return 0;
}

