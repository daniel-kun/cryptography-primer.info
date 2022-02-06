---
hide:
  - navigation
---

# ChaCha

!!! success "This algorithm is recommended"

    Use ChaCha in it's XChaCha20-Poly1305 variation.

    XChaCha20-Poly1305 is considered __secure__[^1] and fast. It has a strong security level and provides authentication.

    It is arguably easier to use than [AES](/algorithms/aes/), because it has less (insecure) variations. However, when using AES as AES-256-GCM, the differences in security to ChaCha20-Poly1305 are negligible. Note that AES is only fast to use then hardware acceleration is available - while this is very common nowadays, it might be a constraint to consider. ChaCha can be implemented very fast in software only and does not require special CPU instructions.

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

## Modes of operation

ChaCha is a Stream Cipher, which means that it can encode arbitrary length of data - in contrast to Block Ciphers, which need "modes of operation" that help concatenate and pad data so that it fits into multiple of the Block Cipher's block size.

So ChaCha can be used "raw" as it is, in theory. But in practice, you should use ChaCha together with a MAC to achieve AEAD to make the cipher resitant to CCA. By far the most common MAC used with ChaCha is Poly1305, which makes __ChaCha20-Poly1305__ the most common incarnation of ChaCha nowadays.

|Cipher|Description|
|------|-----------|
|XChaCha20-Poly1305|<div class="admonition success"><p class="admonition-title">Recommended</p><p>This is basically the same as ChaCha20-Poly1305, but uses a larger `nonce` of 192 Bit (24 Bytes). Because `nonce`-reuse is the point of an implementation that can go wrong easiest, XChaCha20-Poly1305 offers more "ease of implementation". Other than that, the security attributes are equal to ChaCha20-Poly1305</p></div>|
|ChaCha20-Poly1305|<div class="admonition success"><p class="admonition-title">Recommended if you can't use XChaCha20-Poly1305</p><p>ChaCha20-Poly1305 is a very common Stream Cipher that is considered secure. It is widely deployed, studied and very fast. Because it uses a smaller `nonce` than XChaCha20-Poly1305, the dangers of accidental `nonce`-reuse is higher, which makes it a bit more error prone. Other than that, the security attributes are equal to XChaCha20-Poly1305.</p></div>|
|ChaCha20|<div class="admonition info"><p class="admonition-title">Use ChaCha20-Poly1305 instead</p><p>Raw ChaCha20 without authorization is not recommended, because there is usually no reason not to used ChaCha20-Poly1305 instead.</p>|
|ChaCha12|<div class="admonition warning"><p class="admonition-title">Use at your own risk</p><p>ChaCha12 might be a bit faster than ChaCha20, but is has multiple downsides:<ul><li>It does not provide authentication, so it is vulnerable to common attacks</li><li>It has lower security than ChaCha20</li><li>It is not nearly as widely deployed as ChaCha20, and is not as widely studied, so the exact security is not very clear.</li></ul><p></div>|
|ChaCha8|<div class="admonition failure"><p class="admonition-title">Not recommended</p><p>There have been practical attacks against ChaCha reduced to 7 rounds<sup><a class="footnote-ref" id="fnref:2" href="#fn:2">2</a></sup>, which is not very far from ChaCha8 8 rounds. So it is likely that ChaCha8 does not have very strong security.</p></div>|

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
    <li>It is very important that you don't use the same `nonce` multiple times with the same key.</li>
    <li>Don't use raw ChaCha ciphers (e.g. without Poly1305). <a href="https://tonyarcieri.com/all-the-crypto-code-youve-ever-written-is-probably-broken">(detailed explanation on Tony Arcieri's blog)</a></li>
    <li>Don't trust your crypto library's defaults - check that you are not accidentally use a discouraged practice, because your library has bad defaults.</li>
    <li>Don't transmit the key between two parties. Either pre-share the key over a secure medium, use a key exchange algorithm (such as DH or ECDH) or an asymmetric encryption algorithm (such as RSA) for this.</li>
</ul>
</td>
        </tr>
    </tbody>
</table>

## Security Level

--8<-- "includes/security_level_explained.md"

In 2022, ChaCha20 is considered to have a full security level of 256 Bits, which is it's original Key Size. To quote the report[^3] "Security Analysis of ChaCha20-Poly1305 AEAD" from KDDI Research:

!!! quote

    Therefore, we conclude that we cannot find any weaknesses in ChaCha20-Poly1305 AEAD.

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