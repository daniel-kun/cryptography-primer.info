---
hide:
  - navigation
---

# What is the difference between Hashing, Signing and MAC?

Hashes, MACs and digital signatures are primitives of cryptography, where hashes are also used outside of cryptography - e.g. to validate that a message has not been corrupted during transport.

Hashes, MACs and digital signatures have a few things in common:

- They can be used to validate the "integrity" of a message - this means that you can be sure that the message is the same as the one providing you the hash, signature or MAC wanted to give you.
- The original message can not be extracted from them
- Hence, they __don't__ encrypt messages and are not encryption algorithms

Here is a table showing the differences of the possibilities for each primitive:

|Feature|Hash|Message Authentication Code (MAC)|Digital Signature|
|-------|:--:|:---------------:|:-:|
|Validate that data has not been tampered with or has been corrupted ("Integrity")|:fontawesome-solid-check-circle:|:fontawesome-solid-check-circle:|:fontawesome-solid-check-circle:|
|Validate the sender of a message by using the Private Key ("Authentication")|:fontawesome-solid-times:|:fontawesome-solid-check-circle:|:fontawesome-solid-check-circle:|
|Validate the sender of a message by using the Public Key ("Authentication")|:fontawesome-solid-times:|:fontawesome-solid-times:|:fontawesome-solid-check-circle:|
|Prove that the sender has written and published a message ("Non-Repudiation")|:fontawesome-solid-times:|:fontawesome-solid-times:|:fontawesome-solid-check-circle:|

## What are use-cases for hashes?

A hash basically "reduces" an arbitrary large message into a fixed size digest in a non-reversible way. In particular, a hash function aims to do this in a way that possible _collisions_ are as unlikely as possible. Nowadays, when you say "hash function", you usually mean cryptographic hash functions. There are non-cryptographic hash functions[^1], too (but some even refuse to call those hash functions): Most notably CRC[^2] (cyclic redundancy check), which is often used to verify that data has not been (unintentionally) corrupted during transport.

But even cryptographic hash functions can be used for non-cryptographic and also cryptographic use cases:

### Non-Cryptographic use-cases for hash functions

Here are some examples how hash functions are used in non-cryptographic context:

- Validate that a message has not been corrupted (or modified) during transport. For example, you can often find hashes next to a download link that can be used to validate that the file has exactly the same content as it supposed to have after you have downloaded it.
- "Shrink" information to a unique identifier that can be used for lookups. For example, you can look up a whole sentence or even a whole paragraph of text in a database by using it's hash, instead of comparing all characters of the paragraph in the database.

### Cryptographic use-cases for hash functions

Here are some examples how hash functions ar used in cryptograhpic context:

- Usually digital signatures are not applied to the whole message or data block, but on a hash digest of that message. In this scenario, the collision-resistance of the hash function is of utter importance[^3][^4].
- Store passwords (TODO: Add a dedicated chapter to this topic).
- Some MAC algorithms are based on hash functions - these are called "HMAC" (hash-based message authentication code) and basically build a hash on a mixup of the Private Key and the message.

## Comparison of hashing functions

--8<-- "includes/hashing_comparison.md"

## What are use-cases for digital signatures?

Digital signatures also provide the integrity validation function of hashes. But additionally, digital signatures let you verify that the sender of the message is authentic, e.g. the message originates from the source that you expected.

Because digital signatures are using "asymmetric cryptography", you can use the Public Key to validate the integrity and authenticity of the message. This has the advantage that you do not need to share a common Private Key between the sender and the recipient.

Use-cases for digital signatures:

- Publish a message and "sign" it so that everyone can verify that it has been written and published by you.
- For example, TLS (and therefore HTTPS, which builds on TLS) uses digital signatures to authenticate the server behind the domain that you have requested data from.
- The underlying building block for this are x.509 certificates that are also widely used in other systems where it is important to let anybody know that a "certificate", that provides arbitrary permissions or identifications, can be trusted.
- Mobile platforms such as Apple's iOS and Google's Android use digital signatures to sign apps in they App Store/Play Store so that the system is able to trust these apps (and in turn is able to block running untrusted apps).

## Comparison of digital signature algorithms

--8<-- "includes/signing_comparison.md"

## What are MACs used for?

!!! hint inline end

    You should usually not require to use MACs yourself, because these are often part of an "authenticated encryption" cipher such as [AES-GCM](/algorithms/aes/) or ChaCha20-Poly1305.

MACs are similar to digital signatures, but they do not have the advantage of asymmetric cryptography, because they require the same Private Key for "signing" a message and authenticating the message.

- MACs are of utter importance to prevent CCA on ciphers[^5] - every cipher should include message authentication, which is usually accomplished by using a MAC.

--8<-- "includes/abbrevations.md"

[^1]: [List of hash functions](https://en.wikipedia.org/wiki/List_of_hash_functions) on Wikipedia
[^2]: [CRC](https://en.wikipedia.org/wiki/Cyclic_redundancy_check) on Wikipedia
[^3]: [MD5 considered harmful today - Creating a rogue CA certificate](https://www.win.tue.nl/hashclash/rogue-ca/) from Eindhoven University of Technology
[^4]: [Announcing the first SHA1 collision](https://security.googleblog.com/2017/02/announcing-first-sha1-collision.html) on Google Security Blog
[^5]: [All the crypto code you’ve ever written is probably broken](https://tonyarcieri.com/all-the-crypto-code-youve-ever-written-is-probably-broken) as blogged by Tony Arcieri.
