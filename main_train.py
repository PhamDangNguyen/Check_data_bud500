import json
from functions_N import check_mono
from functions_N import VoiceForce_alignment,VoiceAPI_STT

def check_monoJson(json_path):
    with open(json_path, 'r',encoding="utf-8") as file:
        data = json.load(file)
        i = 0
    for info in data:
        path_wav = info["name"]
        if check_mono(path_wav):
            i = i+1
        else:
            print(f"File âm thanh {path_wav} không phải là monno")
    return i

def run_force_alignment_STTScore(path_json,API_key,save_info_delete,save_info_notdelete,path_save_check_stt=None,path_remove_stt_score=None):
    path_save_check_stt = "/home/pdnguyen/VietAIbud500/Check_data_bud500/filter_data/STT_score/train/score_STT_get_data.json"
    path_remove_stt_score = "/home/pdnguyen/VietAIbud500/Check_data_bud500/filter_data/STT_score/train/score_STT_remove_data.json"

    FORCE_API = VoiceForce_alignment(api_key=API_key)
    with open(path_json, 'r',encoding="utf-8") as file:
        data = json.load(file)
    data_trim = []
    data_not_trim = []
    number_data = 0
    number_trim = 0
    number_nottrim = 0

    save_final_json_stt = []
    remove_save_final_json_stt = []

    for info in data:
        print("train")
        number_data = number_data + 1 
        path_wav = info["name"]
        scripts = info["transcript"] 
        duration = info["duration"]
        task_id = FORCE_API.upload_audio(file_path=path_wav,transcript=scripts)
        results = FORCE_API.get_API_forceAli(task_id=task_id)["force_align_result"]["list_align"]
        start_time = results[0]["start"]
        end_time = results[len(results)-1]["end"]
        if start_time > 0.5 or (duration - end_time) > 0.5:
            dict_align_trim = {
                "path_wav": path_wav,
                "transcripts":scripts,
                "time_slient_start":start_time,
                "time_slient_end":duration - end_time
            }
            data_trim.append(dict_align_trim)
            number_trim = number_trim + 1
        else:
            dict_align_nottrim = {
                "path_wav": path_wav,
                "transcripts":scripts,
                "time_slient_start":start_time,
                "time_slient_end":duration - end_time
            }
            data_not_trim.append(dict_align_nottrim)
            number_nottrim = number_nottrim + 1
            #check lan 2 score cua file .wav
            STT_API = VoiceAPI_STT(api_key=API_key)
            score = STT_API.upload_audio(file_path=path_wav)["confident_score"]
            if(score>0.65):
                save_final_data = {
                "path_wav": path_wav,
                "transcripts":scripts,
                "score": score
                }
                save_final_json_stt.append(save_final_data)
            else:
                remove_final_data = {
                "path_wav": path_wav,
                "transcripts":scripts,
                "score": score
                }
                remove_save_final_json_stt.append(remove_final_data)
                
    print("Tổng số data đã cắt là",number_trim)
    print("Tổng số data còn lại là",number_nottrim)
    json_object_delete = json.dumps(data_trim,indent=4,ensure_ascii=False)
    json_object_notdelete = json.dumps(data_not_trim,indent=4,ensure_ascii=False)
    json_object_save_final = json.dumps(save_final_json_stt,indent=4,ensure_ascii=False)
    json_object_delete_final = json.dumps(remove_save_final_json_stt,indent=4,ensure_ascii=False)
    # Writing to sample.json
    with open(save_info_delete, "w",encoding="utf-8") as outfile:
        outfile.write(json_object_delete)
    with open(save_info_notdelete, "w",encoding="utf-8") as outfile:
        outfile.write(json_object_notdelete)
    with open(path_save_check_stt, "w",encoding="utf-8") as outfile:
        outfile.write(json_object_save_final)
    with open(path_remove_stt_score, "w",encoding="utf-8") as outfile:
        outfile.write(json_object_delete_final)
    return number_data

def check_score(path_json,api_key,info_save_json):
    STT_API = VoiceAPI_STT(api_key)

    with open(path_json, 'r',encoding="utf-8") as file:
        data = json.load(file)
    data_score_less_65 = []
    
    number_data = 0
    remove_nb = 0

    for info in data:
        print("mode train")
        number_data = number_data + 1 
        path_wav = info["name"]
        scripts = info["transcript"] 
        duration = info["duration"]
        if number_data > 0:
            score = STT_API.upload_audio(file_path=path_wav)["confident_score"]
            if(score<0.65):
                remove_nb = remove_nb + 1
                print(path_wav)
                save_final_data = {
                "path_wav": path_wav,
                "transcripts":scripts,
                "duration": duration,
                "score": score
                }
                data_score_less_65.append(save_final_data)
                json_object_delete_final = json.dumps(save_final_data,indent=4,ensure_ascii=False)
                with open(info_save_json+f"/{remove_nb}.json", "w",encoding="utf-8") as outfile:
                    outfile.write(json_object_delete_final)
    
    return remove_nb,number_data

if __name__ == '__main__':
    API_key= "mtqijSUcj3hC96vWB6bsmqkgTud7y1tYQ4Tawa0R2V8OwShEAp8E3GEuCZ4F8Uo5"
    path_json_train = "/home/pdnguyen/VietAIbud500/Bud500_convert/train/meta_data.json"
    path_save_info = "/home/pdnguyen/VietAIbud500/Check_data_bud500/filter_data/STT_score/train/data_score_less_65"

    check_score_audio,total_data = check_score(path_json=path_json_train,api_key=API_key,info_save_json=path_save_info)
    print(f"loại {check_score_audio} trong tổng số {total_data} data")