import numpy as np
import matplotlib.pyplot as plt
import commlib as cl

def Q1(x):
    return np.exp(-(x ** 2) / 2)

def Q2(x):
    return 0.25 * (np.exp(-(x ** 2))) + 0.25 * np.exp(-(x ** 2) / 2)

def Q3(x):
    return (np.exp(-(x ** 2) / 2)) / 12 + (np.exp( (-2 * (x ** 2) ) / 3 )) / 4

def QiE(Q, Qi):
    return np.abs(Qi - Q) / np.abs(Q)

def plot_q(fig_counter, x, Q, Qi, errors_i, legend_Q, legend_Qi, Qi_color):
    custom_lines = [plt.Line2D([0], [0], color="blue"),
                    plt.Line2D([0], [0], color=Qi_color, linestyle=('--')),
                    plt.Line2D([0], [0], color='white')]
    plt.figure(fig_counter)
    plt.semilogy(x, Q)
    plt.semilogy(x, Qi, '--', color = Qi_color)
    plt.xlabel('x')
    plt.ylabel('Q(x)')
    plt.legend(custom_lines, [legend_Q, legend_Qi, 'εi = ' + errors_i])
    plt.ylim([1e-14, 1])

x = np.linspace(2, 7, 1000)

Q = cl.Qfunction(x)

Q1 = Q1(x)
Q2 = Q2(x)
Q3 = Q3(x)

Q1E = QiE(Q, Q1)
Q2E = QiE(Q, Q2)
Q3E = QiE(Q, Q3)

errors1 = str(np.trapz(Q1E, x))
errors2 = str(np.trapz(Q2E, x))
errors3 = str(np.trapz(Q3E, x))

plt.close('all')

plot_q(1, x, Q, Q1, errors1, 'Q(x)', 'Q1(x)', 'purple')
plot_q(2, x, Q, Q2, errors2, 'Q(x)', 'Q2(x)', 'green')
plot_q(3, x, Q, Q3, errors3, 'Q(x)', 'Q3(x)', 'orange')

plt.show()







