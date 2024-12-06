
PROTOS=$(wildcard protos/*.proto)

%_pb2_grpc.py %_pb2.py %_pb2.pyi: $(PROTOS)
	python -m grpc_tools.protoc -I./protos --python_out=./pyrewall/grpc/ --pyi_out=./pyrewall/grpc/ --grpc_python_out=./pyrewall/grpc/ %