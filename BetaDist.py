import argparse
import os
import numpy as np
from scipy.stats import beta
import matplotlib.pyplot as plt
from scipy import integrate
from math import log


def entropy(f):
    return -integrate.quad(lambda x: f(x) * np.log(f(x)), 0, 1)[0]

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', nargs='?', const=os.path.splitext(__file__)[0] + ".pdf")
    parser.add_argument('counts', nargs=2, type=int, help='count')
    args = parser.parse_args()

    p = np.linspace(0.0, 1.0, 101)

    a = args.counts[0] + 1
    b = args.counts[1] + 1
    f = beta(a, b).pdf
    y = f(p)

    for pp,yy in zip(p, y):
        print("{}\t{}".format(pp, yy))

    plt.plot(p, y)
    plt.title("beta vs p (a = {}, b = {})".format(a, b))

    plt.xlim(0.0, 1.0)
#    plt.ylim(0, 3.0)

    plt.tight_layout()
    if args.output:
        plt.savefig(args.o)
        print("output to", args.o)
    else:
        plt.show()

