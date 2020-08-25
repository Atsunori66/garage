import sys
import math
import pygame
from random import randint, choice

# ウィンドウの大きさを指定
WIDTH = 800
HEIGHT = 500

# ボールの初期速度、直径、色（RGB）を指定
INIT_SPEED = 12
BALL_SIZE = 20
BALL_COLOR = (255, 255, 255)

# ラケットの長さを指定
RACKET_LENGTH = int(HEIGHT / 5)

# プレイヤーラケットの移動速度、位置、色を指定
SWING = 22
RACKET1_SIZE = (10, int((HEIGHT - RACKET_LENGTH) / 2), 10, RACKET_LENGTH)
RACKET1_COLOR = (255, 255, 255)

# AI ラケットの初期移動速度、位置、色を指定
AI_SWING = int(SWING / 4)
RACKET2_SIZE = (WIDTH - 20, int((HEIGHT - RACKET_LENGTH) / 2), 10, RACKET_LENGTH)
RACKET2_COLOR = (255, 0, 0)

# 外枠とセンターラインの位置を指定
BORDER_TOP_SIZE = (0, 0, WIDTH, 5)
BORDER_BOTTOM_SIZE = (0, HEIGHT - 5, WIDTH, 5)
BORDER_CENTER_SIZE = (int(WIDTH / 2 - 2), 0, 4, HEIGHT)
BORDER_LEFT_SIZE = (0, 0, 5, HEIGHT)
BORDER_RIGHT_SIZE = (WIDTH - 5, 0, 5, HEIGHT)

# 外枠の色を指定
BORDER_COLOR = (255, 255, 255)

