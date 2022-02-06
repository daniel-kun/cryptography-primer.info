??? info ""Security Level" explained"

    In cryptography, anything that lets you decrypt a message or extract the secret key with less effort than "brute force" is considered a "break" or a possible "attack". "Brute force" means testing out the key in the whole key space - for 128 Bits (like in AES-128) this means trying all 340,282,366,920,938,463,463,374,607,431,768,211,456 possible values that an 128 Bit (16 Bytes) value can have. For 256 Bits (like in ChaCha20 or AES-256), these are 115,792,089,237,316,195,423,570,985,008,687,907,853,269,984,665,640,564,039,457,584,007,913,129,639,936 possible values.

    As you can imagine, not every "attack" is a real problem. Having an attacker have to try out for example 2<sup>127</sup> values (instead of 2<sup>128</sup>) is not a risk in practice.

    With the help of certain "attacks" it is possible to reduce the key space required to try out in order to break the encryption. The lowest key space that you can attain for a given cipher using one or a combination of attacks is considered the <b>"security level"</b>.

    In cryptography, a key space of 2<sup>80</sup> (this is a security level of 80 Bits) has long been considered secure. This might no longer be the case, depending on how strong your security needs to be. The BSI (German Institute of Cybersecurity) recommends a security level of at least 100 Bits and even 120 Bits for high security[^10] in 2022.

    The security level of a cipher is not fix in time. It might become lower if attacks on the cipher have been found. That is why security recommendations are valid usually not more than one or two years into the future.