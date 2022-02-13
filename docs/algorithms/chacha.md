---
hide:
  - navigation
---

# ChaCha

!!! success "This algorithm is recommended"

    Use ChaCha in it's XChaCha20-Poly1305 or ChaCha20-Poly1305 variations.

    XChaCha20-Poly1305 and ChaCha20-Poly1305 are considered __secure__[^1] and fast. It has a strong security level and provides authentication (AEAD).

    It is arguably easier to use than [AES](/algorithms/aes/), because it has less (insecure) variations and modes of operation. However, when using AES as AES-256-GCM, the differences in security to ChaCha20-Poly1305 are negligible. Note that AES is only fast to use when hardware acceleration is available - while this is very common nowadays, it might be a constraint to consider. ChaCha can be implemented very fast in software only and does not require special CPU instructions.

--8<-- "includes/disclaimer.md"

On this page you will learn:

* What is ChaCha, and features does it provide?
* How secure is ChaCha?
* What can I use instead of ChaCha?
* What modes of operation can I use with ChaCha?

!!! info "Quick Info"

    |ChaCha| |
    |----|-|
    |Names|ChaCha (with various additions, see below)|
    |Attributes|Symmetric (Private Key), Stream Cipher|
    |Features|Encryption, AEAD|
    |Private Key Size|256 Bits (32 Bytes)|
    |First Published|2008|
    |Designers|D. J. Bernstein|

## ChaCha in Practice

In practice, ChaCha is mostly used as the ChaCha20-Poly1305 variant, which is also recommended. The Private Key is always 256 Bits (32 Bytes). There are variations that trade security for speed by reducing the number of internal computation rounds: ChaCha12 and ChaCha8. We will not go into detail on these variants, because they are seldomly used.

## ChaCha Key Generation

{{ key_generation_snippet('ChaCha') }}

## How to use passwords to encrypt/decrypt with ChaCha

{{ password_keygen_snippet('ChaCha', '256 Bits, which are 32 Bytes') }}

