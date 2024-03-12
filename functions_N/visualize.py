import matplotlib.pyplot as plt
import json
import numpy as np

path_json = '/home/pdnguyen/VietAIbud500/Bud500_convert/train/meta_data.json'

arr_time = [0] * 6
# Tính giá trị trung bình của các khoảng số nguyên
x = np.arange(0.5, len(arr_time) + 0.5)  # Bắt đầu từ 0.5 và kết thúc ở len(y) + 0.5

# Mở tệp JSON
with open(path_json) as json_file:
    data = json.load(json_file)

for info in data: 
    duration = info["duration"]
    if(duration<1):
        arr_time[0] = arr_time[0] + 1
    elif(duration>=1 and duration <2):
        arr_time[1] = arr_time[1] + 1
    elif(duration>=2 and duration <3):
        arr_time[2] = arr_time[2] + 1
    elif(duration>=3 and duration <4):
        arr_time[3] = arr_time[3] + 1
    elif(duration>=4 and duration <5):
        arr_time[4] = arr_time[4] + 1
    else:
        arr_time[5] = arr_time[5] + 1
  

# Vẽ đồ thị cột
plt.bar(x, height=arr_time, width=1, align='center', color='blue', edgecolor='black')

# Đặt tiêu đề và nhãn cho các trục
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Train data distributied')

# Đặt các điểm trên trục x
plt.xticks(np.arange(0, len(arr_time) + 1), np.arange(0, len(arr_time) + 1))
plt.savefig('/home/pdnguyen/VietAIbud500/image_check_data/train.png')
# Hiển thị đồ thị
plt.show()