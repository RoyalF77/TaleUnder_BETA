import pygame

class Personnage:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.img = pygame.image.load("ressources/personnage.png")
        self.speed = 60
        self.velocity = [0,0]
        self.rect = self.img.get_rect(x=0,y=0)
        self.img = pygame.transform.scale(self.img, (60, 60))

    def get_position(self):
        return (self.x, self.y)
    
    def get_image(self):
        return self.img

    def set_position(self, pos):
        self.x,self.y = pos
        self.rect.update(self.x,self.y,60,60)

    def deplacer(self):
        self.rect.x += self.velocity[0] * self.speed
        self.rect.y += self.velocity[1] * self.speed
class Map:

    def __init__(self,img):
        self.x = 0
        self.y = 0
        self.img = img
        self.rect  = self.img.get_rect(x=0,y=0)
    
    def set_position(self, pos):
        self.x, self.y = pos

class Camera:

    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height
        self.SCREEN_WIDTH = 1280
        self.SCREEN_HEIGHT = 824

    def apply(self, entity_or_surface):
        if hasattr(entity_or_surface, 'rect'):
            return entity_or_surface.rect.move(self.camera.topleft)
        else:
            return entity_or_surface.get_rect(topleft=self.camera.topleft)

    def update(self, target):
        x = -target.rect.x + int(self.SCREEN_WIDTH / 2)
        y = -target.rect.y + int(self.SCREEN_HEIGHT / 2)


        x = min(0, x)
        y = min(0, y)
        x = max(-(self.width - self.SCREEN_WIDTH), x)-50
        y = max(-(self.height - self.SCREEN_HEIGHT), y)-50

        self.camera = pygame.Rect(x, y, self.width, self.height)

class Obstacle:

    def __init__(self,rect):
        self.rect = rect
    
    def collisions(self,perso):
        if self.rect.colliderect(perso.rect):
            if perso.velocity[0] == 1 and perso.velocity[1] == 0:
                perso.rect.right = self.rect.left
            elif perso.velocity[0] == -1 and perso.velocity[1] == 0:
                perso.rect.left = self.rect.right
            if perso.velocity[1] == -1 and perso.velocity[0] == 0:
                perso.rect.top = self.rect.bottom
            elif perso.velocity[1] == 1 and perso.velocity[0] == 0:
                perso.rect.bottom = self.rect.top

class Debutcombat:
    def __init__(self,rect):
        self.rect = rect
    def collisions(self,perso):
        if self.rect.colliderect(perso.rect):
            print("Collisions!")

class Item:
    def __init__(self,rect):
        self.rect = rect
    def collisions(self,perso):
        if self.rect.colliderect(perso.rect):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER:
                    print("pris")