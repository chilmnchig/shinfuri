class Point():

    all_objects = []

    def __init__(self, lis):
        self.kind = lis[0]
        if hasattr(self, 'alpha'):
            i = 2
        else:
            i = 1
        self.num = int(lis[i])
        self.point = int(lis[i + 2])
        self.all_objects.append(self)

    def convert_point(self):
        point = self.point
        if point < 50:
            return 0
        elif point < 100:
            return point // 5 - 9
        else:
            return 10

    def add(self, total, unit, point, inc_scale=True):
        if inc_scale:
            total += self.num * point * self.scale
            unit += self.num * self.scale
        else:
            total += self.num * point
            unit += self.num
        return total, unit


class Compulsory(Point):
    scale = 1


class Select(Point):

    def __init__(self, lis):
        self.alpha = lis[1]
        super().__init__(lis)

    @classmethod
    def write_scale(cls, objects, unit, multi=True):
        objects = sorted(
            objects, key=lambda object: object.point, reverse=True)

        alpha_set = set()
        ct = 0
        top = []
        btm = objects

        while ct < unit and len(btm) > 0:
            object = btm.pop(0)
            top.append(object)
            ct += object.num
            if multi:
                alpha_set.add(object.alpha)

        if multi and len(alpha_set) == 1:
            for btmobject in btm:
                if btmobject.alpha not in alpha_set:
                    topobject = top.pop()
                    ct -= topobject.num
                    top.append(btmobject)
                    ct += btmobject.num
                    btm.remove(btmobject)
                    if ct < unit:
                        top.append(topobject)
                        ct += topobject.num
                    else:
                        btm.insert(0, topobject)
                    break

        for object in btm:
            object.scale = 0.1

        if ct > unit:
            object = top.pop()
            object.scale = (object.num - 0.9 * (ct - unit)) / object.num

        for object in top:
            object.scale = 1


class SelectAD(Select):
    objects = []

    def __init__(self, lis):
        super().__init__(lis)
        self.objects.append(self)

    @classmethod
    def write_scale(cls):
        return super().write_scale(cls.objects, 6, multi=True)


class SelectEF(Select):
    objects = []

    def __init__(self, lis):
        super().__init__(lis)
        self.objects.append(self)

    @classmethod
    def write_scale(cls):
        return super().write_scale(cls.objects, 6, multi=True)


class SelectL(Select):
    objects = []

    def __init__(self, lis):
        super().__init__(lis)
        self.objects.append(self)

    @classmethod
    def write_scale(cls):
        return super().write_scale(cls.objects, 3, multi=False)


class Etc(Point):
    scale = 0.1
