import time
import mss
from trigger_key import PressKey, ReleaseKey, VK_X
from PIL import Image, ImageStat

# Definizione delle variabili per il rilevamento visivo
SCREEN_LOCATION = {"top": 290, "left": 295, "width": 25, "height": 30}
CONTROL_SCREEN_LOCATION = {"top": 293, "left": 293, "width": 10, "height": 10}
COLOR_MINIMUM_THRESHOLD = 225
KEYPRESS_DURATION_SEC = 0.01
EXTRA_DELAY_AFTER_RELEASE = 0.05
CONTROL_LATENCY_MS = 200  # Latenza per evitare doppi trigger

# Inizializza l'acquisizione dello schermo
sct = mss.mss()

# Linea temporale interna (linea reale) per tracciare i salti
real_timeline = []

# Setup cronometro per il timing basato sul tempo come fallback
backup_latency = 890  # Valore di latenza iniziale
MARGIN_OF_TOLERANCE = 50  # Tolleranza aggiuntiva in millisecondi per i salti di backup

# Variabile per tracciare l'ultimo trigger del controllo di luce
last_control_trigger_time = 0

# Funzione per il controllo visivo
def check_if_the_time_is_right():
    sct_img = sct.grab(SCREEN_LOCATION)
    img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
    extrema = ImageStat.Stat(img).extrema
    print(f"Controllo visivo: {extrema}")  # Stampa a console invece di creare popup
    return extrema[1][1] > COLOR_MINIMUM_THRESHOLD

# Funzione per il controllo del riquadro aggiuntivo
def check_control_box():
    sct_img = sct.grab(CONTROL_SCREEN_LOCATION)
    img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
    extrema = ImageStat.Stat(img).extrema
    print(f"Controllo riquadro aggiuntivo: {extrema}")  # Stampa a console
    return extrema[1][1] > COLOR_MINIMUM_THRESHOLD

# Funzione principale che esegue i salti
def rope_jumper():
    global backup_latency, last_control_trigger_time  # Assicura che queste variabili siano globali

    print("Attendere 3 secondi prima di iniziare...")
    time.sleep(3)  # Aggiunge una pausa di 3 secondi prima di iniziare

    jump_count = 0
    time_was_right_last_time = False
    last_jump_time = time.time()

    while jump_count < 9000:  # O fino a quando vuoi
        the_time_is_right = check_if_the_time_is_right()
        control_triggered = False

        current_time = time.time()
        time_since_last_jump = current_time - last_jump_time

        # Controllo del riquadro aggiuntivo
        if current_time - last_control_trigger_time > CONTROL_LATENCY_MS / 1000:
            if check_control_box() and not control_triggered:
                last_control_trigger_time = current_time
                control_triggered = True
                print(f"Controllo attivato al salto {jump_count}")
                real_timeline.append(current_time)  # Aggiungi questo input alla timeline

        if the_time_is_right and not time_was_right_last_time:
            # Se rileva visivamente il momento giusto, esegue il salto
            PressKey(VK_X)
            time.sleep(KEYPRESS_DURATION_SEC)
            ReleaseKey(VK_X)
            time.sleep(EXTRA_DELAY_AFTER_RELEASE)  # Evita input multipli
            jump_count += 1
            print(f"{jump_count}x  Salto rilevato visivamente")

            # Aggiorna la linea temporale reale
            real_timeline.append(current_time)
            last_jump_time = current_time

        elif time_since_last_jump > (backup_latency + MARGIN_OF_TOLERANCE) / 1000:
            # Se passa troppo tempo senza rilevamento visivo, esegue un salto di backup
            print(f"{jump_count}x  Salto di backup a causa del timer")
            PressKey(VK_X)
            time.sleep(KEYPRESS_DURATION_SEC)
            ReleaseKey(VK_X)
            time.sleep(EXTRA_DELAY_AFTER_RELEASE)
            jump_count += 1

            # Aggiorna la linea temporale reale
            real_timeline.append(current_time)
            last_jump_time = current_time

        time_was_right_last_time = the_time_is_right

    print("Il gioco ha raggiunto il massimo numero di salti.")

rope_jumper()
