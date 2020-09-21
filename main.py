import copy
from PIL import Image, ImageDraw  # Подключим необходимые библиотеки.
import math
import time

class piramid:
    def __init__(self, image):
        self.sred = []
        self._create_piramid(image)

    def uvel(self, image):
        ch_str = 30 - len(image) % 30
        ch_st = 30 - len(image[0]) % 30
        ch_str_sv = ch_str // 2
        ch_str_sn = ch_str - ch_str_sv
        ch_st_sp = ch_st // 2
        ch_st_sl = ch_st - ch_st_sp

        for i in range(ch_str_sv):
            new_str = copy.deepcopy(image[0])
            image.insert(0, new_str)
        for i in range(ch_str_sn):
            new_str = copy.deepcopy(image[-1])
            image.append(new_str)

        for i in range(ch_st_sl):
            for j in image:
                new_st = copy.deepcopy(j[0])
                j.insert(0, new_st)
        for i in range(ch_st_sp):
            for j in image:
                new_st = copy.deepcopy(j[0])
                j.insert(0, new_st)
            new_str = copy.deepcopy(image[-1])
            image.append(new_str)


    def set_sred(self, sred):
        self.sred = copy.deepcopy(sred)

    def get_sr(self):
        return self.sred

    def get_znach(self, image):
        new_mas_sr = [[0 for j in range(len(image[0]) // 2)] for i in range(len(image) // 2)]

        for i in range(0, len(new_mas_sr)):
            for j in range(0, len(new_mas_sr[0])):
                new_mas_sr[i][j] = (image[i * 2][j * 2] + image[i * 2 + 1][j * 2] +
                                    image[i * 2][j * 2 + 1] + image[i * 2 + 1][j * 2 + 1]) / 4
        if len(image[0]) % 2 != 0:
            n = len(image) // 2
            for i in range(n):
                new_mas_sr[i].append((image[i * 2][-1] + image[i * 2 + 1][-1]) / 2)
        if len(image) % 2 != 0:
            n = len(image[0]) // 2
            new_str_sr = []
            for i in range(n):
                new_str_sr.append((image[-1][i * 2] + image[-1][i * 2 + 1]) / 2)
            new_mas_sr.append(new_str_sr)
        if len(image) % 2 != 0 and len(image[0]) % 2 != 0:
            new_mas_sr[-1].append(image[-1][-1])
        return new_mas_sr

    def get_sr_znach(self, image):
        new_mas_sr = [[0 for j in range(len(image[0]) // 2)] for i in range(len(image) // 2)]

        for i in range(0, len(new_mas_sr)):
            for j in range(0, len(new_mas_sr[0])):
                new_mas_sr[i][j] = (image[i * 2][j * 2] + image[i * 2 + 1][j * 2] +
                                    image[i * 2][j * 2 + 1] + image[i * 2 + 1][j * 2 + 1]) // 4
        if len(image[0]) % 2 != 0:
            n = len(image) // 2
            for i in range(n):
                new_mas_sr[i].append((image[i * 2][-1] + image[i * 2 + 1][-1]) // 2)
        if len(image) % 2 != 0:
            n = len(image[0]) // 2
            new_str_sr = []
            for i in range(n):
                new_str_sr.append((image[-1][i * 2] + image[-1][i * 2 + 1]) // 2)
            new_mas_sr.append(new_str_sr)
        if len(image) % 2 != 0 and len(image[0]) % 2 != 0:

            new_mas_sr[-1].append(image[-1][-1])
        return new_mas_sr

    def _create_piramid(self, image):
        self.sred.append(image)
        msr = self.get_znach(image)
        while True:
            self.sred.append(msr)
            if len(msr) < 30 or len(msr[0]) < 30:
                return
            msr = self.get_sr_znach(msr)

    def __getitem__(self, key):
        return self.sred[key]

    def __len__(self):
        return len(self.sred)


class vector_dviz:
    def __init__(self, pir1, pir2):
        self.pir_baz = copy.deepcopy(pir1)
        self.pir_sdv = copy.deepcopy(pir2)

    def get_sad(self, n):
        pass

    def get_vect(self):
        vect_nach, vect_kon = search_3step(self.pir_baz[-1], self.pir_sdv[-1], 1, 1)
        k = 1
        for i in range(len(self.pir_baz) - 2, -1, -1):
            if k < 8:
                k *= 2
            vect_nach[0] *= 2
            vect_kon[0] *= 2
            vect_nach[1] *= 2
            vect_kon[1] *= 2
            vect_nach, vect_kon = search_3step(self.pir_baz[i], self.pir_sdv[i], k, k, vect_nach, vect_kon)

        return vect_nach, vect_kon

def get_sad(image1, image2, x, y, x1, y1, size_gor, size_vert):
    sad = 0
    for i in range(0, size_vert):
        for j in range(0, size_gor):
            sad += (image2[x1 + i][y1 + j] - image1[x + i][y + j])
    return sad

def poln_search(image_ish, image, x_nach, y_nach, x_kon, y_kon):
    pass

def search_3step(image_ish, image, size_gor, size_vert, nach=None, kon=None):

    if nach == None or kon == None:
        count_vert = len(image) // size_vert
        if len(image) % size_vert != 0:
            count_vert += 1

        count_gor = len(image[0]) // size_gor
        if len(image) % size_gor != 0:
            count_gor += 1
    else:
        if kon[0] < len(image) // 2:
            count_vert = (kon[0] * 2) // size_vert
        else:
            count_vert = ((len(image) - kon[0]) * 2) // size_vert
        if kon[1] < len(image[0]) // 2:
            count_gor = (kon[1] * 2) // size_gor
        else:
            count_gor = ((len(image[0]) - kon[1]) * 2) // size_gor

    shag_vert = count_vert // 4
    shag_gor = count_gor // 4

    if nach == None or kon == None:
        k = [size_vert * shag_vert * 2, size_gor * shag_gor * 2]
        koord_sr = [size_vert * shag_vert * 2, size_gor * shag_gor * 2]
    else:
        k = nach
        koord_sr = kon

    koord_toch = [[koord_sr[0] - (shag_vert * size_vert), koord_sr[1] - size_gor * shag_gor],
                  [koord_sr[0] - size_vert * shag_vert, koord_sr[1]],
                  [koord_sr[0] - size_vert * shag_vert, koord_sr[1] + size_gor * shag_gor],
                  [koord_sr[0], koord_sr[1] - size_gor * shag_gor], [koord_sr[0], koord_sr[1] + size_vert * shag_gor],
                  [koord_sr[0] + (shag_vert * size_vert), koord_sr[1] - size_gor * shag_gor],
                  [koord_sr[0] + size_vert * shag_vert, koord_sr[1]],
                  [koord_sr[0] + size_vert * shag_vert, koord_sr[1] + size_gor * shag_gor]]
    #print(koord_toch)
    if nach == None or kon == None:
        vect = 1000000000000
    else:
        vect = abs(get_sad(image_ish, image, k[0], k[1], koord_sr[0], koord_sr[1], size_vert, size_gor))
    while shag_gor > 1 or shag_vert > 1:
        koord = koord_sr
        for i in koord_toch:
            sad = get_sad(image_ish, image, k[0], k[1], i[0], i[1], size_vert, size_gor)
            if abs(sad) < vect:
                vect = abs(sad)
                koord = i
        shag_gor //= 2
        shag_vert //= 2
        koord_sr = koord
        koord_toch = [[koord_sr[0] - (shag_vert * size_vert), koord_sr[1] - size_gor * shag_gor], [koord_sr[0] - size_vert * shag_vert, koord_sr[1]], [koord_sr[0] - size_vert * shag_vert, koord_sr[1] + size_gor * shag_gor],
                  [koord_sr[0], koord_sr[1] - size_gor * shag_gor],  [koord_sr[0], koord_sr[1] + size_vert * shag_gor],
                  [koord_sr[0] + (shag_vert * size_vert), koord_sr[1] - size_gor * shag_gor], [koord_sr[0] + size_vert * shag_vert, koord_sr[1]], [koord_sr[0] + size_vert * shag_vert, koord_sr[1] + size_gor * shag_gor]]
        #print(koord_toch)
    #print(koord_sr[0] - k[0], koord_sr[1] - k[1])
    return k, koord_sr



def read_image(name):
    image = Image.open(name)  # Открываем изображение.

    pix = image.load()  # Выгружаем значения пикселей.
    width = image.size[0]  # Определяем ширину.
    height = image.size[1]  # Определяем высоту.

    new_mas = [[0 for i in range(width)] for j in range(height)]
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            S = (a + b + c) // 3
            new_mas[j][i] = S

    return new_mas


def print_image(image1, old_name, name):
    image = Image.open(old_name)  # Открываем изображение.
    draw = ImageDraw.Draw(image)
    width = image.size[0]  # Определяем ширину.
    height = image.size[1]  # Определяем высоту.
    for i in range(len(image1)):
        for j in range(len(image1[0])):
            draw.point((j, i), (int(image1[i][j]), int(image1[i][j]), int(image1[i][j])))
    image.save(name, "TIFF")
    del draw

a = 'D:\обработка изображений\dz4\\0' + str(1) + '.tif'
mas = read_image(a)
asd = piramid(mas)

for i in range(2, 13):
    t1 = time.time()
    #print(i)
    if i >= 10:
        a = 'D:\обработка изображений\dz4\\' + str(i) + '.tif'
    else:
        a = 'D:\обработка изображений\dz4\\0' + str(i) + '.tif'

    mas1 = read_image(a)
    asd1 = piramid(mas1)
    qwe = vector_dviz(asd, asd1)
    otv1, otv2 = qwe.get_vect()
    print(otv2[0] - otv1[0], otv2[1] - otv1[1])
    print(time.time() - t1)
    print()
    #print_image(mas, a, 'D:\обработка изображений\dz4\\' + 'b' + str(i) + '.tif')
