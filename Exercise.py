# กำหนดช่วงของเลข
start = 21
end = 40

# สร้างลิสต์สำหรับเลขคู่และเลขคี่
odd_numbers = []
even_numbers = []

# วนลูปผ่านช่วงของเลข
for number in range(start, end + 1):
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

# แสดงผลลัพธ์
print("เลขจำนวนคี่:", odd_numbers)
print("เลขจำนวนคู่:", even_numbers)
