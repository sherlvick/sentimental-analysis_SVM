from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import sys


def find_cur_running_path():
    script_path = sys.path[0]
    return script_path


def configure_style():
    # Style - Not defined style near imports as it needs a window to work with.
    ttk.Style().configure('Heading.TLabel', background='black', foreground='orange', font=('Courier New', 14, 'bold'),
                          padding=5)
    ttk.Style().configure('RedVal.TLabel', foreground='dark red', font=('Courier New', 10, 'bold'), padding=5)
    ttk.Style().configure('GreenVal.TLabel', foreground='dark green', font=('Courier New', 10, 'bold'), padding=5)

    ttk.Style().configure('TButton', foreground='blue', font=('Courier New', 10, 'bold'), background='black')
    ttk.Style().configure('TLabel', font=('Courier New', 10, 'bold'), padding=5)
    ttk.Style().configure('TCheckbutton', font=('Courier New', 10), padding=10)
    ttk.Style().configure('TRadiobutton', font=('Courier New', 10), padding=10)
    ttk.Style().configure('TEntry', font=('Courier New', 10), padding=10)
    return


def open_log_panel(obj, obj_frame, row_base, column_base):
    button_logo_path = find_cur_running_path() + '\\Resources\\BtnImg.gif'
    ttk.Label(obj_frame, text='Choose The File To Analyze').\
        grid(row=row_base, column=column_base, columnspan=3, sticky="nw", padx=3)
    obj.OpenLogPath = ttk.Entry(obj_frame, width=38)
    obj.OpenLogPath.insert(0, 'Click the button to select a save path ->')
    obj.OpenLogPath.config(state=DISABLED)
    obj.OpenLogPath.grid(row=row_base+1, column=column_base, columnspan=2, padx=(10, 0), sticky="nw")
    obj.OpenBrowseButtonLogo = PhotoImage(file=button_logo_path)
    obj.OpenBrowseButton = Button(obj_frame, cursor="hand2")
    obj.OpenBrowseButton.config(image=obj.OpenBrowseButtonLogo, command=lambda: browse(obj))
    obj.OpenBrowseButton.grid(row=row_base+1, column=column_base+2, sticky="w")
    return obj


def browse(op_obj):
    op_obj.live_console_txt_fld.delete('1.0', END)
    file_name = str(askopenfilename(initialdir='/', title="Select File", filetypes=[("CSVs", "*.csv"),
                                                                                    ("Text File", "*.txt")]))
    if file_name is "":
        return

    op_obj.OpenLogPath.config(state='normal')
    op_obj.OpenLogPath.delete(0, END)
    op_obj.OpenLogPath.insert(0, file_name.replace("/", "\\"))
    op_obj.analysis_btn.config(state='normal')
    browse.alist = file_name.split('/')



def filename1():
    file_name1 = browse.alist.pop()
    return file_name1