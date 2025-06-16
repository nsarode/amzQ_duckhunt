from ursina import *
import random
import json
import os

# Initialize the game
app = Ursina()
window.vsync = False  # Disable vsync for more responsive input
window.fps_counter.enabled = True  # Show FPS counter to monitor performance
window.exit_button.visible = True  # Make sure the exit button is visible
window.borderless = False  # Allow window borders for resizing
window.fullscreen = False  # Start in windowed mode
window.size = (800, 600)  # Smaller default window size
window.vsync = False  # Disable vsync for more responsive input
window.fps_counter.enabled = True  # Show FPS counter to monitor performance

# Global variables
GAME_TIME = 60  # seconds
score = 0
high_score = 0
time_remaining = GAME_TIME
game_active = False
game_paused = False
ducks = []
duck_speed_multiplier = 1.0
shots_fired = 0
shots_hit = 0

# Try to load high score from file
def load_high_score():
    global high_score
    try:
        if os.path.exists('duck_hunt_high_score.json'):
            with open('duck_hunt_high_score.json', 'r') as f:
                data = json.load(f)
                high_score = data.get('high_score', 0)
    except Exception as e:
        print(f"Error loading high score: {e}")

# Save high score to file
def save_high_score():
    try:
        with open('duck_hunt_high_score.json', 'w') as f:
            json.dump({'high_score': high_score}, f)
    except Exception as e:
        print(f"Error saving high score: {e}")

# Load high score at startup
load_high_score()

# Create game states
class GameState(Enum):
    MAIN_MENU = 0
    PLAYING = 1
    GAME_OVER = 2
    PAUSED = 3

current_state = GameState.MAIN_MENU

# Sound effects (placeholders - would need actual sound files)
shoot_sound = None
hit_sound = None
miss_sound = None
quack_sound = None

try:
    # Load sounds if available
    shoot_sound = Audio('shoot.wav', loop=False, autoplay=False)
    hit_sound = Audio('hit.wav', loop=False, autoplay=False)
    miss_sound = Audio('miss.wav', loop=False, autoplay=False)
    quack_sound = Audio('quack.wav', loop=False, autoplay=False)
except:
    print("Sound files not found. Continuing without sound.")

# Create UI elements
score_text = Text(text="Score: 0", position=(-0.85, 0.45), scale=2, origin=(0, 0))
high_score_text = Text(text=f"High Score: {high_score}", position=(-0.85, 0.4), scale=1.5, origin=(0, 0))
time_text = Text(text=f"Time: {GAME_TIME}", position=(0.7, 0.45), scale=2, origin=(0, 0))
accuracy_text = Text(text="Accuracy: 0%", position=(0, 0.45), scale=1.5, origin=(0, 0))

# Main menu UI
title_text = Text(text="DUCK HUNT", scale=4, origin=(0, 0), y=0.3)
start_button = Button(text="Start Game", scale=(0.3, 0.1), position=(0, 0), on_click=lambda: start_game())
quit_button = Button(text="Quit", scale=(0.3, 0.1), position=(0, -0.15), on_click=application.quit)

# Add window size controls to main menu
window_size_text = Text(text="Window Size Controls:", scale=1.5, origin=(0, 0), y=-0.3)
window_size_help = Text(text="F9: Increase | F10: Decrease | F11: Toggle Fullscreen", scale=1, origin=(0, 0), y=-0.35)
window_size_text.enabled = True
window_size_help.enabled = True

# Game over UI
game_over_text = Text(text="GAME OVER", scale=4, origin=(0, 0), y=0.3, enabled=False)
final_score_text = Text(text="Final Score: 0", scale=2, origin=(0, 0), y=0.1, enabled=False)
restart_button = Button(text="Play Again", scale=(0.3, 0.1), position=(0, -0.1), on_click=lambda: start_game(), enabled=False)
menu_button = Button(text="Main Menu", scale=(0.3, 0.1), position=(0, -0.25), on_click=lambda: show_main_menu(), enabled=False)

# Pause menu UI
pause_text = Text(text="PAUSED", scale=4, origin=(0, 0), y=0.3, enabled=False)
resume_button = Button(text="Resume", scale=(0.3, 0.1), position=(0, 0), on_click=lambda: resume_game(), enabled=False)
pause_menu_button = Button(text="Main Menu", scale=(0.3, 0.1), position=(0, -0.15), on_click=lambda: show_main_menu(), enabled=False)

# Create game environment
def create_environment():
    # Sky
    Sky()
    
    # Ground
    ground = Entity(
        model='plane',
        scale=(100, 1, 100),
        color=color.green,
        texture='grass',
        collider='box',
        position=(0, -1, 0)
    )
    
    # Trees (simple placeholders)
    for i in range(15):
        x = random.uniform(-40, 40)
        z = random.uniform(-40, -5)  # Trees in the background
        
        trunk = Entity(
            model='cylinder',
            color=color.brown,
            scale=(1, random.uniform(3, 5), 1),
            position=(x, 0, z)
        )
        
        leaves = Entity(
            model='sphere',
            color=color.green,
            scale=(3, 2, 3),
            position=(x, trunk.scale_y + 1, z)
        )

