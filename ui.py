# -*- coding: utf8 -*-

import os
import sys
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import rm_vrc_sdk

project_path = ''


# Utility
def get_current_path():
    current_dir = os.getcwd()
    return current_dir


# イベント処理関数
def select_project_dir(edit_box):
    global project_path
    edit_box.delete(0, tk.END)
    project_path = filedialog.askdirectory(initialdir=project_path)
    edit_box.insert(tk.END, project_path)

def on_rm_clicked(self):
    global project_path

    self.configure(state=tk.DISABLED)
    result = rm_vrc_sdk.rm_vrcsdk(project_path + '\\')
    if result != '':
        messagebox.showerror(
            title='エラー',
            message=result
        )
    self.configure(state=tk.NORMAL)

if __name__ == "__main__":

    # GUIの初期処理
    root = tk.Tk()
    root.title('VRCSDK削除ツール')
    root.geometry("400x100")

    # ラベル
    label1 = tk.Label(text='Unityプロジェクトフォルダの選択')
    label1.place(x=5, y=5)

    # パス入力ボックス
    path_edit_box = tk.Entry(width=50)
    path_edit_box.insert(tk.END, get_current_path())
    path_edit_box.place(x=5, y=30)

    project_path = path_edit_box.get()

    # フォルダパス選択ボタン
    select_button = tk.Button(
        text='フォルダを選択', 
        command= lambda : select_project_dir(path_edit_box)
    )
    select_button.place(x=310, y=25)

    # 削除ボタン
    rm_button = tk.Button(
        text='削除',
        width=50,
        command= lambda : on_rm_clicked(rm_button)
    )
    rm_button.place(x=20, y=65)

    root.mainloop()