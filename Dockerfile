# Sử dụng image Python chính thức
FROM python:3.11-slim

# Tạo thư mục làm việc
WORKDIR /app

# Cài đặt các gói cần thiết cho Pygame (phải có môi trường hiển thị ảo)
RUN apt-get update && apt-get install -y \
    python3-dev \
    libglu1-mesa-dev \
    libgles2-mesa-dev \
    libgl1-mesa-dev \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

# Copy file requirements
COPY requirements.txt .

# Cài thư viện
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ code
COPY . .

# Chạy game với màn hình ảo (vì AWS không có GUI thật)
CMD xvfb-run -s "-screen 0 800x600x24" python snake_game.py
