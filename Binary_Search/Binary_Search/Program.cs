int Binary_Search(int item, int[] list)
{
    int L = 0, H = list.Length - 1, count = 0;
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

        count++;
    }
    return -1;
}

var list = new[]{ 10, 20, 30, 50, 60, 80, 110, 130, 140, 170 };
int res = Binary_Search(110, list);
Console.WriteLine(res);