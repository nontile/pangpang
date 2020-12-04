# # A1, A2 ~ A20
# 
# for i in range(1, 21):
#     if i % 2 == 1:
#         print("A" + str(i), end=" ")

for i in range(1, 21)[::4]:  # 2칸씩 띄워서
    print("A" + str(i), end=" ")