# 以下ゲーム本体
def main():
    # 初期化、キー入力受付間隔、フレームレート取得、画面生成、タイトル生成
    pygame.init()
    pygame.key.set_repeat(1, 1)
    clock = pygame.time.Clock()
    surface = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Pong ver.3.3.1')

    # ボールのスピードを初期速度に設定
    speed = INIT_SPEED

    # プレイヤー、AI の得点
    score1 = 0
    score2 = 0

    # プレイヤー、AI の勝利フラグ
    victory_1 = False
    victory_2 = False

    # スコア表示のフォントを指定
    score_font = pygame.font.Font(None, 36)

    # ゲーム終了時メッセージフォントを指定
    end_font = pygame.font.Font(None, 50)

    # プレイヤー勝利時メッセージ設定
    message_win1 = end_font.render('You win!', True, (255, 255, 255))
    message_pos1 = message_win1.get_rect()
    message_pos1.centerx = int(WIDTH / 4)
    message_pos1.centery = int(HEIGHT / 2)

    # プレイヤー敗北時メッセージ設定
    message_win2 = end_font.render('You lose...', True, (255, 255, 255))
    message_pos2 = message_win2.get_rect()
    message_pos2.centerx = int(WIDTH * 3 / 4)
    message_pos2.centery = int(HEIGHT / 2)

    # ボール、ラケットを生成
    ball = pygame.Rect(surface.get_rect().centerx, surface.get_rect().centery, BALL_SIZE, BALL_SIZE)
    racket1 = pygame.Rect(RACKET1_SIZE)
    racket2 = pygame.Rect(RACKET2_SIZE)

    # 外枠、センターラインを生成
    border_top = pygame.Rect(BORDER_TOP_SIZE)
    border_bottom = pygame.Rect(BORDER_BOTTOM_SIZE)
    border_center = pygame.Rect(BORDER_CENTER_SIZE)
    border_left = pygame.Rect(BORDER_LEFT_SIZE)
    border_right = pygame.Rect(BORDER_RIGHT_SIZE)

    # ボールの初期射出角度をランダムに指定（画面中央から真上、真下に射出されるのを防止）
    direction = choice([randint(50, 70), randint(110, 130), randint(230, 250), randint(290, 310)])

    # 以下ゲーム進行をループ
    while True:

        # プレイヤーのスコア表示を設定
        score1_show = score_font.render('You: ' + str(score1), True, (255, 255, 255))
        score1_pos = score1_show.get_rect()
        score1_pos.centerx = int(WIDTH / 4)
        score1_pos.centery = 40

        # AI のスコア表示を設定
        score2_show = score_font.render('Pong AI: ' + str(score2), True, (255, 255, 255))
        score2_pos = score2_show.get_rect()
        score2_pos.centerx = int(WIDTH * 3 / 4)
        score2_pos.centery = 40

        # キー入力およびプレイヤーの挙動を設定
        # 矢印キーの上下左右で移動
        # Esc キーか画面の×ボタンで終了
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and racket1.top > 10:
                    racket1.centery -= SWING
                if event.key == pygame.K_DOWN and racket1.bottom < HEIGHT - 10:
                    racket1.centery += SWING
                if event.key == pygame.K_LEFT and racket1.left > 10:
                    racket1.centerx -= SWING
                if event.key == pygame.K_RIGHT and racket1.right < 100:
                    racket1.centerx += SWING
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        # AI の挙動を設定
        # AI ラケットがボールより上にあったら下に移動
        # AI ラケットがボールより下にあったら上に移動
        # ボールが遠くにあったら早く移動
        if racket2.centery < ball.centery and racket2.bottom < HEIGHT - 5:
            racket2.centery += AI_SWING
            if racket2.centery < ball.centery - int(HEIGHT / 8) and ball.centerx > int(WIDTH / 2):
                racket2.centery += AI_SWING + randint(-3, 3)
        elif racket2.centery > ball.centery and racket2.top > 5:
            racket2.centery -= AI_SWING
            if racket2.centery > ball.centery + int(HEIGHT / 8) and ball.centerx > int(WIDTH / 2):
                racket2.centery -= AI_SWING + randint(-3, 3)

        # ラケットとボール衝突時、角度を反射（ランダムで誤差あり）、ボールを加速
        if racket1.colliderect(ball):
            direction = -(racket1.centery - ball.centery) + randint(-20, 20)
            speed += 0.3
        if racket2.colliderect(ball):
            direction = 180 + (racket2.centery - ball.centery) + randint(-20, 20)
            speed += 0.1

        # ボールが上下の枠に当たった時、角度を反射、ボールを加速
        if ball.centery < 0 or ball.centery > HEIGHT:
            direction = -direction
            speed += 0.2

        # ボールが画面内にある時、ボールを移動
        # プレイヤーか AI がボールを逸らした時、点数処理
        # 片方が2点差以上を付け、11点以上を獲得した時、勝利フラグを立てる（卓球ルールを踏襲）
        if ball.centerx >= 0 and ball.centerx <= WIDTH:
            ball.centerx += int(math.cos(math.radians(direction)) * speed)
            ball.centery += int(math.sin(math.radians(direction)) * speed)
        else:
            if (score1 < 11 and score2 < 11) or (score1 >=11 and score1 < score2 + 2) or (score2 >= 11 and score2 < score1 + 2):
                if ball.centerx > WIDTH:
                    score1 += 1
                    ball.left = int(WIDTH / 2)
                    ball.top = int(HEIGHT / 2)
                    direction = choice([randint(50, 70), randint(110, 130), randint(230, 250), randint(290, 310)])
                    speed = INIT_SPEED
                if ball.centerx < 0:
                    score2 += 1
                    ball.left = int(WIDTH / 2)
                    ball.top = int(HEIGHT / 2)
                    direction = choice([randint(50, 70), randint(110, 130), randint(230, 250), randint(290, 310)])
                    speed = INIT_SPEED
            if score1 >= 11 and score1 >= score2 + 2:
                victory_1 = True
            if score2 >= 11 and score2 >= score1 + 2:
                victory_2 = True

        # 画面に色を描画（卓球台に寄せた）
        surface.fill((0, 100, 200))

        # プレイヤーか AI が勝利条件を満たしたとき、メッセージを画面に描画
        if victory_1:
            surface.blit(message_win1, (message_pos1))
        if victory_2:
            surface.blit(message_win2, (message_pos2))

        # 外枠、センターラインを画面に描画
        pygame.draw.rect(surface, BORDER_COLOR, border_top)
        pygame.draw.rect(surface, BORDER_COLOR, border_bottom)
        pygame.draw.rect(surface, BORDER_COLOR, border_center)
        pygame.draw.rect(surface, BORDER_COLOR, border_left)
        pygame.draw.rect(surface, BORDER_COLOR, border_right)

        # スコアを画面に描画
        surface.blit(score1_show, (score1_pos))
        surface.blit(score2_show, (score2_pos))

        # ラケットを画面に描画
        pygame.draw.rect(surface, RACKET1_COLOR, racket1)
        pygame.draw.rect(surface, RACKET2_COLOR, racket2)

        # ボールを画面に描画
        pygame.draw.ellipse(surface, BALL_COLOR, ball)

        # 画面を更新、フレームレートの最大値を 60fps に設定
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()