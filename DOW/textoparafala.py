import os
import unicodedata
import simpleaudio as sa

# Caminho onde o áudio será guardado
audiopath = r'\Users\Gabriel\Desktop\ProjetoDOW-main\DOW\audios\speech.wav'

# Função para gerar e rodar o áudio
def CriarAudio(text):

    # Tratamento do texto para a requisição GET
    text = unicodedata.normalize("NFD", text)
    text = text.replace(" ", "%20")
    text = text.replace("R$", "reais")
    text = bytes(text, 'ascii', 'ignore')
    text = str(text, 'utf-8')
    
    # Chama IDE para retornar o áudio
    os.system('curl -X GET -u "apikey:BPP_bcM-zxkHfu5_JAQOP6AOby-a9Yc5jcl2n4EBxddx" ^ --output '+audiopath+' ^ "https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/76c5fa83-ba39-47c3-ad17-a398d2504b9d/v1/synthesize?accept=audio%2Fwav&text='+text+'%20&voice=pt-BR_IsabelaV3Voice"')

    # Roda o áudio
    wave_obj = sa.WaveObject.from_wave_file(audiopath)
    play_obj = wave_obj.play()
    play_obj.wait_done()
