import random

# สุ่มเลข 3 ตัวที่อาจจะซ้ำกัน
random_numbers = [random.randint(0, 10) for _ in range(3)]

# คูณเลขทั้งหมด
product = 1
for number in random_numbers:
    product *= number

# หารด้วย 3
result = product / 3

print("เลขสุ่ม:", random_numbers)
print("ผลคูณ:", product)
print("ผลหารด้วย 3:", result)