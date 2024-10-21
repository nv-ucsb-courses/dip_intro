from PIL import Image

def Flop(A:Image)->Image:
    # Create a new image by flipping the original image horizontally
    newimg = Image.new("RGBA", A.size)
    newim = newimg.load()

    width = A.size[0]
    height = A.size[1]

    for y in range(height):
        for x in range(width):
            newim[width-1-x, y] = A.getpixel((x, y))
    return newimg

def FLIP(A:Image)->Image:
    # Create a new image by flipping the original image verticvally
    newimg = Image.new("RGBA", A.size)
    newim = newimg.load()

    width = A.size[0]
    height = A.size[1]

    for y in range(height):
        for x in range(width):
            newim[x, height-1-y] = A.getpixel((x, y))
    return newimg

def Atop(A,B):
    # Create a new image by placing image A on top of image B
    # A - source image, B - destination image
   
    # Convert the images to RGBA mode
    if A.mode != "RGBA":
        A = A.convert("RGBA")
    if B.mode != "RGBA":
        B = B.convert("RGBA")

    # Resize the source image to the size of the destination image
    if A.size != B.size:
        A = A.resize(B.size)
    
    newimg = Image.new("RGBA", B.size)
    newim = newimg.load()

    width = B.size[0]
    height = B.size[1]

    # Asrc⋅[s]+Adest⋅[d]+Aboth⋅[b]
    # Asrc=αs⋅(1−αd)Adst=αd⋅(1−αs)Aboth=αs⋅αd

    for y in range(height):
        for x in range(width):
            R_src, G_src, B_src, Alpha_src = A.getpixel((x, y)) # RGBA values of image A
            R_dest, G_dest, B_dest, Alpha_dest = B.getpixel((x, y)) # RGBA values of image B

            # Normalize the alpha values to be between 0 and 1
            Alpha_src = Alpha_src/255
            Alpha_dest = Alpha_dest/255

            A_src = Alpha_src*(1-Alpha_dest)
            A_dest = Alpha_dest*(1-Alpha_src)
            A_both = Alpha_src*Alpha_dest

            R_new = int(A_src*0 + A_dest*R_dest + A_both*(R_src))
            G_new = int(A_src*0 + A_dest*G_dest + A_both*(G_src))
            B_new = int(A_src*0 + A_dest*B_dest + A_both*(B_src))
            Alpha_new = int(255*(A_src*Alpha_src + A_dest*Alpha_dest + A_both*(Alpha_src*Alpha_dest)))

            newim[x, y] = (R_new, G_new, B_new, Alpha_new)
            
    return newimg

def Over(A,B):
    # Create a new image by placing image A on top of image B
    # A - source image, B - destination image
   
    # Convert the images to RGBA mode
    if A.mode != "RGBA":
        A = A.convert("RGBA")
    if B.mode != "RGBA":
        B = B.convert("RGBA")

    # Resize the source image to the size of the destination image
    if A.size != B.size:
        A = A.resize(B.size)
    
    newimg = Image.new("RGBA", B.size)
    newim = newimg.load()

    width = B.size[0]
    height = B.size[1]

    for y in range(height):
        for x in range(width):
            R_src, G_src, B_src, Alpha_src = A.getpixel((x, y)) # RGBA values of image A
            R_dest, G_dest, B_dest, Alpha_dest = B.getpixel((x, y)) # RGBA values of image B

            # Normalize the alpha values to be between 0 and 1
            Alpha_src = Alpha_src/255
            Alpha_dest = Alpha_dest/255

            A_src = Alpha_src*(1-Alpha_dest)
            A_dest = Alpha_dest*(1-Alpha_src)
            A_both = Alpha_src*Alpha_dest

            R_new = int(A_src*R_src + A_dest*R_dest + A_both*(R_src))
            G_new = int(A_src*G_src + A_dest*G_dest + A_both*(G_src))
            B_new = int(A_src*B_src + A_dest*B_dest + A_both*(B_src))
            Alpha_new = int(255*(A_src*Alpha_src + A_dest*Alpha_dest + A_both*(Alpha_src*Alpha_dest)))

            newim[x, y] = (R_new, G_new, B_new, Alpha_new)
            
    return newimg


if __name__ == "__main__":
    # Open an image file
    img=Image.open("HW2_Background1.jpg")

    #Call the function FLIP
    flip_img=FLIP(img)
    flip_img.show()

    #Call the function Flop
    flop_img=Flop(img)
    flop_img.show()

    src_img=Image.open("HW2_source.png")      
    dest_img=Image.open("HW2_dest.png")

    #Call the function Atop
    atop_img=Atop(src_img,dest_img)
    atop_img.show()

    #Call the function Over
    over_img=Over(src_img,dest_img)
    over_img.show()

    out = Atop(FLIP(dest_img), Flop(src_img))
    out.show()

    out = Atop(Flop(src_img), Flop(dest_img))
    out.show()
    