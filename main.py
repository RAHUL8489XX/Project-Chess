import pygame
from board import Board

pygame.init()
WIDTH, HEIGHT = 640, 640
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Chess")

board = Board(WIN)

def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        board.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                board.handle_click(pos)

    pygame.quit()

if __name__ == "__main__":
    main()
