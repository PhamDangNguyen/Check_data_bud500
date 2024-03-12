import wave
import librosa

def convert_to_lowercase(sentence):
    """
    Chuyển đổi các chữ cái trong câu thành chữ thường nếu có chữ hoa.
    
    Args:
    sentence (str): Câu cần chuyển đổi.
    
    Returns:
    str: Câu đã được chuyển đổi thành chữ thường nếu có chữ hoa.
    """
    # Kiểm tra xem câu có chứa chữ hoa không
    if any(char.isupper() for char in sentence):
        # Nếu có, chuyển đổi thành chữ thường
        sentence = sentence.lower()
    return sentence

def remove_whitespace(sentence):
    """
    Loại bỏ dấu cách trong câu.
    
    Args:
    sentence (str): Câu cần loại bỏ dấu cách.
    
    Returns:
    str: Câu đã được loại bỏ dấu cách.
    """
    # Sử dụng phương thức replace để thay thế dấu cách bằng chuỗi rỗng
    return sentence.replace(",","")

def check_mono(audio_path):
    try:
        with wave.open(audio_path, 'r') as wf:
            num_channels = wf.getnchannels()
            if num_channels == 1:
                return True
    except Exception as e:
        print(f"Lỗi khi đọc tệp âm thanh: {e}")
        return None
    
# if __name__ == '__main__':
#     path_json = '/home/pdnguyen/VietAIbud500/Bud500_convert/test/wavs/0.wav'
#     get_audio_channels(path_json)
