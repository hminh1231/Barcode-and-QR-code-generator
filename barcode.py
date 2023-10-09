import barcode
from barcode.writer import ImageWriter

# Product data
name = 'App1'
project_name = 'Project App 1'
dept = 'App1 Dept'
other = None

# Format data string with delimiters
data = f"{name}|{project_name}|{dept}|{other}"

# Create Code 128 barcode
barcode_maker = barcode.get_barcode_class('code128')
barcoded_data = barcode_maker(data, writer=ImageWriter())

# Save barcode to image file
filename = 'product_barcode'
barcoded_data.save(filename)