# Duck class
class Duck(Entity):
    def __init__(self, **kwargs):
        # Use a simple cube as placeholder for the duck model
        super().__init__(
            model='cube',
            texture='white_cube',
            scale=(1, 0.5, 1),
            color=color.orange,
            collider='box',
            position=(random.uniform(-15, 15), random.uniform(0, 10), random.uniform(-10, -20)),
            **kwargs
        )
        
        # Movement parameters
        self.speed = random.uniform(3, 5) * duck_speed_multiplier
        self.direction = Vec3(
            random.uniform(-1, 1),
            random.uniform(-0.2, 0.5),
            random.uniform(0.5, 1)
        ).normalized()
        
        # Add simple animation
        self.animate_x(self.x + random.uniform(-5, 5), duration=1, loop=True, curve=curve.in_out_sine)
        self.animate_y(self.y + random.uniform(-2, 2), duration=1.5, loop=True, curve=curve.in_out_sine)
        
        # Add wings (simple placeholders)
        self.left_wing = Entity(
            parent=self,
            model='cube',
            color=color.orange.tint(-.1),
            scale=(0.7, 0.1, 0.5),
            position=(-0.7, 0, 0)
        )
        
        self.right_wing = Entity(
            parent=self,
            model='cube',
            color=color.orange.tint(-.1),
            scale=(0.7, 0.1, 0.5),
            position=(0.7, 0, 0)
        )
        
        # Animate wings
        self.left_wing.animate_rotation_z(30, duration=0.5, loop=True, curve=curve.in_out_sine)
        self.right_wing.animate_rotation_z(-30, duration=0.5, loop=True, curve=curve.in_out_sine)
        
        # Add a bill
        self.bill = Entity(
            parent=self,
            model='cube',
            color=color.yellow,
            scale=(0.3, 0.2, 0.7),
            position=(0, -0.1, 0.6)
        )
    
    def update(self):
        if not game_active or game_paused:
            return
            
        # Move the duck
        self.position += self.direction * self.speed * time.dt
        
        # Change direction randomly or when reaching boundaries
        if random.random() < 0.01 or \
           abs(self.x) > 20 or \
           self.y < 0 or self.y > 15 or \
           self.z > 10 or self.z < -30:
            
            # Ensure duck stays in playable area
            if self.x < -20: self.x = -20
            if self.x > 20: self.x = 20
            if self.y < 0: self.y = 0
            if self.y > 15: self.y = 15
            if self.z < -30: self.z = -30
            if self.z > 10: 
                # If duck gets too close to camera, send it back
                self.z = -25
                
            # New random direction
            self.direction = Vec3(
                random.uniform(-1, 1),
                random.uniform(-0.2, 0.5),
                random.uniform(0.5, 1) if self.z < -15 else random.uniform(-1, 0.5)
            ).normalized()
    
    def hit(self):
        global score, shots_hit
        
        # Play hit sound
        if hit_sound:
            hit_sound.play()
            
        # Increase score
        score += 10
        shots_hit += 1
        update_score_display()
        
        # Create hit effect
        create_hit_effect(self.position)
        
        # Duck falling animation
        self.animate_y(-5, duration=2, curve=curve.in_out_sine)
        self.animate_rotation_x(-90, duration=2)
        
        # Remove duck after animation
        invoke(self.remove_duck, delay=2)
    
    def remove_duck(self):
        if self in ducks:
            ducks.remove(self)
        destroy(self)
        
        # Spawn a new duck
        if game_active and not game_paused:
            spawn_duck()

# Create hit effect (particles)
def create_hit_effect(position):
    for i in range(15):
        particle = Entity(
            model='sphere',
            color=color.yellow,
            scale=0.2,
            position=position,
            texture='circle'
        )
        
        # Random direction
        direction = Vec3(
            random.uniform(-1, 1),
            random.uniform(-1, 1),
            random.uniform(-1, 1)
        ).normalized()
        
        # Animate particle
        particle.animate_position(
            position + direction * random.uniform(1, 3),
            duration=0.5,
            curve=curve.out_expo
        )
        
        particle.animate_scale(0, duration=0.5)
        particle.animate_color(color.clear, duration=0.5)
        
        # Destroy particle after animation
        destroy(particle, delay=0.5)

