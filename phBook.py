import tkinter as tk
from tkinter import ttk, messagebox
import pymysql
import uuid


class PhoneBook:

    def __init__(self, root):
        self.root = root
        self.root.title("Phone Book Management System")
        self.root.geometry("1200x700")
        self.root.minsize(1000, 600)
        self.root.configure(bg="#f4f6f8")

        self.cities = ["Delhi", "Kolkata", "Mumbai"]

        self.create_variables()
        self.setup_style()
        self.create_widgets()

    # ---------------------------------------------------------
    # VARIABLES
    # ---------------------------------------------------------

    def create_variables(self):
        self.city_var = tk.StringVar()
        self.name_var = tk.StringVar()
        self.addr_var = tk.StringVar()
        self.phone_var = tk.StringVar()

        self.search_city_var = tk.StringVar()
        self.search_name_var = tk.StringVar()

    # ---------------------------------------------------------
    # DATABASE CONNECTION
    # ---------------------------------------------------------

    def dbFun(self):
        self.con = pymysql.connect(
            host="localhost",
            user="root",
            password="1234",
            database="phonebook"
        )

        self.cur = self.con.cursor()

    # ---------------------------------------------------------
    # STYLE
    # ---------------------------------------------------------

    def setup_style(self):
        style = ttk.Style()

        try:
            style.theme_use("clam")
        except:
            pass

        style.configure(
            "Treeview",
            background="white",
            foreground="#222222",
            rowheight=32,
            fieldbackground="white",
            font=("Segoe UI", 10)
        )

        style.configure(
            "Treeview.Heading",
            font=("Segoe UI", 10, "bold"),
            background="#263238",
            foreground="white"
        )

        style.map(
            "Treeview",
            background=[("selected", "#1976D2")],
            foreground=[("selected", "white")]
        )

        style.configure(
            "TCombobox",
            padding=6,
            font=("Segoe UI", 10)
        )

    # ---------------------------------------------------------
    # GUI
    # ---------------------------------------------------------

    def create_widgets(self):

        # ================= HEADER =================

        header = tk.Frame(
            self.root,
            bg="#263238",
            height=90
        )
        header.pack(fill="x")
        header.pack_propagate(False)

        title = tk.Label(
            header,
            text="PHONE BOOK MANAGEMENT SYSTEM",
            font=("Segoe UI", 24, "bold"),
            bg="#263238",
            fg="white"
        )
        title.pack(pady=(15, 0))

        subtitle = tk.Label(
            header,
            text="Manage contacts from Delhi, Kolkata and Mumbai",
            font=("Segoe UI", 10),
            bg="#263238",
            fg="#CFD8DC"
        )
        subtitle.pack()

        # ================= MAIN AREA =================

        main = tk.Frame(
            self.root,
            bg="#f4f6f8"
        )
        main.pack(fill="both", expand=True, padx=20, pady=20)

        # ================= LEFT PANEL =================

        left = tk.Frame(
            main,
            bg="white",
            bd=1,
            relief="solid"
        )
        left.pack(
            side="left",
            fill="y",
            padx=(0, 15)
        )

        left_title = tk.Label(
            left,
            text="Add New Contact",
            font=("Segoe UI", 16, "bold"),
            bg="white",
            fg="#263238"
        )
        left_title.pack(
            anchor="w",
            padx=20,
            pady=(20, 15)
        )

        # City

        tk.Label(
            left,
            text="City",
            font=("Segoe UI", 10, "bold"),
            bg="white",
            fg="#455A64"
        ).pack(
            anchor="w",
            padx=20,
            pady=(5, 5)
        )

        self.city_combo = ttk.Combobox(
            left,
            textvariable=self.city_var,
            values=self.cities,
            state="readonly",
            width=30
        )
        self.city_combo.pack(
            padx=20,
            pady=(0, 12)
        )

        # Name

        tk.Label(
            left,
            text="Person Name",
            font=("Segoe UI", 10, "bold"),
            bg="white",
            fg="#455A64"
        ).pack(
            anchor="w",
            padx=20,
            pady=(5, 5)
        )

        tk.Entry(
            left,
            textvariable=self.name_var,
            font=("Segoe UI", 11),
            width=32,
            bd=1,
            relief="solid"
        ).pack(
            padx=20,
            pady=(0, 12),
            ipady=7
        )

        # Address

        tk.Label(
            left,
            text="Address",
            font=("Segoe UI", 10, "bold"),
            bg="white",
            fg="#455A64"
        ).pack(
            anchor="w",
            padx=20,
            pady=(5, 5)
        )

        tk.Entry(
            left,
            textvariable=self.addr_var,
            font=("Segoe UI", 11),
            width=32,
            bd=1,
            relief="solid"
        ).pack(
            padx=20,
            pady=(0, 12),
            ipady=7
        )

        # Phone

        tk.Label(
            left,
            text="Phone Number",
            font=("Segoe UI", 10, "bold"),
            bg="white",
            fg="#455A64"
        ).pack(
            anchor="w",
            padx=20,
            pady=(5, 5)
        )

        tk.Entry(
            left,
            textvariable=self.phone_var,
            font=("Segoe UI", 11),
            width=32,
            bd=1,
            relief="solid"
        ).pack(
            padx=20,
            pady=(0, 20),
            ipady=7
        )

        # Add button

        tk.Button(
            left,
            text="ADD CONTACT",
            command=self.insertFun,
            font=("Segoe UI", 10, "bold"),
            bg="#1976D2",
            fg="white",
            activebackground="#1565C0",
            activeforeground="white",
            bd=0,
            cursor="hand2",
            width=28,
            pady=10
        ).pack(
            padx=20,
            pady=(0, 10)
        )

        # Clear button

        tk.Button(
            left,
            text="CLEAR FIELDS",
            command=self.clear_fields,
            font=("Segoe UI", 10, "bold"),
            bg="#ECEFF1",
            fg="#263238",
            activebackground="#CFD8DC",
            bd=0,
            cursor="hand2",
            width=28,
            pady=10
        ).pack(
            padx=20,
            pady=(0, 20)
        )

        # ================= RIGHT PANEL =================

        right = tk.Frame(
            main,
            bg="white",
            bd=1,
            relief="solid"
        )
        right.pack(
            side="left",
            fill="both",
            expand=True
        )

        # Search title

        search_title = tk.Label(
            right,
            text="Search Contact",
            font=("Segoe UI", 16, "bold"),
            bg="white",
            fg="#263238"
        )
        search_title.pack(
            anchor="w",
            padx=20,
            pady=(20, 15)
        )

        # Search controls

        search_frame = tk.Frame(
            right,
            bg="white"
        )
        search_frame.pack(
            fill="x",
            padx=20
        )

        tk.Label(
            search_frame,
            text="City",
            font=("Segoe UI", 10, "bold"),
            bg="white",
            fg="#455A64"
        ).grid(
            row=0,
            column=0,
            padx=(0, 8),
            pady=5
        )

        self.search_city_combo = ttk.Combobox(
            search_frame,
            textvariable=self.search_city_var,
            values=self.cities,
            state="readonly",
            width=15
        )
        self.search_city_combo.grid(
            row=0,
            column=1,
            padx=(0, 15)
        )

        tk.Label(
            search_frame,
            text="Person Name",
            font=("Segoe UI", 10, "bold"),
            bg="white",
            fg="#455A64"
        ).grid(
            row=0,
            column=2,
            padx=(0, 8)
        )

        tk.Entry(
            search_frame,
            textvariable=self.search_name_var,
            font=("Segoe UI", 10),
            width=22,
            bd=1,
            relief="solid"
        ).grid(
            row=0,
            column=3,
            padx=(0, 15),
            ipady=6
        )

        tk.Button(
            search_frame,
            text="SEARCH",
            command=self.searchFun,
            font=("Segoe UI", 9, "bold"),
            bg="#1976D2",
            fg="white",
            bd=0,
            cursor="hand2",
            padx=15,
            pady=7
        ).grid(
            row=0,
            column=4,
            padx=5
        )

        tk.Button(
            search_frame,
            text="DELETE",
            command=self.delFun,
            font=("Segoe UI", 9, "bold"),
            bg="#D32F2F",
            fg="white",
            bd=0,
            cursor="hand2",
            padx=15,
            pady=7
        ).grid(
            row=0,
            column=5,
            padx=5
        )

        tk.Button(
            search_frame,
            text="SHOW ALL",
            command=self.show_all,
            font=("Segoe UI", 9, "bold"),
            bg="#388E3C",
            fg="white",
            bd=0,
            cursor="hand2",
            padx=15,
            pady=7
        ).grid(
            row=0,
            column=6,
            padx=5
        )

        # ================= TABLE =================

        table_frame = tk.Frame(
            right,
            bg="white"
        )
        table_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        columns = (
            "city",
            "id",
            "name",
            "addr",
            "phone"
        )

        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )

        self.tree.heading(
            "city",
            text="CITY"
        )

        self.tree.heading(
            "id",
            text="ID"
        )

        self.tree.heading(
            "name",
            text="PERSON NAME"
        )

        self.tree.heading(
            "addr",
            text="ADDRESS"
        )

        self.tree.heading(
            "phone",
            text="PHONE NUMBER"
        )

        self.tree.column(
            "city",
            width=100,
            anchor="center"
        )

        self.tree.column(
            "id",
            width=130,
            anchor="center"
        )

        self.tree.column(
            "name",
            width=160
        )

        self.tree.column(
            "addr",
            width=200
        )

        self.tree.column(
            "phone",
            width=140,
            anchor="center"
        )

        vertical_scroll = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.tree.yview
        )

        horizontal_scroll = ttk.Scrollbar(
            table_frame,
            orient="horizontal",
            command=self.tree.xview
        )

        self.tree.configure(
            yscrollcommand=vertical_scroll.set,
            xscrollcommand=horizontal_scroll.set
        )

        self.tree.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        vertical_scroll.grid(
            row=0,
            column=1,
            sticky="ns"
        )

        horizontal_scroll.grid(
            row=1,
            column=0,
            sticky="ew"
        )

        table_frame.grid_rowconfigure(
            0,
            weight=1
        )

        table_frame.grid_columnconfigure(
            0,
            weight=1
        )

    # ---------------------------------------------------------
    # ADD CONTACT
    # ---------------------------------------------------------

    def insertFun(self):

        city = self.city_var.get()
        name = self.name_var.get().strip()
        addr = self.addr_var.get().strip()
        phone = self.phone_var.get().strip()

        if city == "":
            messagebox.showwarning(
                "Missing Information",
                "Please select a city."
            )
            return

        if name == "":
            messagebox.showwarning(
                "Missing Information",
                "Please enter the person's name."
            )
            return

        if addr == "":
            messagebox.showwarning(
                "Missing Information",
                "Please enter the address."
            )
            return

        if phone == "":
            messagebox.showwarning(
                "Missing Information",
                "Please enter the phone number."
            )
            return

        try:

            self.dbFun()

            # Generate a unique 15-character ID
            contact_id = uuid.uuid4().hex[:15]

            query = f"""
                INSERT INTO `{city}` (id, name, addr, phNo)
                VALUES (%s, %s, %s, %s)
            """

            self.cur.execute(
                query,
                (contact_id, name, addr, phone)
            )

            self.con.commit()

            self.con.close()

            messagebox.showinfo(
                "Success",
                "Contact added successfully!"
            )

            self.clear_fields()
            self.show_all()

        except Exception as e:

            try:
                self.con.close()
            except:
                pass

            messagebox.showerror(
                "Database Error",
                str(e)
            )

    # ---------------------------------------------------------
    # SEARCH CONTACT
    # ---------------------------------------------------------

    def searchFun(self):

        city = self.search_city_var.get()
        name = self.search_name_var.get().strip()

        if city == "":
            messagebox.showwarning(
                "Missing Information",
                "Please select a city."
            )
            return

        if name == "":
            messagebox.showwarning(
                "Missing Information",
                "Please enter a person's name."
            )
            return

        try:

            self.dbFun()

            query = f"""
                SELECT id, name, addr, phNo
                FROM `{city}`
                WHERE name LIKE %s
            """

            self.cur.execute(
                query,
                (f"%{name}%",)
            )

            rows = self.cur.fetchall()

            self.con.close()

            self.clear_table()

            for row in rows:

                self.tree.insert(
                    "",
                    "end",
                    values=(
                        city,
                        row[0],
                        row[1],
                        row[2],
                        row[3]
                    )
                )

            if not rows:

                messagebox.showinfo(
                    "Search Result",
                    "No contact found."
                )

        except Exception as e:

            try:
                self.con.close()
            except:
                pass

            messagebox.showerror(
                "Database Error",
                str(e)
            )

    # ---------------------------------------------------------
    # DELETE CONTACT
    # ---------------------------------------------------------

    def delFun(self):

        city = self.search_city_var.get()
        name = self.search_name_var.get().strip()

        if city == "":
            messagebox.showwarning(
                "Missing Information",
                "Please select a city."
            )
            return

        if name == "":
            messagebox.showwarning(
                "Missing Information",
                "Please enter the person's name."
            )
            return

        confirm = messagebox.askyesno(
            "Confirm Delete",
            f"Are you sure you want to delete contacts named '{name}'?"
        )

        if not confirm:
            return

        try:

            self.dbFun()

            query = f"""
                DELETE FROM `{city}`
                WHERE name = %s
            """

            self.cur.execute(
                query,
                (name,)
            )

            deleted = self.cur.rowcount

            self.con.commit()
            self.con.close()

            if deleted > 0:

                messagebox.showinfo(
                    "Success",
                    f"{deleted} contact(s) deleted successfully."
                )

            else:

                messagebox.showinfo(
                    "Delete",
                    "No matching contact found."
                )

            self.show_all()

        except Exception as e:

            try:
                self.con.close()
            except:
                pass

            messagebox.showerror(
                "Database Error",
                str(e)
            )

    # ---------------------------------------------------------
    # SHOW ALL CONTACTS
    # ---------------------------------------------------------

    def show_all(self):

        try:

            self.dbFun()

            self.clear_table()

            for city in self.cities:

                query = f"""
                    SELECT id, name, addr, phNo
                    FROM `{city}`
                """

                self.cur.execute(query)

                rows = self.cur.fetchall()

                for row in rows:

                    self.tree.insert(
                        "",
                        "end",
                        values=(
                            city,
                            row[0],
                            row[1],
                            row[2],
                            row[3]
                        )
                    )

            self.con.close()

        except Exception as e:

            try:
                self.con.close()
            except:
                pass

            messagebox.showerror(
                "Database Error",
                str(e)
            )

    # ---------------------------------------------------------
    # CLEAR TABLE
    # ---------------------------------------------------------

    def clear_table(self):

        for item in self.tree.get_children():
            self.tree.delete(item)

    # ---------------------------------------------------------
    # CLEAR INPUT FIELDS
    # ---------------------------------------------------------

    def clear_fields(self):

        self.city_var.set("")
        self.name_var.set("")
        self.addr_var.set("")
        self.phone_var.set("")


# =============================================================
# MAIN PROGRAM
# =============================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = PhoneBook(root)

    root.mainloop()