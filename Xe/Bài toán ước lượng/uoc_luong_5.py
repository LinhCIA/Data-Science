"""
    Bài toán ước lượng số 5: Ước lượng kỳ vọng
Ước lượng giá thành trung bình của mẫu xe Civic Sport có sự khác biệt so với giá thành 
trung bình của mẫu xe Pilot Sport.
"""
import pandas as pd 





# BƯỚC 1: LỌC DỮ LIỆU MẪU XE CIVIC SPORT VÀ PILOT SPORT TỪ TỔNG THỂ 
df = pd.read_excel("C:/Users/88690/Downloads/honda_sample.xlsx")    # đọc dữ liệu

# Dữ liệu của xe Civic Sport
data_civic = df[df["Model"] == "Civic Sport"]["Price"]
# Dữ liệu của xe Pilot Sport
data_pilot = df[df["Model"] == "Pilot Sport"]["Price"]


# BƯỚC 2: TIẾN HÀNH ƯỚC LƯỢNG 
print("Giá trung bình của mẫu xe Civic Sport:", data_civic.mean())
print("Giá trung bình của mẫu xe Pilot Sport:", data_pilot.mean())
d = abs(data_civic.mean() - data_pilot.mean())
print("Giá trung bình khác biệt giữa hai mẫu xe:", d)


# BƯỚC 3: DIỄN GIẢI KẾT QUẢ
if d > 10000:
    print("Tiến hành kiểm định!")
else:
    print("Không cần kiểm định!")
