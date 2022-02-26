---
hide:
  - navigation
---

# ECIES

!!! success "This algorithm is recommended"

    TODO: Parameters recommendations

--8<-- "includes/disclaimer.md"

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
|Ed25519||{{ recommendation("success", "Recommended: Best choice", None) }}|
|Curve25519||{{ recommendation("success", "Recommended: Best choice if Ed25519 is not available", None) }}|
|Curve2213|M-221|{{ recommendation("success", "Recommended", None) }}|
|Curve1174||{{ recommendation("success", "Recommended", None) }}|
|Curve383187||{{ recommendation("success", "Recommended", none) }}|
|Curve41417||{{ recommendation("success",  "Recommended", none) }}|
|Curve448|Ed448, Ed448-Goldilocks|{{ recommendation("success", "Recommended", none) }}|
|E-222||{{ recommendation("success", "Recommended", none) }}|
|E-382||{{ recommendation("success", "Recommended", none) }}|
|M-383||{{ recommendation("success", "Recommended", none) }}|
|M-511||{{ recommendation("success", "Recommended", none) }}|
|E-521||{{ recommendation("success", "Recommended", none) }}|
|secp256k1||{{ recommendation("success", "Recommended. This curve is used in Bitcoin[^2]", none) }}|
|secp256r1|NIST P-256|{{ recommendation("info", "Considered safe, but using this curve securly is very hard, see SafeCurves[^1]", None) }}|
|secp384r1|NIST P-384|{{ recommendation("info", "Considered safe, but using this curve securly is very hard, see SafeCurves[^1]", None) }}|
|secp521r1|NIST P-521|???|
|secp224r1|NIST P-224|{{ recommendation("info", "Considered safe, but using this curve securly is very hard, see SafeCurves[^1]", None) }}|
|secp192r1|NIST P-192|{{ recommendation("failure", "Not recommended", None) }}|
|Brainpool P256R1||   {{ recommendation("failure", "Not recommended", None) }}|
|Brainpool P512R1||   {{ recommendation("failure", "Not recommended", None) }}|
|sect571k1|NIST K-571|{{ recommendation("failure", "Not recommended", None) }}|
|sect409k1|NIST K-409|{{ recommendation("failure", "Not recommended", None) }}|
|sect283k1|NIST K-283|{{ recommendation("failure", "Not recommended", None) }}|
|sect233k1|NIST K-233|{{ recommendation("failure", "Not recommended", None) }}|
|sect163k1|NIST K-163|{{ recommendation("failure", "Not recommended", None) }}|
|sect571r1|NIST B-571|{{ recommendation("failure", "Not recommended", None) }}|
|sect409r1|NIST B-409|{{ recommendation("failure", "Not recommended", None) }}|
|sect283r1|NIST B-283|{{ recommendation("failure", "Not recommended", None) }}|
|sect233r1|NIST B-233|{{ recommendation("failure", "Not recommended", None) }}|
|sect163r2|NIST B-163|{{ recommendation("failure", "Not recommended", None) }}|

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