import calcula_pb2
import logging
import random
import grpc
import calcula_pb2
import calcula_pb2_grpc

def generateArray():
    array = []
    for _ in range(0, 10):
        n = random.randint(0, 500000)
        array.append(n)
    return array

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        array = generateArray()
        stub = calcula_pb2_grpc.CalculaStub(channel)
        response = stub.FindNumbers(calcula_pb2.FindNumbersRequest(vector=array, start=0, end=0))
        print(response.min, response.max)

if __name__ == '__main__':
    logging.basicConfig()
    run()
