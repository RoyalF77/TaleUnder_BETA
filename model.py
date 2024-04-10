import pygame
# Enemy DATABASE

class Kopa:

    def __init__(self):
        self.sheet = pygame.image.load("sprites/enemy/Kopa_sheet.png").convert_alpha()
        self.img = pygame.image.load("sprites/enemy/Kopa_model.png").convert_alpha()
        self.rect = self.img.get_rect()
        self.size = self.img.get_size()
        self.index = [0,0]
        self.info = {
            "name" : "Kopa",
            "desc" : "* Kopa - Royal Guard\nShe will not let you pass",
            "hp" : 100,
            "at" : 10,
            "df" : 10,
            "xp_reward" : 50,
            "gold_reward" : 200,
            "KR" : False
        }
        self.act = {
            0 : "check",
            1 : "compliment",
            2 : "insult",
            3 : "call help"
        }
        self.act_txt = {
            "check" : "* 10 ATK 10 DEF\n* She's looking at you with a hatefull face",
            "compliment" : "* She don't seems to care",
            "insult" : "* She don't seems to care of your words",
            "call help" : "* But nobody came"
        }
        self.mercy = {
            0 : "Spare",
        }
        self.mercy_txt = {
            "Spare" : "* Your Sparing Kopa, Nothing Happend"
        }
        self.Attack_bullet =pygame.image.load("sprites/ui/att1.png").convert_alpha()
        self.Spear = pygame.image.load("sprites/ui/att3.png").convert_alpha()
        self.Spear = pygame.transform.scale_by(self.Spear,4)


    def update(self):
        self.rect = self.img.get_rect()
        self.size = self.img.get_size()
    
    def anim_simple(self,boxrect):
        x,y = self.size
        img = pygame.Surface((x,y),pygame.SRCALPHA).convert_alpha()

        self.index[0] += 0.1
        if self.index[0] >= 6:
            self.index[0] = 0

        if self.index[0] < 1:
            img.blit(self.sheet,(0,0),(0,y*0,x,y))

        elif self.index[0] < 2:
            img.blit(self.sheet,(0,0),(0,y*1,x,y))

        elif self.index[0] < 3:
            img.blit(self.sheet,(0,0),(0,y*2,x,y))

        elif self.index[0] < 4:
            img.blit(self.sheet,(0,0),(0,y*3,x,y))

        elif self.index[0] < 5:
            img.blit(self.sheet,(0,0),(0,y*4,x,y))

        elif self.index[0] < 6:
            img.blit(self.sheet,(0,0),(0,y*5,x,y))

        img = pygame.transform.scale_by(img,3.5)

        x,y = boxrect.midtop
        rect = img.get_rect(midbottom = (x+20,y-10))
        self.rect = rect
        return img,rect
    
    def anim_eyes(self,boxrect):
        x,y = self.size
        img = pygame.Surface((x,y),pygame.SRCALPHA).convert_alpha()

        self.index[0] += 0.02
        if self.index[0] >= 2:
            self.index[0] = 0

        if self.index[0] < 1:
            img.blit(self.sheet,(0,0),(0,y*7,x,y))

        elif self.index[0] < 2:
            img.blit(self.sheet,(0,0),(0,y*8,x,y))

        img = pygame.transform.scale_by(img,3.5)

        x,y = boxrect.midtop
        rect = img.get_rect(midbottom = (x+20,y-10))
        self.rect = rect
        return img,rect

    def looking(self,boxrect):
        x,y = self.size
        img = pygame.Surface((x,y),pygame.SRCALPHA).convert_alpha()

        img.blit(self.sheet,(0,0),(0,y*6,x,y))

        img = pygame.transform.scale_by(img,3.5)

        x,y = boxrect.midtop
        rect = img.get_rect(midbottom = (x+20,y-10))
        self.rect = rect
        return img,rect
    
    def looking_at_yu(self,boxrect):
        x,y = self.size
        img = pygame.Surface((x,y),pygame.SRCALPHA).convert_alpha()

        img.blit(self.sheet,(0,0),(0,y*9,x,y))

        img = pygame.transform.scale_by(img,3.5)

        x,y = boxrect.midtop
        rect = img.get_rect(midbottom = (x+20,y-10))
        self.rect = rect
        return img,rect

    def degat(self, att,player,rect,vitesse,sens,rect1,type,taille=(0,0)):
        rect1[0]=att[0]
        rect1[1]=att[1]

        if rect1.colliderect(player.rect) and player.info["current_hp"] >= self.info["at"]//2:
            if type == 'b':
                player.info["current_hp"]-= self.info["at"]//2
            if type == 's':
                player.info["current_hp"]-= int(self.info["at"]*0.6)
            return False
        
        if type == "b":
            if sens == 'r' and att[0] > rect.right-10-vitesse:
                return False
            if sens == 'l'and att[0] < rect.left-vitesse:
                return False
            if sens == 't' and att[1] < rect.top-vitesse :
                return False
            if sens == 'd'and att[1] > rect.bottom-15-vitesse :
                return False
            
        if type == "s":
            w,h = taille
            if sens == 'r' and att[0] > w:
                return False
            if sens == 'l'and att[0] < -200:
                return False
            if sens == 't' and att[1] < -200 :
                return False
            if sens == 'd'and att[1] > h :
                return False


        return True
                
