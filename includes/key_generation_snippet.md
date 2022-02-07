Private keys for {{ algorithm }} do not have to follow a specific form - they just need to be (crypto-secure) random bits of the required size. Other algorithms, such as RSA or EC, require the values to conform to some mathematical requirements, but {{ algorithm }} keys do not.

However, it is important to make sure that the key is generated properly, because otherwise the key generation can be an attack vector - and maybe even a very easy one to attack, if key generation is not "random enough".

Here are a few recommendations that you should keep in mind when implementing {{ algorithm }} key generation:

<ul class="recommendations">
    <li>Use a CSPRNG (Cryptographically-secure Pseudo Random Number Generator) or HSM (Hardware Security Module), if possible
    <li>Otherwise make sure that you seed your random number generator properly (<b>don't</b> only use the current timestamp)</li>
    <li>Always seed a key generator with new randomness - don't succinctly generate multiples keys from the same random number seed</li>
    <li>Generate keys where they will be ultimately needed and stored - e.g. don't generate keys server-side to use them on the client, but generate them client-side instead.</li>
    <li>Store private keys securely</li>
    <li>Avoid transferring private keys</li>
    <li>It is highly recommended to re-negotiate or rotate keys as often as possible. Don't see a Private Key as something "permanently" bound to a person or a node, but instead make it something ephemeral that can change on a frequent basis.</li>
</ul>