TODO: See the [code sample below](/algorithms/chacha/#key-derivation-from-passwords).

## Modes of operation

ChaCha is a Stream Cipher, which means that it can encode arbitrary length of data - in contrast to Block Ciphers, which need "modes of operation" that help concatenate and pad data so that it fits into multiple of the Block Cipher's block size.

So ChaCha can be used "raw" as it is, in theory. But in practice, you should use ChaCha together with a MAC to achieve AEAD to make the cipher resitant to CCA. By far the most common MAC used with ChaCha is Poly1305, which makes __ChaCha20-Poly1305__ the most common incarnation of ChaCha nowadays.

|Cipher|Description|
|------|-----------|
|XChaCha20-Poly1305|<div class="admonition success"><p class="admonition-title">Recommended</p><p>This is basically the same as ChaCha20-Poly1305, but uses a larger nonce of 192 Bit (24 Bytes). Because nonce-reuse[^7] is the point of an implementation that can go wrong easiest, XChaCha20-Poly1305 offers more "ease of implementation", because it makes it practically feasible to use random numbers as nonces easily. Other than that, the security attributes are equal to ChaCha20-Poly1305</p></div>|
|ChaCha20-Poly1305|<div class="admonition success"><p class="admonition-title">Recommended if you can't use XChaCha20-Poly1305</p><p>ChaCha20-Poly1305 is a very common Stream Cipher that is considered secure. It is widely deployed, studied and very fast. Because it uses a smaller nonce than XChaCha20-Poly1305, the dangers of accidental nonce-reuse[^7] is higher, which makes it a bit more error prone. Other than that, the security attributes are equal to XChaCha20-Poly1305.</p></div>|
|ChaCha20|<div class="admonition info"><p class="admonition-title">Use ChaCha20-Poly1305 instead</p><p>Raw ChaCha20 without authentication is not recommended, because there is usually no reason not to use ChaCha20-Poly1305 instead.</p>|
|ChaCha12|<div class="admonition warning"><p class="admonition-title">Use only combined with authentication</p><p>While the reduction of the rounds might not impose practically weaker security[^5], there is no common or standardized cipher that uses ChaCha12 with authentication, which is why you should use XChaCha20-Poly1305 or ChaCha20-Poly1305 instead, if feasible. If you require the higher throughput/faster speed that ChaCha12 provides, you need to apply Encrypt-then-MAC[^6]<p></div>|
|ChaCha8|<div class="admonition warning"><p class="admonition-title">Use only combined with authentication</p><p>While the reduction of the rounds might not impose practically weaker security[^5], there is no common or standardized cipher that uses ChaCha8 with authentication, which is why you should use XChaCha20-Poly1305 or ChaCha20-Poly1305 instead, if feasible. If you require the higher throughput/faster speed that ChaCha8 provides, you need to apply Encrypt-then-MAC[^6]<p></div>|

## Security Recommendations

<table>
    <thead>
        <tr>
            <th>Recommended</th>
            <th>Discouraged</th>
        </tr>
    </thead>
    <tbody>
        <tr>
<td>
<ul class="recommendations">
    <li>Use ChaCha20-Poly1305.</li>
    <li>Use a key derivation function such as <a href="algorithms/pbkdf2.md">PBKDF2</a> to convert a password into an ChaCha-compatible key.</li>
    <li>When you need asymmetric encryption (e.g. sender and receiver can not share a password and can not use a key exchange algorithm), use ChaCha20 together with RSA and encrypt the ChaCha-key using the RSA public key.<b>TODO: Create a page with detailed instructions</b></li>
</ul>
</td>
<td>
<ul class="discouragements">
    <li>It is very important that you don't use the same nonce multiple times with the same key.</li>
    <li>Don't use raw ChaCha ciphers (e.g. without Poly1305). <a href="https://tonyarcieri.com/all-the-crypto-code-youve-ever-written-is-probably-broken">(detailed explanation on Tony Arcieri's blog)</a></li>
    <li>Don't trust your crypto library's defaults - check that you are not accidentally use a discouraged practice, because your library has bad defaults.</li>
    <li>Don't transmit the key between two parties. Either pre-share the key over a secure medium, use a key exchange algorithm (such as DH or ECDH) or an asymmetric encryption algorithm (such as RSA) for this.</li>
</ul>
</td>
        </tr>
    </tbody>
</table>

## Code Samples

### ChaCha key generation

This code sample shows how to securely generate a new ChaCha key:

!!! warning 

    Do not use your regular "random" function for key generation,
    but use your crypto library's dedicated functions for this.

