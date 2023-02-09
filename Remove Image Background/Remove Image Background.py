from rembg import remove
from PIL import Image
input_path = '.jpg'
output_path = '.png'
input Image.open(input_path)
output = remove(input)
output.save(output_path)