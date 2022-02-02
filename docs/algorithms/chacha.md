---
hide:
  - navigation
---

# ChaCha

!!! success "This algorithm is recommended"

    ChaCha20-Poly1305 is considered __secure__[^1]. It has a strong security level and provides authentication.

On this page you will learn:

* What is ChaCha, and features does it provide?
* How secure is ChaCha?
* What can I use instead of ChaCha?
* What modes of operation can I use with ChaCha?
* Where and how is ChaCha being used?

!!! info "Quick Info"

    |ChaCha| |
    |----|-|
    |Names|ChaCha (with various additions, see below)|
    |Attributes|Symmetric (Private Key), Stream Cipher|
    |Features|Encryption, AEAD|
    |Private Key Size|256 Bits (32 Bytes)|
    |First Published|2008|

## ChaCha in Practice

In practice, ChaCha is mostly used as the ChaCha20-Poly1305 variant, which is also recommended. The Private Key is always 256 Bits (32 Bytes). There are variations that trade security for speed by reducing the number of internal computation rounds: ChaCha12 and ChaCha8. We will not go into detail on these variants, because they are seldomly used.

## ChaCha Key Generation

{{ key_generation_snippet('ChaCha') }}

## How to use passwords to encrypt/decrypt with ChaCha

{{ password_keygen_snippet('ChaCha', '256 Bits, which are 32 Bytes') }}

TODO: See the [code sample below](/algorithms/chacha/#key-derivation-from-passwords).

[^1]: TODO: Find a reference that recognizes ChaCha20-Poly1305 as secure
