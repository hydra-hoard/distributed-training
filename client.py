# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import grpc


from protobuf.deviceSpecs import deviceSpecs_pb2
from protobuf.deviceSpecs import deviceSpecs_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:5000') as channel:
        stub = deviceSpecs_pb2_grpc.NodeInformationStub(channel)
        response = stub.FindCompute(deviceSpecs_pb2.Node(domain='localhost',port=5000,nodeId=bytes(1)))
    print("Greeter client received: " + str(response.time))


if __name__ == '__main__':
    run()