import os
import simpleaudio as sa

audiopath = r'\Users\Gabriel\Desktop\ProjetoDOW-main\DOW\audios\speech.wav'
def CriarAudio():
    os.system('curl -X GET -u "apikey:BPP_bcM-zxkHfu5_JAQOP6AOby-a9Yc5jcl2n4EBxddx" ^ --output '+audiopath+' ^ "https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/76c5fa83-ba39-47c3-ad17-a398d2504b9d/v1/synthesize?accept=audio%2Fwav&text=a%20&voice=pt-BR_IsabelaV3Voice"')

    wave_obj = sa.WaveObject.from_wave_file(audiopath)
    play_obj = wave_obj.play()
    play_obj.wait_done()

CriarAudio()
