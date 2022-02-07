??? info inline end "What does it mean when a cipher is "broken"?"

    In cryptanalysis, which is the science of analysing and breaking cryptographic primitives, a cipher is "broken"
    if a way is found to decrypt the ciphertext or find the Private Key in less rounds than a brute force attack, which
    means trying all possible values in the Private Key's key space.

    In practice, not every cipher that is "broken" by the definition of cryptanalysis is indeed insecure. For example,
    for AES a technique was found to reduce the theoretic maximum key space of 256 Bits down to 254 Bits. Because this
    reduced key space is still large enough for modern encryption requirements, AES is still very secure, although 
    you might find statements that it has been "broken".
