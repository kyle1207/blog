# _*_coding: utf-8_*_
#
# @Project_Name:cnblog
# @File_name: validCode
# @author: kyle
# @date: 2021/12/5 0:57
from numpy import random


# 随机函数
def get_random_color():
    return (random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),)


def get_valid_code_img(request):
    # 方式四：
    from PIL import Image, ImageDraw, ImageFont
    from io import BytesIO
    import random
    img = Image.new("RGB", (270, 40), color=get_random_color())
    draw = ImageDraw.Draw(img)
    kumo_font = ImageFont.truetype("static/font/kumo.ttf", size=36)

    valid_code_str = ""
    for i in range(5):
        random_num = str(random.randint(0, 9))
        random_low_alpha = chr(random.randint(95, 122))
        random_upper_alpha = chr(random.randint(65, 90))
        random_char = random.choice([random_num, random_low_alpha, random_upper_alpha])
        draw.text((i * 46 + 20, 5), random_char, get_random_color(), font=kumo_font)

        # 保存验证码
        valid_code_str += random_char

    # 噪点和线
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

    print("valid_code_str", valid_code_str)
    # 保存每一个用户的验证码
    request.session["valid_code_str"] = valid_code_str
    # 内存处理
    f = BytesIO()
    img.save(f, "png")
    data = f.getvalue()
    return data

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
