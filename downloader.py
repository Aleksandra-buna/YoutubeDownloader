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

direct = ""


def choice_path():
    path.config(text='')
    global direct
    direct = filedialog.askdirectory()
    path.config(text=direct)


def download():
    url = str_url.get()
    selected_type = type_record.get()

    if len(url) < 7:
        error_link.config(text='"'+url+'"'+'INCORRECT!')
    if len(direct) < 3:
        path_error.config(text='"'+selected_type+'"'+'Incorrect Path!')
    else:
        error_link.config(text='')
        path_error.config(text='')
        try:
            yt = YouTube(url)
            try:
                if selected_type == types_entry[0]:
                    file = yt.streams.order_by('resolution').desc().first()
                elif selected_type == types_entry[1]:
                    file = yt.streams.filter(res='360p').desc().first()
                elif selected_type == [2]:
                    file = yt.streams.filter(only_audio=True).desc().first()

                try:
                    file.download(direct)
                    download_info.config(text='DOWNLOADED!')

                    name = file.title
                    size = file.filesize/1024000
                    size = round(size, 1)

                    download_name.config(text='Name: '+name)
                    download_size.config(text='Size: '+str(size)+'MB')
                    download_path.config(text='Path: '+direct)
                except:
                    download_info.config('Sorry, try again, please!')
            except:
                download_info.config('Sorry, try again, please!')
        except:
            error_link.config(text='"' + url + '"' + 'INCORRECT!')


# creating a window "URL"
title_link = tk.Label(master=window, text='URL', bg='#b3d6d5', fg='#2d29a0', font=('Cambria', 16, 'bold'))
title_link.pack(padx=30, pady=38, anchor='nw')

str_url = tk.StringVar()
link = tk.Entry(master=window, bg='white', fg='#2d29a0', font=('Cambria', 16), width=38, textvariable=str_url)
link.place(x=92, y=104)

error_link = tk.Label(master=window, bg='#b3d6d5', fg='red', font=('Cambria', 12, 'bold'))
error_link.place(x=30, y=142)

# creating a window for input to path
title_path = tk.Label(master=window, text='Path', bg='#b3d6d5', fg='#2d29a0', font=('Cambria', 14, 'bold'))
title_path.pack(padx=30, pady=18, anchor='nw')

path = tk.Label(master=window, bg='white', fg='#2d29a0', font=('Cambria', 16), width=38)
path.place(x=92, y=188)

path_error = tk.Label(master=window, bg='#b3d6d5', fg='red', font=('Cambria', 12, 'bold'))
path_error.place(x=30, y=260)

select_button = tk.Button(master=window, text='select', bg='#2d29a0', fg='#b3d6d5', font=('Cambria', 11, 'bold'),
                          activeforeground='#2d29a0', activebackground='#b3d6d5', command=choice_path)
select_button.place(x=300, y=230)

# creating a window "Type Video"
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

type_record = ttk.Combobox(master=window, values=types_entry, font=('Cambria', 14, 'bold'),
                           width=27, state='readonly')
type_record.current(0)
type_record.place(x=159, y=308)
# changing appearance of the list of components
type_record.master.option_add('*TCombobox*Listbox.foreground', '#2d29a0')
type_record.master.option_add('*TCombobox*Listbox.selectForeground', '#2d29a0')
type_record.master.option_add('*TCombobox*Listbox.selectBackground', '#b3d6d5')
type_record.master.option_add('*TCombobox*Listbox.font', ('Cambria', 12))

# creating a button "Download"
download_button = tk.Button(master=window, text='DOWNLOAD', background='#2d29a0', foreground='#b3d6d5',
                            font=('Cambria', 22, 'bold'), activeforeground='#2d29a0', activebackground='#b3d6d5',
                            width=20, command=download)
download_button.pack(pady=20)

download_info = tk.Label(master=window,
                         text='You have to fill all windows and click the "Download" button, then will begin '
                              'download.', bg='#b3d6d5', fg='#2d29a0', font=('Cambria', 11, 'bold'))
download_info.place(x=30, y=500)

# creating a window of information about the downloaded file
download_name = tk.Label(master=window, bg='#b3d6d5', fg='#2d29a0', font=('Cambria', 12, 'bold'))
download_name.place(x=30, y=550)

download_size = tk.Label(master=window, bg='#b3d6d5', fg='#2d29a0', font=('Cambria', 12, 'bold'))
download_size.place(x=30, y=600)

download_path = tk.Label(master=window, bg='#b3d6d5', fg='#2d29a0', font=('Cambria', 12, 'bold'))
download_path.place(x=30, y=650)

if __name__ == '__main__':
    window.mainloop()
