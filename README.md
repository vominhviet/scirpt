#  Ghi hinh tu nhieu camera RTSP bang Python va FFmpeg

Script nay giup ghi hinh tu nhieu camera RTSP dong thoi. Moi camera se duoc ghi thanh tung file video 1 gio, va luu vao thu muc theo ngay va gio.

---

##  Tinh nang

- Ghi hinh dong thoi tu nhieu camera RTSP
- Su dung FFmpeg de luu video khong nen lai (copy codec)
- Luu file video vao thu muc co ten theo dinh dang `YYYY-MM-DD_HH`
- Lap lai tu dong sau moi gio ghi
- In log ra console de giam sat


## cài đặt python 3.6 trở lên
- cài đặt trên trang chủ của python
 https://www.python.org/ftp/python/3.13.5/python-3.13.5-amd64.exe

- kiểm tra version
```bash
python --version
```

---

## cài đặt ffmpeg 
- cài đặt trên trang chủ của ffmpeg
https://www.gyan.dev/ffmpeg/builds/

- kiểm tra version
```bash
ffmpeg -version
```
---
## chạy script
```bash
python main.py
```

## stop script
``` bash 
q
```
