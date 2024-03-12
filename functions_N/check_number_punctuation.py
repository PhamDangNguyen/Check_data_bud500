import re
import json
import string

def remove_punctuation(text):
    """Loại bỏ dấu câu khỏi một chuỗi văn bản
    Args:
        text(str): Từ đầu vào
    Returns:
        text(str): thay thế mọi ký tự không phải là ký tự chữ cái, chữ số hoặc khoảng trắng bằng một chuỗi rỗng ''
    """
    return re.sub(r'[^\w\s]', '', text)

def _contains_digit(text):
    """Kiểm tra từ có chứa chữ số không

    Args:
        text(str): Từ đầu vào
    Returns:
        (bool): True nếu chứa chữ số còn lại là False
    """
    pattern = r'\d'
    return bool(re.search(pattern, text))

def check_punctuation(script):
    """Kiểm tra xem có dấu câu trong script hay không
    Args:
        Script(str): Script đầu vào
    Returns:
        bool: true nếu có dấu câu và False nếu không có dấu trong câu
    """
    if any(char in script for char in string.punctuation):
        return True
    else:
        return False
    
def check_number_json(path_json,path_save_info):
    """Kiểm tra transcript chứa chữ số không
    Args:
        path_json(str): Path đầu vào của Json file
        path_save_info(str): Path save lại thông tin file .wav có chứa chữ số
    Returns:
        Dictionary: Thông tin về transcript và file wav chứa chữ số
    """
    dict_info = []
    with open(path_json, 'r') as file:
        data = json.load(file)
    for key,info in enumerate(data):
        print(key)
        text = info["transcript"]
        if _contains_digit(text=text):
            dict_info.append(info)
            print(info["transcript"])

    json_object = json.dumps(dict_info, indent=4,ensure_ascii=False)
    with open(path_save_info, "w") as outfile:
        outfile.write(json_object)

def check_punctuation_json(path_json,path_save_info):
    """Kiểm tra transcript chứa lẫn dấu câu không không (chỉ có câu nguyên từ mới tính là không chứa dấu)
    Args:
        path_json(str): Path đầu vào của Json file
        path_save_info(str): Path save lại thông tin file .wav có chứa dấu câu
    Returns:
        Dictionary: Thông tin về transcript và file wav chứa dấu câu
    """
    dict_info = []
    with open(path_json, 'r') as file:
        data = json.load(file)
    for key,info in enumerate(data):
        print(key)
        text = info["transcript"]
        if check_punctuation(text):
            dict_info.append(info)
            print(info["transcript"])

    json_object = json.dumps(dict_info, indent=4,ensure_ascii=False)
    with open(path_save_info, "w") as outfile:
        outfile.write(json_object)

if __name__ == '__main__':
    path_json = "/home/pdnguyen/VietAIbud500/Bud500_convert/train/meta_data.json"
    path_save_info = "/home/pdnguyen/VietAIbud500/Check_data_bud500/evaluate/Info_check_data/Symbol_punctuation_in_script/train.json"
    check_punctuation_json(path_json=path_json,path_save_info=path_save_info)
   
        