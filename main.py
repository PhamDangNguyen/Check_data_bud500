import os
from functions_N import getAPI_data

def STT_API(API_key, path_wav):
    STT_API_ = getAPI_data.VoiceAPI_STT(API_key)
    response = STT_API_.upload_audio(file_path=path_wav)
    return response

if __name__ == '__main__':

    API_key = 'mtqijSUcj3hC96vWB6bsmqkgTud7y1tYQ4Tawa0R2V8OwShEAp8E3GEuCZ4F8Uo5'

    path_wav = '/home/dang_nguyen/check_data_bud500h/Check_data_bud500/00004.wav'

    text_gen = STT_API(API_key=API_key,path_wav=path_wav)
    print(text_gen)