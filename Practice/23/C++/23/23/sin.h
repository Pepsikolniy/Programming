#ifndef SIN_H
#include <iostream>
#include "fact.h"
#define SIN_H

int sin(double x, double k)
{
    double result = 0;
        for (double i = 1; i <= k; i++)
            result += pow((-1), k) * (pow(x, 2 * k + 1) / fact(2 * k + 1));
    return result;
}

#endif