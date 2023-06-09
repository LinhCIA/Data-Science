"""
    Bài toán ước lượng số 5: 
Kiểm định có sự khác nhau giữa giá thành trung bình giữa mẫu xe Civic Sport và Pilot Sport hay không?

Giả thuyết Ho: Giá thành trung bình Civic Sport = Giá thành trung bình Pilot Sport
Đối thuyết H1: Giá thành trung bình Civic Sport ≠ Giá thành trung bình Pilot Sport

    
    
    
    Phương pháp: 
Để kiểm tra điều này, ta thu thập ngẫu nhiên gồm 500 chiếc xe của hãng 
Vì ta nghi ngờ về phương sai của hai mẫu xe này là không bằng nhau nên ta sẽ sử dụng
phương pháp Phép thử t - Welch's.

    Các bước giải quyết bài toán:
+)  Bước 1: Tạo hàm kiểm định ttest_ind()
+)  Bước 2: Lọc dữ liệu
+)  Bước 3: Tiến hành kiểm định
+)  Bước 4: Diễn giải kết quả
"""


#   BƯỚC 1: TẠO HÀM KIỂM ĐỊNH TTEST_IND
#   Mã nguồn hàm ttest_ind do chính tay tôi tạo ra 
from scipy.stats import t

def ttest_ind(data1, data2):
    # Kiểm tra đầu vào:
    if len(data1) == 0 or len(data2) == 0:
        raise ValueError("Mảng dữ liệu rỗng!")
    
    # Tính mean của mỗi mẫu
    mean1 = sum(data1)/len(data1)
    mean2 = sum(data2)/len(data2)

    # Tính phương sai của mỗi mẫu
    # Tuân theo phân phối student 
    # Công thức tính phương sai là: σ^2 = (∑(i=1)→n〖(x_i - x_ngang)^2〗) / (n-1)
    variance1 = sum((x - mean1) ** 2 for x in data1) / (len(data1) - 1)
    variance2 = sum((x - mean2) ** 2 for x in data2) / (len(data2) - 1)

    # Tính độ lệch chuẩn của mỗi mẫu
    std1 = variance1**0.5       # std1 = sqrt(variance1)
    std2 = variance2**0.5       # std2 = sqrt(variance2)

    # Tính thống kê kiểm định t
    # Tính phương sai tổng hợp
    pooled_variance = ((len(data1) - 1) * variance1 + (len(data2) - 1) * variance2) / (len(data1) + len(data2) - 2)
    # Tính giá trị t
    t_statistic = (mean1 - mean2) / (pooled_variance * (1 / len(data1) + 1 / len(data2))) ** 0.5

    # Tính xác suất ý nghĩa p-value
    # Tính bậc tự do
    """
        Bậc tự do là gì?
        Bậc tự do đề cập đến số lượng các giá trị độc lập tối đa của một hệ, 
    là các giá trị có thể thay đổi tự do trong mẫu dữ liệu. 
    """
    degrees_of_freedom = len(data1) + len(data2) - 2

    # Tính điểm giới hạn (giá trị gàng) critical_value
    critical_value = t.ppf(0.975, degrees_of_freedom) # 0.975 = (1-alpha)/2; với alpha=1-95%

    # Tính giá trị p
    # Thứ nhất, vì p-value là tích phân của miền ý nghĩa. Thứ 2, là vì miền này đối xứng
    # => Nhân 2 
    p_value = 2 * (1 - abs(t.cdf(t_statistic, df=degrees_of_freedom))) 

    # Trả về giá trị của t và p
    return t_statistic, p_value


#   BƯỚC 2: LỌC DỮ LIỆU 
import pandas as pd
import numpy as np 


# đọc dữ liệu MẪU
df = pd.read_excel("C:/Users/88690/Downloads/honda_sample.xlsx") 


# dữ liệu của mẫu xe Civic Sport
print("Bảng Mẫu xe Civic Sport và Giá")
print(df[103:124][["Model", "Price"]])
print("Danh sách Giá thành của mẫu xe Civic Sport")
data_civic = np.array(df[103:124]["Price"])
print(data_civic)


# dữ liệu của mẫu xe Pilot Sport
print("Bảng Mẫu xe Pilot Sport và Giá")
print(df[392:425][["Model", "Price"]])
print("Danh sách Giá thành của mẫu xe Pilot Sport")
data_pilot = np.array(df[392:425]["Price"])
print(data_pilot)


#   BƯỚC 3: TIẾN HÀNH KIỂM ĐỊNH
t_statistic, p_value = ttest_ind(data1=data_civic, data2=data_pilot)


#   BƯỚC 4: DIỄN GIẢI KẾT QUẢ

print("Thống kê kiểm định t=", t_statistic)

print("Với độ tin cậy là 95% thì giả thuyết Ho đúng với xác suất ý nghĩa p=",p_value)