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
