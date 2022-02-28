from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from fpdf import FPDF
import os
 
# Open an Image
img = Image.open('1.jpg')
# Call draw Method to add 2D graphics in an image
I1 = ImageDraw.Draw(img)
font_bold = ImageFont.truetype('MYRIADPRO-BOLD.OTF', 45)
font_normal  = ImageFont.truetype('MYRIADPRO-REGULAR.OTF', 45)

# Add Text to an image
I1.text((630, 510), "MR. SHIBL NASSER PALAVILA",font = font_bold ,fill=(0, 0, 0))
I1.text((630, 580), "7825132",font = font_normal ,fill=(0, 0, 0))
I1.text((630, 650), "21Y / Male - 11/06/2000",font = font_normal ,fill=(0, 0, 0))
I1.text((2350, 510), "CMP61401322",font = font_bold ,fill=(0, 0, 0))
I1.text((2350, 580), "26/Feb/2021 10:30 AM",font = font_normal ,fill=(0, 0, 0))
I1.text((2350, 650), "CMP61401322",font = font_normal ,fill=(0, 0, 0))
I1.text((2350, 720), "CMP61401322",font = font_normal ,fill=(0, 0, 0))

# Display edited image
img.save("1_temp.jpg")


img = Image.open('2.jpg')

I1 = ImageDraw.Draw(img)
I1.text((630, 510), "MR. SHIBL NASSER PALAVILA",font = font_bold ,fill=(0, 0, 0))
I1.text((630, 580), "7825132",font = font_normal ,fill=(0, 0, 0))
I1.text((630, 650), "21Y / Male - 11/06/2000",font = font_normal ,fill=(0, 0, 0))
I1.text((2350, 510), "CMP61401322",font = font_bold ,fill=(0, 0, 0))
I1.text((2350, 580), "26/Feb/2021 10:30 AM",font = font_normal ,fill=(0, 0, 0))
I1.text((2350, 650), "CMP61401322",font = font_normal ,fill=(0, 0, 0))
I1.text((2350, 720), "CMP61401322",font = font_normal ,fill=(0, 0, 0))



copy_image = Image.open('qr.png')
copy_image = copy_image.resize((300,300))
back_im = img.copy()
back_im.paste(copy_image, (160,2450))
back_im.save("2_temp.jpg")

imagelist = ['1_temp.jpg', '2_temp.jpg']
pdf = FPDF()
    # imagelist is the list witsh all image filenames
for image in imagelist:
    pdf.add_page()
    pdf.image(image,0,0,210,297)
pdf.output('final.pdf', "F")

os.remove(imagelist[0])
os.remove(imagelist[1])

 
# Save the edited image
