---
hide:
  - navigation
---

# Encryption

## Overview and Comparison

On this page, you will learn about what Symmetric Encryption (also known as Private Key Encryption), Asymmetric Encryption (also known as Public Key Encryption) and Authenticated Encryption with Associated Data is and where to learn more about the different algorithms that implement these.

--8<-- "includes/encryption_comparison.md"

## What is Encryption?

With "encryption" we mean a way to alter a given "plaintext" (although this often is not only text, but can be arbitrary data, such as files or a byte stream) to make it incomprehensible without knowing some kind of "secret". Encryption reaches one of the fundamental goals of cryptography: Confidentiality.

(__Info__: With the help of the right mode, even Authenticity and Integrity can be added. See each encryption algorithm for the available modes.)

There are two fundamentally different approaches to encryption. One is called "Symmetric Encryption" (also known as Private Key Encryption) and the other is called "Asymmetric Encryption" (also known as Public Key Encryption).

Both approaches can be combined with different "modes" to reach different levels of security. Some modes even add a new fundamental goal: Authentication. Cipher suites with these modes are called "AEAD" (Authenticated Encryption with Associated Data) and makes it possible to verify the sender of the ciphertext, in addition to make the ciphertext readable without knowledge of the secret (Private Key).

### What is Symmetric Encryption?

(Also known as Private Key Encryption)

In Symmetric Encryption, the "secret" that is used to make the "plaintext" incomprehensible (this form is called the "ciphertext") is the same as the secret that is used to decrypt the ciphertext back into plaintext. This means that the sender and the recepient of the ciphertext need to know exactly the same secret. This secret is called the "Private Key". It is "private", because it must only be known to the peers that are allowed to know the plaintext.

The advantage of symmetric encryption is it's speed, because it only requires relatively easy calculations.

The biggest downside of symmetric encryption is that the private key needs to be shared between the sender and the recepient. This yields the problem that somehow this secret private key must be exchanged before the ciperhtext can be decrypted. This in itself can be a problem, especially when communication takes place over a public medium such as the internet or via radio frequencies.

This narrows the use case of Symmetric Encryption to situations where this secret can be securely shared between the sender and the receipient.

Populare Symmetric Encryption algorithms are DES, 3DES and AES. While AES is state-of-the-art secure, you should not use DES or 3DES anymore, because they have been provem to be breakable.

### What is Asymmetric Encryption?

(Also known as Public Key Encryption)

Asymmetric Encryption does not have the problem that a secret must be shared between the sender and the receipient, because encryption takes place with a Public Key and decryption can be done with a Private Key. Or the other way around: It's also possible to encrypt using the Private Key and decrypt using the Public Key - although this often does not make too much sense, because the Public Key could be available to anybody. The Public Key - as the name suggests - can be shared freely and must not be transmitted securely. You can post it on the internet and it will not be a problem, because you can not decrypt ciphertext with the Public Key that was encrypted using the Public Key. Hence, when a sender wants to send a message securely to a receipient, it must know the receipient's Public Key, can encrypt a message using the Public Key, and the receipient c
an decrypt it using it's Private Key.

The advantage of Asymmetric Encryption is that it is not required for a secret to be shared between the sender and the receipient, and hence no secure channel must be established before an encrypted message can be exchanged.

The disadvantage of asymmetric encryption is that it is compute intensive, and hence can not be used where scale or speed is of importance.

To mitigate this main disadvantage, Asymmetric Encryption is usually combined with Symmetric Encryption in a way that the shared secret (Privat Key) for the Symmetric Encryption will be encrypted using Asymmetric Encryption and the actual message is then encrypted using the shared secret and a Symmetric Encryption algorithm. This way, only a tiny bit of the transported data - the shared secret (Private Key of the Symmetric Encryption) - must be encrypted using the compute-expensive Asymmetric Encryption algorithm, and the main content of the transported data can be encrypted using the fast Symmetric Encryption.

Populare Asymmetric Encryption algorithms are TLS and Elliptic Curves, but they are seldomely used alone.

### What is Authenticated Encryption with Associated Data (AEAD)?

...

--8<-- "includes/abbrevations.md"