---
hide:
  - navigation
---

# AES (Advanced Encryption Standard)

!!! success "This algorithm is recommended"

    AES is considered __secure__[^1]. Use AES with 128, 192 or 256 (pick the largest size feasible for your system) with GCM mode of operation.
    GCM provides authentication, which makes this an AEAD cipher.

    A very good and fast alternative is [ChaCha](/algorithms/chacha/), which comes in less variations and there are fewer things
    that can be done wrong when implementing it. Also, ChaCha might be faster on certain hardware that does not provide AES hardware-acceleration (which most common chipsets, even embedded ones, provide).

--8<-- "includes/disclaimer.md"

On this page you will learn:

* What is AES, and features does it provide?
* How secure is AES?
* What can I use instead of AES?
* What modes of operation can I use with AES?

!!! info "Quick Info"

    |Advanced Encryption Standard| |
    |----|-|
    |Names|AES, Advanced Encryption Standard, Rijndael|
    |Attributes|Symmetric (Private Key), Block Cipher|
    |Features|Encryption, AEAD|
    |Block Size|128 Bits (16 Bytes)|
    |Private Key Sizes|128, 192, 256|
    |First Published|1998|
    |Designers|Joan Daemen, Vincent Rijmen|

## AES in Practice

!!! hint inline end 

    The key sizes 192 and 256 do not change the block size. The block size is always 128 Bits, even when larger keys are being used.

AES comes in multiple forms: AES-128, AES-192, AES-256. The number specifies the size of the private key that is being used. The higher the number, the higher the security (but also the slower the encryption and decryption speed). Even the smallest 128 Bit (16 Bytes) key size is currently considered secure[^1] and safe to use mid-term. With AES-256 you can even achieve quantum resistance from the current state of research (Januar 2022)[^2][^9].

## AES Key Generation

Private keys for AES do not have to follow a specific form - they just need to be (crypto-secure) random bits of the required size. Other algorithms, such as RSA or EC, require the values to conform to some mathematical requirements, but AES keys do not.

{{ key_generation_snippet('AES') }}

## How to use passwords to encrypt/decrypt with AES

{{ password_keygen_snippet('AES', 'either 128, 192 or 256 Bits - which are 16, 24 or 32 Bytes, respectively') }}

