import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pokémon Battle")

# Load images (replace these filenames with actual image paths)
player_pokemon_image = pygame.image.load("P.png")
enemy_pokemon_image = pygame.image.load("C.png")

background_image = pygame.image.load("B.png")
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Scale images to fit the screen
player_pokemon_image = pygame.transform.scale(player_pokemon_image, (150, 150))
enemy_pokemon_image = pygame.transform.scale(enemy_pokemon_image, (150, 150))

# Define Pokemon class (similar to your existing code)
class Pokemon:
    def __init__(self, name, hp, max_hp, attack, defense, speed):
        self.name = name 
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.max_hp = hp

    def determine_turn_order(pokemon1, pokemon2):
        if pokemon1.speed > pokemon2.speed:
            return pokemon1, pokemon2 
        else: 
            return pokemon2, pokemon1
    
    def take_damage(self, damage):
        self.hp -= damage

    def is_fainted(self):
        return self.hp <= 0





# Set up fonts
font = pygame.font.Font(None, 36)

# Attack options
attack_options = ["Thunderbolt", "Quick Attack"]
selected_attack = None

# Animation variables
attack_animation_frames = 10
attack_animation_speed = 10

# Animation function
def animate_attack(attacker, defender):
    attacker_x, attacker_y = 50, 300
    defender_x, defender_y = 650, 100

    attacker_step = (defender_x - attacker_x) / attack_animation_frames
    defender_step = (attacker_x - defender_x) / attack_animation_frames

    for i in range(attack_animation_frames):
        screen.blit(background_image, (0, 0))  # Clear the screen

        attacker_x += attacker_step
        defender_x += defender_step

        screen.blit(player_pokemon_image, (attacker_x, attacker_y))
        screen.blit(enemy_pokemon_image, (defender_x, defender_y))

        pygame.draw.rect(screen, (0, 0, 0), (50, 480, 200, 20))
        pygame.draw.rect(screen, (0, 0, 0), (650, 280, 200, 20))

        pygame.draw.rect(screen, (0, 255, 0), (50, 480, (attacker.hp / attacker.max_hp) * 200, 20))
        pygame.draw.rect(screen, (0, 255, 0), (650, 280, (defender.hp / defender.max_hp) * 200, 20))

        pygame.display.flip()
        pygame.time.delay(attack_animation_speed)

    pygame.time.delay(500)

# Main game loop
def main():
    clock = pygame.time.Clock()
    running = True
    player_turn = True
    player_pokemon = Pokemon("Pikachu", 100, 120, 10, 7, 9)  
    enemy_pokemon = Pokemon("Charmander", 100, 120, 8, 9, 8)
    show_attack_options(player_pokemon, enemy_pokemon)
    
    while running:
        # player attacks
        player_turn = False
  
        # enemy attacks 
        player_turn = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and player_turn:
                if 350 <= event.pos[0] <= 550 and 500 <= event.pos[1] <= 550:
                    selected_attack = show_attack_options(player_pokemon, enemy_pokemon)
                    if selected_attack:
                        animate_attack(player_pokemon, enemy_pokemon)
                        enemy_pokemon.take_damage(player_pokemon.attack)
                        player_turn = False

        screen.blit(background_image, (0, 0))
        screen.blit(player_pokemon_image, (50, 300))
        screen.blit(enemy_pokemon_image, (650, 100))
        if not player_pokemon.is_fainted():
            pygame.draw.rect(screen, (0, 255, 0), (50, 480, (player_pokemon.hp / player_pokemon.max_hp) * 200, 20))
  
        else:
            faint_text = font.render("Fainted", True, (0, 0, 0))
            screen.blit(faint_text, (260, 475))

        if not enemy_pokemon.is_fainted():
            pygame.draw.rect(screen, (0, 255, 0), (650, 280, (enemy_pokemon.hp / enemy_pokemon.max_hp) * 200, 20))
  
        else:
            faint_text = font.render("Fainted", True, (0, 0, 0))
            screen.blit(faint_text, (850, 275))
        pygame.draw.rect(screen, (0, 0, 0), (50, 480, 200, 20))
        pygame.draw.rect(screen, (0, 0, 0), (650, 280, 200, 20))
        
        pygame.draw.rect(screen, (0, 255, 0), (50, 480, (player_pokemon.hp / player_pokemon.max_hp) * 200, 20))
        pygame.draw.rect(screen, (0, 255, 0), (650, 280, (enemy_pokemon.hp / enemy_pokemon.max_hp) * 200, 20))

        player_hp_text = font.render(str(player_pokemon.hp), True, (0, 0, 0))
        enemy_hp_text = font.render(str(enemy_pokemon.hp), True, (0, 0, 0))
        screen.blit(player_hp_text, (260, 475))
        screen.blit(enemy_hp_text, (850, 275))

        player_name_text = font.render(player_pokemon.name, True, (0, 0, 0))
        enemy_name_text = font.render(enemy_pokemon.name, True, (0, 0, 0))
        screen.blit(player_name_text, (50, 450))
        screen.blit(enemy_name_text, (650, 250))

        attack_button = pygame.Rect(350, 500, 200, 50)
        pygame.draw.rect(screen, (255, 0, 0), attack_button)
        attack_text = font.render("Attack", True, (255, 255, 255))
        screen.blit(attack_text, (420, 510))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

def show_attack_options(player_pokemon, enemy_pokemon):
    print(player_pokemon.name)
    attack_choice_text = font.render("Choose an Attack:", True, (0, 0, 0))
    option1_text = font.render("1. " + attack_options[0], True, (0, 0, 0))
    option2_text = font.render("2. " + attack_options[1], True, (0, 0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return attack_options[0]
                elif event.key == pygame.K_2:
                    return attack_options[1]
        
        screen.blit(background_image, (0, 0))
        screen.blit(player_pokemon_image, (50, 300))
        screen.blit(enemy_pokemon_image, (650, 100))

        pygame.draw.rect(screen, (0, 0, 0), (50, 480, 200, 20))
        pygame.draw.rect(screen, (0, 0, 0), (650, 280, 200, 20))
        
        pygame.draw.rect(screen, (0, 255, 0), (50, 480, (player_pokemon.hp / player_pokemon.max_hp) * 200, 20))
        pygame.draw.rect(screen, (0, 255, 0), (650, 280, (enemy_pokemon.hp / enemy_pokemon.max_hp) * 200, 20))

        player_hp_text = font.render(str(player_pokemon.max_hp), True, (0, 0, 0))
        enemy_hp_text = font.render(str(enemy_pokemon.max_hp), True, (0, 0, 0))
        screen.blit(player_hp_text, (260, 475))
        screen.blit(enemy_hp_text, (850, 275))

        player_name_text = font.render(player_pokemon.name, True, (0, 0, 0))
        enemy_name_text = font.render(enemy_pokemon.name, True, (0, 0, 0))
        screen.blit(player_name_text, (50, 450))
        screen.blit(enemy_name_text, (650, 250))

        attack_button = pygame.Rect(350, 500, 200, 50)
        pygame.draw.rect(screen, (255, 0, 0), attack_button)
        attack_text = font.render("Attack", True, (255, 255, 255))
        screen.blit(attack_text, (420, 510))

        screen.blit(attack_choice_text, (570, 510))
        screen.blit(option1_text, (570, 540))
        screen.blit(option2_text, (570, 570))

        pygame.display.flip()


if __name__ == "__main__":
    main()
