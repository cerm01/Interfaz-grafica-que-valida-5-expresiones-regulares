import re
from tkinter import *

def validate_email(email):
    pattern = re.compile(r"^[a-zA-Z][a-zA-Z0-9._]+@[a-zA-Z0-9]+.[a-zA-Z]{2,}$")
    return True if pattern.match(email) else False

def validate_ip(ip):
    pattern = re.compile(r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9]{1,2})\.(25[0-5]|2[0-4][0-9]|[01]?[0-9]{1,2})\.(25[0-5]|2[0-4][0-9]|[01]?[0-9]{1,2})\.(25[0-5]|2[0-4][0-9]|[01]?[0-9]{1,2})$")
#"^(25[0-5]|2[0-4][0-9]|[01]?[0-9]{1,2})\.(25[0-5]|2[0-4][0-9]|[01]?[0-9]{1,2})\.(25[0-5]|2[0-4][0-9]|[01]?[0-9]{1,2})\.(25[0-5]|2[0-4][0-9]|[01]?[0-9]{1,2})$"
    return True if pattern.match(ip) else False

def validate_mac(mac):
    pattern = re.compile(r"^([0-9A-Fa-f]{2}:){5}([0-9A-Fa-f]{2})$")
    return True if pattern.match(mac) else False

def validate_time(time):
    pattern = re.compile(r"^(0[1-9]|1[0-2]):[0-5][0-9]\s[(AM)(PM)(am)(pm)]$")
    return True if pattern.match(time) else False

def validate_rfc(rfc):
    pattern = re.compile(r'^[A-ZÑ&]{3,4}[0-9]{2}(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-9]|3[0-1])[A-Z0-9]{2}[0-9A]$')
    return True if pattern.match(rfc) else False

def validate():
    email = email_entry.get()
    email_valid = validate_email(email)
    email_result.config(text="Valido" if email_valid else "Invalido")

    ip = ip_entry.get()
    ip_valid = validate_ip(ip)
    ip_result.config(text="Válido" if ip_valid else "Invalido")

    mac = mac_entry.get()
    mac_valid = validate_mac(mac)
    mac_result.config(text="Válido" if mac_valid else "Invalido")

    time = time_entry.get()
    time_valid = validate_time(time)
    time_result.config(text="Válido" if time_valid else "Invalido")

    rfc = rfc_entry.get()
    rfc_valid = validate_rfc(rfc)
    rfc_result.config(text="Válido" if rfc_valid else "Invalido")

root = Tk()
root.title("Validación")
root.geometry("350x280")
root.resizable(0,0)

email_label = Label(root, text="Email:")
email_label.grid(row=0, column=0, padx=10, pady=10)

email_entry = Entry(root)
email_entry.grid(row=0, column=1, padx=10, pady=10)

email_result = Label(root)
email_result.grid(row=0, column=2, padx=10, pady=10)

ip_label = Label(root, text="Direccion IP:")
ip_label.grid(row=1, column=0, padx=10, pady=10)

ip_entry = Entry(root)
ip_entry.grid(row=1, column=1, padx=10, pady=10)

ip_result = Label(root)
ip_result.grid(row=1, column=2, padx=10, pady=10)

mac_label = Label(root, text="Direccion MAC:")
mac_label.grid(row=2, column=0, padx=10, pady=10)

mac_entry = Entry(root)
mac_entry.grid(row=2, column=1, padx=10, pady=10)

mac_result = Label(root)
mac_result.grid(row=2, column=2, padx=10, pady=10)

time_label = Label(root, text="Hora:")
time_label.grid(row=3, column=0, padx=10, pady=10)

time_entry = Entry(root)
time_entry.grid(row=3, column=1, padx=10, pady=10)

time_result = Label(root)
time_result.grid(row=3, column=2, padx=10, pady=10)

rfc_label = Label(root, text="RFC:")
rfc_label.grid(row=4, column=0, padx=10, pady=10)

rfc_entry = Entry(root)
rfc_entry.grid(row=4, column=1, padx=10, pady=10)

rfc_result = Label(root)
rfc_result.grid(row=4, column=2, padx=10, pady=10)

validate_button = Button(root, text="Validar", command=validate)
validate_button.grid(row=5, column=1, padx=10, pady=10)

root.mainloop()