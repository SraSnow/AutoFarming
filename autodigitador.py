import time
import pyautogui

def autodigitador():
    texto = input("Digite o texto que você quer que seja digitado automaticamente: ")
    intervalo = float(input("Digite o intervalo de tempo entre as mensagens (em segundos): "))

    print("O autodigitador começará em 5 segundos. Pressione Ctrl + C para interromper.")

    try:
        time.sleep(5)
        while True:
            for caractere in texto:
                pyautogui.write(caractere)
                time.sleep(0.1)  # Ajuste esse valor conforme necessário
            pyautogui.press('enter')  # Envie a mensagem
            time.sleep(intervalo)
    except KeyboardInterrupt:
        print("\nAutodigitador interrompido.")

if __name__ == "__main__":
    autodigitador()
