
def load_data(data_folder):

    text_file_path = f'{data_folder}/captions.txt'

    class_file_path = f'{data_folder}/classes.txt'

    # Open the caption.txt file and read its contents
    with open(text_file_path) as f1:
        lines = f1.readlines()

    # Open the other text file and read its contents
    with open(class_file_path) as f2:
        descriptions = f2.readlines()

    # Create a dictionary mapping image class numbers to image class text descriptions
    class_dict = {}
    for line in descriptions:
        image_class = line[:3]
        class_text = line[4:].strip()
        class_dict[image_class] = class_text

    # Append the image class text to each image name in caption.txt
    for i, line in enumerate(lines):
        image_name = line.strip()
        image_class = image_name[:3]
        class_text = class_dict.get(image_class, 'unknown')
        new_line = f"{image_name},{class_text}\n"
        lines[i] = new_line

    # Write the updated lines to caption.txt
    with open(text_file_path, 'w') as f3:
        f3.writelines(lines)

