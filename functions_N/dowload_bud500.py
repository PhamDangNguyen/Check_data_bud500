from datasets import load_dataset
import json
from scipy.io.wavfile import write
import numpy as np
import librosa


def get_audio_duration(file_path):
    # Load audio file
    y, sr = librosa.load(file_path, sr=None)
    # Calculate duration
    duration = librosa.get_duration(y=y, sr=sr)
    return duration



if __name__ == '__main__':

    # get_audio_duration(file_path="/home/pdnguyen/VietAIbud500/Bud500_convert/valid/wavs/0.wav")

    # # load all (649158 samples, ~100gb, ~2hrs to complete loading)
    dataset = load_dataset("linhtran92/viet_bud500", split='train')
    print(dataset)
   
    data_save = []
    total_time = 0

    for idx, info in enumerate(dataset):
        # print(info['audio']['array'])
        # print(info['audio']['sampling_rate'])
        # print(info['transcription'])
        # break
        name_wav_path = f"/home/pdnguyen/VietAIbud500/Bud500_convert/train/wavs/{idx}.wav"
        audio_array_s16 = (info["audio"]["array"] * 32767).astype(np.int16)
        write(
            name_wav_path,
            info["audio"]["sampling_rate"],
            audio_array_s16,
        )
        duration_wav = get_audio_duration(name_wav_path)
       
        dict_info = {
        "name": name_wav_path,
        "duration":duration_wav,
        "transcript": str(info['transcription']),
        }

        total_time = total_time + duration_wav
        data_save.append(dict_info)

    print(f"Total time is {total_time/3600}")


        # Serializing json
    json_object = json.dumps(data_save, indent=4,ensure_ascii=False)

    # Writing to sample.json
    with open("/home/pdnguyen/VietAIbud500/Bud500_convert/train/meta_data.json", "w") as outfile:
        outfile.write(json_object)
    

