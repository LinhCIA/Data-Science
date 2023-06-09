"""
    Top 10 mẫu xe bán chạy nhất của hãng
"""
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px 


#   BƯỚC 1: ĐỌC DỮ LIỆU
def doc_du_lieu():
    # Đường dẫn tới file excel cần đọc
    path = "C:/Users/88690/Downloads/honda_sell_data.csv"

    try:
        # Đọc file excel bằng pandas
        df = pd.read_csv(path)

        # Kiểm tra kích thước của file excel
        if df.shape[0] > 100000:
            raise ValueError("Kích thước file excel quá lớn.")

        # # Kiểm tra trường hợp dữ liệu bị thiếu hoặc lỗi
        # if df.isnull().values.any() or df.dtypes.apply(
        #         lambda x: x.replace('$', '').replace(',', b'').replace('Not Priced', '0')).astype(int):
        #     raise ValueError("File excel chứa dữ liệu thiếu hoặc lỗi.")

        return df

        # Xử lý dữ liệu

    except FileNotFoundError:
        print("File excel không tồn tại hoặc đường dẫn không đúng.")
    except PermissionError:
        print("Bạn không có quyền truy cập file excel.")
    except ValueError as e:
        print(str(e))
    except Exception as e:
        print("Đã có lỗi xảy ra: ", str(e))


#   BƯỚC 2: VẼ BIỂU ĐỒ TOP 10 MẪU XE BẠN CHẠY NHẤT TỪ NĂM 1981-2023
def bieu_do_2():
    data = doc_du_lieu()
    
    # Phân tổ mức xếp hạng đánh giá theo mẫu
    a = data["Model"].value_counts()

    # Bảng Top 10 mẫu xe bán chạy nhất
    print(a.head(10))

    # Vẽ biểu đồ
    a.sort_values().tail(10).plot.barh(color='blue')
    plt.title("Top 10 mẫu xe bán chạy nhất từ năm 1981-2023")
    plt.show()
    

bieu_do_2()