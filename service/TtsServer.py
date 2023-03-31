
import pb
from pb.tts_pb2 import Response
from pb.tts_pb2_grpc import GoogleTranslateTTSServicer


class GoogleTranslateTTSService(pb.tts_pb2_grpc.GoogleTranslateTTSServicer):
    def TextToSpeech(self, request, context) -> Response:
        print("Got request" + str(request))
        return Response(success=True, fileResponse=None)
