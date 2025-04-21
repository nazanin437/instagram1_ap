from tkinter import *
from tkinter import ttk, messagebox, simpledialog
import random

class SignUpWindow:
    def __init__(self, parent):
        self.current_username = ""
        self.file_path = r"C:\Users\Ofogh Rayaneh0211\Desktop\my_p\users.txt"

        self.signup_window = Toplevel(parent)
        self.signup_window.title("Sign Up")
        self.signup_window.geometry("900x500")
        self.signup_window.configure(bg="white")

        self.photo_sign = PhotoImage(file=r"C:\Users\Ofogh Rayaneh0211\Desktop\my_p\user.png")
        photo_s = Label(self.signup_window, image=self.photo_sign, border=0)
        photo_s.place(x=400, y=20)

        
        self.email_label = Label(self.signup_window, text="Email:", font=("Helvetica", 12), bg="white")
        self.email_label.place(x=300, y=150)
        self.email_entry = Entry(self.signup_window, width=30, font=("Helvetica", 12))
        self.email_entry.place(x=400, y=150)

        self.username_label = Label(self.signup_window, text="Username:", font=("Helvetica", 12), bg="white")
        self.username_label.place(x=300, y=200)
        self.username_entry = Entry(self.signup_window, width=30, font=("Helvetica", 12))
        self.username_entry.place(x=400, y=200)

        self.password_label = Label(self.signup_window, text="Password:", font=("Helvetica", 12), bg="white")
        self.password_label.place(x=300, y=250)
        self.password_entry = Entry(self.signup_window, width=30, font=("Helvetica", 12), show="*")
        self.password_entry.place(x=400, y=250)

        self.signup_button = Button(self.signup_window, text="Sign Up", font=("Helvetica", 12), bg="#62449d", fg="white", command=self.valid_and_save)
        self.signup_button.place(x=400, y=300)

        self.result_label = Label(self.signup_window, text="", font=("Helvetica", 12), bg="white")
        self.result_label.place(x=400, y=350)

    def valid_and_save(self):
        email = self.email_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if "@" not in email or "." not in email:
            self.result_label.config(text="invalid Email!", fg="red")
        elif len(username) < 2:
            self.result_label.config(text="Username must be at least 2 characters!", fg="red")
        elif len(password) < 4:
            self.result_label.config(text="Password must be at least 4 characters!", fg="red")
        elif self.tekrari(email, username):
            self.result_label.config(text="User already exists!", fg="red")
        else:
            self.save_user(email, username, password)
            self.current_username = username 
            self.result_label.config(text="Registration Successful!", fg="green")
            self.open_new_window()
    def tekrari(self, email, username):
        try:
            with open(r"C:\Users\Ofogh Rayaneh0211\Desktop\my_p\users.txt", "r") as file:
                for line in file:
                    parts = line.split(",")
                    if len(parts) != 3:
                        continue 
                    stored_email, stored_username, _ = parts
                    if stored_email == email or stored_username == username:
                        return True
        except FileNotFoundError:
            return False
        return False
    def save_user(self, email, username, password):
        with open(self.file_path, "a") as file:
            file.write(f"{email},{username},{password}\n")

    def open_new_window(self):
        new_window = Toplevel(self.signup_window)
        new_window.title("instagram")
        new_window.geometry("900x500")
        new_window.configure(bg="white")

        global photo_new, photo_new2, photo_new3

        top_label = Label(new_window, text="To protect the security of your account, please keep your password confidential and use compatible devices. Now choose one of the options below", 
                         font=("Helvetica", 12), bg="white", wraplength=800, justify="center")
        top_label.pack(pady=10)

        photo_new = PhotoImage(file=r"C:\Users\Ofogh Rayaneh0211\Desktop\my_p\icons8-search-150.png")
        Button_new = Button(new_window, image=photo_new, border=0, highlightthickness=0, borderwidth=0, command=self.open_search_window)
        Button_new.place(x=150, y=100)
        lb_new = Label(new_window, text="search", font=("Helvetica", 15, "bold"), bg="white")
        lb_new.place(x=180, y=300)

        photo_new2 = PhotoImage(file=r"C:\Users\Ofogh Rayaneh0211\Desktop\my_p\icons8-user-page-100.png")
        Button_new2 = Button(new_window, image=photo_new2, border=0, highlightthickness=0, borderwidth=0, command=self.open_user_page_window)
        Button_new2.place(x=350, y=100)
        lb_new2 = Label(new_window, text="user page", font=("Helvetica", 15, "bold"), bg="white")
        lb_new2.place(x=380, y=300)

        photo_new3 = PhotoImage(file=r"C:\Users\Ofogh Rayaneh0211\Desktop\my_p\icons8-home-150.png")
        Button_new3 = Button(new_window, image=photo_new3, border=0, highlightthickness=0, borderwidth=0, command=self.open_home_window)
        Button_new3.place(x=550, y=100)
        lb_new3 = Label(new_window, text="home", font=("Helvetica", 15, "bold"), bg="white")
        lb_new3.place(x=590, y=300)

    def open_search_window(self):
        search_window = Toplevel(self.signup_window)
        search_window.title("Search")
        search_window.geometry("600x400")
        search_window.configure(bg="white")

        Label(search_window, text="Enter username to search:", font=("Helvetica", 12), bg="white").pack(pady=10)
        username_entry = Entry(search_window, width=30, font=("Helvetica", 12))
        username_entry.pack(pady=5)
        def search_user():
            q = username_entry.get()
            users_dict = {}
            try:
                with open(self.file_path, "r") as file:
                    for line in file:
                        if not line:
                            continue
                        parts = line.split(",")
                        if len(parts) >= 3:
                            username = parts[1]
                            users_dict[username] = {
                                "posts": random.randint(1, 50),
                                "followers": random.randint(10, 1000),
                                "following": random.randint(5, 500),
                                "bio": "Dream big, stay curious, and keep growing."}   
                if q in users_dict:
                    user_data =   [q]
                    self.show(search_window, q, user_data)
                else:
                    Label(search_window, text="User not found!", font=("Helvetica", 12), fg="red", bg="white").pack(pady=10)
            except FileNotFoundError:
                Label(search_window, text="Users file not found!", font=("Helvetica", 12), fg="red", bg="white").pack(pady=10)
        Button(search_window, text="Search", font=("Helvetica", 12),  bg="#62449d", fg="white", command=search_user).pack(pady=10)

    def show(self, window2, username, user_data):

        user_page = Toplevel(window2)
        user_page.title("instagram")
        user_page.geometry("500x400")
        user_page.configure(bg="white")

        Label(user_page, text=f"Username: {username}", font=("Helvetica", 14, "bold"), bg="white").pack(pady=10)
        Label(user_page, text=f"Bio: {user_data['bio']}", font=("Helvetica", 12), bg="white", wraplength=400).pack(pady=10)
        Label(user_page, text=f"Posts: {user_data['posts']} | Followers: {user_data['followers']} | Following: {user_data['following']}", 
              font=("Helvetica", 12), bg="white").pack(pady=10)
        def follow_user():
            Label(user_page, text=f"You followed {username}!", font=("Helvetica", 12), fg="green", bg="white").pack(pady=5)
        def unfollow_user():
            Label(user_page, text=f"You unfollowed {username}!", font=("Helvetica", 12), fg="orange", bg="white").pack(pady=5)
        Button(user_page, text="Follow", font=("Helvetica", 12), bg="#62449d", fg="white", command=follow_user).pack(pady=5)
        Button(user_page, text="Unfollow", font=("Helvetica", 12), bg="red", fg="white", command=unfollow_user).pack(pady=5)

    def open_user_page_window(self):
        user_page_window = Toplevel(self.signup_window)
        user_page_window.title(" Profile")
        user_page_window.geometry("700x600")
        
        notebook = ttk.Notebook(user_page_window)
        notebook.pack(fill=BOTH, expand=True)
        
        self.profile_tab(notebook)
        self.posts_tab(notebook)
        self.settings_tab(notebook)
        
    def profile_tab(self, notebook):
        profile_frame = Frame(notebook, bg="white")
        notebook.add(profile_frame, text="Edit profile")
        
        user_data = self.get_user_data()

        fields = [("username:", "username", user_data.get("username", "")),("bio:", "bio", user_data.get("bio", ""))]

        self.entries = {}
        indices = range(len(fields)) 
        for index, (label_safe, field, value) in zip(indices, fields):
            Label(profile_frame, text=label_safe, bg="white", font=("Helvetica", 12)).grid(row=index, column=0, padx=10, pady=10, sticky="e")
            if field == "bio":
                entry = Text(profile_frame, height=5, width=30, font=("Helvetica", 12))
                entry.insert("1.0", value)
            else:
                entry = Entry(profile_frame, font=("Helvetica", 12))
                entry.insert(0, value)
            
            entry.grid(row=index, column=1, padx=10, pady=10)
            self.entries[field] = entry

        Button(profile_frame, text="Changes saved.",command=self.update_profile, bg="#405DE6",fg="white",font=("Helvetica", 12)).grid(row=len(fields), column=1, pady=20)

    def posts_tab(self, notebook):
        posts_frame = Frame(notebook, bg="white")
        notebook.add(posts_frame, text=" My posts")
        
        my_posts = self.get_user_posts()
        Label(posts_frame, text="My posts:",font=("Helvetica", 14),bg="white").pack(pady=10)
        
        for post in my_posts:
            post_frame = Frame(posts_frame, bg="white", bd=1, relief=SOLID)
            post_frame.pack(fill=X, padx=10, pady=5)
            
            Label(post_frame, text=post["title"],font=("Helvetica", 12),bg="white").pack(side=LEFT, padx=10)
            Button(post_frame,text="View",command=lambda p=post: self.view_post(p),bg="#405DE6",fg="white").pack(side=LEFT)

    def settings_tab(self, notebook):
        settings_frame = Frame(notebook, bg="white")
        notebook.add(settings_frame, text="settings")
        
        privacy_frame = LabelFrame(settings_frame, text="Privacy", bg="white")
        privacy_frame.pack(fill=X, padx=10, pady=10)
        
        self.account_type = StringVar(value="public")
        Radiobutton(privacy_frame, text="Public Account",variable=self.account_type,value="public",bg="white",font=("Helvetica", 12)).pack(anchor=W)
        Radiobutton(privacy_frame, text="Private Account",variable=self.account_type,value="private",bg="white",font=("Helvetica", 12)).pack(anchor=W)
        
        
        saved_frame = LabelFrame(settings_frame, text="saved", bg="white")
        saved_frame.pack(fill=X, padx=10, pady=10)
        
        saved_posts = self.get_saved_posts()
        for post in saved_posts:
            Label(saved_frame, 
                text=post,
                bg="white",
                font=("Helvetica", 12)).pack(anchor=W)
        blocked_frame = LabelFrame(settings_frame, text="Blocked users", bg="white")
        blocked_frame.pack(fill=X, padx=10, pady=10)
        
        blocked_users = self.get_blocked_users()
        for user in blocked_users:
            frame = Frame(blocked_frame, bg="white")
            frame.pack(fill=X, pady=5)
            Label(frame, 
                text=user,
                bg="white",
                font=("Helvetica", 12)).pack(side=LEFT)
            Button(frame,text="Unblock",command=lambda u=user: self.unblock_user(u),bg="red",fg="white").pack(side=LEFT)
    def get_user_data(self):
            with open(self.file_path, "r") as file:
                for line in file:
                    parts = line.split(",")
                    if len(parts) >= 3 and parts[1] == self.current_username:
                        return {
                            "username": parts[1],
                            "bio": parts[2] if len(parts) > 3 else ""}
    def update_profile(self):
        new_username = self.entries["username"].get()
        new_bio = self.entries["bio"].get("1.0", END)
        with open(self.file_path, "r") as file:
            lines = file.readlines()
        new_lines = []
        for line in lines:
            parts = line.split(",")
            if len(parts) >= 3 and parts[1] == self.current_username:
                parts[1] = new_username
                if len(parts) > 3:
                    parts[3] = new_bio
                else:
                    parts.append(new_bio)
                line = ",".join(parts) + "\n"
                self.current_username = new_username
            new_lines.append(line)
        with open(self.file_path, "w") as file:
            file.writelines(new_lines)
        messagebox.showinfo("profile", "Profile updated successfully")
    def get_user_posts(self):
        return [
    {"id": 1, "title": "Post 1", "content": "_"},
    {"id": 2, "title": "Post 2", "content": "_"}]
    def get_saved_posts(self):
        return ["post1", "post2"]
    def get_blocked_users(self):
        return ["user1", "user2"]
    def unblock_user(self, username):
        messagebox.showinfo("Unblock", f"{username} emoved")
    def view_post(self, post):
        post_window = Toplevel()
        post_window.title(post["title"])
        post_window.geometry("500x400")
        global photo

        if post["id"] == 2: 
            photo = PhotoImage(file=r"C:\Users\Ofogh Rayaneh0211\Desktop\my_p\son2.png")  # تصویر دوم
        elif post["id"] == 1: 
            photo = PhotoImage(file=r"C:\Users\Ofogh Rayaneh0211\Desktop\my_p\son1.png")  # تصویر پیش‌فرض
        Label(post_window, image=photo, font=("B Nazanin", 14)).pack(pady=10)
        content_text = Text(post_window, wrap=WORD, font=("B Nazanin", 12))
        content_text.pack(padx=10, pady=10)
        content_text.insert("1.0", post["content"])  
    def open_new_home_window(self):
            new_home_window = Toplevel(self.home_window)
            new_home_window.title("Menu")
            new_home_window.geometry("600x500")
            new_home_window.configure(bg="white")
            def send_message():
                username = username_entry.get()
                message = message_entry.get()
                with open(r"C:\Users\Ofogh Rayaneh0211\Desktop\my_p\users.txt", "r") as file:
                    found = False
                    for line in file:
                        parts = line.split(',')
                        if len(parts) == 3 and parts[1] == username:  
                            found = True
                            break
                if found:
                    print(f"Message to {username}: {message}")
                else:
                    print("No such user exists")
            def create_group():
                try:
                    with open(r"C:\Users\Ofogh Rayaneh0211\Desktop\my_p\users.txt", "r") as file:
                        users = [line.split(',')[1] for line in file if len(line.split(',')) == 3]
                    group_name = simpledialog.askstring("Group Name", "Enter group name:")
                    if not group_name:
                        print("Group cancelled.")
                        return
                    selected_users = simpledialog.askstring("Group Members", f"Available users: {', '.join(users)}\nEnter usernames ")
                    if not selected_users:
                        print("No members selected for the group.")
                        return
                    selected_users_list = [user.strip() for user in selected_users.split(',')]
                    for user in selected_users_list:
                        if user not in users:
                            print(f"User {user} not found in the file!")
                            return
                    with open(r"C:\Users\Ofogh Rayaneh0211\Desktop\my_p\groups.txt", "a") as group_file:
                        group_file.write(f"Group: {group_name}, Members: {', '.join(selected_users_list)}\n")
                    print(f"Group '{group_name}' created with members: {', '.join(selected_users_list)}")
                except FileNotFoundError:
                    print("User file not found")

            notebook = ttk.Notebook(new_home_window)
            notebook.pack(fill='both', expand=True)

            messages_frame = Frame(notebook, bg="white")
            notebook.add(messages_frame, text="Messages")

            Label(messages_frame, text="Username:", bg="white").pack(pady=5)
            username_entry = Entry(messages_frame)
            username_entry.pack(pady=5)

            Label(messages_frame, text="Message:", bg="white").pack(pady=5)
            message_entry = Entry(messages_frame)
            message_entry.pack(pady=5)

            Button(messages_frame, text="Send Message", bg="#62449d", fg="white", command=send_message).pack(pady=20)

            Button(messages_frame, text="Send Message", bg="#62449d", fg="white", command=send_message).pack(pady=20)
            Button(messages_frame, text="Create Group", bg="#3b7dd8", fg="white", command=create_group).pack(pady=10)
            
            def on_accept(user):
                print(f"Followed : {user}")

            def on_reject(user):
                print(f"Unfollowed: {user}")

            followers_frame = Frame(notebook, bg="white")
            notebook.add(followers_frame, text="Request to follow")
            requests = ["kokab", "teramp", "ahoora"]
            for req in requests:
                frame = Frame(followers_frame, bg="white")
                frame.pack(fill='x', padx=20, pady=5)
                Label(frame, text=req, bg="white", width=15).pack(side='left')
                Button(frame, text="Follow ", bg="green", fg="white", command=lambda r=req: on_accept(r)).pack(side='left', padx=5)
                Button(frame, text="Unfollow", bg="red", fg="white", command=lambda r=req: on_reject(r)).pack(side='left')

            stories_frame = Frame(notebook, bg="white")
            notebook.add(stories_frame, text="Stories")

            friends =  ["kokab", "teramp", "ahoora"]
            for friend in friends:
                btn = Button(stories_frame,text=friend,command=lambda f=friend: show_story(f),bg="#405DE6",  fg="white",font=("B Nazanin", 12),width=15)
                btn.pack(pady=5)

            def show_story(friend_name):
                story_win = Toplevel()
                story_win.title(f"story {friend_name}")
                story_win.geometry("300x400")

                Label(story_win, text=f"story {friend_name}",font=("Helvetica", 14)).pack(pady=50)
                Button(story_win,text="like ❤️",bg="red",fg="white",command=lambda: like_story(friend_name)).pack()
                Button(story_win,text="close", command=story_win.destroy).pack(pady=20)

            def like_story(name):
                messagebox.showinfo("like", f"You liked {name} story.")   
    def open_home_window(self):
        self.home_window = Toplevel(self.signup_window)
        self.home_window.title("Home")
        self.home_window.geometry("600x800")
        self.home_window.configure(bg="white")

        username_label = Label(self.home_window, text="hasan_90", font=("Helvetica", 12, "bold"), bg="white", anchor="w")
        username_label.pack(fill="x", padx=10, pady=5)

        date_label = Label(self.home_window, text="11-20-0202 📅", font=("Helvetica", 10), bg="white", anchor="w")
        date_label.pack(fill="x", padx=10, pady=2)

        photo = PhotoImage(file=r"C:\Users\Ofogh Rayaneh0211\Desktop\my_p\the-little-girl-whos.png")
        caption_label = Label(self.home_window, image=photo, bg="white")
        caption_label.image = photo
        caption_label.pack(padx=10, pady=5)

        stats_label = Label(self.home_window, text="Comments: 2 💬 Likes: 12 ❤️\nShare: 0 ✉ Save: 0 💾", font=("Helvetica", 10), bg="white", anchor="w")
        stats_label.pack(fill="x", padx=10, pady=5)

        comments_label = Label(self.home_window, text="Comments 💬:", font=("Helvetica", 12, "bold"), bg="white", anchor="w")
        comments_label.pack(fill="x", padx=10, pady=5)

        comments_= Text(self.home_window, width=60, height=10, font=("Helvetica", 10))
        comments_.pack(padx=10, pady=5)

        comments_.insert(END, "@lili: 😍it was great\n")
        comments_.insert(END, "@kokab: where are you\n")
        comments_.insert(END, "@twramp: wonderful😊\n")
        comments_.config(state=DISABLED)

        comment_entry = Entry(self.home_window, width=50, font=("Helvetica", 12))
        comment_entry.pack(padx=10, pady=5)

        def add_comment():
            new_comment = comment_entry.get()
            if new_comment:
                comments_.config(state=NORMAL)
                comments_.insert(END, f"you: {new_comment}\n")
                comments_.config(state=DISABLED)
                comment_entry.delete(0, END)

        Button(self.home_window, text="Add Comment 💬", command=add_comment, bg="#62449d", fg="white", 
              font=("Helvetica", 10)).pack(padx=10, pady=5)

        _frame = Frame(self.home_window, bg="white")
        _frame.pack(pady=10)

        Button(_frame, text="Like", command=self.like_post, bg="#62449d", fg="white", 
              font=("Helvetica", 10)).grid(row=0, column=0, padx=5)
        Button(_frame, text="Share", command=self.share_post, bg="#62449d", fg="white", 
              font=("Helvetica", 10)).grid(row=0, column=1, padx=5)
        Button(_frame, text="Save", command=self.save_post, bg="#62449d", fg="white", 
              font=("Helvetica", 10)).grid(row=0, column=2, padx=5)

        def view_followed_posts():
            followed_window = Toplevel(self.home_window)
            followed_window.title("Followed Users' Posts")
            followed_window.geometry("600x500")
            followed_window.configure(bg="white")

            followed_posts = [
                {"username": "kokab", "date": "11-21-0202 📅", "caption": "beautiful day", 
                 "comments": ["@lili: wonderful!", "@x:interesting !"]},
                {"username": "teramp", "date": "11-22-0202 📅", "caption": "!", 
                 "comments": ["@lona: great!", "@maya: how great !"]}
            ]
            for post in followed_posts:
                post_frame = Frame(followed_window, bg="white", relief=RIDGE, borderwidth=2)
                post_frame.pack(pady=10, padx=10, fill="x")

                Label(post_frame, text=post["username"], font=("Helvetica", 12, "bold"), bg="white").pack(anchor="w", padx=10, pady=5)
                Label(post_frame, text=post["date"], font=("Helvetica", 10), bg="white").pack(anchor="w", padx=10, pady=2)
                Label(post_frame, text=post["caption"], font=("Helvetica", 14), bg="white", 
                     wraplength=500, justify="right").pack(padx=10, pady=5)
                Label(post_frame, text="--------------------------------", font=("Helvetica", 10), bg="white").pack(pady=5)

                comments_display = Text(post_frame, width=60, height=5, font=("Helvetica", 10))
                comments_display.pack(padx=10, pady=5)
                comments_display.config(state=NORMAL)
                for comment in post["comments"]:
                    comments_display.insert(END, f"├── {comment}\n")
                comments_display.config(state=DISABLED)

        Button(self.home_window, text="View Followed Users' Posts", command=view_followed_posts, 
              bg="#62449d", fg="white", font=("Helvetica", 12)).pack(pady=10)
        
        menu_button = Button(self.home_window, text="Menu", command=self.open_new_home_window, 
                        bg="#62449d", fg="white", font=("Helvetica", 12))
        menu_button.pack(pady=10)

    def like_post(self):
        print("Post liked!")

    def share_post(self):
        print("Post shared!")

    def save_post(self):
        print("Post saved locally!")

