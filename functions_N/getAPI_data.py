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
        retry = 0
        while retry < 5000:
            response = requests.request("POST", url, headers=self.headers, data=payload, files=files)
            if response.status_code == 200:
                print(f"File {file_path} đã được gửi thành công.")
                time.sleep(1)
                return response.json()
            time.sleep(2)
            retry += 1
            print(f"Retry {retry} . . . . .")
        raise Exception("Loi roi anh em oi")


class VoiceForce_alignment:
    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {'api_key': api_key}

    def upload_audio(self, file_path, transcript):
        url = "https://voicestreaming.cmccist.ai/force_alignment"
        payload = {'transcript': transcript,'repeat_limit': '2'}
        files=[
        ('content',('0.wav',open(file_path,'rb'),'audio/wav'))
        ]
        response = requests.request("POST", url, headers=self.headers, data=payload, files=files)
        if response.status_code == 200:
            print(f"File {file_path} đã được gửi thành công.")
        response_json = response.json()
        return response_json["task_id"]
    
    def get_API_forceAli(self, task_id):
        url = "https://voicestreaming.cmccist.ai/get_result_force_alignment?=fffa3a16-ca1c-481b-a80e-169ae737b09e"
        payload = {'task_id': task_id}
        files=[]
        head = {}
        Check_percent = 0
        while Check_percent != 100:
            response = requests.request("POST", url, headers=head, data=payload, files=files)
            Check_percent = response.json()["percentage"]
            print(f"Wating .... {Check_percent}%")
            if Check_percent == 100:  
                return response.json()
            time.sleep(1)
            
                
        
if __name__ == '__main__':
    API_key= "mtqijSUcj3hC96vWB6bsmqkgTud7y1tYQ4Tawa0R2V8OwShEAp8E3GEuCZ4F8Uo5"
    Audio_path = '/home/pdnguyen/VietAIbud500/Bud500_convert/test/wavs/0.wav' 
    # Scripts = 'tôi thì tôi nghĩ rằng là hầu hết tất cả'
    # FORCE_ob = VoiceForce_alignment(api_key=API_key)
    # FORCE_task_id = FORCE_ob.upload_audio(file_path=Audio_path,transcript=Scripts)
    # response_force = FORCE_ob.get_API_forceAli(FORCE_task_id)["force_align_result"]["list_align"]
    # start_time = response_force[0]["start"]
    # end_time = response_force[len(response_force)-1]["end"]
    # print(end_time)
    score = VoiceAPI_STT(api_key=API_key).upload_audio(file_path=Audio_path)
    print(score)
   
  










    


    
    






