def attack1(att,vitesse,sens):
    x,y=att
    if sens == 't':
        att[1]-=vitesse
    if sens == 'd':
        att[1]+=vitesse
    if sens == 'r':
        att[0]+=vitesse
    if sens == 'l':
        att[0]-=vitesse
    (x,y) = att
    return x,y    


# ITEM DATABASE
Bandage = {
    "state" : "armor",
    "name" : "Bandage",
    "desc" : "It has already been used several times.",
    "hp_give" : 10,
    "price" : "Free"
}

Monster_Candy = {
    "state" : "consumable",
    "name" : "Monster Candy",
    "desc" : "Has a distinct, non-licorice flavor.",
    "hp_give" : 10,
    "price" : "Free"
}

Spider_Donut = {
    "state" : "consumable",
    "name" : "Spider Donut",
    "desc" : "A donut made with Spider Cider in the batter.",
    "hp_give" : 12,
    "price" : [7,9999]
}

Spider_Cider = {
    "state" : "consumable",
    "name" : "Spider Cider",
    "desc" : "Made with whole spiders, not just the juice.",
    "hp_give" : 10,
    "price" : [18,9999]
}

Butterscotch_Pie = {
    "state" : "consumable",
    "name" : "Butterscotch Pie",
    "desc" : "Butterscotch-cinnamon pie, one slice. ",
    "hp_give" : "ALL",
    "price" : "Free"
}

Snail_Pie = {
    "state" : "consumable",
    "name" : "Snail Pie",
    "desc" : "Heals Some HP. An acquired taste.",
    "hp_give" : "All-1",
    "price" : "Free"
}

Snowman_Piece = {
    "state" : "consumable",
    "name" : "Snowman Piece",
    "desc" : "Please take this to the ends of the earth. ",
    "hp_give" : 45,
    "price" : "Free"
}

Power = {
    "state" : "consumable",
    "name" : "Power Of Friendship",
    "desc" : "Love and Hate",
    "hp_give" : 999,
    "price" : [15,25,"Free",12]
}

Name = {
    "state" : "consumable",
    "name" : "Name",
    "desc" : "Desc",
    "hp_give" : 0,
    "price" : [7,9999]
}

#PLAYER INFO AND OTHER SYSTEM
def sort_inv():
    """
    Sort the player inventory
    """
    player_inventory.sort(key=lambda x:x["name"])

