import streamlit as st
import numpy as np


# Source : https://pythonnumericalmethods.berkeley.edu/notebooks/chapter19.03-Bisection-Method.html
def my_bisection(f, a, b, tol): 
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception("The scalars a and b do not bound a root")
    m = (a + b)/2
    if np.abs(f(m)) < tol:
        return m
    elif np.sign(f(a)) == np.sign(f(m)):
        return my_bisection(f, m, b, tol)
    elif np.sign(f(b)) == np.sign(f(m)):
        return my_bisection(f, a, m, tol)

st.write("""
        # Metode Biseksi
        #### Dibuat oleh I Putu Agus Wahyu Dupayana
""")
st.markdown("""
            Jika $f(x) = x^3 - x^2 + x - 1$
            """)

a = st.number_input("Masukkan nilai batas bawah",value=1)
b = st.number_input("Masukkan nilai batas atas",value=2)
tol = st.number_input("Masukkan nilai toleransi",value=0.000001,format="%0.6f")


hitung = st.button("Hitung")

f = lambda x: x**3 - x**2 - x + 1

if f(a) * f(b) > 0.0 :
    if hitung :
        st.warning('Masukkan nilai batas bawah dan batas atas dengan benar.')
else :
    r1 = my_bisection(f, a, b, tol)
    if hitung :
        st.success("Hasilnya yaitu $x = %0.6f$ dan $f(x) = %0.6f$" %(r1,f(r1)))

