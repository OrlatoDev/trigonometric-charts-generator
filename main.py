import streamlit as st
from scipy import interpolate
import numpy as np
import matplotlib.pyplot as plt

line_color = "#FF4B4B"
background_color = "#0E1117"
grade_color = "#262730"

st.title("Gerador de Gráficos de Funções Trigonométricas")

st.latex(
    r'''
    f(x) = a \cdot trig(b \cdot x + c) + d
    ''')

trig = st.selectbox(
    r"Selecione a função $trig$",
    ("sen", "cos", "tg"))

col1, col2, col3, col4 = st.columns(4)

with col1:
    a = st.slider(r"Selecione o valor de $a$", -10, 10, 1)

with col2:
    b = st.slider(r"Selecione o valor de $b$", -10, 10, 1)

with col3:
    c = st.slider(r"Selecione o valor de $c$", -10, 10, 0)

with col4:
    d = st.slider(r"Selecione o valor de $d$", -10, 10, 0)

st.latex(
    f'''
    f(x) = {a} \cdot {trig}({b} \cdot x + {c}) + {d}
    '''
)

x = np.linspace(-np.pi, 4*np.pi, 200)

if trig == "sen":
    y = a * np.sin(b * x + c) + d
elif trig == "cos":
    y = a * np.cos(b * x + c) + d
elif trig == "tg":
    y = a * np.tan(b * x + c) + d

f = interpolate.interp1d(x, y, kind="cubic")
y_interp = f(x)

fig, ax = plt.subplots()
ax.plot(x, y_interp, color=line_color)

ticks = [-np.pi, -np.pi/2, 0, np.pi/2, np.pi, np.pi*3 /
         2, 2*np.pi, np.pi*5/2, 3*np.pi, np.pi*7/2, 4*np.pi]
ticklabels = ["-π", "-π/2", "0", "π/2", "π",
              "3π/2", "2π", "5π/2", "3π", "7π/2", "4π"]
ax.set_xticks(ticks)
ax.set_xticklabels(ticklabels)

ax.spines["bottom"].set_color("white")
ax.spines["left"].set_color("white")
ax.spines["top"].set_color("white")
ax.spines["right"].set_color("white")

ax.tick_params(colors="white")

ax.set_facecolor(background_color)
fig.set_facecolor(background_color)
ax.grid(color=grade_color, linestyle=':', linewidth=1)

st.pyplot(fig)
