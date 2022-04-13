import os
from uuid import uuid4
import grpc
from py_protos import file_server_pb2, file_server_pb2_grpc
import _credentials
from concurrent import futures
from utils.lib import get_file_chunks, save_chunks_to_file


class FileServerHandler(file_server_pb2_grpc.FileServiceServicer):
    def __init__(self):
        class Servicer(file_server_pb2_grpc.FileServiceServicer):
            def __init__(self):
                self.root_path = os.path.abspath(os.getcwd()) + '/uploads/'

            def upload(self, request_iterator, context):
                tmp_file_name = self.root_path + uuid4().hex + ".png"
                print(f'---> upload new file: {tmp_file_name}')
                save_chunks_to_file(request_iterator, tmp_file_name)
                return file_server_pb2.Reply(length=os.path.getsize(tmp_file_name))

            def download(self, request, context):
                if request.name:
                    return get_file_chunks(self.root_path)

        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        file_server_pb2_grpc.add_FileServiceServicer_to_server(Servicer(), self.server)
        
    def start(self, port):
        server_credentials = grpc.ssl_server_credentials([(_credentials.SERVER_CERTIFICATE_KEY, _credentials.SERVER_CERTIFICATE)])
        self.server.add_secure_port('[::]:50051', server_credentials)
        print(f'Server is listening on port {port}')
        self.server.start()
        self.server.wait_for_termination()



if __name__ == '__main__':
    FileServerHandler().start(50051)