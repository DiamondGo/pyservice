# from tempfile import NamedTemporaryFile
from io import BytesIO
from pb.tts_pb2 import Response, File
from pb.tts_pb2_grpc import GoogleTranslateTTSServicer
from gtts import gTTS
# from langdetect import detect # total rubbish, works like shxt
# from googletrans import Translator # not working either
import detectlanguage


class GoogleTranslateTTSService(GoogleTranslateTTSServicer):
    def __init__(self, detectlanguage_apikey) -> None:
        super().__init__()
        detectlanguage.configuration.api_key = detectlanguage_apikey

    def TextToSpeech(self, request, context) -> Response:
        text = request.text
        try:
            language = self.GetLang(text)
        except:
            language = "en"
        speech = gTTS(text, lang=language)

        buffer = BytesIO()
        speech.write_to_fp(buffer)
        buffer.seek(0)

        return Response(success=True, fileResponse=File(name="speech.mp3", data=buffer.read()))

    def GetLang(self, text):
        detected = detectlanguage.detect(text)
        lang = detected[0]["language"]
        if lang == 'zh-Hant':
            lang = 'zh-TW'
        return lang
