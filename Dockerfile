# Sử dụng Python
FROM python:3.10-slim

# Cài đặt thư viện cần thiết
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ mã nguồn
COPY . .

# Mở port Flask
EXPOSE 5000

# Chạy Flask app
CMD ["python", "app.py"]
