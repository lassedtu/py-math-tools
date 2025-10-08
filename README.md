# py-math-tools

A bunch of math utilities I built from scratch, mainly as a way to improve both my math and programming skills at the same time.

It’s written in Python and started out as a personal learning project, but you can use it for whatever you want.

## What’s Inside

Right now, it includes a few basic algorithms, like finding the greatest common divisor (GCD) using the Euclidean algorithm but I’ll definitely keep adding more as I go.

### GCD

Here’s how to use the `gcd` function:

```python
import math_tools

result = math_tools.gcd(a, b)
print(result)
```

* `a` and `b` should be integers
* returns the greatest common divisor of `a` and `b`

### is_prime

Here’s how to use the `is_prime` function:
```python
import math_tools

result = math_tools.is_prime(n)
print(result)
```

* `n` should be a positive integer
* returns `True` if `n` is a prime number, `False` otherwise

---

I made this project mainly for myself, to get better at writing clean, efficient math-related code. But if it can help you with your own learning or projects, that’s great.
