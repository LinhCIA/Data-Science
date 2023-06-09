"""
    Bài toán kiểm định số 6:
Với chính sách bán hàng mới của Hãng, tỷ lệ xe cũ bán ra có thay đổi.
    Phương pháp để giải bài toán này là: Kiểm định tỉ lệ
    Giả thuyết H0: Tỷ lệ xe cũ bán ra thay đổi
    Đối thuyết H1: Tỷ lệ xe cũ bán ra không thay đổi.
"""


from statsmodels.stats.proportion import proportions_ztest
import numpy as np


# BƯỚC 1: TẠO DỮ LIỆU

# dữ liệu kể từ năm 2022 về trước
sample_success_a, sample_size_a = (190, 500)
# dữ liệu kể từ năm 2022 trở về sau
sample_success_b, sample_size_b = (130, 400)

# Cố định dữ liệu
successes = np.array([sample_success_a, sample_success_b])
samples = np.array([sample_size_a, sample_size_b])


# BƯỚC 2: TIẾN HÀNH KIỂM ĐỊNH
z_stat, p_value = proportions_ztest(count=successes,
nobs=samples, alternative='two-sided')

# BƯỚC 3: DIỄN GIẢI KẾT QUẢ
print('z_stat: %0.3f, p_value: %0.3f' % (z_stat, p_value))

