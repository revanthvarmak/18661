"""Main script for the solution."""

import numpy as np
import pandas as pd
import argparse

import npnn


def _get_args():
    p = argparse.ArgumentParser()
    p.add_argument("--lr", help="learning rate", type=float, default=0.1)
    p.add_argument("--opt", help="optimizer", default="SGD")
    p.add_argument(
        "--epochs", help="number of epochs to train", type=int, default=20)
    p.add_argument(
        "--save_stats", help="Save statistics to file", action="store_true")
    p.add_argument(
        "--save_pred", help="Save predictions to file", action="store_true")
    p.add_argument("--dataset", help="Dataset file", default="mnist.npz")
    p.add_argument(
        "--test_dataset", help="Dataset file (test set)",
        default="mnist_test.npz")
    p.set_defaults(save_stats=False, save_pred=False)
    return p.parse_args()


if __name__ == '__main__':
    args = _get_args()
    X, y = npnn.load_mnist(args.dataset)

    # TODO
    # Create dataset (see npnn/dataset.py)
    # Create model (see npnn/model.py)
    # Train for args.epochs
    model = None
    stats = pd.DataFrame()

    # Save statistics to file.
    # We recommend that you save your results to a file, then plot them
    # separately, though you can also place your plotting code here.
    if args.save_stats:
        stats.to_csv("data/{}_{}.csv".format(args.opt, args.lr))

    # Save predictions.
    if args.save_pred:
        X_test, _ = npnn.load_mnist("mnist_test.npz")
        y_pred = np.argmax(model.forward(X_test), axis=1).astype(np.uint8)
        np.save("mnist_test_pred.npy", y_pred)