def take_dmg(enemy_hp,enemy_df,player_dmg):
    """
    Return the damage taken by the enemy
    """
    if enemy_hp==0:
        return (0,0)
    
    elif enemy_df == 0 and player_dmg > enemy_hp*0.8:
        return (0,enemy_hp)
    
    elif player_dmg == 0:
        player_dmg = enemy_df + 1

    elif player_dmg < enemy_df:
        player_dmg = enemy_df + 1

    damage = player_dmg - enemy_df

    if damage == 0:
        damage = 1
    if damage < 0:
        damage = -damage

    enemy_hp -= damage

    if enemy_hp in [1,2,3,4,5] and player_dmg < enemy_df:
        return (0,damage+enemy_hp)
    
    elif enemy_hp <= 0:
        return (0,damage)
    
    return enemy_hp, damage

#Health System
hp_system = {}
base = 20
for i in range(1,21):
    hp_system[i] = base
    base += 4
hp_system[20] = 99
#Experience System
xp_system = {}
xp_system[1] = 10
xp_system[2] = 20
xp_system[3] = 40
xp_system[4] = 50
xp_system[5] = 80
xp_system[6] = 100
xp_system[7] = 200
xp_system[8] = 300
xp_system[9] = 400
xp_system[10] = 500
xp_system[11] = 800
xp_system[12] = 1000
xp_system[13] = 1500
xp_system[14] = 2000
xp_system[15] = 3000
xp_system[16] = 5000
xp_system[17] = 10000
xp_system[18] = 25000
xp_system[19] = 49999
#Attack System
at_system = {}
base = 10
for i in range(1,21):
    at_system[i] = base
    base += 2
#Defence System
df_system = {}
base = 10
for i in range(1,21):
    if i < 5:
        df_system[i] = base
    elif i < 9:
        df_system[i] = base + 1
    elif i < 12:
        df_system[i] = base + 2
    elif i < 17:
        df_system[i] = base + 3
    else:
        df_system[i] = base + 4
#Player Inventory
player_inventory = [Butterscotch_Pie,Bandage,Snail_Pie,Power]
sort_inv()

def recover_hp(player,hp):
    if type(hp) == str:
        if hp == 'ALL':
            player.info["current_hp"] = player.info["hp"]
        if hp == 'All-1':
            player.info["current_hp"] = player.info["hp"] -1
    else:

        temp = player.info["current_hp"] + hp
        if temp >= player.info["hp"]:
            player.info["current_hp"] = player.info["hp"]
        else:
            player.info["current_hp"] = temp


red_soul = pygame.image.load("sprites/Souls/new_soul.png").convert_alpha()
blue_soul = pygame.image.load("sprites/Souls/blue_soul.png").convert_alpha()

class Player:

    def __init__(self,info,inventory):
        self.img = pygame.image.load("sprites/Souls/new_soul.png").convert_alpha()
        self.size = self.img.get_size()
        self.rect = self.img.get_rect(x=0,y=0)
        self.info = info
        self.speed = 4.5
        self.velocity = [0,0]
        self.inv = inventory
        
    def __str__(self):
         return f"({self.img}\n{self.rect}\n{self.info})"
    
    def move(self,surface):
        self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)
        self.rect.clamp_ip(surface)
        
    def swap_img(self,flags):
        if flags == 'red':
            self.img = red_soul
        if flags == 'blue':
            self.img = blue_soul

    def update_stats(self):
        if self.info["level"]<20 and xp_system[self.info["level"]] <= self.info["xp"]:
            ecart = self.info["xp"] - xp_system[self.info["level"]]
            self.info["xp"] = ecart
            if self.info["level"]<20:
                self.info["level"] += 1
                self.info["hp"] = hp_system[self.info["level"]]
                self.info["current_hp"] = self.info["hp"]

        self.info["hp"] = hp_system[self.info["level"]]
        self.info["at"] = at_system[self.info["level"]]
        self.info["df"] = df_system[self.info["level"]]