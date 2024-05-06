from PIL import Image
import os
import random


# data & 저장 경로
image_dir = "C:/Users/mjhoy/PycharmProjects/salt-pepper_noise_add/data"
output_dir = "C:/Users/mjhoy/PycharmProjects/salt-pepper_noise_add/data_noise"

# data_noise 폴더 생성
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def add_salt_and_pepper_noise(image, salt_colors, pepper_colors, salt_prob, pepper_prob, noise_size):
    noisy_image = image.copy()
    width, height = noisy_image.size
    pixels = noisy_image.load()

    # salt noise 설정
    num_salt = int(salt_prob * width * height) #소금 확률에 따라 생성할 소금의 수 계산
    for i in range(num_salt):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        salt_color = random.choice(salt_colors)
        for i in range(x - noise_size, x + noise_size):
            for j in range(y - noise_size, y + noise_size):
                if 0 <= i < width and 0 <= j < height:
                    pixels[i, j] = salt_color

    # pepper noise 설정
    num_pepper = int(pepper_prob * width * height) #후추 확률에 따라 생성할 소금의 수 계산
    for _ in range(num_pepper):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        pepper_color = random.choice(pepper_colors)
        for i in range(x - noise_size, x + noise_size):
            for j in range(y - noise_size, y + noise_size):
                if 0 <= i < width and 0 <= j < height:
                    pixels[i, j] = pepper_color

    return noisy_image

# 소금 & 후추 확률 설정
salt_prob = 0.008
pepper_prob = 0.008

# 노이즈 색(빨간색, 노란색, 초록색, 파란색)
salt_colors = [(255, 0, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255)]
pepper_colors = [(255, 0, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255)]

# noise 생성 과정
count = 0  # 이미지 처리 횟수를 추적하는 변수
for filename in os.listdir(image_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):  # file이 image인지 체크하기
        count += 1  # 이미지 처리 횟수를 증가시킴

        # img 불러오기
        image_path = os.path.join(image_dir, filename)
        image = Image.open(image_path)

        # salt-pepper noise 추가
        noisy_image = add_salt_and_pepper_noise(image, salt_colors, pepper_colors, salt_prob, pepper_prob, noise_size=2)

        # img 저장
        output_path = os.path.join(output_dir, filename)
        noisy_image.save(output_path)

        print(f"Image {count}: {filename} was saved in {output_path}")

print("Noise addition complete.")