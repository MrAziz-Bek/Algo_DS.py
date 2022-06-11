Console.WriteLine(findMaximum(23, 34, 12));

static int findMaximum(int a, int b, int c)
{
    int max = a;

    if (max < b)
        max = b;
    if (max < c)
        max = c;

    return max;
}