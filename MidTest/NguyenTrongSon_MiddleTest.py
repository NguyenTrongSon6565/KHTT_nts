# Viết chương trình trong python mà bao gồm: 
# Tính t, v, x, y trong chuyển động ném xiên (các tham số có
# Vẽ đồ thì cho mối liên hệ giữa các tham số mình chọn
# Có thể sử dụng Numpy, pandas, spicy, (array, table, ...), ...

'''
Vẽ đồ thị quỹ đạo của chuyển động ném xiên.
    
Input:
- v0: Vận tốc ban đầu (m/s)
- theta_deg: Góc ném (độ)
- g: Gia tốc trọng trường (m/s^2), mặc định là 9.8
   
Output:
- t: Mảng thời gian
- x, y: Mảng tọa độ theo các thời điểm của t
'''                            

# Khai báo thư viện numpy và matplotlib
import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd

# Tạo hàm vẽ đồ thị quỹ đạo ném xiên
def DoThiNemXien(v0, theta_deg, g=9.8, filename="nem_xien_data.csv"):
    theta = np.radians(theta_deg)  # Chuyển đổi góc sang radian
    
    # Thời gian bay tối đa
    t_max = 2 * v0 * np.sin(theta) / g
    
    # Chia t thành các khoảng nhỏ từ 0 đến t_max
    t = np.linspace(0, t_max, num=20)
    
    # Tính tọa độ x, y theo thời gian
    x = v0 * np.cos(theta) * t
    y = v0 * np.sin(theta) * t - 0.5 * g * t**2
    
    # Lưu tọa độ vào DataFrame và ghi vào file CSV
    df = pd.DataFrame({"ThoiGian (s)": t, "ToaDoX (m)": x, "ToaDoY (m)": y})
    df.to_csv(filename, index=False)
 
    print(f"Dữ liệu đã được lưu vào {filename}")
 
    # Đọc lại dữ liệu từ file CSV
    df_read = pd.read_csv(filename)
    print(df_read.head())
    
    # Vẽ đồ thị quỹ đạo
    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, label=f"Quỹ đạo ném xiên (v0={v0} m/s, θ={theta_deg}°)")
    plt.xlabel("Tọa độ x (m)")
    plt.ylabel("Tọa độ y (m)")
    plt.title("Đồ thị quỹ đạo ném xiên")
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.legend()
    plt.grid()
    plt.show()
    
    return t, x, y

# Phương trình ném xiên với v0=10 m/s, theta=30° và toạ độ của x và y theo thời gian t.
t1, x1, y1 = DoThiNemXien(10, 30)

