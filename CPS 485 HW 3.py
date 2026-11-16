# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 17:53:46 2026

@author: Ssanp
"""

"""
CPS485 Homework 3
Group members: Sean Sanpietro

No because H can assign labels independently on any finite set,
seeing the labels of some inputs can tell the learner nothing about
the rest. This can happen no matter how many examples it gets.

Pick any learner and any positive sample size m. Use a uniform
distribution over 2m positive integers and give each one an
independent fair coin flip as its label. Each target is in H because
it labels only finitely many integers 1. If we double the sample size,
we also double the number of possible inputs. Since m draws can cover
at most m distinct inputs, at least half the inputs are always unseen.
Each unseen label is still a fair coin flip given the training data,
so the learner gets it wrong half the time on average. That puts the
expected true error at 1/2 times 1/2, or at least 1/4.

Let p be the chance that the true error exceeds 1/8. Since the error
is at most 1/8 on a success and at most 1 on a failure, its average
is at most (1-p)/8 + p. That average is at least 1/4, so p must be
at least 1/7. Because p averages over all targets, at least one fixed
target must fail at least that often. Since 1/7 is greater than 1/10
for any sample size we choose, the learner cannot guarantee error
at most 1/8 with 90% confidence. Thus H is not PAC-learnable.
"""

from random import Random

if __name__ == "__main__":
    rng = Random(485)
    sample_size = 8
    trials = 1000
    points = range(1, 2 * sample_size + 1)
    failures = 0

from fractions import Fraction
for _ in range(trials):
        positives = {point for point in points if rng.randrange(2)}
        seen = set(rng.choices(points, k=sample_size))

if __name__ == "__main__":
    epsilon = Fraction(1, 8)
    delta = Fraction(1, 10)
    expected_error_bound = Fraction(1, 4)
    failure_bound = (expected_error_bound - epsilon) / (1 - epsilon)
        # The learner memorizes seen labels and predicts 0 on unseen points.
    error = len(positives - seen) / len(points)
    if error > 1 / 8:
            failures += 1

    print(f"Failure probability is at least {failure_bound} for some target.")
    print(f"Error exceeded 1/8 in {failures} of {trials} trials.")