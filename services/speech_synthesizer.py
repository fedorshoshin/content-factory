import os
import azure.cognitiveservices.speech as speechsdk


def text_to_speech(messages, filename):
    i = 0
    for message in messages:
        speech_synthesizer = __configure_speech_service(filename + str(i))
        __synthesize_speech(speech_synthesizer, message)
        i += 1


def __configure_speech_service(filename):
    speech_config = speechsdk.SpeechConfig(subscription=os.getenv('SPEECH_KEY'), region=os.getenv('SPEECH_REGION'))
    speech_config.speech_synthesis_voice_name = "en-US-AndrewNeural"
    audio_config = speechsdk.audio.AudioOutputConfig(filename=os.getenv('TEMP_DIR') + filename)
    speech_config.set_speech_synthesis_output_format(speechsdk.SpeechSynthesisOutputFormat.Audio48Khz192KBitRateMonoMp3)
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    return speech_synthesizer


def __synthesize_speech(speech_synthesizer, text):
    speech_synthesizer.speak_ssml_async(f"""
    <speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis'
           xmlns:mstts='http://www.w3.org/2001/mstts'
           xml:lang='en-US'>
      <voice name='en-US-ChristopherMultilingualNeural'>
        <mstts:express-as style='angry'>
          {text}
        </mstts:express-as>
      </voice>
    </speak>
    """).get()
