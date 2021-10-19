import match
import view

while True:
    v = view
    v.start_game()
    var = match.Match(int(v.length_matrix()), int(v.num_players()))
    winner = None
    v.print_matrix(var.get_matrix(), var.get_length())
    while var.get_game_state():
        i = 0
        while i < len(var.get_num_players()) and winner is None:
            mossa = False
            while mossa is False:
                x, y = v.move(i)
                if var.add_symbol(i, x, y):
                    var.check_row()
                    var.check_col()
                    var.check_diag_top_bot_dx()
                    var.check_diag_bot_top_dx()
                    var.check_diag_bot_top_sx()
                    var.check_diag_top_bot_sx()
                    v.print_matrix(var.get_matrix(), var.get_length())
                    v.print_point(var.get_point())
                    mossa = True
                    winner = var.check_win()
                    i += 1
                else:
                    v.print_err(x, y)
    v.winner(winner + 1)
    if v.rematch() is False:
        break
    var.clear_all()
