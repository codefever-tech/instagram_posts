from barcode import Code128  
from barcode.writer import ImageWriter  
barcode = Code128("123456789", writer=ImageWriter())  
barcode.save("barcode")  
