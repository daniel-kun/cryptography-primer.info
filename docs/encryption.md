---
hide:
  - navigation
---

# Encryption

## Overview and Comparison

On this page, you will learn what...

- [__Symmetric Encryption__](#symmetric) (also known as __Private Key Encryption__),
- [__Asymmetric Encryption__](#asymmetric) (also known as __Public Key Encryption__),
- [__Authenticated Encryption__](#ae) (AE)
- [__Authenticated Encryption with Associated Data__](#aead) (AEAD)

... are and where to learn more about the different algorithms that implement these.

--8<-- "includes/encryption_comparison.md"

## What is Encryption?

With "encryption" we mean a way to alter a given "plaintext" (although this often is not only text, but can be arbitrary data, such as files or a byte stream) to make it incomprehensible without knowing some kind of "secret". Encryption reaches one of the fundamental goals of cryptography: __Confidentiality__.

Modern encryption schemes - and only those are recommended on this site - also provide __Authenticity__, which guarantees that the ciphertext and therefore the plaintext have not been altered without knowing the secret key. This is a very important attribute of an encryption scheme, because modifying the ciphertext can be a powerful attack vector.

There are two fundamentally different approaches to encryption. One is called "Symmetric Encryption" (also known as Private Key Encryption) and the other is called "Asymmetric Encryption" (also known as Public Key Encryption).

### <a name="symmetric"></a>What is Symmetric Encryption?

(Also known as Private Key Encryption)

In Symmetric Encryption, the "secret" that is used to make the "plaintext" incomprehensible (this incomprehensible form is called "ciphertext") is the same as the secret that is used to decrypt the ciphertext back into plaintext. This means that the sender and the recipient of the ciphertext need to know exactly the same secret. This secret is called the "Private Key". It is "private", because it must only be known to the peers that are allowed to know the plaintext.

The advantage of symmetric encryption is it's speed, because it only requires relatively easy calculations.

The biggest downside of symmetric encryption is that the private key needs to be shared between the sender and the recipient. This yields the problem that somehow this secret private key must be exchanged before the ciperhtext can be decrypted. This in itself can be a problem, especially when communication takes place over a public medium such as the internet or via radio frequencies.

This narrows the use case of Symmetric Encryption to situations where this secret can be securely shared between the sender and the receipient. These are some common ways to exchange the secret key:

- Pre-sharing the key over a secured medium - e.g. separately writing the key to the system that encrypts, and the system that decrypts the data
- Key exchange algorithms such as Diffie-Hellman (DH) and Elliptic Curve Diffie-Hellman (ECDH)
- Encrypting the secret key alongside the ciphertext using an asymmetric encryption scheme

Popular Symmetric Encryption algorithms are AES, ChaCha20, 3DES and DES. While AES and ChaCha20 are state-of-the-art secure, you should not use DES or 3DES anymore, because they have been provem to be breakable.

### <a name="asymmetric"></a>What is Asymmetric Encryption?

(Also known as Public Key Encryption)

Asymmetric Encryption does not pose the problem that a secret must be shared between the sender and the receipient, because encryption takes place with a Public Key and decryption can be done with a Private Key.[^1]. The Public Key - as the name suggests - can be shared freely and must not be transmitted securely. You can post it on the internet and it will not be a problem, because you can not decrypt ciphertext with the Public Key that was encrypted using the Public Key. Hence, when a sender wants to send a message securely to a receipient, it must know the receipient's Public Key, can encrypt a message using the Public Key, and the receipient c
an decrypt it using it's Private Key.

So the advantage of Asymmetric Encryption is that it is not required for a secret to be shared between the sender and the receipient, and hence no secure channel must be established before an encrypted message can be exchanged.

But the disadvantage of asymmetric encryption is that it is compute intensive, and hence can not be used where scale or speed is of importance.

To mitigate this main disadvantage, Asymmetric Encryption is usually combined with Symmetric Encryption in a way that the shared secret (Private Key) for the Symmetric Encryption will be encrypted using Asymmetric Encryption and the actual message is then encrypted using the shared secret and a Symmetric Encryption algorithm. This way, only a tiny bit of the transported data - the shared secret (Private Key of the Symmetric Encryption) - must be encrypted using the compute-expensive Asymmetric Encryption algorithm, and the main content of the transported data can be encrypted using the fast Symmetric Encryption.

Popular Asymmetric Encryption algorithms are RSA and Elliptic Curves, but they are seldomely used alone for encryption.

### <a name="ae"></a>What is Authenticated Encryption (AE)?

Encryption does not guarantee that the sender of a ciphertext knows the Private Key. Of course you need a Private Key to construct a plausible ciphertext, but you can also modify a ciphertext - or completely guess a ciphertext from scratch - without knowing the Private Key as an attacker. This is called CCA and usually poses a problem to an encryption system, because it can help to break the security.

Authenticated Encryption can be used to mitigate this risk, because it can __authenticate__ the ciphertext and/or plaintext to be assembled by a sender that knows the Private Key. The decryption algorithm will not only decrypt the message, but also check a MAC against the message and only continue decryption if the MAC is constructed correctly.

It is strongly advised to only use Authenticated Encryption. When Authenticated Encryption is not feasible, it is strongly advised to separately authenticate the ciphertext using Encrypt-then-MAC[^2].

A popular and very secure cipher that supports authenticated encryption is ChaCha20-Poly1305.

### <a name="aead"></a>What is Authenticated Encryption with Associated Data (AEAD)?

AEAD is an extension of AE that allows sending plaintext data alongside the ciphertext that can be read - and later authenticated by the recipient without previously knowing the private key.

One exampe could be that the associated data contains an identifier that the recipient can use to look up the private key that is required the decrypt and authenticate the message.

A popular and very secure cipher that supports AEAD is [AES-GCM](/algorithms/aes/).
...

--8<-- "includes/abbrevations.md"

[^1]: Or the other way around: It's also possible to encrypt using the Private Key and decrypt using the Public Key - although this often does not make too much sense, because the Public Key could be available to anybody
[^2]: [All the crypto code you’ve ever written is probably broken](https://tonyarcieri.com/all-the-crypto-code-youve-ever-written-is-probably-broken) as blogged by Tony Arcieri.