#!/bin/bash

# Instalar o Python caso não esteja instalado
if ! command -v python &> /dev/null; then
    echo "Instalando o Python..."
    pkg install -y python
fi

# Instalar o pip caso não esteja instalado
if ! command -v pip &> /dev/null; then
    echo "Instalando o pip..."
    pkg install -y python-pip
fi

# Instalar as dependências do pyautogui
echo "Instalando as dependências do pyautogui..."
pkg install -y libx11 libxext libxrandr libxinerama libxcursor libxi libxtst
pip install pyautogui

echo "Instalação concluída."
