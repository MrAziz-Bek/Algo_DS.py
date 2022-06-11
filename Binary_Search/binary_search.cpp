#include <iostream>

using namespace std;

int binary_search(int list[], int item)
{
    int L = 0, H = sizeof(list) - 1;
    while (L <= H)
    {
        int m = (L + H) / 2;
        int guess = list[m];
        if (guess == item)
            return m;
        else if (guess > item)
            H = m - 1;
        else
            L = m + 1;
    }
    return -1;
}

int main()
{
    int list[] = {10, 20, 30, 50, 60, 80, 110, 130, 140, 170};

    cout << binary_search(list, 110) << endl;
    return 0;
}