li = """
Give me the C++ code for adding two Values using pointers.


```cpp
#include<iostream>
using namespace std;

int main() {
    int a = 5, b = 7, *p, *q;
    p = &a;
    q = &b;

    cout << "The sum of " << a << " and " << b << " is " << (*p) + (*q) << endl;

    return 0;
}
```

In this code, we first declare two integer variables `a` and `b` and two pointers `p` and `q`. We then assign the address of `a` to `p` and the address of `b` to `q`. Finally, we use the `*` operator to dereference the pointers and add the values of `a` and `b`. The result is printed on the screen.

"""



import time

start = time.perf_counter()

def fibonacci(n):
    if n <= 1:
        return n
    # The logic splits into two branches every time, causing O(2^n) growth
    return fibonacci(n-1) + fibonacci(n-2)

n_terms = 40
print(f"Calculating Fibonacci term {n_terms}...")
result = fibonacci(n_terms)
print(f"Result: {result}")

end = time.perf_counter()

print(f"Execution time is{end-start: .6f} seconds")