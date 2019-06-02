
import pygame, time, sys
from enum import Enum, unique


class classproperty:

    def __init__(self, func):
        self.__func = func
    
    def __get__(self, ins, cls):
        return self.__func(cls)


class BVector2(object):

    @classproperty
    def zero(cls): return BVector2(0, 0)
    @classproperty
    def one(cls): return BVector2(1, 1)
    @classproperty
    def up(cls): return BVector2(0, -1)
    @classproperty
    def down(cls): return BVector2(0, 1)
    @classproperty
    def left(cls): return BVector2(-1, 0)
    @classproperty
    def right(cls): return BVector2(1, 0)
    
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, v):
        if isinstance(v, (int, float)) and self.__x != v:
            self.__x = v
            if self.valueChanged:
                self.valueChanged()
    
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, v):
        if isinstance(v, (int, float)) and self.__y != v:
            self.__y = v
            if self.valueChanged:
                self.valueChanged()
    
    @property
    def normalized(self):
        return
    
    @property
    def magnitude(self):
        return self.sqrMagnitude ** 0.5
    
    @property
    def sqrMagnitude(self):
        return self.x ** 2 + self.y ** 2
    
    def Normalize(self):
        return
    
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
        self.valueChanged = None
    
    def __add__(self, other):
        if isinstance(other, BVector2):
            return BVector2(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        if isinstance(other, BVector2):
            return BVector2(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return BVector2(self.x * other, self.y * other)
    
    def __eq__(self, other):
        if isinstance(other, BVector2):
            return (self.x, self.y) == (other.x, other.y)
        elif isinstance(other, (int, float)):
            return self.magnitude == other ** 2
    
    def __nq__(self, other):
        if isinstance(other, BVector2):
            return (self.x, self.y) != (other.x, other.y)
        elif isinstance(other, (int, float)):
            return self.magnitude != other ** 2
    
    def __gt__(self, other):
        if isinstance(other, BVector2):
            return self.magnitude > other.magnitude
        elif isinstance(other, (int, float)):
            return self.magnitude > other ** 2
    
    def __lt__(self, othrt):
        if isinstance(other, BVector2):
            return self.magnitude < other.magnitude
        elif isinstance(other, (int, float)):
            return self.magnitude < other ** 2
    
    def __ge__(self, other):
        if isinstance(other, BVector2):
            return self.magnitude >= other.magnitude
        elif isinstance(other, (int, float)):
            return self.magnitude >= other ** 2
    
    def __le__(self, other):
        if isinstance(other, BVector2):
            return self.magnitude <= other.magnitude
        elif isinstance(other, (int, float)):
            return self.magnitude <= other ** 2
    
    def __str__(self):
        return f'({self.x}, {self.y})'
    
    def __float__(self):
        return self.sqrMagnitude
    
    def __int__(self):
        return int(self.sqrMagnitude)
    
    def __len__(self):
        return self.sqrMagnitude


class BObject(object):

    @classmethod
    def FindObjectOfType(cls, t):
        if t in cls.__objectsTypeDict:
            if len(cls.__objectsTypeDict[t]):
                return cls.__objectsTypeDict[t][0]
    
    @classmethod
    def FindObjectsOfType(cls, t):
        if t in cls.__objectsTypeDict:
            if len(cls.__objectsTypeDict[t]):
                return tuple(cls.__objectsTypeDict[t])

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, v):
        self.__name = v

    def Destroy(self):
        self._shouldDestory = True
    
    def DestoryImmediate(self):
        self._Destroy()
        del self

    def OnDestroy(self):
        pass

    __objectsTypeDict = {}

    @classmethod
    def __RegisteObjectWithType(cls, obj):
        if obj:
            if type(obj) not in cls.__objectsTypeDict:
                cls.__objectsTypeDict[type(obj)] = []
            cls.__objectsTypeDict[type(obj)].append(obj)
    
    @classmethod
    def __RemoveObjectFromTypeDict(cls, obj):
        if obj:
            if type(obj) in cls.__objectsTypeDict:
                if obj in cls.__objectsTypeDict[type(obj)]:
                    cls.__objectsTypeDict[type(obj)].remove(obj)

    def __init__(self):
        self.name = ''
        self._shouldDestory = False
    
    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls)
        cls.__RegisteObjectWithType(obj)
        return obj
    
    def __str__(self):
        return f'Type: {type(self)}  Name: {self.name}'
    
    def _Destroy(self):
        self.OnDestroy()
        BObject.__objectsTypeDict[type(self)].remove(self)


