"""
    Giá trị trung bình của sản phẩm qua từng năm kèm theo điều kiện
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 


# Bước 1: Đọc dữ liệu
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


#   BƯỚC 2: LẬP BẢNG PHÂN TỔ GIỮA TÌNH TRẠNG XE VÀ GIÁ CẢ
def phan_to_3():
    df = doc_du_lieu()
    condition_car = df.groupby(['Condition','Year']).mean().reset_index()
    return condition_car


#   BƯỚC 3: VẼ BIỂU ĐỒ
def bieu_do_3():
    data = doc_du_lieu()
    fig = plt.figure(figsize=(20,8))
    ax1= fig.add_subplot(121)
    sns.lineplot(data,y='Price',x='Year',hue='Condition')
    ax1.set(title="Price over year based on the condition")
    plt.show()


bieu_do_3()
