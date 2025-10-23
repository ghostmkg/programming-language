"""
Minimal Recurrent Neural Network (RNN) demonstration.

Forward propagation explanation:
https://towardsdatascience.com/forward-propagation-in-neural-networks-simplified-math-and-code-version-bbcfef6f9250
RNN fundamentals:
https://towardsdatascience.com/recurrent-neural-networks-d4642c9bc7ce/
"""

import math
import random


def sigmoid_function(value: float, deriv: bool = False) -> float:
    if deriv:
        return value * (1 - value)
    return 1 / (1 + math.exp(-value))


# Initial constants
INITIAL_VALUE = 0.02  # learning rate
SEQUENCE_LENGTH = 5  # time steps in the sequence


def forward_propagation_rnn(expected: int, number_propagations: int) -> float:
    random.seed(0)

    # Random weight initialization
    w_xh = random.random() * 2 - 1  
    w_hh = random.random() * 2 - 1  
    w_hy = random.random() * 2 - 1  

    # Training loop
    for _ in range(number_propagations):
        h_prev = 0.0  
        total_error = 0.0

        # Forward pass through time
        for _t in range(SEQUENCE_LENGTH):
           
            x_t = INITIAL_VALUE
            h_t = sigmoid_function(w_xh * x_t + w_hh * h_prev)
            y_t = sigmoid_function(w_hy * h_t)
            error_t = (expected / 100) - y_t
            total_error += abs(error_t)

            # Backpropagation Through Time 
            d_y = error_t * sigmoid_function(y_t, True)
            d_h = d_y * w_hy * sigmoid_function(h_t, True)

            w_hy += INITIAL_VALUE * d_y * h_t
            w_xh += INITIAL_VALUE * d_h * x_t
            w_hh += INITIAL_VALUE * d_h * h_prev

            h_prev = h_t

    final_output = y_t * 100
    return final_output


if __name__ == "__main__":
    expected = 50
    number_propagations = 100
    print(forward_propagation_rnn(expected, number_propagations))
