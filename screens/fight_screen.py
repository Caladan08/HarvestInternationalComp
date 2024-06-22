import pygame
from pygame.locals import *
from config import *
from functions import *
from components import *
from player import *
import pygame_widgets

def fight_screen(self, max_enemy_hp):
  fight = True
  discard_screen = False
  remaining_screen = False

  remaining_cards = []
  discarded_cards = []

  deck_title = pygame.font.Font("EBGaramond.ttf", 45)

  fight_background = pygame.transform.scale(self.raw_fight_background, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
  enemy_hp = 10
  raw_card_img = pygame.image.load("./images/StrikeCard.png")

  black_bg = pygame.Surface((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), pygame.SRCALPHA)
  black_bg.fill((0, 0, 0, 200))

  fade_in(self, self.SCREEN_WIDTH, self.SCREEN_HEIGHT, fight_background)

  player_health_bar = PlayerHealthBar(self.screen, self.player_hp)
  enemy_health_bar = EnemyHealthBar(self.screen, enemy_hp, max_enemy_hp)

  discard_pile = DiscardPile(self.screen)  
  remaining_pile = RemainingPile(self.screen)
    
  while fight:
    while remaining_screen:
      events = pygame.event.get()

      for event in events:
        if event.type == pygame.QUIT:
          fight = False
          self.running = False
          self.playing = False
        elif event.type == VIDEORESIZE:
          self.screen.blit(pygame.transform.scale(black_bg, event.dict['size']), (0, 0))
          self.SCREEN_WIDTH, self.SCREEN_HEIGHT = event.dict['size']

      back_arrow = BackArrow(self.screen, "left", self.SCREEN_WIDTH)

      title = deck_title.render("Remaining Cards", True, WHITE)
      title_coords = title.get_rect(center=(self.SCREEN_WIDTH / 2, 40))
      self.screen.blit(title, title_coords)

      if back_arrow.is_pressed():
        remaining_screen = False
        self.screen.blit(fight_background, (0, 0))

      pygame.display.update()

    while discard_screen:
      events = pygame.event.get()

      for event in events:
        if event.type == pygame.QUIT:
          fight = False
          self.running = False
          self.playing = False
        elif event.type == VIDEORESIZE:
          self.screen.blit(pygame.transform.scale(black_bg, event.dict['size']), (0, 0))
          self.SCREEN_WIDTH, self.SCREEN_HEIGHT = event.dict['size']

      back_arrow = BackArrow(self.screen, "right", self.SCREEN_WIDTH)

      title = deck_title.render("Discarded Cards", True, WHITE)
      title_coords = title.get_rect(center=(self.SCREEN_WIDTH / 2, 40))
      self.screen.blit(title, title_coords)

      if back_arrow.is_pressed():
        discard_screen = False
        self.screen.blit(fight_background, (0, 0))

      pygame.display.update()
      
    events = pygame.event.get()
    for event in events:
      if event.type == pygame.QUIT:
        fight = False
        self.running = False
        self.playing = False
      elif event.type == VIDEORESIZE:
        self.screen.blit(pygame.transform.scale(black_bg, event.dict['size']), (0, 0))
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = event.dict['size']

    player_health_bar.draw(self.screen)
    enemy_health_bar.draw(self.screen, self.SCREEN_WIDTH)

    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    # display_piles()
    discard_pile.draw(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
    remaining_pile.draw(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)

    show_card(self, "left", self.SCREEN_HEIGHT, raw_card_img)
    show_card(self, "mid", self.SCREEN_HEIGHT, raw_card_img)
    show_card(self, "right", self.SCREEN_HEIGHT, raw_card_img)

    if remaining_pile.is_pressed(mouse_pos, mouse_pressed):
      self.screen.blit(black_bg, (0, 0))
      remaining_screen = True

    if discard_pile.is_pressed(mouse_pos, mouse_pressed):
      self.screen.blit(black_bg, (0, 0))
      discard_screen = True

    pygame_widgets.update(events)
    pygame.display.update()