class BComponent(BObject):

    @property
    def gameObject(self):
        return self._gameObject
    
    @property
    def transform(self):
        return self._transform
    
    def GetComponent(self, t):
        if self.gameObject:
            return sel.gameObject.GetComponent(t)
    
    def GetComponentInChildren(self, t):
        if self.gameObject:
            return sel.gameObject.GetComponentInChildren(t)
    
    def GetComponentInParent(self, t):
        if self.gameObject:
            return sel.gameObject.GetComponentInParent(t)
    
    def GetComponents(self, t):
        if self.gameObject:
            return sel.gameObject.GetComponents(t)
    
    def GetComponentsInChildren(self, t):
        if self.gameObject:
            return sel.gameObject.GetComponentsInChildren(t)
    
    def GetComponentsInParent(self, t):
        if self.gameObject:
            return sel.gameObject.GetComponentsInParent(t)

    def __init__(self):
        super().__init__()
        self._gameObject = None
        self._transform = None
    
    def _Destroy(self):
        super()._Destroy()
        self._transform = None
        if self._gameObject:
            self._gameObject._RemoveCompoment(self)
            self._gameObject = None


class BTransform(BComponent):

    @property
    def childCount(self):
        return len(self.__children)
    
    @property
    def parent(self):
        return self.__parent
    @parent.setter
    def parent(self, v):
        if self.__parent != v and (isinstance(v, BTransform) or not v):
            self.__RemoveFromParent()
            if v:
                v.__AddChild(self)
    
    @property
    def root(self):
        return self.__root
    
    def GetChildWithName(self, n):
        for c in self.__children:
            if c.name == n:
                return c
    
    def GetChildWithIndex(self, i):
        if i < len(self.__children):
            return self.__children[i]
    
    def IsChildOf(self, p):
        if self.parent and self.parent != self:
            if self.parent == p:
                return True
            else:
                return self.parent.IsChildOf(p)
        return False
    
    @property
    def siblingIndex(self):
        if self.parent and self.parent != self:
            return self.parent.__children.index(self)
        return -1
    @siblingIndex.setter
    def siblingIndex(self, i):
        j = self.siblingIndex
        if j >= 0 and j != i and i < len(self.parent.childCount):
            self.parent.__children.remove(self)
            self.parent.__children.insert(i, self)

    def SetAsLastSibling(self):
        self.SetSiblingIndex(len(self.parent.childCount) - 1)
    
    def SetAsFirstSibling(self):
        self.SetSiblingIndex(0)
    
    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, v):
        if isinstance(v, BVector2) and self.position != v:
            self.__position = v
            self.__localPosition = self.position
            if self.parent and self.parent != self:
                self.__localPosition = self.position - self.parent.position
            self.__RelayoutChildren()
    
    @property
    def localPosition(self):
        return self.__localPosition
    @localPosition.setter
    def localPosition(self, v):
        if isinstance(v, BVector2) and self.localPosition != v:
            self.__localPosition = v
            self.__position = self.localPosition
            if self.parent and self.parent != self:
                self.__position = self.parent.position + self.localPosition
            self.__RelayoutChildren()
    
    @property
    def localScale(self):
        return self.__localScale
    @localPosition.setter
    def localScale(self, v):
        if isinstance(v, BVector2) and self.localScale != v:
            self.__localScale = v

    def __RelayoutChildren(self):
        for c in self.__children:
            c.position = self.__position + c.__localPosition

    def __init__(self):
        super().__init__()
        self._transform = self
        self.__parent = self
        self.__children = []
        self.__root = self
        self.__position = BVector2.zero
        self.__localPosition = BVector2.zero
        self.__localScale = BVector2.one
    
    def __AddChild(self, chi):
        if isinstance(chi, BTransform) and chi not in self.__children:
            chi.__RemoveFromParent()
            chi.__parent = self
            if self != chi:
                self.__children.append(chi)
                chi.__ChangeRoot(self.root)
            else:
                chi.__ChangeRoot(self)
    
    def __RemoveFromParent(self):
        if self.__parent and self != self.__parent:
            self.__parent.__children.remove(self)
            self.__parent = self
            self.__ChangeRoot(self)
    
    def __ChangeRoot(self, roo):
        if isinstance(roo, BTransform) or not roo:
            self.__root = roo if roo else self
            for c in self.__children:
                c.__root = self.__root


