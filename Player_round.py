import Player
import Tile


def player_round(player:Player.Player):
    while player.actions > 1:
        print("Tvoje moznosti:")
        if player.position.sand_level < 2:
            print("Pohyb - 'W', 'A', 'S', 'D'")
        if player.position.sand_level == 0 and player.position.is_opened == False:
            print("Odkryti dilku - 'O'")
        if player.position.sand_level > 0:
            print("Odkopani pisku 'O'")
        if player.position.sand_level == 0 and player.position.is_opened == True:
            print("Ziskani jedne soucastky - 'O'")


        pohyb = input(f"Mas jeste {Player.Player.get_actions(Player)} kroku.")
        pohyb.upper()
        if pohyb == 'W' or pohyb == 'A' or pohyb == 'S' or pohyb == 'D':
            if pohyb == 'W' and Player.Player.get_y(Player) > 0:
                player.actions -= 1
                Player.Player.change_y_minus(Player)
                print("Posunul ses.")
            elif pohyb == 'S' and Player.Player.get_y(Player) < 5:
                player.actions -= 1
                Player.Player.change_y_plus()
                print("Posunul ses.")
            elif pohyb == 'A' and Player.Player.get_x(Player) > 0:
                player.actions -= 1
                Player.Player.change_x_minus()
                print("Posunul ses.")
            elif pohyb == 'D' and Player.Player.get_x(Player) < 5:
                player.actions -= 1
                Player.Player.change_x_plus()
                print("Posunul ses.")
            else:
                print("Pohyb nebyl umoznen, protoze uz jsi na okraji mapy.")
        if pohyb == 'O':
            player.actions -= 1
            if Tile.Tile.get_sand_level(Tile) > 0:
                Tile.Tile.remove_sand(Tile)
                print("Odebral jsi jeden pisek.")
            elif Tile.Tile.get_sand_level(Tile) == 0 and Tile.Tile.get_open(Tile) == False:
                Tile.Tile.open(Tile)
                print("Odkryl jsi misto")
            elif Tile.Tile.get_sand_level(Tile) == 0 and Tile.Tile.get_open(Tile) == True and




