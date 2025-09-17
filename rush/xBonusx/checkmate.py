def read_board(file_path):
    
    try:
        with open(file_path, 'r') as f:
            board = [line.strip() for line in f.readlines()]
            if all(len(row) == len(board) for row in board):
                return board
            else:
                return None
    except FileNotFoundError:
        return None

def process_board(board):

    if not is_valid_board(board):
        return "Error"
    try:
        if is_king_checked(board):
            return "Success"
        else:
            return "Fail"
    except Exception:
        return "Error"
    
def is_valid_board(board):
    
    if board is None:
        return False
    
    king_count = sum(row.count('K') for row in board)
    if king_count != 1:
        return False

    board_size = len(board)
    if not all(len(row) == board_size for row in board):
        return False
    
    piece_counts = {
        'P': 0,
        'B': 0,
        'R': 0,
        'Q': 0,
        'K': 0
    }

    for row in board:
        for cell in row:
            if cell in piece_counts:
                piece_counts[cell] += 1
            elif cell != '.':
                return False

    if piece_counts['Q'] > 1:
        print("There must be exactly one Queen or fewer.")
        return False
    if piece_counts['B'] > 2:
        print("There must be exactly two Bishops or fewer.")
        return False
    if piece_counts['P'] > 8:
        print("There must be exactly eight Pawns or fewer.")
        return False
    if piece_counts['R'] > 2:
        print("There must be exactly two Rooks or fewer.")
        return False

    return True

def is_king_checked(board):

    n = len(board)
    king_positions = [(i, row.index('K')) for i, row in enumerate(board) if 'K' in row]

    kx, ky = king_positions[0]

    def is_in_bounds(x, y):
        return 0 <= x < n and 0 <= y < n

    pawn_dirs = [(1, 1), (1, -1)]
    bishop_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    rook_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queen_dirs = bishop_dirs + rook_dirs

    for dx, dy in pawn_dirs:
        nx, ny = kx + dx, ky + dy
        if is_in_bounds(nx, ny) and board[nx][ny] == 'P':
            return True

    for piece, directions in [('B', bishop_dirs), ('R', rook_dirs), ('Q', queen_dirs)]:
        for dx, dy in directions:
            x, y = kx, ky
            while True:
                x, y = x + dx, y + dy
                if not is_in_bounds(x, y):
                    break
                if board[x][y] == piece:
                    return True
                elif board[x][y] != '.':
                    break

    return False
