from PIL import Image

file = "G:\\编程\\python\\图片转字符串\\medal.png"
ascii_char = list("~!@#$%^&*()_+`123456789?-=qwertyuiop[]\asdfghjkl;'zxcvbnm,./{}|:H<>0")  #设置要转换的字符串
#根据RGBA值获得转换的字符串
def get_char(r,g,b,alpha):      
    if alpha == 0:
        return " "
    length = len(ascii_char)
    val = int(0.2126*r+0.7152*g+0.0722*b)                                               #RGB值进行灰度值转换
    uint = 257.0/length
    return ascii_char[int(val/uint)]

if __name__ == "__main__":
    im = Image.open(file)                                                               #打开图像文件
    im = im.resize((102,80))                                                            #重新对图像进行大小设置，防止图像太大显示效果不好
    width,height = im.size
    txt = ""
    for i in range(height):
        for j in range(width):
            temp = get_char(*im.getpixel((j,i)))                                        #注意星形表达式用法，此外还要注意图像宽度和高度，以及换行
            txt += temp
        txt += '\n'
    print(txt)
    with open("G:\\编程\\python\\图片转字符串\\output.txt","w") as f:
        f.write(txt)
    
