---
hide:
  - navigation
---

# AES (Advanced Encryption Standard)

!!! success "This algorithm is recommended"

    AES is considered __secure__[^1]. Use AES with 128, 192 or 256 (pick the largest size feasible for your system) with GCM mode of operation.
    GCM provides authentication, which makes this an AEAD cipher.

On this page you will learn:

* What is AES, and features does it provide?
* How secure is AES?
* What can I use instead of AES?
* What modes of operation can I use with AES?
* Where and how is AES being used?

!!! info "Quick Info"

    |Advanced Encryption Standard| |
    |----|-|
    |Names|AES, Advanced Encryption Standard, Rijndael|
    |Attributes|Symmetric (Private Key), Block Cipher|
    |Features|Encryption, AEAD|
    |Block Size|128 Bits (16 Bytes)|
    |Private Key Sizes|128, 192, 256|
    |First Published|1998|
    |Broken by|✅ *Not broken, yet*|

## AES in Practice

!!! hint inline end 

    The key sizes 192 and 256 do not change the block size. The block size is always 128 Bits, even when larger keys are being used.

AES comes in multiple forms: AES-128, AES-192, AES-256. The number specifies the size of the private key that is being used. The higher the number, the higher the security (but also the slower the encryption and decryption speed). Even the smallest 128 Bit (16 Bytes) key size is currently considered secure[^1] and safe to use mid-term. With AES-256 you can even achieve quantum resistance from the current state of research (Januar 2022)[^2][^9].

## How to use passwords to encrypt/decrypt with AES

Usually you use AES in a manner that the key is derived from the password that a user has to enter to encrypt/decrypt the data. Because the key is of fixed length (either 128, 192 or 256 Bits - which are 16, 24 or 32 Bytes, respectively), you can not use the password as the key directly, because that would impose insecure and inpractical constraints on the password that the user has to choose.

Instead, a key derivation function is used to create an AES-compatible key from a password. [PBKDF2](algorithms/pbkdf2.md) (Password Based Key Derivation Function 2) is a state of the art key derivation function.

