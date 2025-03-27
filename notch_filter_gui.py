import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

class NotchFilterGUI:
   def __init__(self, image_path):
       # Tkinter 창 초기화
       self.root = tk.Tk()
       self.root.title("Contour Notch Filter Control")
       
       # 프레임 생성
       self.top_frame = ttk.Frame(self.root)
       self.top_frame.pack(fill=tk.X, padx=5, pady=5)
       
       # 주파수 표시 라벨 초기화
       self.freq_label = ttk.Label(self.top_frame, text="Notch Frequency: 0")
       self.freq_label.pack(side=tk.LEFT)
       
       # 이미지 로드 및 윤곽선 추출
       self.img = cv2.imread(image_path)
       gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
       _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
       self.contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
       
       # 푸리에 디스크립터 계산
       self.fourier_descs = []
       for contour in self.contours:
           complex_contour = contour[:, 0, 0] + 1j * contour[:, 0, 1]
           fourier_desc = np.fft.fft(complex_contour)
           self.fourier_descs.append(fourier_desc)
       
       # matplotlib 설정
       self.fig, (self.ax1, self.ax2) = plt.subplots(1, 2, figsize=(12, 5))
       self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
       self.canvas.draw()
       self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
       
       # 마우스 이벤트 연결
       self.canvas.mpl_connect('motion_notify_event', self.on_mouse_move)
       
       # 초기 플롯
       self.update_plot(50)
       
   def apply_notch_filter(self, fourier_desc, notch_freq, width=5):
       filtered = fourier_desc.copy()
       n = len(filtered)
       
       # 노치 필터 적용
       filtered[notch_freq-width:notch_freq+width] = 0
       filtered[n-notch_freq-width:n-notch_freq+width] = 0
       
       return filtered
   
   def update_plot(self, notch_freq):
       # Clear previous plots
       self.ax1.clear()
       self.ax2.clear()
       
       # 원본 윤곽선 플롯
       for contour in self.contours:
           self.ax1.plot(contour[:, 0, 0], contour[:, 0, 1], 'b-')
       self.ax1.set_title('Original Contours')
       self.ax1.axis('equal')
       
       # 필터링된 윤곽선 계산 및 플롯
       for fourier_desc in self.fourier_descs:
           filtered_desc = self.apply_notch_filter(fourier_desc, notch_freq)
           filtered_contour = np.fft.ifft(filtered_desc)
           
           x = filtered_contour.real
           y = filtered_contour.imag
           self.ax2.plot(x, y, 'r-')
           
       self.ax2.set_title('Notch Filtered Contours')
       self.ax2.axis('equal')
       
       # 캔버스 업데이트
       self.canvas.draw()
       
       # 라벨 업데이트
       self.freq_label.config(text=f"Notch Frequency: {notch_freq}")
       
   def on_mouse_move(self, event):
       if event.inaxes:
           # 마우스 x 좌표를 주파수로 변환 (2~100 범위)
           notch_freq = int(max(2, min(100, event.xdata)))
           self.update_plot(notch_freq)
           
   def run(self):
       self.root.mainloop()

# 실행
if __name__ == "__main__":
   image_path = "inverted_gears.jpg"  # Update this path to your image
   app = NotchFilterGUI(image_path)
   app.run()