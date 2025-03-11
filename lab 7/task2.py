import pygame
import sys
import os


pygame.init()

pygame.mixer.init()
clock = pygame.time.Clock()

size = (700, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Music player')


image = pygame.image.load("/Users/adiyarkarim/Downloads/1.jpeg")


music_dir = "/Users/adiyarkarim/Desktop/songs"
music_files = [f for f in os.listdir(music_dir) if f.endswith('.m4a')]

if not music_files:
    print("No music files found in the specified directory.")
    pygame.quit()
    sys.exit()


font = pygame.font.SysFont('Avenir', 30)


i = 0
vol = 1
begin = False
is_playing = False


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                begin = True
                pygame.mixer.music.load(os.path.join(music_dir, music_files[i]))
                pygame.mixer.music.play()
                is_playing = True

            if event.key == pygame.K_SPACE and begin:
                if is_playing:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
                is_playing = not is_playing

            if event.key == pygame.K_RIGHT and begin:
                i = (i + 1) % len(music_files)
                pygame.mixer.music.load(os.path.join(music_dir, music_files[i]))
                pygame.mixer.music.play()
                is_playing = True

            if event.key == pygame.K_LEFT and begin:
                i = (i - 1) % len(music_files)
                pygame.mixer.music.load(os.path.join(music_dir, music_files[i]))
                pygame.mixer.music.play()
                is_playing = True

            if event.key == pygame.K_UP:
                vol += 0.1
                pygame.mixer.music.set_volume(min(vol, 1.0))

            if event.key == pygame.K_DOWN:
                vol -= 0.1
                pygame.mixer.music.set_volume(max(vol, 0.0))


    
    screen.blit(image, (0, 0))


    if begin:
        s = font.render(music_files[i][:-4], True, 'black') 
        screen.blit(s, (34, 50))
    clock.tick(10)
    pygame.display.flip()