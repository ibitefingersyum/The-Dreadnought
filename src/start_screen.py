import pygame
import sys

class StartScreen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.font_title = pygame.font.Font(None, 80)
        self.font_subtitle = pygame.font.Font(None, 40)
        self.font_text = pygame.font.Font(None, 30)
        self.clicked = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.clicked = True
        return True

    def draw(self, screen):
        screen.fill((10, 10, 30))
        
        title = self.font_title.render("THE DREADNOUGHT", True, (150, 0, 200))
        title_rect = title.get_rect(center=(self.width // 2, self.height // 4))
        screen.blit(title, title_rect)
         
        subtitle = self.font_subtitle.render("ngl hella ai generated", True, (50, 150, 200))
        subtitle_rect = subtitle.get_rect(center=(self.width // 2, self.height // 2 - 50))
        screen.blit(subtitle, subtitle_rect)
        
        start_text = self.font_text.render("Click to Start", True, (255, 255, 0))
        start_rect = start_text.get_rect(center=(self.width // 2, self.height // 2 + 100))
        screen.blit(start_text, start_rect)
        
        pygame.display.flip()

    def is_done(self):
        return self.clicked
