import tkinter as tk
from tkinter import scrolledtext, simpledialog, messagebox, filedialog
import random

class StoryPlatformGUI:
    def __init__(self, master):
        self.master = master
        master.title("EnglishPairLearningClub.")

        # Setting custom colors as instance attributes
        self.bg_color = '#142338'
        self.button_color = '#daa520'
        self.text_color = 'white'

        master.configure(bg=self.bg_color)

        # Title Label(This is where I have the title)
        tk.Label(master, text="EnglishLearningMatch", font=("Times New Roman", 16), bg=self.bg_color,
                 fg="#daa520").pack()

        # User details input
        tk.Label(master, text="First Name:", bg=self.bg_color, fg=self.text_color).pack()
        self.first_name = tk.Entry(master)
        self.first_name.pack()

        tk.Label(master, text="Last Name:", bg=self.bg_color, fg=self.text_color).pack()
        self.last_name = tk.Entry(master)
        self.last_name.pack()

        tk.Label(master, text="Class:", bg=self.bg_color, fg=self.text_color).pack()
        self.user_class = tk.Entry(master)
        self.user_class.pack()

        # Initialize buttons
        self.setup_buttons()

        # Story display area
        self.story_text = scrolledtext.ScrolledText(master, width=40, height=10)
        self.story_text.pack()

        # File names
        self.story_file = "collaborative_story.txt"
        self.word_file = "word_of_the_day.txt"
        self.grammar_file = "grammar_rule.txt"

    def setup_buttons(self):
        # Adding padding between buttons
        button_padx = 10
        button_pady = 5

        tk.Button(self.master, text="Contribute to Story", bg=self.button_color, command=self.contribute_to_story).pack(padx=button_padx, pady=button_pady)
        tk.Button(self.master, text="Post Word of the Day", bg=self.button_color, command=self.post_word_of_the_day).pack(padx=button_padx, pady=button_pady)
        tk.Button(self.master, text="Post Grammar Rule", bg=self.button_color, command=self.post_grammar_rule).pack(padx=button_padx, pady=button_pady)
        tk.Button(self.master, text="View Story", bg=self.button_color, command=self.view_story).pack(padx=button_padx, pady=button_pady)
        tk.Button(self.master, text="Find Study Match", bg=self.button_color, command=self.find_study_match).pack(padx=button_padx, pady=button_pady)
        tk.Button(self.master, text="Save Story", bg=self.button_color, command=self.save_story).pack(padx=button_padx, pady=button_pady)
        tk.Button(self.master, text="Exit", bg=self.button_color, command=self.master.quit).pack(padx=button_padx, pady=button_pady)

    # ... rest of the methods ...
    def contribute_to_story(self):
        if self.validate_user_details():
            contribution = simpledialog.askstring("Contribute to Story",
                                                  "Enter your sentence or paragraph for the story:")
            if contribution:
                with open(self.story_file, "a") as story_file:
                    story_file.write(
                        f"{self.first_name.get()} {self.last_name.get()} ({self.user_class.get()}): {contribution}\n")
                messagebox.showinfo("Success", "Contribution added to the story!")

    def post_word_of_the_day(self):
        word_of_the_day = simpledialog.askstring("Word of the Day", "Enter the Word of the Day:")
        if word_of_the_day:
            with open(self.word_file, "w") as word_file:
                word_file.write(word_of_the_day)
            messagebox.showinfo("Success", "Word of the Day posted!")

    def post_grammar_rule(self):
        grammar_rule = simpledialog.askstring("Grammar Rule", "Enter the Grammar Rule:")
        if grammar_rule:
            with open(self.grammar_file, "w") as grammar_file:
                grammar_file.write(grammar_rule)
            messagebox.showinfo("Success", "Grammar Rule posted!")

    def view_story(self):
        self.story_text.delete('1.0', tk.END)
        try:
            with open(self.story_file, "r") as story_file:
                self.story_text.insert(tk.INSERT, story_file.read())
            with open(self.word_file, "r") as word_file:
                self.story_text.insert(tk.INSERT, "\nWord of the Day:\n" + word_file.read())
            with open(self.grammar_file, "r") as grammar_file:
                self.story_text.insert(tk.INSERT, "\nGrammar Rule:\n" + grammar_file.read())
        except FileNotFoundError:
            messagebox.showerror("Error", "File not found.")

    def save_story(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.story_text.get("1.0", tk.END))
            messagebox.showinfo("Success", "Story saved successfully!")

    def find_study_match(self):
        # This function assumes you have a list of students to match.
        # Placeholder list for example:
        students = ['Alice', 'Bob', 'Charlie', 'Dana', 'Evan', 'Fiona', 'George', 'Hannah']
        if len(students) < 2:
            messagebox.showerror("Error", "Not enough students to form a match.")
            return

        # Shuffle the list and pair students
        random.shuffle(students)
        matches = "\n".join([f"{students[i]} & {students[i + 1]}" for i in range(0, len(students) - 1, 2)])
        messagebox.showinfo("Study Matches", "Here are the study pairs:\n" + matches)

    def validate_user_details(self):
        if not all([self.first_name.get(), self.last_name.get(), self.user_class.get()]):
            messagebox.showerror("Error", "Please enter your first name, last name, and class.")
            return False
        return True

if __name__ == "__main__":
    root = tk.Tk()
    app = StoryPlatformGUI(root)
    root.mainloop()






