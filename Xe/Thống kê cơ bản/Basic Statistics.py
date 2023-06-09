import pandas as pd 


def thong_ke():

    #   Đọc dữ liệu từ file excel
    data = pd.read_excel("C:/Users/88690/Downloads/honda_sell_data.xlsx")

    #   Lọc cột giá
    cot_gia = data["Price"]

    #   Tính doanh thu trung bình
    trung_binh = cot_gia.mean()

    #   Tìm ra Mẫu xe có giá cao nhất 
    gia_cao_nhat = cot_gia.max()
    index_gia_cao_nhat = cot_gia.idxmax()
    mau_xe_gia_cao_nhat = data.loc[index_gia_cao_nhat, 'Model']
    nam_gia_cao_nhat = data.loc[index_gia_cao_nhat, 'Year']

    #   Tìm ra Mẫu xe có giá thấp nhất
    gia_thap_nhat = cot_gia.min()
    index_gia_thap_nhat = cot_gia.idxmin()
    mau_xe_gia_thap_nhat = data.loc[index_gia_thap_nhat, 'Model']
    nam_gia_thap_nhat = data.loc[index_gia_thap_nhat, 'Year']

    #   Tính trung vị cột giá
    trung_vi = cot_gia.median()

    #   Bảng phân tổ
    nhom_gia = data.groupby(['Price', 'Year', 'Model'])

    #   Hiển thị kết quả
    print("Doanh thu trung bình của Hãng là:", trung_binh)

    print("Giá xe cao nhất:")
    print("  - Mẫu xe:", mau_xe_gia_cao_nhat)
    print("  - Năm:", nam_gia_cao_nhat)
    print("  - Mức giá:", gia_cao_nhat)

    print("Giá xe thấp nhất:")
    print("  - Mẫu xe:", mau_xe_gia_thap_nhat)
    print("  - Năm:", nam_gia_thap_nhat)
    print("  - Mức giá:", gia_thap_nhat)

    print("Trung vị giá:", trung_vi)

    for gia, nhom in nhom_gia:
        print("Giá:", gia)
        print(nhom)
    

thong_ke()


