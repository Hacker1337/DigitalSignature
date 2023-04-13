# Digital Signature

This project contains module for signing text messages with ECDSA algorithm `signing_module.py`

Example in `work_example.py` shows how author can generate secret key 
and encrypt simple "Hello, world!" message from `message.txt` file.
The signature is saved into `signature.yaml` file.

Than it shows how user can verify that this file was signed with this public key.

Run by `python work_example.py`