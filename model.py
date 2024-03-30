import pygame
# Enemy DATABASE

class Sans:

    def __init__(self):
        self.sheet = pygame.image.load("sprites/enemy/Sans_sheet.png").convert_alpha()
        self.img = pygame.image.load("sprites/enemy/Sans_Model.png").convert_alpha()
        self.rect = self.img.get_rect()
        self.size = self.img.get_size()
        self.index = [0,0]
        self.info = {
            "name" : "Sans",
            "desc" : "* Sans - 1 ATK 1 DEF\n* The easiest enemy.\n* Can only deal 1 damage.",
            "hp" : 40,
            "at" : 1,
            "df" : 1,
            "xp_reward" : 0,
            "gold_reward" : 0,
            "KR" : True
        }
        self.act = {
            0 : "check",
            1 : "compliment",
            2 : "insult",
            3 : "limitless",
            4 : "mental kill",
            5 : "topo",
        }
        self.act_txt = {
            "check" : "* The easiest enemy.\n* Can only deal 1 damage.",
            "compliment" : "* He don't seems to care\n* Its too late.",
            "insult" : "* He's ATK power increased",
            "limitless" : "* Wait what is thats ?"
        }
        self.mercy = {
            0 : "Spare",
        }
        self.mercy_txt = {
            "Spare" : "* Wait wait, sparing now ?\n* NO YOU WILL NOT =)"
        }
    
    def update(self):
        self.rect = self.img.get_rect()
        self.size = self.img.get_size()
    
    def anim_simple(self,boxrect):
        x,y = self.img.get_size()
        img = pygame.Surface((x,y),pygame.SRCALPHA).convert_alpha()
        self.index[0] += 0.03
        if self.index[0] >= 2:
            self.index[0] = 0
        if self.index[0] < 1:
            img.blit(self.sheet,(0,0),(0,y*10,x,y))
        elif self.index[0] < 2:
            img.blit(self.sheet,(0,0),(0,y*11,x,y))
        x,y = boxrect.midtop
        rect = img.get_rect(midbottom = (x+20,y-10))
        return img,rect
    
    def anim_hand_up(self):
        frame_1 = pygame.image.load("sprites/enemy/Sans/sans_hand_up.png").convert_alpha()
        frame_2 = pygame.image.load("sprites/enemy/Sans/sans_hand_up_down_trans.png").convert_alpha()
        frame_3 = pygame.image.load("sprites/enemy/Sans/sans_hand_down.png").convert_alpha()
        self.index[1] += 0.1
        if self.index[1] >= 3:
            self.index[1] = 0
        if self.index[1] < 0.5:
            self.img = frame_3
        elif self.index[1] < 1:
            self.img = frame_2
        elif self.index[1] < 3:
            self.img = frame_1
    
    def anim_hand_down(self):
        frame_1 = pygame.image.load("sprites/enemy/Sans/sans_hand_up.png").convert_alpha()
        frame_2 = pygame.image.load("sprites/enemy/Sans/sans_hand_up_down_trans.png").convert_alpha()
        frame_3 = pygame.image.load("sprites/enemy/Sans/sans_hand_down.png").convert_alpha()
        self.index[1] += 0.1
        if self.index[1] >= 3:
            self.index[1] = 0
        if self.index[1] < 0.5:
            self.img = frame_1
        elif self.index[1] < 1:
            self.img = frame_2
        elif self.index[1] < 3:
            self.img = frame_3
    
    def anim_hand_left(self):
        frame_1 = pygame.image.load("sprites/enemy/Sans/sans_hand_left.png").convert_alpha()
        frame_2 = pygame.image.load("sprites/enemy/Sans/sans_hand_left_trans.png").convert_alpha()
        frame_3 = pygame.image.load("sprites/enemy/Sans/sans_1.png").convert_alpha()
        self.index[1] += 0.1
        if self.index[1] >= 3:
            self.index[1] = 0
        if self.index[1] < 0.5:
            self.img = frame_3
        elif self.index[1] < 1:
            self.img = frame_2
        elif self.index[1] < 3:
            self.img = frame_1

    def anim_hand_left(self):
        frame_1 = pygame.image.load("sprites/enemy/Sans/sans_hand_left.png").convert_alpha()
        frame_2 = pygame.image.load("sprites/enemy/Sans/sans_hand_left_trans.png").convert_alpha()
        frame_3 = pygame.image.load("sprites/enemy/Sans/sans_1.png").convert_alpha()
        self.index[1] += 0.1
        if self.index[1] >= 3:
            self.index[1] = 0
        if self.index[1] < 0.5:
            self.img = frame_1
        elif self.index[1] < 1:
            self.img = frame_2
        elif self.index[1] < 3:
            self.img = frame_3

class Froggit2:

    def __init__(self):
        self.sheet = pygame.image.load("sprites/enemy/Froggit2_sheet.png").convert_alpha()
        self.img = pygame.image.load("sprites/enemy/Froggit2.png").convert_alpha()
        self.rect = self.img.get_rect()
        self.size = self.img.get_size()
        self.index = [0,0]
        self.info = {
            "name" : "Froggit",
            "desc" : "* FROGGIT - ATK 6 DEF 8\n* Life is difficult for this enemy.\n* Seems more powerfull than the others",
            "hp" : 30,
            "at" : 6,
            "df" : 8,
            "xp_reward" : 15,
            "gold_reward" : 30,
            "KR" : False
        }
        self.act = {
            "left_button1" : "stats",
            "left_button2" : "compliment",
            "left_button3" : "insult",
            "right_button1" : "limitless"
        }
        

    def update(self):
        self.rect = self.img.get_rect()
        self.size = self.img.get_size()
    
    def anim_simple(self,boxrect):
        x,y = self.img.get_size()
        img = pygame.Surface((x,y),pygame.SRCALPHA).convert_alpha()
        self.index[0] += 0.03
        if self.index[0] >= 2:
            self.index[0] = 0
        if self.index[0] < 1:
            img.blit(self.sheet,(0,0),(0,0,x,y))
        elif self.index[0] < 2:
            img.blit(self.sheet,(0,0),(0,y,x,y))
        x,y = boxrect.midtop
        rect = img.get_rect(midbottom = (x,y-10))
        return img,rect

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

Nice_Cream = {
    "state" : "consumable",
    "name" : "Nie Cream",
    "desc" : "Instead of a joke, the wrapper says something nice. ",
    "hp_give" : 15,
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
player_inventory = [Butterscotch_Pie,Spider_Cider,Snowman_Piece,Spider_Cider,Spider_Donut,Bandage,Snail_Pie]
sort_inv()

red_soul = pygame.image.load("sprites/Souls/red_soul.png").convert_alpha()
blue_soul = pygame.image.load("sprites/Souls/blue_soul.png").convert_alpha()
yellow_soul = pygame.image.load("sprites/Souls/yellow_soul.png").convert_alpha()
green_soul = pygame.image.load("sprites/Souls/green_soul.png").convert_alpha()
purple_soul = pygame.image.load("sprites/Souls/purple_soul.png").convert_alpha()

class Player:

    def __init__(self,info,inventory):
        self.img = pygame.image.load("sprites/Souls/red_soul.png").convert_alpha()
        self.size = self.img.get_size()
        self.rect = self.img.get_rect(x=0,y=0)
        self.info = info
        self.speed = 3
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
        if flags == 'yellow':
            self.img = yellow_soul
        if flags == 'green':
            self.img = green_soul
        if flags == 'purple':
            self.img = purple_soul

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