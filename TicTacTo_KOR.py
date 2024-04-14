import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # 가로, 세로, 대각선 방향으로 동일한 플레이어 기호가 있는지 확인
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    # 보드가 가득 찼는지 확인
    return all(cell != " " for row in board for cell in row)

def get_empty_positions(board):
    # 비어 있는 위치 반환
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def player_move(board):
    # 플레이어의 입력 받기
    while True:
        row = int(input("행(1-3)을 입력하세요: ")) - 1
        col = int(input("열(1-3)을 입력하세요: ")) - 1
        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
            return row, col
        print("잘못된 위치입니다. 다시 시도해주세요.")

def computer_move(board):
    # 컴퓨터가 무작위 위치로 움직임
    return random.choice(get_empty_positions(board))

def main():
    board = [[" "]*3 for _ in range(3)]
    players = ["X", "O"]
    random.shuffle(players)
    current_player = players[0]

    print("틱택토 게임에 오신 것을 환영합니다!")
    print_board(board)

    while True:
        if current_player == "X":
            row, col = player_move(board)
        else:
            row, col = computer_move(board)
            print(f"컴퓨터가 {current_player}을(를) {row+1}행, {col+1}열에 놓았습니다.")

        board[row][col] = current_player
        print_board(board)

        if check_winner(board, current_player):
            print(f"{current_player} 플레이어가 이겼습니다!")
            break
        elif is_board_full(board):
            print("비겼습니다!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()