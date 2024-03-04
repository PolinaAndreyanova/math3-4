from print_table import print_row
import f

method = 'simple_iteration_method'
# method = 'newtons_method'
k = 0
x_k = -1
y_k = -3
e = 0.001 / 100

header = ['k', 'x_k', 'x_k+1', '|x_k+1 - x_k|', 'y_k', 'y_k+1', '|y_k+1 - y_k|']
print_row(header)
print("-+-".join('-' * 15 for _ in range(7)))

while True:
    if method == 'simple_iteration_method':
       x_k1 = f.simple_iteration_method_x(x_k, y_k)
       y_k1 = f.simple_iteration_method_y(x_k, y_k)
    else:
        x_k1 = f.newtons_method_x(x_k, y_k)
        y_k1 = f.newtons_method_y(x_k, y_k)

    x_e = float(format(abs(x_k1 - x_k), '.10f'))
    y_e = float(format(abs(y_k1 - y_k), '.10f'))

    print_row([str(k), str(x_k), str(x_k1), str(x_e), str(y_k), str(y_k1), str(y_e)])

    if (x_e <= e) and (y_e <= e):
        break

    k += 1
    x_k = x_k1
    y_k = y_k1
