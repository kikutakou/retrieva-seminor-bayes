import random
import argparse


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--simulation', type=int, default=100000, help='number of simulation')
    parser.add_argument('-n', '--num', type=int, default=3, help='number of trial for per simulation')
    parser.add_argument('--seed', type=int, default=None, help='random seed')
    args = parser.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    n_simulation = args.simulation
    n_trial = args.num

    count_smo_win = 0
    count_mle_win = 0
    sum_error_mle = 0.0
    sum_error_smo = 0.0

    for i in range(n_simulation):

        # coin parameter to be estimated
        mu_truth = random.random()

        # exprimental result
        count_man = 0.0
        for j in range(n_trial):
            if random.random() < mu_truth:
                count_man += 1

        # estimation mle:Maximum Likelifood Estimation / smo:Smoothing
        mu_mle = count_man / n_trial
        mu_smo = (count_man + 1) / (n_trial + 2)


        # total
        sqerror_mle = (mu_truth - mu_mle) ** 2
        sqerror_smo = (mu_truth - mu_smo) ** 2

        if sqerror_smo < sqerror_mle:
            count_smo_win += 1
        elif sqerror_smo > sqerror_mle:
            count_mle_win += 1
        else:
            pass  # even

        sum_error_mle += sqerror_mle
        sum_error_smo += sqerror_smo

    print("count Smoothing win: {} : ( {:.1f} percent )".format(count_smo_win, 100.0 * count_smo_win / n_simulation))
    print("count MLE  win:      {} : ( {:.1f} percent )".format(count_mle_win, 100.0 * count_mle_win / n_simulation))
    print("Error total Smoothing : {:6.2f}".format(sum_error_smo))
    print("Error total MLE :       {:6.2f}".format(sum_error_mle))



