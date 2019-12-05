from PIL import Image
# import split_folders
import os


# resize all images to 72 pixel height
def resize_image(input_dir, infile, output_dir="resized", size=(320, 180)):
    outfile = os.path.splitext(infile)[0]
    extension = os.path.splitext(infile)[1]

    try:
        img = Image.open(input_dir + '/' + infile)
        width, height = img.size
        width = int(72.0 / height * width)
        img = img.resize((width, 72))
        new_file = output_dir + "/" + outfile + extension
        img.save(new_file)
    except IOError:
        print("unable to resize image {}".format(infile))


if __name__ == "__main__":
    dir = os.getcwd()
    input_dir = '/home/sihui/Documents/OfficeHomeDataset_10072016'
    output_dir = input_dir + '_resized'
    full_input_dir = input_dir
    if not os.path.exists(os.path.join(dir, output_dir)):
        os.mkdir(output_dir)
    try:
        for file in os.listdir(full_input_dir):
            print('file: {}'.format(file))
    except OSError:
        print('file not found')
    try:
        i = 1
        for subdir in os.listdir(full_input_dir):
            oo = str(i)
            while len(oo) < 4:
                oo = "0" + oo
            full_subdir = output_dir+"/"+ oo
            subdir_input = full_input_dir+"/"+subdir
            if not os.path.exists(full_subdir):
                os.mkdir(full_subdir)
            for file in os.listdir(subdir_input):
                resize_image(subdir_input, file, full_subdir)
            i = i+1
    except OSError:
        print('file not found')

# split_folders.ratio('input_folder', output="output", seed=1337, ratio=(.8, .1, .1)) # default values
