---
hide:
  - navigation
---

# RSA (used for encryption)

!!! success "This algorithm is recommended"

    It is recommended to use RSA encryption with the padding OAEP and in conjunction with AES or ChaCha in a Hybrid Encryption scheme.

    The key size must be at least 2048 Bits (256 Bytes), [see below](#security-level) for details.

--8<-- "includes/disclaimer.md"

!!! info "Quick Info"

    |ECIES| |
    |----|-|
    |Names|RSA|
    |Attributes|Asymmetric (Public Key), Hybrid Cipher|
    |Features|Encryption, Digital Signature|
    |Private Key Size|Variable, >= 2048 Bits recommended|
    |First Published|1977|

## RSA in practice

Very often, RSA is used for digital signatures. The most widespread use is for TLS (HTTPS) certificates that every website requires nowadays.

RSA can also be used to encrypt data using Public Key encryption - also called Asymmetric Encryption - mechanisms. In contrast to Private Key encryption, where both parties need to know a shared Private Key, in Public Key encryption it is possible to freely share your Public Key and let senders encrypt data using that Public Key for the receiver that knows the Private Key, and only the receiver can decrypt the data with the help of the Private Key.

### Plain RSA encryption (uncommon)

It is possible to encrypt data for a receiver using only RSA and the receiver's Public Key.

![Public Key Encryption visualization](/images/public-key-encryption.png)

However, this is not very efficient and might not be suitable for low latency or high throughput requirements.

Plain RSA encryption can only encrypt plaintexts that are the exact same size as the Private Key. To encrypt data that is smaller or larger than the Private Key, a padding is required ([see below](#rsa-paddings)).

### Hybrid RSA encryption (faster)

To mkae encryption faster, Asymmetric Encryption is often used in conjunction with Symmetric Encryption algorithms such as AES or ChaCha. In this scheme, the sender first generates a fresh Symmetric Private Key, and then encrypts this Symmetric Private Key using the receiver's Public Key, and encrypts the plaintext with the Symmetric Private Key.

Then, the receiver can first decrypt the Symmetric Private Key using it's Private Key and with the Symmetric Private Key it can decrypt the ciphertext to gain the plaintext.

![Hybrid Encryption visualization](/images/hybrid-encryption.png)

In this scheme, the slower RSA encryption only needs to take place on a relatively small Private Key (usually 128 Bits/16 Bytes or 256 Bits/32 Bytes), while the actual ciphertext can be much larger and will be encrypted using an efficient Symmetric Encryption algorithm. Such a scheme, where Asymmetric Encryption and Symmetric Encryption are used together, is called Hybrid Encryption.

## RSA key generation

!!! hint "Key Sizes"
    See [Security Level](#security-level) for recommendations on key size.

RSA key generation is, in contrast to Symmetric Encryption key generation, a slow process. It works by finding very large prime numbers, which is compute intensive and requires enough entropy and a CSPRNG to seed the start of finding a prime.

RSA keys can - and should - be password protected. There are standardized formats for password protection of RSA keys, so usually you just provide a password when saving or loading a private key and it will be interoperable between libraries and programs.

<ul class="recommendations">
    <li>Use a renown program or library to create RSA keys that makes sure that the process is properly random-seeded.</li>
    <li>Store your RSA keys password-protected.</li>
    <li>Use a recommended <a href="#security-level">key size</a> - at least 2048 bits.</li>
</ul>

## RSA paddings

RSA requires padding when encrypting data that is not of exact the same size as the used RSA Private Key - so basically almost always.

Here's a list of available padding modes:

|Padding Mode|Full Name|Recommendation|
|------------|---------|--------------|
|OAEP|Optimal Asymmetric Encryption Padding|{{ recommendation("success", "Recommended", "This is the most secure padding more for RSA and is highly recommended.") }}|
|PKCS1 v1.5|Public Key Cryptography Standards 1, Version 1.5|{{ recommendation("failure", "Not recommended", "This padding has known security weaknesses and is not recommended in new systems. However, it can be required to use this mode for compatibility with legacy systems.") }}|
|PSS|Probabilistic Signature Scheme|{{ recommendation("info", "Secure, but can not be used for encryption", "This padding can only be used when creating digital signatures with RSA and can not be used for RSA encryption.") }}|

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
    <li>Use at least 2048 Bit key sizes. For keys that are meant to be secure for longer than 2 years, use 4096 Bits or more.</li>
    <li>TODO.</li>
</ul>
</td>
<td>
<ul class="discouragements">
    <li>Don't use key sizes smaller than 2048 Bits.</li>
    <li>TODO.</li>
</ul>
</td>
      </tr>
    </tbody>
</table>

## Code Samples

TODO

## Security Level

--8<-- "includes/security_level_explained.md"

In 2022, RSA is considered to have the following security levels for practically usable RSA key sizes:

|RSA Key Size|Security Level|Recommendation|
|------------|--------------|--------------|
|1024|80|{{ recommendation("failure", "Not recommended", None) }}|
|2048|112|{{ recommendation("success", "Recommended for most use cases", None) }}|
|3072|128|{{ recommendation("success", "Recommended", "For information on the performance/security trade-off, see [^1] and [^2].") }}|
|4096|142|{{ recommendation("success", "Recommended", "For information on the performance/security trade-off, see [^1] and [^2].") }}|

For reference, the following security levels are to be expected for huge, usually impractical key sizes:

|RSA Key Size|Security Level|
|------------|--------------|
|7680|192|
|15360|256|

## Alternatives

Other encryption algorithms are:

--8<-- "includes/encryption_comparison.md"

## History

|Year|Event|
|--------|----|
|TODO||

## References

[^1]: [RSA Key Sizes: 2048 or 4096 bits?](https://danielpocock.com/rsa-key-sizes-2048-or-4096-bits/) on danielpocock.com
[^2]: [So you're making an RSA key for an HTTPS certificate. What key size do you use?](https://expeditedsecurity.com/blog/measuring-ssl-rsa-keys/) on expeditecdsecurity.com

--8<-- "includes/abbrevations.md"
