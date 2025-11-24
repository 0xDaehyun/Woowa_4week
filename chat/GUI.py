from socket import *
import threading
import tkinter as tk
from tkinter import scrolledtext

port = 8080
clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1', port))

# GUI 이름 설정하기
root = tk.Tk()
root.title("바로 메신저 - Client")

# 채팅 내용이 쌓이는 창
chat_area = scrolledtext.ScrolledText(root, width=50, height=20, state='disabled')
chat_area.pack(padx=10, pady=10)

# 메시지 입력 , 전송
input_frame = tk.Frame(root)
input_frame.pack(padx=10, pady=(0, 10), fill='x')

input_entry = tk.Entry(input_frame)
input_entry.pack(side='left', expand=True, fill='x')

send_button = tk.Button(input_frame, text="전송")
send_button.pack(side='left', padx=(5, 0))

# 이름 커스텀하기
name_label = tk.Label(root, text="내 이름")
name_label.pack(padx=10, pady=(0, 0), anchor='w')

name_entry = tk.Entry(root)
name_entry.pack(padx=10, pady=(0, 10), fill='x')


def append_text(text):
    chat_area.configure(state='normal')
    chat_area.insert(tk.END, text + '\n')
    chat_area.configure(state='disabled')
    chat_area.yview(tk.END)


def send_message(event=None):
    msg = input_entry.get().strip()
    if msg == '':
        return
    name = name_entry.get().strip()
    if name == '':
        name = '나'

    full_msg = f"{name}: {msg}"
    append_text(full_msg)
    # 여기서는 화면에 안 찍고
    clientSock.send(full_msg.encode('utf-8'))  # 서버로만 전송
    input_entry.delete(0, tk.END)


def recv_loop():
    while True:
        data = clientSock.recv(1024)
        if not data:
            break
        text = data.decode('utf-8')

        def add():
            append_text(text)

        root.after(0, add)


def on_close():
    clientSock.close()
    root.destroy()


send_button.config(command=send_message)
input_entry.bind("<Return>", send_message)
root.protocol("WM_DELETE_WINDOW", on_close)

t = threading.Thread(target=recv_loop)
t.daemon = True
t.start()

root.mainloop()