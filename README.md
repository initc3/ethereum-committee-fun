Ethereum Multisignature Threshold Verification
----------------------------------------------

This project contains a working example, including both
a precompiled EVM contract implementation in pyethereum 
and a Solidity contract that uses it, of threshold signature
verification implemented in Ethereum.  The scheme used is
based on a Gap-Diffie-Hellman Group [Boldyreva 2003].

This threshold signature verification is intended to allow
for robust distributed key generation and large committees that
incur a majority of their cost off-chain.  More information about
the project vision is available in the "slides" folder.


Installation
------------

1. Install HoneyBadger and Python dependencies according to README folder.
2. Install pyethereum, replacing ethereum/specials.py with the specials.py in this Github.
3. Deploy and run the Solidity contract (likely as a library), following the example formatting pattern in "contract_creation".
4. Enjoy cheap multisignature transactions!


Optionally:
1. Generate example signatures with gen.py (or use Honey Badger library for generation)
2. Remove the debug print statements in specials.py


TODO:
1. Disributed key generation protocol 


The Team
--------
Phil Daian, Elaine Shi, Hubert Chan, Mike Harder, Sid Harder, Siqiu Yao
