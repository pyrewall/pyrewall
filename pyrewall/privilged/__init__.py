import grpc

from concurrent import futures

from pyrewall.grpc.pyrewall_pb2_grpc import SystemInfoServicer, add_SystemInfoServicer_to_server
from pyrewall.grpc.pyrewall_pb2 import SystemInfoResponse

class SystemInfo(SystemInfoServicer):
    def GetSystemInfo(self, request, context):
        return SystemInfoResponse(hostname="test-hostname")

s = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
add_SystemInfoServicer_to_server(SystemInfo(), s)
s.add_insecure_port('unix:///tmp/pyrewall.sock')
