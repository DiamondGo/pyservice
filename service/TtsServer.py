# from tempfile import NamedTemporaryFile
from io import BytesIO
from pb.tts_pb2 import Response, File
from pb.tts_pb2_grpc import GoogleTranslateTTSServicer
from gtts import gTTS


class GoogleTranslateTTSService(GoogleTranslateTTSServicer):
    def TextToSpeech(self, request, context) -> Response:
        text = request.text
        speech = gTTS(text, lang="en")

        buffer = BytesIO()
        speech.write_to_fp(buffer)
        buffer.seek(0)

        return Response(success=True, fileResponse=File(name="speech.mp3", data=buffer.read()))
