# ~/protobuf/buildProto/bin/protoc -I . deviceSpecs/deviceSpecs.proto --go_out=plugins=grpc:.
python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. deviceSpecs/deviceSpecs.proto