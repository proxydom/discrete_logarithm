# Discrete Logarithm Solver in Python

This Python script calculates discrete logarithms, a foundational problem in cryptography, particularly in the Diffie-Hellman key exchange.

## What is a Discrete Logarithm?

Given the equation `g^x ≡ h (mod p)`, the discrete logarithm is the integer `x`. Simply put, it's the exponent to which you raise `g` to get `h`, working modulo `p`.

## Why It Matters in Cryptography

Imagine you and a friend want to share a secret code, but you're in a crowded room where everyone can hear you. You need a way to create a secret key without actually whispering it to each other. That's where discrete logarithms come in.

* **Diffie-Hellman: The Secret Key Exchange**
    * This protocol allows two parties to establish a shared secret over an insecure channel.
    * It relies on the fact that calculating powers is easy, but finding the exponent (the discrete logarithm) is hard.
    * Think of it like mixing paint: it's easy to mix colors, but hard to separate them back into the original colors.
    * Basically, you and your friend perform some calculations with publicly known numbers, and some secret numbers. The result of these calculations can be publicly known.
    * Even if someone is listening they cannot easily get the secret numbers. However, you and your friend can both use your secret numbers, and the public numbers to come to the same shared secret.

* **The Difficulty Factor**
    * The "magic" lies in the fact that it's easy to calculate `g^x (mod p)`, but extremely hard to find `x` if you only know `g`, `h`, and `p`, especially when these numbers are very large.
    * This one-way function is what makes Diffie-Hellman secure.

In essence, the discrete logarithm is a mathematical "one-way street" that allows us to create secure communication channels.

## Script Functionality

This script employs two methods:

1.  **Simplification (if possible):** If `h` is a power of `g`, the logarithm is efficiently calculated.
2.  **Brute Force (otherwise):** If simplification fails, the script iterates through possible values of `x`. (Note: this is inefficient for large numbers. I'll add more algorithm in the future)

## Usage

1.  Clone the repository: `git clone https://github.com/proxydom/discrete_logarithm`
2.  Run the script:

```bash
python discrete_log.py -m <modulo> -b <base> -e <exponent>
```
## Example
```bash
$ python discrete_log.py -m 23 -b 5 -e 17
Il logaritmo discreto di 17 in base 5 (mod 23) è: 7

```
Meaning 5<sup>7</sup> ≡ 17 (mod 23)

## Contributing
Contributions are welcome! Please submit pull requests or open issues.

## Final remarks
I wrote the program in italian, not in english. i'll translate it as soon as i implement other algorithms, like the Baby-Step Giant-Step and the Pohlig–Hellman. 
