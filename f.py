def simple_iteration_method_x(x_k, y_k):
    x_k1 = x_k - 0.25 * (x_k - y_k + 2) + 0.25 * (x_k * y_k - 3)
    return float(format(x_k1, '.10f'))


def simple_iteration_method_y(x_k, y_k):
    y_k1 = y_k + 0.75 * (x_k - y_k + 2) + 0.25 * (x_k * y_k - 3)
    return float(format(y_k1, '.10f'))


def newtons_method_x(x_k, y_k):
    x_k1 = (x_k * y_k - 2 * x_k + 3) / (x_k + y_k)
    return float(format(x_k1, '.10f'))


def newtons_method_y(x_k, y_k):
    y_k1 = (x_k * y_k + 2 * y_k + 3) / (x_k + y_k)
    return float(format(y_k1, '.10f'))
