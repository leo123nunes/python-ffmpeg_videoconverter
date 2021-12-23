import fnmatch, os, subprocess

origin_path = input('Digite a pasta onde está o vídeo para converter: ')
converted_path = os.path.join(origin_path, 'converted_videos')
video_type = input(f'Digite o tipo de vídeo que deseja converter: ')

ffmpeg_command = 'ffmpeg'
video_codec = '-c:v libx264'
crf = '-crf 23'
preset = '-preset ultrafast'
audio_codec = '-c:a aac'
audio_bitrate = '-b:a 320k'
debug = '-ss 00:00:00 -to 00:00:10'

if not os.path.exists(origin_path):
    raise FileNotFoundError(f'O diretório de origem {origin_path} não existe.')

for dirpath, dirnames, filenames in os.walk(origin_path):

    for filename in filenames:

        if fnmatch.fnmatch(filename, f'*.{video_type}') and dirpath != converted_path:

            if not os.path.exists(converted_path):
                os.mkdir(converted_path)

            input_path = os.path.join(dirpath, filename)
            output_path = os.path.join(converted_path, f'converted_{filename}')
            
            command = f'{ffmpeg_command} -i "{input_path}" {video_codec} {crf} ' \
                f'{preset} {audio_codec} {audio_bitrate} {debug} "{output_path}"'


            try:
                ret_code = subprocess.call(command, shell=True)

                if ret_code != 0:
                    raise Exception(f'Ocorreu um erro ao tentar converter o video: {filename}')

            except Exception as e:
                print(e)