class BGameObject(BObject):
    
    @classmethod
    def FindGameObjectWithTag(cls, tag):
        if tag and tag in cls.__objectsTagDict:
            if len(cls.__objectsTagDict[tag]) > 0:
                return cls.__objectsTagDict[tag][0]

    @classmethod
    def FindGameObjectsWithTag(cls, tag):
        if tag and tag in cls.__objectsTagDict:
            if len(cls.__objectsTagDict[tag]) > 0:
                return tuple(cls.__objectsTagDict[tag])
    
    @property
    def tag(self):
        return self.__tag
    @tag.setter
    def tag(self, v):
        if isinstance(v, str) and self.tag != v:
            BGameObject.__RemoveObjectFromTagDict(self)
            self.__tag = v
            BGameObject.__RegisteObjectWithTag(self)

    @property
    def transform(self):
        return self.__transform
    
    @property
    def active(self):
        return self.__active
    @active.setter
    def active(self, v):
        if isinstance(v, bool) and self.__active != v:
            self.__active = v
    
    def AddSubObject(self, subObject):
        if subObject and isinstance(subObject, BGameObject) and self != subObject:
            subObject.transform.parent = self.transform
    
    def RemoveFromParent(self):
        self.transform.parent = None

    def AddComponent(self, com):
        if isinstance(com, BTransform):
            return
        if com not in self.__components:
            self.__components.append(com)
            com._gameObject = self
            com._transform = self.__transform
    
    def GetComponent(self, t):
        if not isinstance(t, BComponent):
            return
        for com in self.__components:
            if isinstance(com, t):
                return com
    
    def GetComponentInChildren(self, t):
        if not isinstance(t, BComponent):
            return
        count = self.transform.childCount
        for i in range(count):
            child = self.transform.GetChildWithIndex(i)
            result = child.GetComponent(t)
            if not result:
                result = chile.GetComponentInChildren(t)
            if result:
                return result

    def GetComponentInParent(self, t):
        if not isinstance(t, BComponent):
            return
        if self.transform.parent and self.transform.parent != self.transform:
            result = self.transform.parent.GetComponent(t)
            if not result:
                result = self.transform.parent.GetComponentInParent(t)
            return result
    
    def GetComponents(self, t):
        if not isinstance(t, BComponent):
            return
        result = []
        for com in self.__components:
            if isinstance(com, t):
                result.append(com)
        return tuple(result)
    
    def GetComponentsInChildren(self, t):
        if not isinstance(t, BComponent):
            return
        result = []
        count = self.transform.childCount
        for i in range(count):
            child = self.transform.GetChildWithIndex(i)
            r = child.GetComponents(t)
            if r:
                result += r
            r_c = child.GetComponentsInChildren(t)
            if r_c:
                result += r_c
        return tuple(result)
    
    def GetComponentsInParent(self, t):
        if not isinstance(t, BComponent):
            return
        result = []
        if self.transform.parent and self.transform.parent != self.transform:
            r = self.transform.parent.GetComponents(t)
            if r:
                result += r
            r_p = self.transform.parent.GetComponentsInParent(t)
            if r_p:
                result += r_p
            return tuple(result)
    
    def _RemoveCompoment(self, com):
        if isinstance(com, BTransform):
            return
        if com and com in self.__components:
            self.__components.remove(com)
        
    def _Update(self, surface, dt):
        if self.active:
            for com in self.__components:
                # print(self.name)
                if isinstance(com, BBehaviour):
                    com._Update(surface, dt)
            count = self.transform.childCount
            for i in range(count):
                child = self.transform.GetChildWithIndex(i)
                child.gameObject._Update(surface, dt)
    
    __objectsTagDict = {}

    @classmethod
    def __RegisteObjectWithTag(cls, obj):
        if obj:
            if obj.tag not in cls.__objectsTagDict:
                cls.__objectsTagDict[obj.tag] = []
            cls.__objectsTagDict[obj.tag].append(obj)
    
    @classmethod
    def __RemoveObjectFromTagDict(cls, obj):
        if obj:
            if obj.tag in cls.__objectsTagDict:
                if obj in cls.__objectsTagDict[obj.tag]:
                    cls.__objectsTagDict[obj.tag].remove(obj)

    def __init__(self):
        super().__init__()
        self.__tag = ''
        self.__transform = BTransform()
        self.__components = [self.__transform]
        self.__transform._gameObject = self
        self.__active = True
    
    def _Destroy(self):
        super()._Destroy()
        BGameObject.__RemoveObjectFromTagDict(self)


