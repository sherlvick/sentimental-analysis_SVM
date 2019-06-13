# -*- coding: utf-8 -*-
import os
import base64
import subprocess
import time
from svm_pipe import *
from svm_pipe_test import *
from ConfigurationGUI import *
from svm_test_0 import *
from os import *
import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from multiprocessing import Process, freeze_support

import sys
sys.path.append('C:\\Users\\Ashwin\\Desktop\\anirudh\\anirudh\\Test\\amazon-reviews-scraper-master')
from amazon_comments_scraper import*


cons =""
class AnalyseGUI:

    def __init__(self, parent):
        self.AnalysisFrame = ttk.Frame(parent)
        self.AnalysisFrame.grid()
        self.config_file_txt = ttk.Label(self.AnalysisFrame, text="Please select an option to get going.")
        self.config_file_txt.grid(row=0, column=0, columnspan=4, sticky="nw")

        self.upload_file_btn = ttk.Button(self.AnalysisFrame, text="Web-Scrape", command=lambda: self.file_maker())
        self.upload_file_btn.grid(row=1, column=0, sticky="nw", padx=(10, 0))
        self.config_file_skip_option = ttk.Button(self.AnalysisFrame, text="Training",
                                                  command=lambda: self.use_def())
        self.config_file_skip_option.grid(row=1, column=1, sticky="nw")
        self.config_file_skip_option = ttk.Button(self.AnalysisFrame, text="Testing",
                                                  command=lambda: self.use_def1())
        self.config_file_skip_option.grid(row=1, column=2, sticky="nw")

        self.LogPanelObj = open_log_panel(self, self.AnalysisFrame, row_base=2, column_base=0)
        self.analysis_btn = ttk.Button(self.AnalysisFrame, text="Start Analysis", state=DISABLED,
                                       command=lambda: self.start_analysis())
        self.analysis_btn.grid(row=5, column=0, columnspan=3, sticky="nw", padx=12, pady=10)

        ttk.Label(self.AnalysisFrame, text="Type your individual review") \
            .grid(row=6, column=0, columnspan=2, sticky="nw", padx=2)
        self.svm_inp = ttk.Entry(self.AnalysisFrame, width=25)
        self.svm_inp.grid(row=6, column=2, sticky="nw", padx=2)
        ttk.Button(self.AnalysisFrame, text="Submit", command=lambda: self.use_def1()) \
            .grid(row=7, column=0, sticky="nw", padx=10)

        ttk.Label(self.AnalysisFrame, text="Live Console").grid(row=8, column=0, sticky="nw", padx=2)

        self.live_console_txt_fld = ScrolledText(self.AnalysisFrame, height=10, width=60, wrap=WORD)
        self.live_console_txt_fld.configure(font=("helvetica", 8))
        self.live_console_txt_fld.grid(row=9, column=0, columnspan=4, padx=10, sticky="nw")
        self.config = "Default"


    def file_maker(self):
        messagebox.showinfo("Hi", "Lets scrape AMAZON...")
        cons = self.live_console_txt_fld.get('1.0', END)
        print(cons)
        scrape = main(cons)
        self.live_console_txt_fld.insert(END, scrape)
        pass


    def use_def(self):
        messagebox.showinfo("Hi", "Lets train some data")
        self.live_console_txt_fld.insert(END, "Now attempting to TRAIN the data")
        self.live_console_txt_fld.insert(END, "\nMachine going under train...\n")
        T_data = training()
        self.live_console_txt_fld.insert(END, T_data[0])
        messagebox.showinfo("Model is trained with:", T_data[1]+" reviews")
        pass

    def use_def1(self):
        #print("testing connection with sbumit")
        #exit()
        self.live_console_txt_fld.insert(END, "Lets check what you just typed")
        fail = -1
        anal1 = self.svm_inp.get()
        print(anal1)
        data3 = testing(anal1)
        #print (anal1)
        print(type(data3))
        print("Data gotten from test function is -", data3)
        #self.live_console_txt_fld.insert(END, "\nSentiment of the typed review is!!\n")
        if data3 == ['__label__2 ']:
            messagebox.showinfo("Sentiment of the typed review is", "Positive")
            #self.live_console_txt_fld.insert(END, "\n Positive")
        else:
            messagebox.showinfo("Sentiment of the typed review is", "Negative")
            #self.live_console_txt_fld.insert(END, "\n Negative")
        pass

    def start_analysis(self):
        messagebox.showinfo("Hi", "Machine going under testing process")
        self.live_console_txt_fld.insert(END, "Lets try to test that file filled with reviews")
        fail = -1
        anal= self.LogPanelObj.OpenLogPath.get()
        anal.replace("\\", "\\\\")
        print(anal)
        data0 = testing1(anal)
        data2 = float(data0[0])
        #print(type(data2))
        print("Data gotten from test function is -", data2)
        self.live_console_txt_fld.insert(END, "\nHere are the results!!\n")
        self.live_console_txt_fld.insert(END, "\nAccuracy - "+ str(data2))
        time.sleep(1)
        cm0 = conf_matrix(data0[1], data0[2])
        self.live_console_txt_fld.insert(END, "\nConfusion matrix - \n")
        self.live_console_txt_fld.insert(END, cm0[0])
        cm0[1].show()

class FooterFrame:
    def __init__(self, parent):
        self.footer_frame2 = Frame(parent)
        self.footer_frame2.pack()
        self.footer_frame = Frame(self.footer_frame2)

        ttk.Label(self.footer_frame, text="Version 0.5 \t     \t").grid(row=0, column=0, sticky="nw")
        self.report_btn = ttk.Button(self.footer_frame, text="Report Bug")
        self.report_btn.grid(row=0, column=1)
        self.footer_frame.lift()
        self.footer_frame.pack(pady=10)
        ttk.Button(self.footer_frame, text="Tutorial", command=lambda: self.launch_tut()).grid(row=0, column=2,
                                                                                               padx=(2, 0))

    @staticmethod
    def launch_tut():
        pass



def launch():
    """ The Module that launches our Analysis GUI"""
    global script_path
    global root
    script_path = find_cur_running_path()
    root = Tk()
    configure_style()
    root.configure()
    root.title("Sentimental Analysis Toolkitv1.0")
    #root.resizable(0, 0)

    # Frames - Main Tabs - Header (frame on top) + Content Frame
    header_frame = Frame(root, borderwidth=2, bg="black")
    header_frame.pack(fill=BOTH,expand = 1)
    content_frame = ttk.Frame(root)
    content_frame.pack()
    footer_frame = ttk.Frame(root)
    footer_frame.pack()
    header_text = ttk.Label(header_frame, text="Welcome to the Sentimental Analysis Toolkit v1.0", style='Heading.TLabel')
    header_text.pack(fill = 'y',expand = 1)
    script_path = find_cur_running_path()
    AnalyseGUI(content_frame)
    FooterFrame(footer_frame)
    root.geometry('500x560+20+20')
    root.mainloop()


if __name__ == "__main__":
    freeze_support()
    p = Process(target=launch())
    p.start()
