#!usr/bin/env python
#-*- coding:utf-8 _*-  
""" 
@author:ZhangHui
@file: CJ_v0.2.pyw
@time: 2018/01/28
"""
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
from tkinter.simpledialog import askinteger
import time
import sys

class app():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('抽奖 v0.2')
        self.w,self.h = self.root.maxsize()
        self.root.geometry("{}x{}".format(self.w-60,self.h-100))
        self.num_luck = 0;self.num_last = 0;self.num_all = []
        self.init_btn()
        self.init_ctn()
        self.init_out()
        self.init_menu()
        self.root.mainloop()
    def init_btn(self):
        #bg='#DC143C'
        self.label_select = tk.Label(self.root,text="需要抽取人数:",font=('Arial',30))\
            .grid(row=1,column=1,columnspan=2,sticky=tk.W,padx=50,pady=30)
        self.allsub = tk.Entry(self.root, width=25,font=('Arial',25))
        self.allsub.grid(row=2, column=1, columnspan=2, sticky=tk.W, padx=50, pady=30)
        self.btn_start = tk.Button(self.root, text="开始抽取", command=self.start,
                                   font=('Arial',25))\
            .grid(row=3, column=1, columnspan = 2 ,sticky=tk.W,padx=50,pady=30)
    def init_ctn(self):
        self.label_info = tk.Label(self.root,text="剩余情况:",font=('Arial',30))\
            .grid(row=1,column=3,columnspan=2,sticky=tk.W,padx=50,pady=30)
        self.label_info_last = tk.Label(self.root,text="剩余:",font=('Arial',20))\
            .grid(row=2,column=3,columnspan=2,sticky=tk.W,padx=50,pady=30)
        self.label_info_luck = tk.Label(self.root, text="已中奖:", font=('Arial', 20)) \
            .grid(row=3, column=3, columnspan=2, sticky=tk.W, padx=50, pady=30)
        self.label_luck_num = tk.Label(self.root, text=self.num_luck, font=('Arial', 20))
        self.label_luck_num.grid(row=3, column=4, columnspan=2, sticky=tk.W, padx=50, pady=30)
        self.label_last_num = tk.Label(self.root, text=self.num_last, font=('Arial', 20))
        self.label_last_num.grid(row=2, column=4, columnspan=2, sticky=tk.W, padx=50, pady=30)
    def init_out(self):
        self.outbox = tk.Text(self.root,width=100,height=100,font=('Arial',20))
        self.outbox.grid(row=5,column=1,columnspan=5,sticky=tk.N+tk.E+tk.W)
        #self.outbox.insert(1.0,'%s\t\t%s\t%s\n' %('抽奖时间','抽奖人数','抽奖结果'))

    def set_outbox(self,*kw):
        if len(kw) == 3:
            result = '%s\t\t%s\t%s\n' %(kw[0],kw[1],kw[2])
            #self.outbox.insert(1.0,"end",values=(kw[0],kw[1],kw[2]))
            self.outbox.insert(1.0,result)
        else:
            pass
    def init_menu(self):
        self.menu = tk.Menu(self.root)
        self.menu.add_command(label='输入总人数',command=self.init_all)
        self.root['menu']=self.menu
    def init_all(self):
        self.num_luck = 0;self.num_last = 0
        self.get_int()
        self.num_all = self.num_last*[0]
        for ii in range(1,self.num_last+1):
            self.num_all[ii-1] = ii
        self.init_btn()
        self.init_ctn()
        self.init_out()
        self.init_menu()
    def get_int(self):
        result = askinteger("请输入人数",'总人数',initialvalue=150)
        if result:
            self.num_last = result
        else:
            self.get_int()
    def start(self):
        num_select = self.allsub.get()
        result,last = self.select(self.num_all,num_select)
        self.num_all = list(set(self.num_all) - set(result))
        self.num_last = len(self.num_all)
        self.num_luck = self.num_luck + int(num_select)
        self.label_luck_num.config(text=self.num_luck)
        self.label_last_num.config(text=self.num_last)
        detail = ''
        for ii in result:
            if detail:
                detail = detail +'、'+str(ii)
            else:
                detail = str(ii)
        now_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        # num_select,result
        self.set_outbox(now_time, num_select, detail)


    def select(self,num_all,num_select):
        num_select = int(num_select)
        if len(num_all) < num_select:
            tk.messagebox.showerror('提示','待抽取人数不足')
        else:
            import random
            result = random.sample(num_all,num_select)
            last = len(num_all) - num_select
            return (result,last)
if __name__=="__main__":
    app = app()
