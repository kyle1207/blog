import random

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def login(request):
    return render(request, "login.html")


def get_validCode_img(request):
    def get_random_color():
        return (random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255),)

    # 方式一：
    # with open("imgname.jpg", "rb") as f:
    #     data = f.read()
    # return HttpResponse(data)

    # 方式二：文件操作 -- 磁盘操作教慢
    # from PIL import Image
    # img = Image.new("RGB", (270, 40), color=get_random_color())
    #
    # with open("validCode.png", "wb") as f:
    #     img.save(f, "png")
    #
    # with open("validCode.png", "rb") as f:
    #     data = f.read()
    #
    # return HttpResponse(data)

    # 方式三：
    # from PIL import Image
    # from io import BytesIO
    # img = Image.new("RGB", (270, 40), color=get_random_color())

    # 内存处理
    # f = BytesIO()
    # img.save(f, "png")
    # data = f.getvalue()
    # return HttpResponse(data)

    # 方式四：
    from PIL import Image, ImageDraw, ImageFont
    from io import BytesIO
    import random
    img = Image.new("RGB", (270, 40), color=get_random_color())
    draw = ImageDraw.Draw(img)
    kumo_font=ImageFont.truetype("static/font/kumo.ttf", size=36)

    for i in range(5):
        random_num = str(random.randint(0,9))
        random_low_alpha = chr(random.randint(95,122))
        random_upper_alpha = chr(random.randint(65,90))
        random_char = random.choice([random_num,random_low_alpha,random_upper_alpha])
        #draw.text((0,5),"python",get_random_color(),font=kumo_font)
        draw.text((i*46+20,5),random_char,get_random_color(),font=kumo_font)
    # width=270
    # height=40
    # for i in range(10):
    #     x1=random.randint(0,width)
    #     x2=random.randint(0,width)
    #     y1=random.randint(0,height)
    #     y2=random.randint(0,height)
    #     draw.line((x1,y1,x2,y2),fill=get_random_color())
    #
    # for i in range(100):
    #     draw.point([random.randint(0, width), random.randint(0, height)], fill=get_random_color())
    #     x = random.randint(0, width)
    #     y = random.randint(0, height)
    #     draw.arc((x, y, x + 4, y + 4), 0, 90, fill=get_random_color())
    #

    f = BytesIO()
    img.save(f, "png")
    data = f.getvalue()
    return HttpResponse(data)