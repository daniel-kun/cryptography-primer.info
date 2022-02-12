---
hide:
  - navigation
---

# ECIES

!!! success "This algorithm is recommended"

    TODO: Parameters recommendations

On this page you will learn:

* What is ECIES, and features does it provide?
* How secure is ECIES?
* What can I use instead of ECIES?
* What modes of operation can I use with ECIES?

!!! info "Quick Info"

    |ECIES| |
    |----|-|
    |Names|ECIES (Elliptic Curve Integrated Encryption Scheme), Elliptic Curve Augmented Encryption Scheme, Elliptic Curve Encryption Scheme|
    |Attributes|Asymmetric (Public Key), Hybrid Cipher|
    |Features|Encryption|
    |Private Key Size|TODO ???|
    |First Published|2001, Victor Shoup|

## ECIES in practice

With ECIES you can achieve Hybrid Encryption, which means that a symmetric encryption key is being generated for each encryption operation, which is then encrypted using the Elliptic Curve Public Key. This encrypted key, alongside with the symmetrically encrypted ciphertext, is then sent to the recipient, which in turn can decrypt the symmetric encryption key using it's Elliptic Curve Private Key, and decrypt the ciphertext using that decrypted key.

ECIES is usually used with [AES](/algorithms/aes) in practice, and many parameters and algorithms can be configured when using ECIES.

!!! danger "TODO: Authentication not provided? (see https://developers.google.com/tink/exchange-data)"

## Elliptic Curve Parameters

Elliptic Curve is a general framework that works with many kinds of curves with different attributes, so there are a lot of parameters that make up an EC cipher.

### EC parameters: Curves

The main parameter of an Elliptic Curve implementation is the curve to be used for the algorithms.

!!! info inline end "Curves with at least 224 Bits are recommended."

|Curve|Also known as|Recommendation|
|-----|-------------|--------------|
|Ed25519||✔ Recommended, best choice|
|Curve25519||✔ Recommended, best choice if Ed25519 is not available|
|Curve2213|M-221|✔ Recommended|
|Curve1174||✔ Recommended|
|Curve383187||✔ Recommended|
|Curve41417||✔ Recommended|
|Curve448|Ed448, Ed448-Goldilocks|✔ Recommended|
|E-222||✔ Recommended|
|E-382||✔ Recommended|
|M-383||✔ Recommended|
|M-511||✔ Recommended|
|E-521||✔ Recommended|
|secp256k1||✔ Recommended. This curve is used in Bitcoin[^2].|
|secp256r1|NIST P-256|⚠ Using this curve securly is very hard, see SafeCurves[^1].|
|secp384r1|NIST P-384|⚠ Using this curve securly is very hard, see SafeCurves[^1].|
|secp521r1|NIST P-521|???|
|secp224r1|NIST P-224|⚠ Using this curve securly is very hard, see SafeCurves[^1].|
|secp192r1|NIST P-192|❌ Not recommended|
|Brainpool P256R1||❌ Not recommended|
|Brainpool P512R1||❌ Not recommended|
|sect571k1|NIST K-571|❌ Not recommended|
|sect409k1|NIST K-409|❌ Not recommended|
|sect283k1|NIST K-283|❌ Not recommended|
|sect233k1|NIST K-233|❌ Not recommended|
|sect163k1|NIST K-163|❌ Not recommended|
|sect571r1|NIST B-571|❌ Not recommended|
|sect409r1|NIST B-409|❌ Not recommended|
|sect283r1|NIST B-283|❌ Not recommended|
|sect233r1|NIST B-233|❌ Not recommended|
|sect163r2|NIST B-163|❌ Not recommended|

## Security Level

TODO: IND-CCA2

## Standardization

|Standard|Date|
|--------|----|
|SEC 1: Elliptic Curve Cryptography v2.0|2009|
|IEEE 1363a|2004 (inactive since 2019)|
|ANSI X9.63|2004|
|ISO/IEC 18033-2:2006|2006|

[^1]: [SafeCurves](https://safecurves.cr.yp.to/) on cr.yp.to by D.J. Bernstein
[^2]: [Secp256k1 on Bitcoin Wiki](https://en.bitcoin.it/wiki/Secp256k1) on en.bitcoin.it