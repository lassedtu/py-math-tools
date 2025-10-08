# py-math-tools

A collection of mathematical utilities created from scratch, aimed at university-level mathematics students and enthusiasts. This project provides implementations of various mathematical algorithms and functions.

## Features

### Greatest Common Divisor (GCD)

This project includes an implementation of the Euclidean algorithm to find the greatest common divisor (GCD) of two integers.

#### Usage

The `gcd` function is accessible via the `math_tools` package:

```python
import math_tools

result = math_tools.gcd(a, b)
print(result)
```

-   `a` and `b` must be integers.
-   The function will return the greatest common divisor of `a` and `b`.
-   If the inputs are not valid integers, it will return `None`.
