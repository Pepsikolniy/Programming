#ifndef SOCH_H
#define SOCH_H
#include "fact.h"

int sochetaniya(int k, int n)
{
	int result;
	result = fact(n) / (fact(k) * fact(n - k));
	return result;
}


#endif
