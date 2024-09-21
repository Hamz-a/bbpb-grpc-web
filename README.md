# bbpb-grpc-web
Decode grpc-web traffic using the NCC Blackbox Protobuf Burp extension.

## Installation instructions
1. Follow the installation guide to install the [NCC Blackbox Protobuf](https://github.com/nccgroup/blackboxprotobuf/tree/master/burp) Burp Suite plugin.
2. Navigate to `blackboxprotobuf/burp/blackboxprotobuf/burp/` and replace the `user_funcs.py` file with the one from this repository.

## Context
For more background context, see:
- https://bhamza.me/blogpost/2024/03/04/Security-assessing-grpc-and-grpcweb-services.html