class BBaseBehaviour(BComponent):

    @property
    def enable(self):
        return self.__enable
    @enable.setter
    def enable(self, v):
        if isinstance(v, bool) and self.enable != v:
            self.__enable = v
            if self.__enable:
                self.OnEnable()
            else:
                self.OnDisable()
    
    @property
    def isActiveAndEnable(self):
        if self.gameObject:
            return self.gameObject.active and self.enable
    
    def OnEnable(self):
        pass
    def OnDisable(self):
        pass
    
    def __init__(self):
        super().__init__()
        self.__enable = True


@unique
class KeyCode(Enum):
    W = pygame.K_w
    A = pygame.K_a
    S = pygame.K_s
    D = pygame.K_d


class Input:
    
    @classmethod
    def GetKeyDown(cls, kc: KeyCode):
        if not cls._lastKeys[kc.value] and cls._keys[kc.value]:
            return True
    
    @classmethod
    def GetKeyUp(cls, kc: KeyCode):
        if not cls._keys[kc.value] and cls._lastKeys[kc.value]:
            return True
    
    @classmethod
    def GetKey(cls, kc: KeyCode):
        if cls._keys[kc.value] and cls._lastKeys[kc.value]:
            return True
    
    _keys = []
    _lastKeys = []


class BBehaviour(BBaseBehaviour):

    def OnStart(self):
        pass
    def OnUpdate(self, surface, dt):
        pass

    def __init__(self, obj=None):
        super().__init__()
        self._didStart = False
        if obj:
            obj.AddComponent(self)

    def _Update(self, surface, dt):
        if not self.enable:
            return
        if self._didStart:
            self.OnUpdate(surface, dt)
        else:
            self._Start()
            self._didStart = True
        count = self.transform.childCount
        for i in range(count):
            child = self.transform.GetChildWithIndex(i)
            for com in child.__components:
                if isinstance(com, BBehaviour):
                    com._Update(surface, dt)
    
    def _Start(self):
        self.OnStart()


class BImage(BBehaviour):

    def __init__(self, img_path='', obj=None):
        super().__init__(obj)
        self.__isImage = False
        self.__content = None
        self.__bgcolor = (255, 0, 0)
        self.__size = BVector2.one * 50
        if img_path:
            self.__isImage = True
            self.__content = pygame.image.load(img_path).convert_alpha()
    
    def OnUpdate(self, surface, dt):
        if self.__isImage and self.__content:
            surface.blit(self.__content, (int(self.transform.position.x), int(self.transform.position.y), int(self.__size.x), int(self.__size.y)))
        else:
            pygame.draw.rect(surface, self.__bgcolor, (self.transform.position.x, self.transform.position.y, self.__size.x, self.__size.y))


class Main:

    __root = None

    @classproperty
    def root(cls):
        if not cls.__root:
            cls.__root = BGameObject()
        return cls.__root

    @classmethod
    def Init(cls, title='BOBO Game', w=0, h=0):
        cls.__pause = True
        cls.__isRuning = False
        cls.__lastUpdateTime = 0
        pygame.init()
        cls._screen = pygame.display.set_mode((w, h))
        pygame.display.set_caption(title)
    
    @classmethod
    def Run(cls):
        cls.__pause = False
        if not cls.__isRuning:
            cls.__isRuning = True
            cls.__MainLoop()
    
    @classmethod
    def Pause(cls, shouldPause):
        cls.__pause = shouldPause
    
    @classmethod
    def Exit(cls):
        pygame.quit()
        sys.exit(0)
    
    _screen = None

    @classmethod
    def __MainLoop(cls):
        while True:
            cls.__EventLoop()
            currentTime = time.time()
            deltaTime = 1 / 60 if cls.__lastUpdateTime == 0 else currentTime - cls.__lastUpdateTime
            if not cls.__pause:
                cls.__Update(deltaTime)
            cls.__lastUpdateTime = currentTime
            sleepTime = 1 / 60 - deltaTime
            if sleepTime > 0:
                time.sleep(sleepTime)
    
    @classmethod
    def __Update(cls, dt):
        cls._screen.fill((255, 255, 255))
        cls.root._Update(cls._screen, dt)
        pygame.display.flip()
    
    @classmethod
    def __EventLoop(cls):
        Input._haveKeyDown = False
        Input._haveKeyUp = False
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                cls.Exit()
        Input._lastKeys = Input._keys
        Input._keys = pygame.key.get_pressed()
