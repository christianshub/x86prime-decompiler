long* main(long* arr, long n) {
    long max = 0;

    for(long i = 1; i < n; ++i) {
        if (arr[max] < arr[i]) {
            max = i;
        }
    }

    return &arr[max];
}