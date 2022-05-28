#include <iostream>

using namespace std;

int gcd(int a, int b)
{
    while (b != 0)
    {
        int temp = a;
        a = b;
        b = temp % b;
    }
    return a;
}

int main()
{
    cout << gcd(60, 96) << endl;
    cout << gcd(20, 8) << endl;
    return 0;
}