See the [code sample below](/algorithms/aes/#key-derivation-from-passwords).

## Modes of operation

!!! hint inline end "IV vs. nonce?"

    *Initialization Vector*

    The IV needs to be random (generated with a CSPRNG, as you can find in your crypto library).
    __You must generate a new IV for each encrypted message.__

    *Nonce*

    "Nonce" means "Number only used once". While this is true for an IV, a nonce does not have the requirement to be random. You can safely
    use a steadily increasing number (a counter) as your nonce - __as long as you don't re-use the same nonce for the same key multiple times__.

AES is a block-cipher, which means that it can only encrypt data with the exact block size of 128 Bits (16 Bytes). This means that it must be combined with a so-called "Mode of operation" in order to be able to encrypt arbitrary number of bytes. 

There are modes that add authentication to the encryption, and there are modes that do not include authentication. You must absolutely authenticate your encrypted data, because this protects against CCA[^4]. The easiest and safest choice is to use an authenticated mode of operation. Alternatively, you can implement Encryt-then-MAC[^6] yourself, but this can easily be done incorrectly.

__We recommend "GCM" (Galois/Counter Mode).__

!!! info "How to pick a mode of operation"

    You can decide your mode of operation using these few rules of thumb:

    1. If your platform provides GCM, then use GCM.
    1. If your platform does not provide GCM, use CCM, EAX or OCB modes (preference in this order, consider that OCB might require a license[^7]).
    1. If your platform does not provide GCM, CCM, EAX or OCB, use CTR or CFB (preference in this order) and apply Encrypt-then-MAC[^6].
    1. If your platform does not provide CTR or CFB, reconsider your platform.
    1. If you can not use a platform that provides better modes, use anything *except* ECB, do your own research on the security of the chosen mode, and apply Encrypt-then-MAC[^6].

    __Never ever use ECB.__[^8]

## Modes with Authentication (AEAD)

|Mode of Operation|Full Name|Description|
|------|---------|-----------|
|GCM|Galois/Counter Mode|<div class="admonition success"><p class="admonition-title">This mode is recommended</p><p>The GCM mode uses a random initialization vector (IV) for better security. This means that the same encrypted plaintext does never result in the same ciphertext. The recommended length of the initialization vector is [96 Bit](https://csrc.nist.gov/publications/detail/sp/800-38d/final) (12 Bytes).</p></div>|
|CCM|Counter with CBC-MAC|<div class="admonition info"><p class="admonition-title">Considered secure</p><p>This mode is considered secure and you can safely use it. It is somewhat slower than GCM, though.</p></div>|
|EAX|<i>unknown</i>|<div class="admonition info"><p class="admonition-title">Not widely used</p><p>This mode is not widely used and hence not widely studied, so it is unsure how secure it is. While it is rather easy to implement, it is also slower than other modes.</p></div>|
|OCB|Offset Codebook Mode|<div class="admonition info"><p class="admonition-title">This mode is patented</p><p>The OCB mode is very, very fast and considered secure. However, it is patented in the U.S. It is free to use in open source software. If you want to use it in a commercial product, you would need to require a license[^7] or permission to use</a>.</p></div>|

## Modes without Authentication

!!! warning

    You should only use modes without authentication when you have reasons to not use a mode with authentication (listed above).

    Unauthenticated modes are vulnerable to CCA (Chosen Ciphertext Attack), which authenticated modes are not.

|Mode of Operation|Full Name|Description|
|------|---------|-----------|
|CTR|Counter Mode|<div class="admonition info"><p class="admonition-title">Use GCM or CCM instead, if possible</p><p>Because this mode does not provide authentication, it is not recommended. However, of all the unauthenticated modes, it is the one with the strongest safety attributes and that is the least easy one to implement incorrectly. If taken care[^5], the IV can be a nonce and does not need to be produced by an CSPRNG, which could be an advantage. Can be parallelized.</p><p><b>You must apply Encrypt-then-MAC[^6] manually when using an unauthenticated mode</b></p></div>|
|CFB|Cipher Feedback|<div class="admonition info"><p class="admonition-title">Use GCM, CCM or CTR instead, if possible</p><p>This mode is pretty similar to CBC, but chains the blocks in a different way. It is also always used with an Initialization Vector, and the IV is required to be produced by a CSPRNG.</p><p><b>You must apply Encrypt-then-MAC[^6] manually when using an unauthenticated mode.</b></p></div>|
|CTS|Ciphertext Stealing|<div class="admonition failure"><p class="admonition-title">Not recommended</p><p>Ciphertext stealing is a variation of ECB or CBC, but is in practice only used like CBC. The difference is that the last two blocks are chained differently. The security is not notably different from CBC.</p></div>|
|CBC|Cipher Block Chaining|<div class="admonition failure"><p class="admonition-title">Not recommended</p><p>This mode requires padding, which makes it vulnerable to padding oracle attacks.</p></div>|
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
    <li>Use a mode that supports authentication (AEAD): GCM is recommended (see above).</li>
    <li>Use a key derivation function such as <a href="algorithms/pbkdf2.md">PBKDF2</a> to convert a password into an AES-compatible key.</li>
    <li>When you need asymmetric encryption (e.g. sender and receiver can not share a password and can not use a key exchange algorithm), use AES together with RSA and encrypt the AES-key using the RSA public key.<b>TODO: Create a page with detailed instructions</b></li>
</ul>
</td>
<td>
<ul class="discouragements">
    <li>Don't use the same `nonce` or `initializatoin vector` multiple times with the same key.</li>
    <li>Don't use a mode without authentication. <a href="https://tonyarcieri.com/all-the-crypto-code-youve-ever-written-is-probably-broken">(detailed explanation on Tony Arcieri's blog)</a></li>
    <li>Don't trust your crypto library's defaults - check that you are not accidentally use a discouraged practice, because your library has bad defaults.</li>
    <li>Don't transmit the key between two parties. Either pre-share the key over a secure medium, use a key exchange algorithm (such as DH or ECDH) or an asymmetric encryption algorithm (such as RSA) for this.</li>
</ul>
</td>
        </tr>
    </tbody>
</table>

## Code Samples

### Key derivation from passwords

This code sample show how to securely derive an encryption key from a password:

=== "Python"

    !!! info

        This code sample requires the widely used [`pyca/cryptography`](https://pypi.org/project/cryptography/) package.

        Install it with `pip install cryptography` or your favorite package manager.

    ``` py
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

    # Salts should be randomly generated and need to be accessible
    # whenever a key is derived from a password. So basically,
    # the salt is usually stored/transmitted alongside the encrypted data.

    salt = bytes.fromhex('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa') # EXAMPLE VALUE - DO NOT USE THIS!

    # derive
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32, # 32 Bytes = 256 Bits
        salt=salt,
        iterations=100000, # This should be the minimum. You can increase the iterations if your system can handle it
                           # to strengthen security.
    )
    key = kdf.derive(b"my great password")
    print(key.hex())

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
    # This ensures that the same plaintext is not encrypted to the same ciphertext.
    # This strengthens security:
    nonce = os.urandom(12)
    # Notice: NEVER re-use the same nonce with the same key.

    # Encrypt the data and add the authenticated (but not encrypted) data:
    ciphertext = aesgcm.encrypt(nonce, plaintext, authenticated_text)

    # The content of "ciphertext" can now be shared via an untrusted medium.
    # The receiver also needs to know the "nonce" and the authenticated text (when used).

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

--8<-- "includes/abbrevations.md"
