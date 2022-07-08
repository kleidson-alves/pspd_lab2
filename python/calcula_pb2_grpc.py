import grpc
import calcula_pb2

class CalculaStub(object):

  def __init__(self, channel):

    self.FindNumbers = channel.unary_unary(
        '/calcula.CalculaService/FindNumbers',
        request_serializer=calcula_pb2.FindNumbersRequest.SerializeToString,
        response_deserializer=calcula_pb2.FindNumbersResponse.FromString,
        )


class CalculaServicer(object):
  def FindNumbers(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CalculaServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'FindNumbers': grpc.unary_unary_rpc_method_handler(
          servicer.FindNumbers,
          request_deserializer=calcula_pb2.FindNumbersRequest.FromString,
          response_serializer=calcula_pb2.FindNumbersResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'calcula.CalculaService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))