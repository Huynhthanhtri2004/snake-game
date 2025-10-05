import pygame
import random
import sys

class SnakeGame:
    def __init__(self):
        # Khởi tạo Pygame
        pygame.init()
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("🐍 Snake Game")

        # Màu sắc
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.green = (0, 255, 0)
        self.red = (255, 0, 0)

        # Cấu hình rắn
        self.snake_block = 10
        self.snake_speed = 15
        self.snake_position = [100, 50]
        self.snake_body = [[100, 50], [90, 50], [80, 50]]

        # Mồi
        self.food_position = [random.randrange(1, (self.width // 10)) * 10,
                              random.randrange(1, (self.height // 10)) * 10]
        self.food_spawned = True

        # Hướng di chuyển
        self.snake_direction = "RIGHT"
        self.change_to = self.snake_direction

        # Điểm
        self.score = 0

        # Font chữ
        self.font = pygame.font.SysFont("bahnschrift", 30)

    def show_score(self):
        score_text = self.font.render(f"Score: {self.score}", True, self.white)
        self.screen.blit(score_text, [10, 10])

    def game_over(self):
        go_font = pygame.font.SysFont("bahnschrift", 50)
        go_surface = go_font.render("GAME OVER!", True, self.red)
        self.screen.blit(go_surface, [self.width / 3, self.height / 3])
        self.show_score()
        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                        self.__init__()  # Khởi tạo lại game
                        self.run_game()
                        waiting = False

    def check_collision(self):
        # Ăn mồi
        if self.snake_position == self.food_position:
            self.food_spawned = False
            self.score += 1
        else:
            self.snake_body.pop()

        # Sinh mồi mới
        if not self.food_spawned:
            self.food_position = [random.randrange(1, (self.width // 10)) * 10,
                                  random.randrange(1, (self.height // 10)) * 10]
            self.food_spawned = True

        # Va chạm tường
        if (self.snake_position[0] < 0 or self.snake_position[0] >= self.width or
                self.snake_position[1] < 0 or self.snake_position[1] >= self.height):
            self.game_over()

        # Va chạm thân
        for block in self.snake_body[1:]:
            if self.snake_position == block:
                self.game_over()

    def draw_objects(self):
        # Vẽ rắn
        for pos in self.snake_body:
            pygame.draw.rect(self.screen, self.red, pygame.Rect(pos[0], pos[1], self.snake_block, self.snake_block))

        # Vẽ mồi
        pygame.draw.rect(self.screen, self.green, pygame.Rect(self.food_position[0], self.food_position[1],
                                                              self.snake_block, self.snake_block))

    def run_game(self):
        clock = pygame.time.Clock()

        while True:
            # Xử lý sự kiện bàn phím
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.snake_direction != "DOWN":
                        self.change_to = "UP"
                    elif event.key == pygame.K_DOWN and self.snake_direction != "UP":
                        self.change_to = "DOWN"
                    elif event.key == pygame.K_LEFT and self.snake_direction != "RIGHT":
                        self.change_to = "LEFT"
                    elif event.key == pygame.K_RIGHT and self.snake_direction != "LEFT":
                        self.change_to = "RIGHT"

            # Cập nhật hướng di chuyển
            self.snake_direction = self.change_to

            # Di chuyển rắn
            if self.snake_direction == "UP":
                self.snake_position[1] -= 10
            elif self.snake_direction == "DOWN":
                self.snake_position[1] += 10
            elif self.snake_direction == "LEFT":
                self.snake_position[0] -= 10
            elif self.snake_direction == "RIGHT":
                self.snake_position[0] += 10

            # Thêm đầu mới vào thân rắn
            self.snake_body.insert(0, list(self.snake_position))

            # Kiểm tra va chạm
            self.check_collision()

            # Vẽ
            self.screen.fill(self.black)
            self.draw_objects()
            self.show_score()

            pygame.display.update()
            clock.tick(self.snake_speed)


if __name__ == "__main__":
    game = SnakeGame()
    game.run_game()
