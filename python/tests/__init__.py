"""The package's checks, for any version of the API: they run the generated code against a local
fake of the API (fake.py) and hold it to samples made from the wire layer's own descriptors
(samples.py) and to the proto's facts (api.py, generated). Run: python -m unittest discover tests -t ."""
