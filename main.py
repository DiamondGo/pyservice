from concurrent import futures
import grpc
import pb.tts_pb2 as tts_pb2
from pb.tts_pb2_grpc import add_GoogleTranslateTTSServicer_to_server
from service.TtsServer import GoogleTranslateTTSService

if __name__ == "__main__":
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    add_GoogleTranslateTTSServicer_to_server(
        GoogleTranslateTTSService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
