import tkinter as tk
import tkinter.ttk as ttk

from pytube import YouTube
from tkinter import filedialog

window = tk.Tk()
window.title('Downloader')
window.geometry('650x700+450+50')
window.resizable(False, False)
window.config(bg='#b3d6d5')

title = tk.Label(master=window, text='Youtube Video Downloader', bg='#b3d6d5', fg='#2d29a0',
                 font=('Cambria', 26, 'bold'))
title.pack(pady=10, anchor='center')

# creating window "URL"
title_link = tk.Label(master=window, text='URL', bg='#b3d6d5', fg='#2d29a0',
                      font=('Cambria', 16, 'bold'))
title_link.pack(padx=30, pady=38, anchor='nw')

url = tk.StringVar()
link = tk.Entry(master=window, bg='white', fg='#2d29a0', font=('Cambria', 16), width=38, textvariable=url)
link.place(x=92, y=104)

error_link = tk.Label(master=window, bg='#b3d6d5', fg='#2d29a0', font=('Cambria', 12, 'bold'))
error_link.place(x=300, y=142)

# creating window for input to path
title_path = tk.Label(master=window, text='Path', bg='#b3d6d5', fg='#2d29a0', font=('Cambria', 14, 'bold'))
title_path.pack(padx=30, pady=18, anchor='nw')

path = tk.Entry(master=window, bg='white', fg='#2d29a0', font=('Cambria', 16), width=38)
path.place(x=92, y=188)

path_error = tk.Label(master=window, bg='#b3d6d5', fg='#2d29a0', font=('Cambria', 12, 'bold'))
path_error.place(x=300, y=260)

select_button = tk.Button(master=window, text='select', bg='#2d29a0', fg='#b3d6d5', font=('Cambria', 11, 'bold'),
                          activeforeground='#2d29a0', activebackground='#b3d6d5')
select_button.place(x=300, y=230)

# creating window "Type Video"
title_type = tk.Label(master=window, text='Type', bg='#b3d6d5', fg='#2d29a0', font=('Cambria', 14, 'bold'))
title_type.pack(padx=98, pady=70, anchor='nw')

types_entry = ['High Quality', 'Low Quality', 'Audio']

# changing appearance of the selected component
combostyle = ttk.Style()
combostyle.theme_create('combostyle', settings={'TCombobox': {'configure':
                                                               {'foreground': '#2d29a0',
                                                                'selectbackground': 'white',
                                                                'selectforeground': '#2d29a0'}}})
combostyle.theme_use('combostyle')

record_window = ttk.Combobox(master=window, values=types_entry, font=('Cambria', 14, 'bold'),
                             width=27, state='readonly')
record_window.current(0)
record_window.place(x=159, y=308)
# changing appearance of the list of components
record_window.master.option_add('*TCombobox*Listbox.foreground', '#2d29a0')
record_window.master.option_add('*TCombobox*Listbox.selectForeground', '#2d29a0')
record_window.master.option_add('*TCombobox*Listbox.selectBackground', '#b3d6d5')
record_window.master.option_add('*TCombobox*Listbox.font', ('Cambria', 12))

# creating button "Download"
# style_download = ttk.Style()
# style_download.configure('DD.TButton', background='#2d29a0', foreground='#b3d6d5',
#                          font=('Cambria', 24, 'bold'))

download_button = tk.Button(master=window, text='DOWNLOAD', background='#2d29a0', foreground='#b3d6d5',
                            font=('Cambria', 22, 'bold'), activeforeground='#2d29a0', activebackground='#b3d6d5', width=20)
download_button.pack(pady=20)


if __name__ == '__main__':
    window.mainloop()
