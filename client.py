import os
import grpc
from py_protos import file_server_pb2, file_server_pb2_grpc
import _credentials
from utils.lib import get_file_chunks, save_chunks_to_file


class ClientHandler:
    def __init__(self, address):
        creds = grpc.ssl_channel_credentials(_credentials.SERVER_CERTIFICATE)
        # channel = grpc.insecure_channel('%s:%d' % ('localhost', 50051)) 
        channel = grpc.secure_channel(address,credentials=creds) 
        self.stub = file_server_pb2_grpc.FileServiceStub(channel)

    def upload(self, in_file_name):
        chunks_generator = get_file_chunks(in_file_name)
        response = self.stub.upload(chunks_generator)
        assert response.length == os.path.getsize(in_file_name)

    def download(self, target_name, out_file_name):
        response = self.stub.download(file_server_pb2.Request(name=target_name))
        save_chunks_to_file(response, out_file_name)
        


if __name__ == '__main__':
    client = ClientHandler('10.1.38.58:50051')

    # demo for file uploading
    in_file_name = 'E:\\data.xlsx'
    client.upload(in_file_name)

    # # demo for file downloading:
    # out_file_name = '/tmp/large_file_out'
    # if os.path.exists(out_file_name):
    #     os.remove(out_file_name)
    # client.download('whatever_name', out_file_name)