# Create miss effect
def create_miss_effect(position):
    # Simple text indicator
    miss_text = Text(
        text="MISS",
        position=position,
        scale=2,
        color=color.red,
        origin=(0, 0)
    )
    
    # Animate and destroy
    miss_text.animate_position(position + Vec3(0, 0.5, 0), duration=0.5)
    miss_text.animate_scale(0, duration=0.5)
    destroy(miss_text, delay=0.5)

# Spawn a duck
def spawn_duck():
    if len(ducks) < 5 and game_active and not game_paused:  # Limit number of ducks
        duck = Duck()
        ducks.append(duck)

# Update score display
def update_score_display():
    score_text.text = f"Score: {score}"
    high_score_text.text = f"High Score: {high_score}"
    
    # Update accuracy
    if shots_fired > 0:
        accuracy = (shots_hit / shots_fired) * 100
        accuracy_text.text = f"Accuracy: {accuracy:.1f}%"
    else:
        accuracy_text.text = "Accuracy: 0%"

# Update time display
def update_time_display():
    time_text.text = f"Time: {int(time_remaining)}"

# Game timer
def game_timer():
    global time_remaining, game_active, high_score
    
    if game_active and not game_paused:
        time_remaining -= time.dt
        update_time_display()
        
        # Increase difficulty over time
        global duck_speed_multiplier
        duck_speed_multiplier = 1.0 + (1.0 - time_remaining / GAME_TIME)
        
        # End game when time runs out
        if time_remaining <= 0:
            time_remaining = 0
            game_active = False
            
            # Update high score
            if score > high_score:
                high_score = score
                save_high_score()
                
            # Show game over screen
            show_game_over()

# Start the game
def start_game():
    global game_active, score, time_remaining, shots_fired, shots_hit, duck_speed_multiplier, current_state
    
    # Reset game variables
    game_active = True
    current_state = GameState.PLAYING
    score = 0
    time_remaining = GAME_TIME
    shots_fired = 0
    shots_hit = 0
    duck_speed_multiplier = 1.0
    
    # Update displays
    update_score_display()
    update_time_display()
    
    # Hide menus
    toggle_main_menu(False)
    toggle_game_over_menu(False)
    toggle_pause_menu(False)
    
    # Show game UI
    score_text.enabled = True
    high_score_text.enabled = True
    time_text.enabled = True
    accuracy_text.enabled = True
    
    # Clear existing ducks
    for duck in ducks[:]:
        destroy(duck)
    ducks.clear()
    
    # Spawn initial ducks
    for _ in range(5):
        spawn_duck()
    
    # Make sure mouse is locked for camera control
    mouse.locked = True
    
    # Reset camera controller target rotation
    if hasattr(camera_controller, 'target_rotation'):
        camera_controller.target_rotation = Vec2(0, 0)

# Show game over screen
def show_game_over():
    toggle_game_over_menu(True)
    final_score_text.text = f"Final Score: {score}"
    
    # Hide game UI
    score_text.enabled = False
    high_score_text.enabled = False
    time_text.enabled = False
    accuracy_text.enabled = False

# Show main menu
def show_main_menu():
    global game_active, game_paused, current_state
    
    game_active = False
    game_paused = False
    current_state = GameState.MAIN_MENU
    
    # Show main menu
    toggle_main_menu(True)
    toggle_game_over_menu(False)
    toggle_pause_menu(False)
    
    # Hide game UI
    score_text.enabled = False
    high_score_text.enabled = False
    time_text.enabled = False
    accuracy_text.enabled = False
    
    # Clear existing ducks
    for duck in ducks[:]:
        destroy(duck)
    ducks.clear()
    
    # Unlock mouse for menu interaction
    mouse.locked = False
    mouse.visible = True

# Toggle main menu visibility
def toggle_main_menu(visible):
    title_text.enabled = visible
    start_button.enabled = visible
    quit_button.enabled = visible
    window_size_text.enabled = visible
    window_size_help.enabled = visible

# Toggle game over menu visibility
def toggle_game_over_menu(visible):
    game_over_text.enabled = visible
    final_score_text.enabled = visible
    restart_button.enabled = visible
    menu_button.enabled = visible

# Toggle pause menu visibility
def toggle_pause_menu(visible):
    pause_text.enabled = visible
    resume_button.enabled = visible
    pause_menu_button.enabled = visible

# Pause the game
def pause_game():
    global game_paused, current_state
    
    if game_active and not game_paused:
        game_paused = True
        current_state = GameState.PAUSED
        toggle_pause_menu(True)
        mouse.locked = False  # Unlock mouse for menu interaction
        mouse.visible = True  # Make mouse visible in menus

# Resume the game
def resume_game():
    global game_paused, current_state
    
    if game_active and game_paused:
        game_paused = False
        current_state = GameState.PLAYING
        toggle_pause_menu(False)
        mouse.locked = True  # Lock mouse for gameplay
        mouse.visible = False  # Hide mouse during gameplay