See the [code sample below](/algorithms/aes/#key-derivation-from-passwords).

## Modes of operation

AES is a block-cipher, which means that it can only encrypt data with the exact block size of 128 Bits (16 Bytes). This means that it must be combined with a so-called "Mode of operation" in order to be able to encrypt arbitrary number of bytes. 

There are modes that add authentication to the encryption, and there are modes that do not include authentication. You must absolutely authenticate your encrypted data, because this protects against CCA[^4]. The easiest and safest choice is to use an authenticated mode of operation. Alternatively, you can implement Encryt-then-MAC[^6] yourself, but this can easily be done incorrectly.

!!! success ""GCM" (Galois/Counter Mode) is highly recommended"

    GCM provides authentication, which prevents many different kinds of attacks, and is well studied and has proven to be very secure.

??? info "How to pick a mode if GCM is not available"

    You can decide your mode of operation using these few rules of thumb:

    1. If your platform provides GCM, then use GCM.
    1. If your platform does not provide GCM, use CCM, EAX or OCB modes (preference in this order, consider that OCB might require a license[^7]).
    1. If your platform does not provide GCM, CCM, EAX or OCB, use CTR or CFB (preference in this order) and apply Encrypt-then-MAC[^6].
    1. If your platform also does not provide CTR or CFB, reconsider your platform.
    1. If you can not use a platform that provides better modes, use anything *except* ECB, do your own research on the security of the chosen mode, and apply Encrypt-then-MAC[^6].

    __Never ever use ECB.__[^8]

??? hint "IV vs. nonce?"

    Neither an IV (initialization vector) nor a nonce are secret and are usually sent alongside the ciphertext.

    __What is an "*Initialization Vector*"?__

    The IV needs to be random (generated with a CSPRNG, as you can find in your crypto library).
    __You must generate a new IV for each encrypted message.__

    __What is a "*Nonce*"?__

    "Nonce" means "Number only used once". While this is also true for an IV, a nonce does not have the requirement to be random. You can safely
    use a steadily increasing number (a counter) as your nonce, but you must not re-use the same number for different encryptions.
    __You must generate a new nonce for each encrypted message.__

## Modes with Authentication (AEAD)

|Mode of Operation|Full Name|Description|
|------|---------|-----------|
|GCM|Galois/Counter Mode|<div class="admonition success"><p class="admonition-title">This mode is recommended</p><p>The GCM mode uses a random initialization vector (IV) for better security. This means that the same encrypted plaintext does never result in the same ciphertext. See [implementation notes for GCM](#implementation-notes-for-gcm).</p></div>|
|CCM|Counter with CBC-MAC|<div class="admonition info"><p class="admonition-title">Considered secure</p><p>This mode is considered secure and you can safely use it. It is somewhat slower than GCM, though.</p></div>|
|EAX|<i>unknown</i>|<div class="admonition info"><p class="admonition-title">Not widely used</p><p>This mode is not widely used and hence not widely studied, so it is unsure how secure it is. While it is rather easy to implement, it is also slower than other modes.</p></div>|
|OCB|Offset Codebook Mode|<div class="admonition info"><p class="admonition-title">This mode is patented</p><p>The OCB mode is very, very fast and considered secure. However, it is patented in the U.S. It is free to use in open source software. If you want to use it in a commercial product, you would need to require a license[^7] or permission to use</a>.</p></div>|

### Implementation notes for GCM

GCM is by far the recommended mode of operation for AES, because:

- It uses a nonce, which strengthens confidentiallity, because the same plaintext will not be encrypted to the same ciphertext.
- It provides AEAD, which prevents CCA.
- It is well supported. For example, it is used in the Web Crypto API[^16] and is mandatory in TLS 1.3[^17].
- It is fast (enough), even for high throughput demands.

However, it comes with one major caveat for implementers[^18]. It supports a nonce of 96 Bits (12 Bytes), which is, depending on the field of application, not enough to use a random value and feel safe enough that it will be unique. After 281,474,976,710,656 messages, you have a 50% chance of re-using a nonce. In practical terms, cryptographers recommend not more than 4,294,967,296 (4 billion) messages with the same key and a random nonce. The fatal thing about this is that a nonce-reuse makes it relatively easy to recover the key and break the security completely (for future __and__ potentially previous messages for this key).

So, if your field of application only encrypts a few thousands or hundred thousands of messages per key, and has a good CSPRNG, you should not face a problem here. For example, when used with TLS, which creates a new Private Key for each session, this is more than unlikely to occur. However, for e.g. password-based schemes, the same key will be used permanently, or at least for a very long time, which makes this more likely.

To prevent this problem that applies to usage of AES-GCM with long-term keys, it is recommended to either

- Implement a key rotation mechanism, if feasible. This minimizes other attack vectors, too, and might prevent the impact of a stolen or broken key.
- Implement a persistent storage and use a counter per Private Key as the nonce.
- Use AES-GCM-SIV[^19] instead, which uses larger nonces that are considered secure when generated at random.

## Modes without Authentication

!!! warning

    You should only use modes without authentication when you have reasons to not use a mode with authentication (listed above).

    Unauthenticated modes are vulnerable to CCA (Chosen Ciphertext Attack), which authenticated modes are not.

    __You must apply Encrypt-then-MAC[^6] manually__ in your encryption scheme to prevent CCA-attacks if you are forced to use an unauthenticated mode.

|Mode of Operation|Full Name|Description|
|------|---------|-----------|
|CTR|Counter Mode|<div class="admonition info"><p class="admonition-title">Use GCM or CCM instead, if possible</p><p>Because this mode does not provide authentication, it is not recommended. However, of all the unauthenticated modes, it is the one with the strongest safety attributes and that is the least easy one to implement incorrectly. If taken care[^5], the IV can be a nonce and does not need to be produced by a CSPRNG, which could be an advantage. Can be parallelized.</p><p><b>You must apply Encrypt-then-MAC[^6] manually when using an unauthenticated mode</b></p></div>|
|CFB|Cipher Feedback|<div class="admonition info"><p class="admonition-title">Use GCM, CCM or CTR instead, if possible</p><p>This mode is pretty similar to CBC, but chains the blocks in a different way. It is also always used with an Initialization Vector, and the IV is required to be produced by a CSPRNG.</p><p><b>You must apply Encrypt-then-MAC[^6] manually when using an unauthenticated mode.</b></p></div>|
|CTS|Ciphertext Stealing|<div class="admonition failure"><p class="admonition-title">Not recommended</p><p>Ciphertext stealing is a variation of ECB or CBC, but is in practice only used like CBC. The difference is that the last two blocks are chained differently. The security is not notably different from CBC.</p></div>|
|CBC|Cipher Block Chaining|<div class="admonition failure"><p class="admonition-title">Not recommended</p><p>This mode requires padding, which makes it vulnerable to padding oracle attacks[^12].</p></div>|
|ECB|Electronic Code Book|<div class="admonition failure"><p class="admonition-title">Do not ever use this<p><p>This method is *not recommended*, because it does not introduce diffusion into the ciphertext, which means that the same block is encrypted to the same ciphertext, effectively leaking patterns, which can easily be used to gain information that should be hidden.</p></div>|

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
    <li>Use the largest key size that your system can handle. You can still feel secure when using 128 Bits, though, but more is better.</li>
    <li>Use a mode that supports authentication (AE or AEAD): GCM is recommended (see above).</li>
    <li>Use a key derivation function such as <a href="algorithms/pbkdf2.md">PBKDF2</a> to convert a password into an AES-compatible key.</li>
    <li>When you need asymmetric encryption (e.g. sender and receiver can not share a password and can not use a key exchange algorithm), use AES together with RSA and encrypt the AES-key using the RSA public key.<b>TODO: Create a page with detailed instructions</b></li>
</ul>
</td>
<td>
<ul class="discouragements">
    <li>It is very important that you don't use the same `nonce` or `initialization vectiro` multiple times with the same key.</li>
    <li>Don't use a mode without authentication. <a href="https://tonyarcieri.com/all-the-crypto-code-youve-ever-written-is-probably-broken">(detailed explanation on Tony Arcieri's blog)</a></li>
    <li>Don't trust your crypto library's defaults - check that you are not accidentally use a discouraged practice, because your library has bad defaults.</li>
    <li>Don't transmit the key between two parties. Either pre-share the key over a secure medium, use a key exchange algorithm (such as DH or ECDH) or an asymmetric encryption algorithm (such as RSA) for this.</li>
</ul>
</td>
        </tr>
    </tbody>
</table>

## Code Samples

### AES key generation

This code sample shows how to securely generate a new AES key:

!!! warning 

    Do not use your regular "random" function for key generation,
    but use your crypto library's dedicated functions for this.

=== "Python"

    !!! info

        This code sample requires the widely used [`pyca/cryptography`](https://pypi.org/project/cryptography/) package.

        Install it with `pip install cryptography` or your favorite package manager.

    ``` py
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM

    # Generate a random 256 Bit private key:
    key = AESGCM.generate_key(bit_length=256)
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

    # `key` can now be used with AES-256.

    # When you use different key sizes (AES-128 or AES-192), you need to specify
    # the corresponding length. 128 Bits = 16 Bytes, 192 Bits = 24 Bytes.
    
    # Further processing can be done to use with AES-256-GCM (explanation and code samples coming soon...)
    ```

=== "Java"

    ``` java
    // TODO
    ```

=== "JavaScript"

    ``` javascript
    // TODO
    ```


### AES encryption and decryption

Here's a code sample on a simple use case to encrypt and decrypt data:

=== "Python"

    !!! info

        This code sample requires the widely used [`pyca/cryptography`](https://pypi.org/project/cryptography/) package.

        Install it with `pip install cryptography` or your favorite package manager.

    ``` py
    import os
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM

    # The text to be encrypted:
    plaintext = b"I am secret"

    # Can be None, when no associated data is required:
    authenticated_text= b"authenticated but unencrypted data"

    # Generate a random private key for this example:
    key = AESGCM.generate_key(bit_length=256)

    # Create an object that can encrypt/decrypt with the following cipher:
    # Algorithm: AES
    # Key Size: 256
    # Mode of Operation: GCM - an authenticated mode (see "AEAD")
    aesgcm = AESGCM(key)

    # Generate a "nonce" for this encryption session of size 96 Bits (12 Bytes).
    # A nonce ensures that the same plaintext is not encrypted to the same ciphertext, which strenghtens security:

    nonce = os.urandom(12)
    # Notice: NEVER re-use the same nonce with the same key. Using a counter - if feasible - is an appropriate
    # way to prevent this. Using a random number might have a realistic chance of reuse,
    # depending on the number of messages that are being encrypted, the implementation of the random number generator
    # and the available entropy in the system.

    # Encrypt the data and add the authenticated (but not encrypted) data:
    ciphertext = aesgcm.encrypt(nonce, plaintext, authenticated_text)

    # The content of "ciphertext" can now be shared via an untrusted medium.
    # The receiver also needs to know the "nonce" and the authenticated text (when used),
    # which can also be shared via an untrusted medium.

    # Decrypt the ciphertext back into the plaintext:
    plaintxt = aesgcm.decrypt(nonce, ciphertext, authenticated_text)

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

In 2022, AES is considered to have the following security levels:

--8<-- "includes/broken.md"

|Variation|Security Level|Considered Secure?|
|------------|--------------|:----------------:|
|AES-128|126.1 Bits| :fontawesome-solid-check-circle: |
|AES-192|189.7 Bits| :fontawesome-solid-check-circle: |
|AES-256|254.4 Bits| :fontawesome-solid-check-circle: |

The security level is lower than the raw key size, because there is an attack method that allows to lower the key space that is required to be searched in order to break an encryption. This attack is called the "Biclique attack"[^11].

## Alternatives

Other Symmetric Encryption algorithms are:

--8<-- "includes/encryption_comparison.md"

## History

|Year|Event|
|----|-----|
|1998|First published by Vincent Rijmen, Joan Daemen|
|2001|Standardized by the NIST as the Advanced Encryption Standard (AES)|
|2003|Endorsed by the U.S. Government to protect classified information|

## References

[^1]: [Is 128-bit security still considered strong in 2020, within the context of both ECC Asym & Sym ciphers](https://crypto.stackexchange.com/questions/77000/is-128-bit-security-still-considered-strong-in-2020-within-the-context-of-both) on crypto.stackexchange.com.
[^2]: [Is AES-256 a post-quantum secure cipher or not?](https://crypto.stackexchange.com/questions/6712/is-aes-256-a-post-quantum-secure-cipher-or-not) on crypto.stackexchange.com.
[^9]: [Post-quantum cryptography](https://en.wikipedia.org/wiki/Post-quantum_cryptography#Symmetric_key_quantum_resistance) on Wikipedia
[^3]: [Using Encryption and Authentication Correctly (for PHP developers)](https://paragonie.com/blog/2015/05/using-encryption-and-authentication-correctly)
[^4]: [All the crypto code you’ve ever written is probably broken](https://tonyarcieri.com/all-the-crypto-code-youve-ever-written-is-probably-broken) as blogged by Tony Arcieri.
[^5]: ["Counter (CTR)" at "Block cipher mode of operation"](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Counter_(CTR)) on Wikipedia
[^6]: [Should we MAC-then-encrypt or encrypt-then-MAC?](https://crypto.stackexchange.com/questions/202/should-we-mac-then-encrypt-or-encrypt-then-mac)
[^7]: [Free Licenses](https://www.cs.ucdavis.edu/~rogaway/ocb/license.htm) on www.cs.ucdavis.edu by Phillip Rogaway
[^8]: ["Electronic codebook (ECB)" at "Block cipher mode of operation"](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Electronic_codebook_(ECB)) on Wikipedia
[^10]: [BSI - Technical Guide - Cryptographic Mechanisms:
Recommendations and Key Lengths](https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Publications/TechGuidelines/TG02102/BSI-TR-02102-1.pdf?__blob=publicationFile) on bsi.bund.de
[^11]: [Biclique attack](https://en.wikipedia.org/wiki/Biclique_attack) on Wikipedia
[^12]: [Padding oracle attack](https://en.wikipedia.org/wiki/Padding_oracle_attack) on Wikipedia
[^13]: [Recommendation for Block Cipher Modes of Operation: Galois/Counter Mode (GCM) and GMAC](https://csrc.nist.gov/publications/detail/sp/800-38d/final) on csrc.nist.gov
[^14]: [Hardware Security Module](https://en.wikipedia.org/wiki/Hardware_security_module) on Wikipedia
[^15]: [Cryptographically-secure pseudorandom number generator](https://en.wikipedia.org/wiki/Cryptographically-secure_pseudorandom_number_generator) on Wikipedia
[^16]: [Web Crypto API's "SubtleCrypto.encrypt()"](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/encrypt) at MDN on developer.mozilla.org
[^17]: [RFC 8446: The Transport Layer Security (TLS) Protocol Version 1.3](https://datatracker.ietf.org/doc/html/rfc8446#section-9.1) on ietf.org
[^18]: [Why AES-GCM Sucks](https://soatok.blog/2020/05/13/why-aes-gcm-sucks/) on soatok.blog
[^19]: [RFC 8452: AES-GCM-SIV: Nonce Misuse-Resistant Authenticated Encryption](https://datatracker.ietf.org/doc/html/rfc8452) on ietf.org

--8<-- "includes/abbrevations.md"
