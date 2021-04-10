# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import hello_pb2 as hello__pb2


class HelloServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.HelloServer = channel.stream_stream(
                '/hello.HelloService/HelloServer',
                request_serializer=hello__pb2.HelloMessage.SerializeToString,
                response_deserializer=hello__pb2.ReplyMessage.FromString,
                )


class HelloServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def HelloServer(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HelloServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'HelloServer': grpc.stream_stream_rpc_method_handler(
                    servicer.HelloServer,
                    request_deserializer=hello__pb2.HelloMessage.FromString,
                    response_serializer=hello__pb2.ReplyMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'hello.HelloService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class HelloService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def HelloServer(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/hello.HelloService/HelloServer',
            hello__pb2.HelloMessage.SerializeToString,
            hello__pb2.ReplyMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
