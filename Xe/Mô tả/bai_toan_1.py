"""
    Bài toán về Tổng lượng xe bán ra trong 10 năm qua
"""
import pandas as pd
import matplotlib.pyplot as plt


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


# Bước 2: Lập bảng phân tổ
def phan_to_1():
    data = doc_du_lieu()
    # Phân tổng số sản phẩm bán đã theo năm
    grouped_data = data.groupby('Year').agg({'Consumer_Car': 'sum'})

    # In kết quả
    print(grouped_data[23:33])

    # Đường dẫn tới file Excel để lưu bảng phân tổ dữ liệu
    output_file_path = "path/to/output/excel/file.xlsx"
    # thực tế là:  "C:/Users/88690/Downloads/tong_luong_xe_ban_ra.xlsx"

    # Tạo đối tượng ExcelWriter để ghi dữ liệu vào file Excel
    writer = pd.ExcelWriter(output_file_path, engine='xlsxwriter')

    # Ghi bảng phân tổ dữ liệu vào file Excel
    grouped_data.to_excel(writer, sheet_name='Sheet1')

    # Lưu file Excel
    writer.save()

    print("Lưu bảng phân tổ dữ liệu vào file Excel thành công!")


# Bước 3: Vẽ biểu đồ
def bai_toan_1():
    data = {'Năm': ['', '2014', '2015', '2016', '2017', '2018', '2019',
                    '2020', '2021', '2022', '2023'],
            'Lượng xe bán ra': ['0', '47111', '92760', '96828', '177484', '299960', '449964',
                                '446272', '429435', '1766144', '2345155']
            }

    df = pd.DataFrame(data, columns=['Năm', 'Lượng xe bán ra'])

    new_colors = ['green', 'blue', 'purple', 'brown', 'teal', 'grey', 'pink',
                  'orange', 'aqua', 'maroon', 'red']

    plt.bar(df['Năm'], df['Lượng xe bán ra'], color=new_colors)
    plt.title('Tổng lượng xe bán ra trong 10 năm qua', fontsize=14)
    plt.xlabel('Năm', fontsize=15)
    plt.ylabel('Lượng xe bán ra', fontsize=15)
    plt.grid(True)
    plt.show()


bai_toan_1()