# simple-fernet

A Python package that streamlines the process of encrypting and decrypting data with [Fernet](https://pypi.org/project/cryptography).

This package leverages user-specified Fernet keys stored in environment variables to simplify the process of encrypting and decrypting data with that key in Fernet. In addition, `simple-fernet` minimizes the amount of time that Fernet keys are held in-memory by only retrieving and using these keys when they're needed to encrypt or decrypt data.

## ⚠️ WARNING

The first version of this tool is actively being developed, and as such should be considered in its "alpha" stages. Expect that the tool, its source code, and its functionality will be incomplete and buggy at this point in time.

## Limitation Related to Environment Variables and Python

Use of `simple-fernet` requires that Fernet keys are both generated and stored in environment variables manually. This is due to limitations around interfacing with system environment variables through Python, especially without requesting or providing privileged access.

Package maintainers are investigating ways to eliminate the need for these manual steps and will implement a solution if found. There are plans to develop a small companion tool to aid in the process of generating Fernet keys while this research is conducted.

For guidance on how to complete these manual steps (if you do not already have a Fernet key stored in environment variables), see the Quick Start below.

## Features

- Initialize instance of `SimpleFernet`, enabling encryption and decryption operations using a Fernet key stored in a user-provided environment variable.
- Implement `encrypt()` method.

## 1.0.0 Roadmap

### In Development

- Implement `decrypt()` method.
- Write initial documentation.

## Ideas for a Future Release

- Add support for generating Fernet keys and storing them in system environment variables.

## Quick Start

This quick start will guide you through the process of using `simple-fernet` in your Python projects.

Please note that this guide assumes that you have not yet generated a Fernet key and includes steps to generate this key and store it in environment variables for `simple-fernet` to use.

If you have any feedback or suggestions to improve this guide, please don't hesitate to [open an issue on GitHub](https://github.com/darkroastcreative/simple-fernet/issues/new/choose)!

### macOS and Linux

Content coming soon!

### Windows

Content coming soon!

## `SimpleFernet` Class

The `SimpleFernet` class is the heart of `simple-fernet`. Instances of the `SimpleFernet` class are used to enable encryption and decryption with a pre-defined Fernet key (stored in an environment variable).

### Initializer

The `SimpleFernet` initializer instantiates an instance of the `SimpleFernet` class and returns it so it can be used to encrypt and decrypt data.

#### Arguments

- `key_environment_variable`: A string representing the name of an  environment variable that contains a Fernet key. Please note that the Fernet key must be generated outside of `simple-fernet` and stored in environment variables before `SimpleFernet` can use it.

#### Returns

An initialized instance of the `SimpleFernet` class with a reference to the environment variable storing the Fernet key to use for encryption and decryption operations.

### `encrypt()` Method

Converts the provided data to `bytes`, encrypts it using Fernet, and returns the encrypted data as `bytes`.

#### Arguments

- `data`: The data to be encrypted.

#### Returns

A `bytes` object representing the encrypted data or `None` (if the encryption operation failed for some reason).

### `decrypt()` Method

Decrypts the provided encrypted data using Fernet and returns it as the decrypted `bytes` value.

#### Arguments

- `encrypted_data`: A `bytes` or `str` value representing data encrypted with Fernet.

#### Returns

A `bytes` object representing the decrypted data.

#### Notes

- The value passed in as `encrypted_data` must be of type `bytes` or `str`. If not, a `TypeError` will be raised.
- This function does not perform any type conversion on the decrypted data. Rather, it returns the decrypted data as `bytes` and leaves the responsibility of converting the data to the user. This is done intentionally to ensure the data is not converted to the wrong type after decryption.
