#ifndef SIN_H
#include <cmath>
#include "fact.h"
#define SIN_H

double sin(double x, int k)
{
        double result = 0;
        for (int i = 0; i < k; i++)
            result += pow(-1, i) * (pow(x, 2 * i + 1) / (fact(2 * i + 1)));
        return result;
}

#endif