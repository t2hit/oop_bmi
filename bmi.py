class BMI:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def calculate_bmi(self):
        # BMIの計算式を返す　体重÷身長2乗
        return self.weight / (self.height ** 2)

# BMIクラスのインスタンス化
tanaka_bmi = BMI(height=1.80, weight=67.0)
sasami_bmi = BMI(height=1.58, weight=80.0)

print(tanaka_bmi.calculate_bmi())
print(sasami_bmi.calculate_bmi())

