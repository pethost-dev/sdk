"""The package's checks, for any version of the API and each of its surfaces (pethost, and a module
such as pethost.sandboxes): they run the generated code against local fakes of the API and of the
server a Connection sends a call to (fake.py), and hold it to samples made from the wire layer's
own descriptors (samples.py) and to the protos' facts (api.py, generated). Run: python -m
unittest discover tests -t ."""
