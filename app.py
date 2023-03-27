from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image
import os
import time
import textwrap


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("python 调整分辨率 ")
        self.master.geometry("500x200")
        self.master.iconbitmap(r"D:\Github\images_compress\my_ico.ico")  # 设置应用程序的图标
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.input_label = Label(self, text="选择要压缩的图像文件：", padx=10, pady=10)
        self.input_label.grid(row=0, column=0, sticky=W)

        self.input_file = ""
        self.select_input_button = Button(
            self, text="浏览", command=self.select_input_file)
        self.select_input_button.grid(row=0, column=1, sticky=W)

        self.output_label = Label(self, text="输出文件名：", padx=10, pady=10)
        # self.output_label.grid(row=1, column=0, sticky=W)
        self.output_label.grid_remove()

        self.output_file = ""
        self.output_entry = Entry(self)
        # self.output_entry.grid(row=1, column=1, sticky=W)
        self.output_entry.grid_remove()

        self.max_size_label = Label(
            self, text="指定允许的最大图像大小（像素）：", padx=10, pady=10)
        self.max_size_label.grid(row=2, column=0, sticky=W)

        self.max_size_entry = Entry(self)
        self.max_size_entry.grid(row=2, column=1, sticky=W)

        self.compress_button = Button(
            self, text="压缩图像", command=self.compress_image)
        self.compress_button.grid(
            row=3, column=0, columnspan=2, padx=10, pady=10)

    def select_input_file(self):
        self.input_file = filedialog.askopenfilename(initialdir="/", title="选择文件",
                                                     filetypes=(("JPEG 文件", "*.jpg"), ("PNG 文件", "*.png"), ("所有文件", "*.*")))
        if self.input_file:
            wrapped_path = textwrap.fill(self.input_file, width=40)
            self.input_label.configure(text=f"已选择文件：\n{wrapped_path}")

    def compress_image(self):
        if not self.input_file:
            messagebox.showerror("错误", "请选择要压缩的图像文件！")
            return
        try:
            max_size = int(self.max_size_entry.get())
        except ValueError:
            messagebox.showerror("错误", "请输入正确的最大图像大小！")
            return
        if max_size <= 0:
            messagebox.showerror("错误", "最大图像大小必须大于0！")
            return
        try:
            img = Image.open(self.input_file)
            width, height = img.size
            if width > max_size or height > max_size:
                ratio = min(max_size / width, max_size / height)
                new_size = (int(width * ratio), int(height * ratio))
                img = img.resize(new_size, resample=Image.LANCZOS)
            output_dir = os.path.dirname(self.input_file)
            output_filename = f"compressed_{int(time.time())}.jpg"
            self.output_file = os.path.join(output_dir, output_filename)
            img.save(self.output_file, optimize=True, quality=80)
            wrapped_path = textwrap.fill(self.output_file, width=40)
            messagebox.showinfo("成功", f"图像压缩完成！\n已保存文件：\n{wrapped_path}")
        except Exception as e:
            messagebox.showerror("错误", f"压缩图像时发生错误：{e}")
            return

root = Tk()
app = Application(master=root)
app.mainloop()