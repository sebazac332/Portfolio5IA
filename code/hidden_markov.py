import numpy as np

possible_observations = {'Positive News': True, 'Negative News': False}

transition_probabilities = np.array([
    [0.7, 0.3],
    [0.4, 0.6]
])

emission_probabilities_positive = np.array([
    [0.8, 0],
    [0, 0.3]
])

emission_probabilities_negative = np.array([
    [0.2, 0],
    [0, 0.7]
])

observations = [True, True, False, False, True, True]  

def forward(observations):
    initial_probabilities = np.array([0.5, 0.5])
    forward_list = [initial_probabilities]
    prev_prob = initial_probabilities

    for obs in observations:
        transition = np.dot(transition_probabilities, prev_prob)
        if obs:
            new_prob = np.dot(emission_probabilities_positive, transition)
        else:
            new_prob = np.dot(emission_probabilities_negative, transition)

        new_prob = new_prob / new_prob.sum()
        forward_list.append(new_prob)
        prev_prob = new_prob

    return forward_list

def backward(observations):
    observations = observations[::-1]
    b_hat = np.array([1.0, 1.0])
    backward_list = [b_hat]

    for obs in observations:
        if obs:
            a = np.dot(emission_probabilities_positive, b_hat)
        else:
            a = np.dot(emission_probabilities_negative, b_hat)

        b = np.dot(a, transition_probabilities)
        b = b / b.sum()
        backward_list.append(b)
        b_hat = b

    return backward_list[::-1]

def smoothing(forward_list, backward_list):
    for i, (f, b) in enumerate(zip(forward_list, backward_list)):
        smoothed_prob = np.multiply(f, b)
        smoothed_prob = smoothed_prob / smoothed_prob.sum()
        print(f"Day {i}: {smoothed_prob}")

print("\nForward Probabilities:")
forward_probs = forward(observations)
print("\nBackward Probabilities:")
backward_probs = backward(observations)
print("\nSmoothing Probabilities:")
smoothing(forward_probs, backward_probs)
