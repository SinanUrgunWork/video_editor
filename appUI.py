import tkinter as tk
from tkinter import filedialog
from moviepy.editor import *
from app import videoMaker  # videoMaker fonksiyonunu nereden aldığınıza dikkat edin

video_entry = None
audio_entry = None
output_entry = None
start_time_entry_video= None
end_time_entry_video= None
start_time_entry_audio= None
end_time_entry_audio = None
video_name_with_extension=None
extension=None
def select_video():
    global video_entry
    video_path = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4")])
    video_entry.delete(0, tk.END)
    video_entry.insert(0, video_path)

def select_audio():
    global audio_entry
    audio_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
    audio_entry.delete(0, tk.END)
    audio_entry.insert(0, audio_path)

def create_video():
    global video_entry, audio_entry, output_entry, video_name_with_extension, extension,start_time_entry_video,end_time_entry_video,start_time_entry_audio,end_time_entry_audio
    video_path = video_entry.get()
    audio_path = audio_entry.get()
    video_name = output_entry.get()
    extension=extension_var.get()
    video_time_start=start_time_entry_video.get()
    video_time_end=end_time_entry_video.get()
    audio_time_start=start_time_entry_audio.get()
    audio_time_end=end_time_entry_audio.get()
    video_name_with_extension=video_name+extension
    print(video_name_with_extension)
    progress_label.config(text="Video oluşturuluyor...")
    root.update() 
    # Çıktı dosyası adı girilmediyse işlem yapma
    if not video_name or not audio_path or not video_path or not extension or not video_time_start or not video_time_end or not  audio_time_start or not audio_time_end:
        error_message = []
        if not video_name:
            error_message.append("bir çıktı adı")
        if not audio_path:
            error_message.append("bir ses")
        if not video_path:
            error_message.append("bir video")
        if not extension:
            error_message.append("bir uzantı")
        if not extension:
            error_message.append("bir Video zaman başlangıc")
        if not extension:
            error_message.append("bir Video zaman bitiş")
        if not extension:
            error_message.append("bir ses zaman giriş")
        if not extension:
            error_message.append("bir ses zaman çıkış")
        tk.messagebox.showerror("Hata", f"Lütfen {', '.join(error_message)} girin!")
    
    videoMaker(video_path, audio_path, video_name_with_extension,video_time_start,video_time_end,audio_time_start,audio_time_end)
    progress_label.config(text="Video oluşturuldu!") 

# Tkinter uygulamasını oluştur
root = tk.Tk()
root.title("Video Oluşturma Arayüzü")

# Arayüz boyutunu ayarla
root.geometry("700x400")

# Stilleri güncelle
root.tk_setPalette(background="#f0f0f0")  # Arka plan rengini değiştir

# Video dosyası seçme bölümü
video_label = tk.Label(root, text="Video Dosyası Seçin:", background="#f0f0f0")
video_label.place(relx=0.1, rely=0.2, anchor="w")
video_entry = tk.Entry(root, width=30)
video_entry.place(relx=0.3, rely=0.2, anchor="w")
video_button = tk.Button(root, text="Seç", command=select_video)
video_button.place(relx=0.75, rely=0.2, anchor="w")

# Video başlangıç zamanı etiketi ve giriş alanı
start_time_label_video = tk.Label(root, text="(Video)Başlangıç Zamanı (dk:sn):", background="#f0f0f0")
start_time_label_video.place(relx=0.1, rely=0.3, anchor="w")
start_time_entry_video = tk.Entry(root, width=10)
start_time_entry_video.place(relx=0.4, rely=0.3, anchor="w")

# Video bitiş zamanı etiketi ve giriş alanı
end_time_label_video = tk.Label(root, text="(Video)Bitiş Zamanı (dk:sn):", background="#f0f0f0")
end_time_label_video.place(relx=0.1, rely=0.4, anchor="w")
end_time_entry_video = tk.Entry(root, width=10)
end_time_entry_video.place(relx=0.4, rely=0.4, anchor="w")
# Ses dosyası seçme bölümü
audio_label = tk.Label(root, text="Ses Dosyası Seçin:", background="#f0f0f0")
audio_label.place(relx=0.1, rely=0.5, anchor="w")
audio_entry = tk.Entry(root, width=30)
audio_entry.place(relx=0.3, rely=0.5, anchor="w")
audio_button = tk.Button(root, text="Seç", command=select_audio)
audio_button.place(relx=0.75, rely=0.5, anchor="w")

# Ses başlangıç zamanı etiketi ve giriş alanı
start_time_label_audio = tk.Label(root, text="(Ses)Başlangıç Zamanı (dk:sn):", background="#f0f0f0")
start_time_label_audio.place(relx=0.1, rely=0.6, anchor="w")
start_time_entry_audio = tk.Entry(root, width=10)
start_time_entry_audio.place(relx=0.4, rely=0.6, anchor="w")

# Ses bitiş zamanı etiketi ve giriş alanı
end_time_label_audio = tk.Label(root, text="(Ses)Bitiş Zamanı (dk:sn):", background="#f0f0f0")
end_time_label_audio.place(relx=0.1, rely=0.7, anchor="w")
end_time_entry_audio = tk.Entry(root, width=10)
end_time_entry_audio.place(relx=0.4, rely=0.7, anchor="w")

# Çıktı dosyası adı giriş bölümü
output_label = tk.Label(root, text="Çıktı Dosyası Adı:", background="#f0f0f0")
output_label.place(relx=0.1, rely=0.8, anchor="w")
output_entry = tk.Entry(root, width=30)
output_entry.place(relx=0.3, rely=0.8, anchor="w")

# Uzantı seçme bölümü
extension_label = tk.Label(root, text="Uzantı Seçin:", background="#f0f0f0")
extension_label.place(relx=0.1, rely=0.9, anchor="w")
extension_var = tk.StringVar(root)
extension_var.set(".mp4")  # Varsayılan uzantı
extension_option = tk.OptionMenu(root, extension_var, ".mp4", ".avi", ".mov")
extension_option.place(relx=0.3, rely=0.9, anchor="w")


progress_label = tk.Label(root, text="", background="#f0f0f0")
progress_label.place(relx=0.5, rely=0.9, anchor="center")
# Oluştur düğmesi
create_button = tk.Button(root, text="Oluştur", command=create_video)
create_button.place(relx=0.7, rely=0.9, anchor="center")

# Uygulamayı çalıştır
root.mainloop()
