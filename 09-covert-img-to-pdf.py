import sys
import img2pdf
import os

filepath = sys.argv[1]
if os.path.isdir(filepath):
    with open("converted_img_to_pdf.pdf", 'wb') as f:
        imgs = []
        for fname in os.listdir(filepath):
            if not fname.endswith('.jpg'):
                continue
            path = os.path.join(filepath, fname)
            if os.path.isdir(path):
                continue
            imgs.append(path)
        f.write(img2pdf.convert(imgs))
elif os.path.isfile(filepath):
    if filepath.endswith('.jpg'):
        with open("converted_img_to_pdf.pdf", 'wb') as f:
            f.write(img2pdf.convert(filepath))
else:
    print("please input file or dir")

# Important 
# If your code is named "09-covert-img-to-pdf.py" and your images are in a folder named "images_to_convert.jpg", you'd run the code like this:
# python 09-covert-img-to-pdf.py images_to_convert
