Usually you use {{ algorithm }} in a manner that the key is derived from the password that a user has to enter to encrypt/decrypt the data. Because the key is of fixed length ({{ keysize }}), you can not use the password as the key directly, because that would impose insecure and inpractical constraints on the password that the user has to choose.

Instead, a key derivation function is used to create an {{ algorithm }}-compatible key from a password. [PBKDF2](algorithms/pbkdf2.md) (Password Based Key Derivation Function 2) is a state of the art key derivation function.
