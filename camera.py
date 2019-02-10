class Camera(object):
    def __init__(self, w, h):
        self.w, self.h = w, h
        self.dx, self.dy = 0, 0

    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - self.w // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - self.h // 2)
