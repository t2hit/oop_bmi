class BMI:
    def __init__(self, height, weight):
        # これも最終的に削除
        # self.height = height
        # self.weight = weight
        # そして全selfを削除
        self.value = weight / (height ** 2)

        if not (10 <= self.value <=40):
            raise ValueError("BMIが正常値の範囲を越えています")

    # 上にValueの分を追加したので下は削除する（リファクタリング）
    # def calculate_bmi(self):
    #     # BMIの計算式を返す　体重÷身長2乗
    #     return self.weight / (self.height ** 2)
    def __str__(self):
        return f"{self.value:.2f}"

# BMIクラスのインスタンス化
tanaka_bmi = BMI(height=1.80, weight=67.0)
sasami_bmi = BMI(height=1.58, weight=80.0)
bob_bmi = BMI(height=1.70, weight=75000.0)

print(tanaka_bmi)
print(sasami_bmi)
print(bob_bmi)
