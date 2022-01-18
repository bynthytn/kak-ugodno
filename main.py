import os

path = "X:\\_cereal\\nobe"
destination = f'{path}\\subtitles'
files = os.listdir(path)

for i in files:
    for j in os.listdir(f'{path}\\{i}'):
        if j.endswith('.srt'):
            dst = f'{destination}\\{j}'
            src = f'{path}\\{i}\\{j}'
            os.rename(src, dst)
