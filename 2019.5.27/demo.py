
from BGame import *


class Head(BBehaviour):

    def OnStart(self):
        self.img = BImage('./a.jpg', self.gameObject)
    
    def OnUpdate(self, surface, dt):
        if Input.GetKey(KeyCode.W):
            self.transform.position.y -= 2
        if Input.GetKey(KeyCode.S):
            self.transform.position.y += 2
        if Input.GetKey(KeyCode.A):
            self.transform.position.x -= 2
        if Input.GetKey(KeyCode.D):
            self.transform.position.x += 2


Main.Init('Test', 480, 320)

obj = BGameObject()
head = Head(obj)
Main.root.AddSubObject(obj)

Main.Run()
