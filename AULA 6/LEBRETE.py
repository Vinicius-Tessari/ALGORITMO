import time
from plyer import notification

def lembrete():
    notification.notify(
        title="Já se hidratou hoje?",
        message="Hora de beber água!",
        timeout=10
    )

while True:
    lembrete()
    time.sleep(10)