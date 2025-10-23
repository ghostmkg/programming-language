import pygame,random,sys,time
pygame.init()
WIDTH, HEIGHT = 600, 400
DOG_SPEED = 8
BONE_FALL_SPEED = 5
TIME_LIMIT = 60  # seconds for no-score timeout
WHITE = (255, 255, 255) # Background color
BROWN = (139, 69, 19) # Dog body color
DARK_BROWN = (100, 50, 20) # Dog ear and tail color
BLACK = (0, 0, 0) # Dog eye and nose color
BONE_LIGHT = (255, 255, 200) # Bone light color
BONE_DARK = (240, 220, 170) # Bone dark color

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐶 Hungry Dog")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 28)
dog = pygame.Rect(WIDTH // 2 - 25, HEIGHT - 70, 60, 40)
bones = []
score = 0
start_time = None  # Timer starts only if score = 0
def draw_bone(bone_rect):
    """Draws a bone using simple circles and rectangles."""
    pygame.draw.rect(
        screen, BONE_DARK, (bone_rect.x + 4, bone_rect.y + 4, bone_rect.width - 8, bone_rect.height - 8)
    )
    pygame.draw.circle(screen, BONE_LIGHT, (bone_rect.x + 5, bone_rect.y + 5), 8)
    pygame.draw.circle(screen, BONE_LIGHT, (bone_rect.x + bone_rect.width - 5, bone_rect.y + 5), 8)
    pygame.draw.circle(screen, BONE_LIGHT, (bone_rect.x + 5, bone_rect.y + bone_rect.height - 5), 8)
    pygame.draw.circle(screen, BONE_LIGHT, (bone_rect.x + bone_rect.width - 5, bone_rect.y + bone_rect.height - 5), 8)

def draw_dog():
    """Draws the cartoon dog."""
    # Body
    pygame.draw.rect(screen, BROWN, dog)
    # Head
    pygame.draw.circle(screen, BROWN, (dog.x + 55, dog.y + 15), 15)
    # Ear
    pygame.draw.polygon(screen, DARK_BROWN, [
        (dog.x + 60, dog.y),
        (dog.x + 70, dog.y - 10),
        (dog.x + 50, dog.y - 5)
    ])
    # Tail
    pygame.draw.polygon(screen, DARK_BROWN, [
        (dog.x, dog.y + 10),
        (dog.x - 10, dog.y),
        (dog.x, dog.y + 20)
    ])
    # Eye & Nose
    pygame.draw.circle(screen, BLACK, (dog.x + 60, dog.y + 10), 3)
    pygame.draw.circle(screen, BLACK, (dog.x + 68, dog.y + 15), 3)

def draw_game():
    """Renders the dog, bones, score, and timer."""
    screen.fill(WHITE)
    draw_dog()
    for bone in bones: # Draw all bones
        draw_bone(bone)
    score_text = font.render(f"Score: {score}", True, BLACK) # Score display
    screen.blit(score_text, (10, 10))
    if start_time and score == 0: # Timer display
        time_left = max(0, TIME_LIMIT - int(time.time() - start_time))
        timer_text = font.render(f"Time Left: {time_left}s", True, BLACK)
        screen.blit(timer_text, (WIDTH - 200, 10))
    pygame.display.flip()
while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed() # Dog movement
    if keys[pygame.K_LEFT] and dog.x > 0:
        dog.x -= DOG_SPEED
    if keys[pygame.K_RIGHT] and dog.x < WIDTH - dog.width:
        dog.x += DOG_SPEED
    if score == 0 and start_time is None:  # Start timer if score is 0
        start_time = time.time()
    if score == 0 and time.time() - start_time >= TIME_LIMIT:  # Check for timeout
        screen.fill(WHITE)
        msg = font.render("⏰ Time's up! Dog is hungry 😢", True, (255, 0, 0))
        screen.blit(msg, (WIDTH // 2 - 180, HEIGHT // 2 - 20))
        pygame.display.flip()
        pygame.time.wait(2500)
        pygame.quit()
        sys.exit()
    if random.randint(1, 30) == 1: # Randomly generate bones
        x_pos = random.randint(0, WIDTH - 40)
        bones.append(pygame.Rect(x_pos, 0, 40, 20))
    for bone in list(bones): # Move bones and check for collisions
        bone.y += BONE_FALL_SPEED
        if bone.y > HEIGHT:
            bones.remove(bone)
        elif dog.colliderect(bone):
            bones.remove(bone)
            score += 1
            start_time = None  # stop timer once score > 0
    draw_game()
