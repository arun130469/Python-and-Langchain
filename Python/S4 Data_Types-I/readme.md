# Data Types - I

- Everything is an object (`id()`, `type()`)
- Numbers (`int`, `float`, `imaginary`)
- How numbers are managed internally in CPython
- Boolean Type (`bool`)
- Truth Value
- `__bool__()` and `__len__()`
- Boolean operators
- Comparison operators and functions
- Bitwise operators
- Text sequence - `str`
- Interning



## floating-point numbers explanation
Let's break down how floating-point numbers (floats) are represented in computers using an example. The representation includes three key components:

1. **Sign**: Whether the number is positive or negative.
2. **Mantissa (or significand)**: The significant digits of the number.
3. **Exponent**: A power of 2 that scales the mantissa.

The formula to represent a floating-point number is:

\[
\text{Number} = (-1)^\text{sign} \times \text{mantissa} \times 2^{\text{exponent}}
\]

### Example: Floating-point representation of 6.75
Let's take the number **6.75** as an example to explain the mantissa, exponent, and sign.

#### Step 1: Convert the number to binary
We first convert **6.75** into binary.

- **6** in binary is: `110`
- **0.75** in binary is: `0.11`

So, 6.75 in binary becomes:  
\[
6.75_{10} = 110.11_2
\]

#### Step 2: Normalize the binary number
To normalize, we express the number in the form of \(1.m \times 2^e\) where \(m\) is the mantissa and \(e\) is the exponent.

In this case, \(110.11_2\) can be written as:
\[
110.11_2 = 1.1011_2 \times 2^2
\]

Here:
- The **mantissa** is `1.1011` (we ignore the leading 1 in most systems).
- The **exponent** is `2` (since we shifted the binary point 2 positions to the left).
  
#### Step 3: Represent in floating-point format
Now, let’s break the number down into the floating-point parts:

- **Sign bit**: Since the number is positive, the sign bit is `0`.
- **Mantissa**: The mantissa is the significant part, which is `1011` after the leading 1 (in IEEE 754 format, the leading `1` is implicit and not stored).
- **Exponent**: The exponent is `2`, but in IEEE 754 format, the exponent is stored with a bias. For double precision (which has 11 bits for the exponent), the bias is `1023`. So, the stored exponent becomes `2 + 1023 = 1025`, which is `10000000001` in binary.

#### Final Representation:
The floating-point representation of **6.75** in double precision (64 bits) would look like this:

- **Sign bit**: `0` (positive)
- **Exponent**: `10000000001` (1025 in decimal, represents exponent `2`)
- **Mantissa**: `1011000000000000000000000000000000000000000000000000` (52 bits)

Putting it all together, the 64-bit representation of **6.75** would be:

```
0 10000000001 1011000000000000000000000000000000000000000000000000
```

This is how floating-point numbers are stored in memory. You can see the key parts:
- **Sign**: `0` (positive number)
- **Exponent**: `10000000001` (biased exponent for `2`)
- **Mantissa**: `1011` followed by zeros (represents `1.1011`)

### Summary of Components
- **Sign**: `0` (positive)
- **Mantissa**: `1.1011` (fractional part of the number)
- **Exponent**: `2` (represents how far to shift the binary point)

So, the formula looks like:

\[
6.75 = (-1)^0 \times 1.1011 \times 2^2
\]


