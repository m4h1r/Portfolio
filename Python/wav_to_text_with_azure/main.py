
import azure.cognitiveservices.speech as speechsdk
speech_key, service_region = "<your_speech_key>", "uksouth"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
source_language_config = speechsdk.languageconfig.SourceLanguageConfig("tr-TR")
speech_recognizer = speechsdk.SpeechRecognizer(
        speech_config=speech_config, source_language_config=source_language_config, audio_config=audio_config)
result = speech_recognizer.recognize_once()


if result.reason == speechsdk.ResultReason.RecognizedSpeech:
    print("Recognized: {}".format(result.text))
elif result.reason == speechsdk.ResultReason.NoMatch:
    print("No speech could be recognized: {}".format(result.no_match_details))
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print("Speech Recognition canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        print("Error details: {}".format(cancellation_details.error_details))
