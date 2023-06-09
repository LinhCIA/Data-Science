"""
    Bài toán ước lượng số 6: 
Với chính sách mới của hãng, tỉ lệ xe cũ bán ra có thay đổi.
"""

# Tỉ lệ xe củ bán ra từ năm 2022 trở về trước
t1 = (193/340)*100
print("Từ năm 2022 trở về trước, tỷ lệ xe cũ bán ra:",t1,"%")

# Tỉ lệ xe củ bán ra từ năm 2022 trở về sau
t2 = (13/569)*100
print("Từ năm 2022 trở về sau:",t2,"%")

# kiểm tra
if t1 >= t2:
    print("Tỉ lệ xe cũ có xu hướng giảm => Kiểm định!")
else:
    print("Tỉ lệ xe cũ có xu hướng tăng => Kiểm định!")