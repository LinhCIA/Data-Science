"""
    Biểu đồ thị phần toàn cầu của hãng
"""
import pandas as pd
import country_converter as coco
import matplotlib.pyplot as plt
from wordcloud import WordCloud



from iii import anh
# Đọc dữ liệu
data = pd.read_csv("C:/Users/88690/Downloads/honda_sell_data.csv")
# Chuyển đổi vị trí của các hãng sang bãng mã quốc gia 3166
country = coco.convert(names = data['Make'], to = "ISO3")
# Vẽ biểu đồ
plt.title("Thương hiệu xe hơi được tìm kiếm nhiều nhất")
anh()
plt.show()