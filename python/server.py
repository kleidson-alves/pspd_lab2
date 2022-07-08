from concurrent import futures
import logging

import grpc
import calcula_pb2
import calcula_pb2_grpc

class Calcula(calcula_pb2_grpc.CalculaServicer):

    def FindNumbers(self, request, context) -> calcula_pb2.FindNumbersResponse:
        print(request.vector)
        print(min(request.vector), max(request.vector))
        return calcula_pb2.FindNumbersResponse(min=min(request.vector), max=max(request.vector))



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calcula_pb2_grpc.add_CalculaServicer_to_server(Calcula(), server)
    # server.add_insecure_port('[::]:50051')
    server.add_insecure_port('localhost:50051')
    server.start()
    print('Listening')
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()
