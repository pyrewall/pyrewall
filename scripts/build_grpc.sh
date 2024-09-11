#!/bin/bash

python -m grpc_tools.protoc -I../protos --python_out=../pyrewall/grpc/ --pyi_out=../pyrewall/grpc/ --grpc_python_out=../pyrewall/grpc/ ../protos/*.proto