=== "Python"

    !!! info

        This code sample requires the widely used [`pyca/cryptography`](https://pypi.org/project/cryptography/) package.

        Install it with `pip install cryptography` or your favorite package manager.

    ``` py
    from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305

    # Generate a random 256 Bit private key:
    key = ChaCha20Poly1305.generate_key()
    print(key.hex())
    ```

=== "Java"

    ``` java
    // TODO
    ```

=== "JavaScript"

    ``` javascript
    // TODO
    ```


### Key derivation from passwords

This code sample show how to securely derive an encryption key from a password:

=== "Python"

--8<-- "includes/password_keygen_code_snippet_python.md"

    # `key` can now be used with ChaCha20-Poly1305
    ```

=== "Java"

    ``` java
    // TODO
    ```

=== "JavaScript"

    ``` javascript
    // TODO
    ```


### ChaCha20-Poly1305 encryption and decryption

Here's a code sample on a simple use case to encrypt and decrypt data:

=== "Python"

    !!! info

        This code sample requires the widely used [`pyca/cryptography`](https://pypi.org/project/cryptography/) package.

        Install it with `pip install cryptography` or your favorite package manager.

    ``` py
    import os
    from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305

    # The text to be encrypted:
    plaintext = b"I am secret"

    # Can be None, when no associated data is required:
    authenticated_text= b"authenticated but unencrypted data"

    # Generate a random private key for this example:
    key = ChaCha20Poly1305.generate_key()

    # Create an object that can encrypt/decrypt with the ChaCha20-Poly1305 AEAD cipher:
    chacha = ChaCha20Poly1305(key)

    # Generate a "nonce" for this encryption session of size 96 Bits (12 Bytes).
    # A nonce ensures that the same plaintext is not encrypted to the same ciphertext, which strenghtens security:

    nonce = os.urandom(12)
    # Notice: NEVER re-use the same nonce with the same key. Using a counter - if feasible - is an appropriate
    # way to prevent this. Using a random number might have a realistic chance of reuse,
    # depending on the number of messages that are being encrypted, the implementation of the random number generator
    # and the available entropy in the system.

    # Encrypt the data and add the authenticated (but not encrypted) data:
    ciphertext = chacha.encrypt(nonce, plaintext, authenticated_text)

    # The content of "ciphertext" can now be shared via an untrusted medium.
    # The receiver also needs to know the "nonce" and the authenticated text (when used),
    # which can also be shared via an untrusted medium.

    # Decrypt the ciphertext back into the plaintext:
    plaintxt = chacha.decrypt(nonce, ciphertext, authenticated_text)

    print(plaintext)

    # Result: "I am secret"
    ```

=== "Java"

    ``` java
    // TODO
    ```

=== "JavaScript"

    ``` javascript
    // TODO
    ```

## Security Level

--8<-- "includes/security_level_explained.md"

In 2022, ChaCha20 is considered to have a full security level of 256 Bits, which is it's original Key Size. To quote the report[^3] "Security Analysis of ChaCha20-Poly1305 AEAD" from KDDI Research:

!!! quote

    Therefore, we conclude that we cannot find any weaknesses in ChaCha20-Poly1305 AEAD.

--8<-- "includes/broken.md"

|Variation|Security Level|Considered Secure?|
|------------|--------------|:----------------:|
|ChaCha20|256 Bits| :fontawesome-solid-check-circle: |
|ChaCha12|256 Bits| :fontawesome-solid-check-circle: |
|ChaCha8|256 Bits| :fontawesome-solid-check-circle: |

The smaller variants of ChaCha, namely ChaCha12 and ChaCha8 might have weaker security than ChaCha20, but no practical attacks[^5] are known, yet. Even the smallest round variant, ChaCha8, is considered secure. The safest that cryptanalysis got in 2022 is reducing the Security Level of a reduced variant of ChaCha with 7 rounds, which you will not find implemented in your crypto library, to (maybe, this is a bit unclear) 237.7 Bits[^2].

## Alternatives

Other Symmetric Encryption algorithms are:

--8<-- "includes/encryption_comparison.md"

## History

|Year|Event|
|----|-----|
|2008|First published by D. J. Bernstein[^4]|

## References

[^1]: TODO: Find a reference that recognizes ChaCha20-Poly1305 as secure
[^2]: [Analysis of Salsa, ChaCha, and Rumba](https://eprint.iacr.org/2007/472.pdf) by Jean-Philippe Aumasson, Simon Fischer, Shahram Khazaei, Willi Meier, and Christian Rechberger on eprint.iacr.org
[^3]: [Security Analysis of ChaCha20-Poly1305 AEAD](https://www.cryptrec.go.jp/exreport/cryptrec-ex-2601-2016.pdf) by KDDI Research, Inc. on cryptrec.go.jp
[^4]: [The ChaCha family of stream ciphers](https://cr.yp.to/chacha.html) by D. J. Bernstein on cr.yp.to
[^5]: [Too Much Crypto](https://eprint.iacr.org/2019/1492.pdf) by Jean-Philippe Aumasson on eprint.iacr.org
[^6]: [Should we MAC-then-encrypt or encrypt-then-MAC?](https://crypto.stackexchange.com/questions/202/should-we-mac-then-encrypt-or-encrypt-then-mac)
[^7]: [Nonce reuse in encryption - what’s the worst that can happen?](https://github.com/christianlundkvist/blog/blob/master/2021_01_25_nonce_reuse_in_encryption/nonce_reuse_in_encryption.md) by Christian Lundkvist on github.com

--8<-- "includes/abbrevations.md"
