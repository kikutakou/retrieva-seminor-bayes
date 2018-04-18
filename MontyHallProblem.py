#!/usr/bin/env python

import random
import argparse

if __name__ == '__main__':


    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--simulations', type=int, default=1000, help='number of simulations')
    parser.add_argument('--seed', type=int, default=None, help='random seed')
    args = parser.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    n_simulation = args.simulations

    count_changed_wins = 0
    count_unchanged_wins = 0

    for i in range(n_simulation):

        truth = random.randrange(3)

        player_selected = random.randrange(3)

        doors_unselected = [r for r in range(3) if r is not player_selected]
        assert len(doors_unselected) == 2

        if player_selected == truth:
            master_selected = random.choice(doors_unselected)
        elif doors_unselected[0] == truth:
            master_selected = doors_unselected[1]
        elif doors_unselected[1] == truth:
            master_selected = doors_unselected[0]
        else:
            raise

        doors_unselected.remove(master_selected)
        assert len(doors_unselected) == 1

        another_door = doors_unselected[0]


        if another_door == truth:
            count_changed_wins += 1
        elif player_selected == truth:
            count_unchanged_wins += 1
        else:
            raise

    print("count_changed_wins:   ", count_changed_wins)
    print("count_unchanged_wins: ", count_unchanged_wins)

