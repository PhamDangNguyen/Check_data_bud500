import requests
import json
import time

class VoiceAPI_STT:
    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {'api_key': api_key}

    def upload_audio(self, file_path):
        url = "https://voicestreaming.cmccist.ai/speech_to_text"
        payload = {'is_normalize': '1',
                        'return_tracking_change_normalize': '1',
                        'detail_word': '0'}
        files=[
                ('content',('113.wav',open(file_path,'rb'),'audio/wav'))
            ]
        
        response = requests.request("POST", url, headers=self.headers, data=payload, files=files)

        if response.status_code == 200:
            print(f"File {file_path} đã được gửi thành công.")
        response_json = response.json()
        return response_json['response']













    


    
    






























