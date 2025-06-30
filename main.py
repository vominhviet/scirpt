import os
import subprocess
import datetime
import threading
import time

# RTSP URLs cho các camera
#RTSP_URLx = "rtsp://user:passwd@IP:Port RTSP/live"
RTSP_URL1 = "rtsp://admin:cxview2025@10.20.5.216:554/live"
RTSP_URL2 = "rtsp://admin:cxview2025@10.20.5.217:554/live"
RTSP_URL3 = "rtsp://admin:cxview2025@10.20.5.218:554/live"
RTSP_URL4 = "rtsp://admin:cxview2025@10.20.5.220:554/live"

# Thư mục gốc để lưu video
BASE_DIR = r"D:\video"



def record_camera(rtsp_url, cam_name):
    while True:
     

        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

        # Tạo thư mục lưu theo giờ
        output_dir = os.path.join(BASE_DIR, now.strftime("%Y-%m-%d_%H"))
        os.makedirs(output_dir, exist_ok=True)

        output_file = os.path.join(output_dir, f"{cam_name}_{timestamp}.mp4")
        print(f"[INFO] Bắt đầu ghi {cam_name} vào {output_file}")

        cmd = [
            "ffmpeg",
            "-rtsp_transport", "tcp",
            "-i", rtsp_url,
            "-t", "3600",  # Ghi đúng 1 giờ (3600 giây)
            "-vcodec", "copy",
            "-acodec", "copy",
            output_file
        ]

        try:
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            for line in process.stdout:
                print(f"[{cam_name}] {line.strip()}")
            process.wait()
        except Exception as e:
            print(f"[ERROR] Lỗi khi ghi {cam_name}: {e}")

        print(f"[INFO] Đã ghi xong 1 giờ video cho {cam_name}. Chuẩn bị lặp lại...")

# Tạo các luồng để ghi nhiều camera song song
threads = [
    threading.Thread(target=record_camera, args=(RTSP_URL1, "ED_cam_1")),
    threading.Thread(target=record_camera, args=(RTSP_URL2, "ED_cam_2")),
    threading.Thread(target=record_camera, args=(RTSP_URL3, "SB_cam_1")),
    threading.Thread(target=record_camera, args=(RTSP_URL4, "SB_cam_2"))
]

for t in threads:
    t.start()

for t in threads:
    t.join()
#dung commad q để tắt
