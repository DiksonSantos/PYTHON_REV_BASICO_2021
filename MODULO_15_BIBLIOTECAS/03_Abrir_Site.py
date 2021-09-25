#!/usr/bin/env python
import webbrowser as wb

print('Escolha o Site:  Y Para Youtube\n'
      'G Para Google')

st_ = str.capitalize(input('Site: '))


def abre_site(site):

    if st_ == 'Y':
        x = wb.open('https://www.youtube.com/')
        return x
    if st_ == 'G':
        y = wb.open('https://www.google.com/')
        return y


d = abre_site(st_)

# Tornar .py em Executavel ->  chmod +x 03_Abrir_Site.py
