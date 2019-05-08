import pygame
import sys
import os
from pygame import Vector2

# added this comment
RESOLUTION = (800, 600)

display_surface = pygame.display.set_mode(RESOLUTION)
tmp = (160, 160, 160)
clock = pygame.time.Clock()

game_running = True
player_image = pygame.image.load("playertank.png")



class Player(pygame.sprite.Sprite):
        def __init__(self, position, size, speed, rotation_speed=1):
                super().__init__()
                self.position = Vector2(position)
                self.base_image = pygame.Surface(size)
                self.bullet_id = bullet_id
                self.base_image.set_colorkey((1, 1, 1))
                self.base_image.fill((255, 0, 0))
                self.image = self.base_image
                self.rect = self.image.get_rect(center=position)
                self.rotation_speed = rotation_speed
                self.current_rotation = 0
                self.base_movement_vector = Vector2(0, speed)
                self.movement_vector = Vector2(0, speed)
 
                

        def rotate(self, direction):
                self.current_rotation += direction * self.rotation_speed
                self.image = pygame.transform.rotate(self.base_image, -self.current_rotation)
                self.rect = self.image.get_rect(center=self.position)


        def move(self, moving_forwards):
                if moving_forwards:
                        self.movement_vector = self.base_movement_vector.rotate(self.current_rotation)
                        self.position += self.movement_vector
                        self.rect = self.image.get_rect(center=self.position)
                else:
                        self.movement_vector = self.base_movement_vector.rotate(self.current_rotation)
                        self.position -= self.movement_vector
                        self.rect = self.image.get_rect(center=self.position)

                




player = Player((50, 50), (40, 52), 5, 3)
player2 = Player((50, 500), (40, 52), 5, 3)
player_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
player_group.add(player)
player_group.add(player2) 

while game_running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        game_running = False
                        break

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_d]:
                player.rotate(1)
        if keys_pressed[pygame.K_a]:
                player.rotate(-1)


        if keys_pressed[pygame.K_w]:
                player.move(True)
        if keys_pressed[pygame.K_s]:
                player.move(False)

        if keys_pressed[pygame.K_RIGHT]:
                player2.rotate(1)
        if keys_pressed[pygame.K_LEFT]:
                player2.rotate(-1)
        if keys_pressed[pygame.K_UP]:
                player2.move(True)
        if keys_pressed[pygame.K_DOWN]:
                player2.move(False) 
        
                
        
        display_surface.fill(tmp)
        player_group.draw(display_surface)
        pygame.draw.rect(display_surface, (255, 255, 0), player.rect, 5)
        bullet_group.update()
        bullet_group.draw(display_surface)
        pygame.display.update()
        
        clock.tick(60)

pygame.quit()

