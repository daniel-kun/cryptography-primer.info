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

## What are use-cases for hashes?

Hashes can be a building block for more complex things - for example, some MACs are actually built using hashes. However, you see hashes often used standalone in systems for these use-cases:

- Validate that a message has not been corrupted (or modified) during transport. For example, you can often find hashes next to a download link that can be used to validate that the file has exactly the same content as it supposed to have after you have downloaded it.
- "Shrink" information to a unique identifier that can be used for lookups. For example, you can look up a whole sentence or even a whole paragraph of text in a database by using it's hash, instead of comparing all characters of the paragraph in the database.
- To store passwords (TODO: Add a dedicated chapter to this topic)

## What are use-cases for digital signatures?

Digital signatures also provide the integrity validation function of hashes. But additionally, digital signatures let you verify that the sender of the message is authentic, e.g. the message originates from the source that you expected.

Because digital signatures are using "asymmetric encryption", you can use the Public Key to validate the integrity and authenticity of the message. This has the advantage that you do not need to share a common Private Key between the sender and the receipient.

Use-cases for digital signatures:

- Publish a message and "sign" it so that everyone can verify that it has been written and published by you.
- For example, TLS (and therefore HTTPS, which builds on TLS) uses digital signatures to authenticate the server behind the domain that you have requested data from.
- The underlying building block for this are x.509 certificates that are also widely used in other systems where it is important to let anybody know that a "certificate", that provides arbitrary permissions or identifications, can be trusted.
- Mobile platforms such as Apple's iOS and Google's Android use digital signatures to sign apps in they App Store/Play Store so that the system is able to trust these apps (and in turn is able to block running untrusted apps).

## What are MACs used for?

MACs are similar to digital signatures, but they do not have the advantage of "asymmetric encryption", because they require the same Private Key for "signing" a message and authenticating the message.

You should usually not require to use MACs yourself, because these are often part of a "authenticated encryption" cipher such as [AES-GCM](/algorithms/aes/) or ChaCha20-Poly1305.

--8<-- "includes/hash_mac_sign_comparison.md"

--8<-- "includes/abbrevations.md"