# Create crosshair
crosshair = Entity(
    model='quad',
    texture='circle',
    color=color.red,
    scale=0.02,
    position=(0, 0),  # Center of screen
    parent=camera.ui,  # Make it part of the UI
    z=-0.1  # Ensure it's in front of other UI elements
)

# Gun model (simple placeholder)
gun = Entity(
    model='cube',
    texture='white_cube',
    color=color.gray,
    scale=(0.3, 0.3, 1),
    position=(0.5, -0.5, 0),
    parent=camera.ui,
    rotation=(0, 0, 0),
    z=-0.2  # Ensure it's behind the crosshair but in front of other UI
)

# Handle input
def input(key):
    global shots_fired
    
    # Emergency exit - always available
    if key == 'q':
        application.quit()
        
    # Toggle fullscreen
    if key == 'f11':
        window.fullscreen = not window.fullscreen
        print(f"Fullscreen: {window.fullscreen}")
    
    # Decrease window size
    if key == 'f10':
        if not window.fullscreen:
            current_size = window.size
            new_size = (int(current_size[0] * 0.8), int(current_size[1] * 0.8))
            window.size = new_size
            print(f"Window size decreased to {new_size}")
    
    # Increase window size
    if key == 'f9':
        if not window.fullscreen:
            current_size = window.size
            new_size = (int(current_size[0] * 1.2), int(current_size[1] * 1.2))
            window.size = new_size
            print(f"Window size increased to {new_size}")
    
    # Main game controls
    if key == 'left mouse down' and game_active and not game_paused:
        # Play shoot sound
        if shoot_sound:
            shoot_sound.play()
            
        # Animate gun recoil
        gun.animate_position((0.5, -0.6, 0), duration=0.05, curve=curve.out_expo)
        gun.animate_position((0.5, -0.5, 0), duration=0.1, delay=0.05, curve=curve.out_bounce)
        
        # Shoot ray from center of screen
        shots_fired += 1
        hit_info = raycast(camera.world_position, camera.forward, distance=100)
        
        # Check for hit
        hit = False
        for duck in ducks[:]:  # Use a copy of the list since we might modify it
            # Check if ray hit a duck
            if hit_info.entity == duck:
                duck.hit()
                hit = True
                break
        
        # If no hit, play miss sound and effect
        if not hit:
            if miss_sound:
                miss_sound.play()
                
            # Create miss effect at the point where the ray hit
            if hit_info.hit:
                create_miss_effect(hit_info.world_point)
            else:
                # If ray didn't hit anything, show miss at a distance
                create_miss_effect(camera.world_position + camera.forward * 20)
                
            # Deduct points for miss
            global score
            score -= 5
            if score < 0:
                score = 0
            update_score_display()
    
    # Pause/unpause game
    if key == 'escape' and game_active:
        if game_paused:
            resume_game()
        else:
            pause_game()
    
    # Restart game
    if key == 'r' and (not game_active or game_paused):
        start_game()

# Update function
def update():
    # Process emergency exit key
    if held_keys['q'] and (held_keys['control'] or held_keys['shift']):
        print("Emergency exit triggered")
        application.quit()
        
    # Run game timer
    if current_state == GameState.PLAYING:
        game_timer()
    
    # Spawn ducks if needed
    if game_active and not game_paused and len(ducks) < 5:
        if random.random() < 0.02:  # Small chance each frame
            spawn_duck()

# Set up the game
def setup_game():
    # Create environment
    create_environment()
    
    # Show main menu
    show_main_menu()
    
    # Hide game UI initially
    score_text.enabled = False
    high_score_text.enabled = False
    time_text.enabled = False
    accuracy_text.enabled = False
    
    # Set mouse settings for better responsiveness
    mouse.locked = True
    mouse.visible = False
    mouse.sensitivity = Vec2(50, 50)

# Set up the game
setup_game()

# Enable mouse control for camera
mouse.locked = True
camera.fov = 90

# Add a custom camera controller to handle mouse movement
class CameraController(Entity):
    def __init__(self):
        super().__init__()
        self.speed = 2
        self.mouse_sensitivity = Vec2(70, 70)  # Increased sensitivity
        self.target_rotation = Vec2(0, 0)
        
    def update(self):
        if not game_active or game_paused:
            return
            
        # Direct camera control without smoothing for more responsive feel
        camera.rotation_x -= mouse.velocity[1] * self.mouse_sensitivity[1] * time.dt
        camera.rotation_y += mouse.velocity[0] * self.mouse_sensitivity[0] * time.dt
        
        # Clamp vertical rotation
        camera.rotation_x = clamp(camera.rotation_x, -90, 90)

# Set up the game
setup_game()

# Enable mouse control for camera
mouse.locked = True
camera.fov = 90

# Create and activate the camera controller
camera_controller = CameraController()

# Run the game
app.run()
