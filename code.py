from numpy import *


def cost(b, m, data_points):
    r_squared = 0

    # predicted Y^ = (mX + b)
    # Mean-Squared-Error = 1/N(sum_for_N_Samples_of(y - y^)^2)
    for i in range(len(data_points)):
        X = data_points[i, 0]
        y = data_points[i, 1]
        r_squared += (y - (m * X + b)) ** 2
    return r_squared / (float(len(data_points)))


def gradient_step(b, m, data_points, alpha):
    b_grad = 0
    m_grad = 0
    N = float(len(data_points))
    for i in range(len(data_points)):
        X = data_points[i, 0]
        y = data_points[i, 1]
        b_grad += -(2/N) * (y - ((m * X) + b))
        m_grad += -(2/N) * X * (y - ((m * X) + b))
    new_b = b - (alpha * b_grad)
    new_m = m - (alpha * m_grad)
    return [new_b, new_m]


def batch_gradient_descent(data_points, initial_b, initial_m, alpha, iterations):
    b = initial_b
    m = initial_m
    for i in range(iterations):
        b, m = gradient_step(b, m, array(data_points), alpha)
    return [b, m]


def predict_y(X):
    b, m = main()
    y_pred = m * X + b
    print(f"The regressor prediction for input 'X' = {X} is 'y' = {y_pred}")


def main():
    data_points = genfromtxt("data.csv", delimiter=",")

    alpha = 0.0001  # Learning Rate

    # predicted Y = mX + b
    # m - slope, b - y_intercept
    initial_m = 0
    initial_b = 0
    iterations = 1000

    start_cost = cost(initial_b, initial_m, data_points)
    print(
        f"Starting Gradient Descent at 'y-intercept' = {initial_b}, 'slope' = {initial_m}, 'cost' = {start_cost}")

    [b, m] = batch_gradient_descent(
        data_points, initial_b, initial_m, alpha, iterations)

    end_cost = cost(b, m, data_points)
    print(
        f"After performing Gradient Descent for {iterations} iterations we got: 'y-intercept' = {b}, 'slope' = {m}, 'cost' = {end_cost}")

    return b, m


if __name__ == "__main__":
    main()
    # predict_y(59.813207869512318)