import pygame
import random

pygame.init()
#バカ
# 色の定義
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 画面のサイズ
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("スペースインベーダー風ゲーム")

# プレイヤーの初期座標
player_x = 300
player_y = 460

# 敵の初期座標
enemy_x = random.randint(50, 650)
enemy_y = random.randint(50, 150)

# 弾の初期座標と速度
bullet_x = player_x + 20
bullet_y = player_y - 10
bullet_speed = 10

# スコア
score = 0

# メインループ
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # キー入力に応じてプレイヤーを移動
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x -= 10
            elif event.key == pygame.K_RIGHT:
                player_x += 10
            elif event.key == pygame.K_SPACE:
                bullet_x = player_x + 20
                bullet_y = player_y - 10

    # 背景色を描画
    screen.fill(BLACK)

    # プレイヤーを描画
    pygame.draw.rect(screen, BLUE, [player_x, player_y, 40, 40])

    # 敵を描画
    pygame.draw.rect(screen, RED, [enemy_x, enemy_y, 40, 40])

    # 弾を描画
    pygame.draw.rect(screen, GREEN, [bullet_x, bullet_y, 5, 10])

    # 敵を移動
    enemy_x += 5
    if enemy_x > 660:
        enemy_x = 50
        enemy_y = random.randint(50, 150)

    # 弾を移動
    bullet_y -= bullet_speed
    if bullet_y < 0:
        bullet_y = player_y - 10

    # 衝突判定
    if bullet_x > enemy_x and bullet_x < enemy_x + 40 and bullet_y > enemy_y and bullet_y < enemy_y + 40:
        score += 10
        enemy_x = random.randint(50, 650)
        enemy_y = random.randint(50, 150)

    # スコアを描画
    font = pygame.font.SysFont("arial", 20)
    text = font.render("SCORE: " + str(score), True, WHITE)
    screen.blit(text, [10, 10])

    # 画面を更新
    pygame.display.update()

    # 60fpsで動作するようにクロックを調整
    clock.tick(60)

# pygameを終

# pygameを終了
pygame.quit()
