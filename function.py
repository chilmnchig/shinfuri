import csv
from object import Point, Compulsory, SelectAD, SelectEF, SelectL, Etc


def process_file(file):
    Point.all_objects.clear()
    SelectAD.objects.clear()
    SelectEF.objects.clear()
    SelectL.objects.clear()

    with open(file) as f:
        reader = csv.reader(f)
        for row in reader:
            register(row)

    SelectAD.write_scale()
    SelectEF.write_scale()
    SelectL.write_scale()


def register(lis):
    kind = lis[0]
    if len(lis) < 4:
        pass
    elif kind == "必修":
        return Compulsory(lis)
    elif kind == "総合":
        alpha = lis[1]
        if alpha in {"A", "B", "C", "D"}:
            return SelectAD(lis)
        elif alpha in {"E", "F"}:
            return SelectEF(lis)
        elif alpha == "L":
            return SelectL(lis)
    else:
        return Etc(lis)


def average(engineer=False):

    total = 0
    unit = 0

    if engineer:
        rest = []

        for object in Point.all_objects:
            if object.scale >= 1:
                point = object.convert_point()
                total, unit = object.add(total, unit, point)
            else:
                rest.append(object)

        rest = sorted(rest, key=lambda object: object.point)
        for object in rest:
            point = object.convert_point()
            ave = total / unit
            if point >= ave:
                total, unit = object.add(total, unit, point, inc_scale=False)
            else:
                total, unit = object.add(total, unit, point)

    else:
        for object in Point.all_objects:
            point = object.point
            total, unit = object.add(total, unit, point)

    return round(total / unit, 4)
