from PIL import Image
# import split_folders
import os


# resize all images to 72 pixel height
def resize_image(input_dir, infile, file_name, output_dir="resized"):
    extension = os.path.splitext(infile)[1]

    try:
        img = Image.open(input_dir + '/' + infile)
        width, height = img.size
        width = int(72.0 / height * width)
        img = img.resize((width, 72))
        new_file = output_dir + "/" + file_name + extension
        img.save(new_file)
    except IOError:
        print("unable to resize image {}".format(infile))


if __name__ == "__main__":
    input_dir = '/home/sihui/Documents/OfficeHomeDataset_10072016'
    output_dir = input_dir + '_resized'
    full_input_dir = input_dir
    subs = ["Art", "Product", "Real World"]
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    try:
        for file in os.listdir(full_input_dir):
            print('file: {}'.format(file))
    except OSError:
        print('file not found')
    try:
        classes = os.listdir(full_input_dir + "/" + subs[0])
        classes.sort()
        j = 1
        for c in classes:
            i = 1
            oo = str(j)
            while len(oo) < 4:
                oo = "0" + oo
            for sub_folder in subs:
                dir = full_input_dir + "/" + sub_folder + "/" + c
                out_dir = output_dir + "/" + oo
                if not os.path.exists(out_dir):
                    os.mkdir(out_dir)
                files = os.listdir(dir)
                files.sort()
                for file in files:
                    of = str(i)
                    while len(of) < 5:
                        of = "0" + of
                    resize_image(dir, file, of, out_dir)
                    i = i+1
            j = j+1
    except OSError:
        print('file not found')

# split_folders.ratio('input_folder', output="output", seed=1337, ratio=(.8, .1, .1)) # default values
