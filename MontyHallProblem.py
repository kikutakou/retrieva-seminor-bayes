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


        remaining_doors = [r for r in range(3) if r is not player_selected]

        if player_selected == truth:
            master_opened = random.choice(remaining_doors)
        elif remaining_doors[0] == truth:
            master_opened = remaining_doors[1]
        elif remaining_doors[1] == truth:
            master_opened = remaining_doors[0]
        else:
            raise

        remaining_doors = [r for r in remaining_doors if r is not master_opened]


        if remaining_doors[0] == truth:
            count_changed_wins += 1
        elif player_selected == truth:
            count_unchanged_wins += 1
        else:
            raise

    print("count_changed_wins:   ", count_changed_wins)
    print("count_unchanged_wins: ", count_unchanged_wins)

