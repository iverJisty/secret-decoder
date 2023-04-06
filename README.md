# Secret Decoder for Kubernetes

This is a Python script that decodes base64-encoded strings in the `data` section of a Kubernetes secret YAML file and outputs them as JSON. It can be used to quickly view the contents of secrets without having to manually decode each value.

## Installation

1. Clone this repository or download the `secret_decoder.py` file.
2. Install the required dependencies by running `pip install -r requirements.txt`.

## Usage

To use this script, pipe a Kubernetes secret YAML file into it using standard input (stdin). For example:

```
cat my-secret.yaml | python secret_decoder.py
```

The decoded values will be output as JSON to standard output (stdout).

Note: This script assumes that all values in the `data` section are base64-encoded strings. If there are any non-base64-encoded values, they will not be decoded and may cause errors.
