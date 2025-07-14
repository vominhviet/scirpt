import subprocess
import re
from datetime import datetime

# Đọc danh sách RTSP từ file
def read_rtsp_links(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip()]

# Tách IP từ link RTSP
def extract_ip(rtsp_url):
    match = re.search(r'rtsp://([^/:]+)', rtsp_url)
    return match.group(1).replace('.', '_') if match else "unknown_cam"

# Chụp 1 khung hình từ RTSP stream
def snapshot_rtsp(rtsp_url):
    ip_name = extract_ip(rtsp_url)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"{ip_name}_{timestamp}.jpg"

    ffmpeg_cmd = [
        "ffmpeg",
        "-rtsp_transport", "tcp",  # Sử dụng TCP để ổn định
        "-i", rtsp_url,
        "-frames:v", "1",          # Chỉ lấy 1 khung hình
        "-q:v", "2",               # Chất lượng ảnh (1 là cao nhất, 31 là thấp nhất)
        output_file,
        "-y"                       # Ghi đè nếu file tồn tại
    ]

    print(f"📸 Capturing snapshot from {rtsp_url} -> {output_file}")
    subprocess.run(ffmpeg_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# MAIN
if __name__ == "__main__":
    rtsp_file = "rtsp_sala.txt"  # File chứa danh sách RTSP
    rtsp_links = read_rtsp_links(rtsp_file)

    for rtsp_url in rtsp_links:
        try:
            snapshot_rtsp(rtsp_url)
        except Exception as e:
            print(f"❌ Error capturing from {rtsp_url}: {e}")
