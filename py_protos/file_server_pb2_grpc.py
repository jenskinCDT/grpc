# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import file_server_pb2 as file__server__pb2


class FileServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.upload = channel.stream_unary(
                '/FileService/upload',
                request_serializer=file__server__pb2.Chunk.SerializeToString,
                response_deserializer=file__server__pb2.Reply.FromString,
                )
        self.download = channel.unary_stream(
                '/FileService/download',
                request_serializer=file__server__pb2.Request.SerializeToString,
                response_deserializer=file__server__pb2.Chunk.FromString,
                )


class FileServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def upload(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def download(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FileServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'upload': grpc.stream_unary_rpc_method_handler(
                    servicer.upload,
                    request_deserializer=file__server__pb2.Chunk.FromString,
                    response_serializer=file__server__pb2.Reply.SerializeToString,
            ),
            'download': grpc.unary_stream_rpc_method_handler(
                    servicer.download,
                    request_deserializer=file__server__pb2.Request.FromString,
                    response_serializer=file__server__pb2.Chunk.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'FileService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FileService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def upload(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/FileService/upload',
            file__server__pb2.Chunk.SerializeToString,
            file__server__pb2.Reply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def download(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/FileService/download',
            file__server__pb2.Request.SerializeToString,
            file__server__pb2.Chunk.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
