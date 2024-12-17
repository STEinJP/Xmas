import tkinter as tk
from tkinter import messagebox
import random
import webbrowser
import re
from sympy import symbols, diff, simplify, sympify

x = symbols('x')

# 祝福影片和整人音樂的連結
BLESSING_VIDEO_URL = "https://youtu.be/rB7SfHPmb5o"
PRANK_MUSIC_URL = "https://youtu.be/aAkMkVFwAoo?si=Aal3ah7FcNUZw9wH"

# 隨機生成微積分題
def generate_calculus_question():
    coef = random.randint(1, 5)
    power = random.randint(1, 4)
    expression = coef * x**power
    question = f"d/dx({coef}x^{power})"
    answer = diff(expression, x)
    return question, answer

# 預處理輸入
def preprocess_input(user_input):
    # 處理如 3x^5 這樣沒有明確乘號的格式，替換為 3 * x^5
    user_input = re.sub(r'(\d)(x)', r'\1*\2', user_input)  # 將 3x 改為 3*x
    user_input = user_input.replace("^", "**")  # 將 ^ 替換為 ** 
    return user_input

# 檢查答案
def check_answer():
    user_input = entry.get()
    processed_input = preprocess_input(user_input)
    print(f"處理過的用戶輸入：{processed_input}")
    
    try:
        # 解析用戶輸入
        user_expr = simplify(sympify(processed_input))
        print(f"解析結果：{user_expr}")
        print(f"正確答案：{correct_answer}")
        
        # 比較用戶輸入和正確答案
        if simplify(user_expr - correct_answer) == 0:
            messagebox.showinfo("答對了！", "恭喜你答對了，跳轉到祝福影片！")
            webbrowser.open(BLESSING_VIDEO_URL)
        else:
            messagebox.showerror("答錯了！", "很遺憾，答錯了，播放整人音樂！")
            webbrowser.open(PRANK_MUSIC_URL)
    except Exception as e:
        messagebox.showerror(
            "錯誤",
            f"無法解析你的輸入，請檢查數學表達式！\n"
            f"提示：使用 `*` 表示乘號，`**` 表示次方。\n"
            f"錯誤詳情：{e}"
        )

# 建立主視窗
root = tk.Tk()
root.title("聖誕節微積分挑戰")

# 顯示題目
question, correct_answer = generate_calculus_question()
label = tk.Label(root, text=f"解答以下微積分題目來獲得聖誕祝福！\n\n{question}", font=("Arial", 16))
label.pack(pady=20)

# 使用者輸入框
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

# 提交按鈕
submit_button = tk.Button(root, text="提交答案", command=check_answer, font=("Arial", 14), bg="green", fg="white")
submit_button.pack(pady=20)

# 啟動程式
root.mainloop()