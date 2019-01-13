# Distributed Training Framework

## Building Instructions

```
./setup.sh
source activate distributed
```

## Goal

Build Docker Containers

Get them to talk to each other

Compare ping response times using open mpi amybe ?

Use horovord for distributed training

Run on differwent machines

## Comm

1. Cluster of machines dockerised
2. Communicate with each other.
3. One master will collect info about each machine
4. Dummy data for now. 


## Libs

Flask and Nginx for server side
Protocol buffers for information exchange.

Then to test for real, use horvod on different machine train cifar10 on 3-4 different machines

