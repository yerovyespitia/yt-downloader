import os
import subprocess
from pathlib import Path

# ⚙️ Configuración
input_video = "input.mp4"       # Cambia por el nombre de tu video
output_folder = "cuts"          # Carpeta donde se guardarán los cortes
segment_duration = 4            # Duración de cada clip en segundos

# Crea carpeta de salida
Path(output_folder).mkdir(exist_ok=True)

# 📏 Obtiene duración del video con ffprobe
def get_video_duration(file_path):
    result = subprocess.run(
        ['ffprobe', '-v', 'error', '-show_entries',
         'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', file_path],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )
    return float(result.stdout)

# ✂️ Corta el video en segmentos de 4 segundos
def cut_video(file_path, segment_duration):
    total_duration = get_video_duration(file_path)
    start = 0
    count = 0

    while start < total_duration:
        output_file = os.path.join(output_folder, f"cut_{count:03d}.mp4")
        command = [
            'ffmpeg', '-y',
            '-ss', str(start),  # ← mueve -ss antes de -i
            '-i', file_path,
            '-t', str(segment_duration),
            '-c:v', 'libx264',  # fuerza recodificación de video
            '-c:a', 'aac',      # recodifica audio también
            '-preset', 'fast',
            output_file
        ]
        print(f"Cortando {output_file} desde {start}s")
        subprocess.run(command)
        start += segment_duration
        count += 1

# 🚀 Ejecutar
cut_video(input_video, segment_duration)
