from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import * # ImageClip
from PIL import Image

thumbnail_dir = os.path.join(SAMPLE_OUTPUTS, "thumbnails")
thumbnail_per_frame_dir = os.path.join(SAMPLE_OUTPUTS, "thumbnails-per-frame")
thumbnail_per_half_second_dir = os.path.join(SAMPLE_OUTPUTS, "thumbnails-per-half-second")
output_video = os.path.join(SAMPLE_OUTPUTS, 'thumbs.mp4')

this_dir = os.listdir(thumbnail_dir)
filepaths = [os.path.join(thumbnail_dir, fname) for fname in this_dir if fname.endswith("jpg")]

directory = {}

for root, dirs, files in os.walk(thumbnail_per_frame_dir):
    for fname in files:
        filepath = os.path.join(root, fname)
        try:
            key = float(fname.replace(".jpg", ""))
        except:
            key = None
        if key != None:
            directory[key] = filepath

new_paths = []
for k in sorted(directory.keys()):
    filepath = directory[k]
    new_paths.append(filepath)

my_clips = []
for path in list(new_paths):
    frame = ImageClip(path)
    my_clips.append(frame.img)


clip = ImageSequenceClip(my_clips, fps=22)
clip.write_videofile(output_video)