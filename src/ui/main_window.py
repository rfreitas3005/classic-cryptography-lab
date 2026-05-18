"""Main application window and UI."""

import tkinter as tk
from tkinter import ttk, messagebox

from src.ciphers import (
    CaesarCipher,
    MonoalphabeticCipher,
    PlayfairCipher,
    VigenereCipher,
    VernamCipher,
    TranspositionCipher,
)
from src.ui.styles import Theme, Fonts, Spacing


class LabCriptoApp:
    """Main application window."""

    def __init__(self, root):
        """Initialize the application."""
        self.root = root
        self.root.title("Lab Cripto 🔐")
        self.root.geometry("900x800")
        self.root.configure(bg=Theme.BG_PRIMARY)

        # Initialize cipher instances
        self.ciphers = {
            "Caesar": CaesarCipher(),
            "Monoalphabetic": MonoalphabeticCipher(),
            "Playfair": PlayfairCipher(),
            "Vigenère": VigenereCipher(),
            "Vernam / OTP": VernamCipher(),
            "Transposition": TranspositionCipher(),
        }

        self.setup_ui()

    def setup_ui(self):
        """Setup the user interface."""
        # Configure ttk style
        self._setup_styles()

        # Create main layout with content and sidebar
        main_container = tk.Frame(self.root, bg=Theme.BG_PRIMARY)
        main_container.pack(fill="both", expand=True)

        # Content area (left side)
        content_frame = tk.Frame(main_container, bg=Theme.BG_PRIMARY)
        content_frame.pack(
            side="left",
            fill="both",
            expand=True,
            padx=Spacing.PADDING_LARGE,
            pady=Spacing.PADDING_LARGE,
        )

        # Header
        self._create_header(content_frame)

        # Input section
        self._create_input_section(content_frame)

        # Button
        self._create_button(content_frame)

        # Results section
        self._create_results_section(content_frame)

        # Footer
        self._create_footer(content_frame)

        # Sidebar (right side)
        self._create_sidebar(main_container)

    def _setup_styles(self):
        """Configure ttk styles."""
        style = ttk.Style()
        style.theme_use("clam")

        # Combobox styling
        style.configure(
            "TCombobox",
            fieldbackground=Theme.INPUT_BG,
            background=Theme.INPUT_BG,
            foreground=Theme.FG_PRIMARY,
        )

    def _create_header(self, parent):
        """Create header section."""
        header_frame = tk.Frame(parent, bg=Theme.BG_PRIMARY)
        header_frame.pack(fill="x", pady=(0, Spacing.PADDING_MEDIUM))

        title = tk.Label(
            header_frame,
            text="🔐 Cryptography Laboratory",
            font=Fonts.TITLE,
            bg=Theme.BG_PRIMARY,
            fg=Theme.ACCENT_BLUE,
        )
        title.pack(anchor="w")

        subtitle = tk.Label(
            header_frame,
            text="Learn classic cipher algorithms with step-by-step calculations",
            font=Fonts.SMALL,
            bg=Theme.BG_PRIMARY,
            fg=Theme.FG_SECONDARY,
        )
        subtitle.pack(anchor="w", pady=(5, 0))

    def _create_input_section(self, parent):
        """Create input fields section."""
        input_frame = tk.Frame(parent, bg=Theme.BG_PRIMARY)
        input_frame.pack(fill="x", pady=(0, Spacing.PADDING_MEDIUM))

        # Cipher selection
        label = tk.Label(
            input_frame,
            text="Choose Cipher:",
            font=Fonts.LABEL_BOLD,
            bg=Theme.BG_PRIMARY,
            fg=Theme.FG_PRIMARY,
        )
        label.pack(anchor="w", pady=(0, 5))

        self.cipher_combo = ttk.Combobox(
            input_frame,
            values=list(self.ciphers.keys()),
            state="readonly",
            width=45,
            font=Fonts.INPUT,
        )
        self.cipher_combo.current(0)
        self.cipher_combo.pack(fill="x", pady=(0, Spacing.PADDING_MEDIUM))
        self.cipher_combo.bind("<<ComboboxSelected>>", self._on_cipher_changed)

        # Message input
        label = tk.Label(
            input_frame,
            text="Message to Encrypt:",
            font=Fonts.LABEL_BOLD,
            bg=Theme.BG_PRIMARY,
            fg=Theme.FG_PRIMARY,
        )
        label.pack(anchor="w", pady=(0, 5))

        self.message_entry = tk.Entry(
            input_frame,
            font=Fonts.INPUT,
            bg=Theme.INPUT_BG,
            fg=Theme.FG_PRIMARY,
            insertbackground=Theme.FG_PRIMARY,
            relief="solid",
            borderwidth=1,
        )
        self.message_entry.pack(fill="x", pady=(0, Spacing.PADDING_MEDIUM), ipady=8)

        # Key input
        self.key_label = tk.Label(
            input_frame,
            text="Displacement (k) [Example: 3]:",
            font=Fonts.LABEL_BOLD,
            bg=Theme.BG_PRIMARY,
            fg=Theme.FG_PRIMARY,
        )
        self.key_label.pack(anchor="w", pady=(0, 5))

        self.key_entry = tk.Entry(
            input_frame,
            font=Fonts.INPUT,
            bg=Theme.INPUT_BG,
            fg=Theme.FG_PRIMARY,
            insertbackground=Theme.FG_PRIMARY,
            relief="solid",
            borderwidth=1,
        )
        self.key_entry.pack(fill="x", ipady=8)

    def _create_button(self, parent):
        """Create encrypt button."""
        button_frame = tk.Frame(parent, bg=Theme.BG_PRIMARY)
        button_frame.pack(fill="x", pady=Spacing.PADDING_MEDIUM)

        self.encrypt_button = tk.Button(
            button_frame,
            text="🔒 Encrypt Message",
            command=self._encrypt,
            bg=Theme.BUTTON_BG,
            fg=Theme.BUTTON_FG,
            font=Fonts.BUTTON,
            relief="flat",
            activebackground=Theme.BUTTON_HOVER,
            activeforeground=Theme.BUTTON_FG,
            cursor="hand2",
            padx=20,
            pady=10,
        )
        self.encrypt_button.pack(fill="x")

    def _create_results_section(self, parent):
        """Create results display section."""
        results_frame = tk.Frame(parent, bg=Theme.BG_PRIMARY)
        results_frame.pack(fill="both", expand=True, pady=(Spacing.PADDING_MEDIUM, 0))

        label = tk.Label(
            results_frame,
            text="Analysis & Results:",
            font=Fonts.LABEL_BOLD,
            bg=Theme.BG_PRIMARY,
            fg=Theme.FG_PRIMARY,
        )
        label.pack(anchor="w", pady=(0, 5))

        # Results text box
        self.result_text = tk.Text(
            results_frame,
            font=Fonts.TERMINAL,
            bg=Theme.TERMINAL_BG,
            fg=Theme.TERMINAL_FG,
            relief="solid",
            borderwidth=1,
            padx=12,
            pady=10,
            wrap="word",
        )
        self.result_text.pack(fill="both", expand=True, pady=(0, Spacing.PADDING_MEDIUM))
        self.result_text.config(state="disabled")

        # Scrollbar
        scrollbar = tk.Scrollbar(
            results_frame, command=self.result_text.yview, bg=Theme.BG_SECONDARY
        )
        scrollbar.pack(side="right", fill="y")
        self.result_text.config(yscrollcommand=scrollbar.set)

    def _create_footer(self, parent):
        """Create footer section."""
        footer_frame = tk.Frame(parent, bg=Theme.BG_PRIMARY)
        footer_frame.pack(fill="x", pady=(Spacing.PADDING_SMALL, 0))

        footer = tk.Label(
            footer_frame,
            text="Educational Purpose Only",
            font=Fonts.SMALL,
            bg=Theme.BG_PRIMARY,
            fg=Theme.FG_MUTED,
        )
        footer.pack(anchor="e")

    def _create_sidebar(self, parent):
        """Create information sidebar."""
        sidebar = tk.Frame(
            parent,
            bg=Theme.BG_SECONDARY,
            width=180,
        )
        sidebar.pack(side="right", fill="y", padx=(10, 0))
        sidebar.pack_propagate(False)

        # Sidebar title
        title = tk.Label(
            sidebar,
            text="Lab Cripto",
            font=("Segoe UI", 16, "bold"),
            bg=Theme.BG_SECONDARY,
            fg=Theme.ACCENT_BLUE,
            pady=10,
        )
        title.pack()

        # Divider
        divider = tk.Frame(sidebar, height=1, bg=Theme.BG_TERTIARY)
        divider.pack(fill="x", padx=10, pady=5)

        # Version
        version_label = tk.Label(
            sidebar,
            text="Version",
            font=("Segoe UI", 9, "bold"),
            bg=Theme.BG_SECONDARY,
            fg=Theme.FG_SECONDARY,
        )
        version_label.pack(anchor="w", padx=15, pady=(10, 2))

        version = tk.Label(
            sidebar,
            text="v1.0.0",
            font=("Segoe UI", 10),
            bg=Theme.BG_SECONDARY,
            fg=Theme.ACCENT_GREEN,
        )
        version.pack(anchor="w", padx=15)

        # Author
        author_label = tk.Label(
            sidebar,
            text="Author",
            font=("Segoe UI", 9, "bold"),
            bg=Theme.BG_SECONDARY,
            fg=Theme.FG_SECONDARY,
        )
        author_label.pack(anchor="w", padx=15, pady=(15, 2))

        author = tk.Label(
            sidebar,
            text="Ricardo Freitas",
            font=("Segoe UI", 10),
            bg=Theme.BG_SECONDARY,
            fg=Theme.FG_PRIMARY,
            wraplength=150,
            justify="left",
        )
        author.pack(anchor="w", padx=15)

        # Purpose
        purpose_label = tk.Label(
            sidebar,
            text="Purpose",
            font=("Segoe UI", 9, "bold"),
            bg=Theme.BG_SECONDARY,
            fg=Theme.FG_SECONDARY,
        )
        purpose_label.pack(anchor="w", padx=15, pady=(15, 2))

        purpose = tk.Label(
            sidebar,
            text="Educational Tool",
            font=("Segoe UI", 9),
            bg=Theme.BG_SECONDARY,
            fg=Theme.FG_PRIMARY,
            wraplength=150,
            justify="left",
        )
        purpose.pack(anchor="w", padx=15)

        # Ciphers count
        ciphers_label = tk.Label(
            sidebar,
            text="Ciphers",
            font=("Segoe UI", 9, "bold"),
            bg=Theme.BG_SECONDARY,
            fg=Theme.FG_SECONDARY,
        )
        ciphers_label.pack(anchor="w", padx=15, pady=(15, 2))

        ciphers = tk.Label(
            sidebar,
            text="6 Algorithms",
            font=("Segoe UI", 10),
            bg=Theme.BG_SECONDARY,
            fg=Theme.ACCENT_TEAL,
        )
        ciphers.pack(anchor="w", padx=15)

        # Bottom divider
        bottom_divider = tk.Frame(sidebar, height=1, bg=Theme.BG_TERTIARY)
        bottom_divider.pack(fill="x", padx=10, pady=(15, 10))

    def _on_cipher_changed(self, event=None):
        """Update key label when cipher changes."""
        cipher_name = self.cipher_combo.get()

        key_labels = {
            "Caesar": "Displacement (k) [Example: 3]:",
            "Monoalphabetic": "Cipher Alphabet [26 shuffled letters]:",
            "Playfair": "Keyword [Example: UTAD]:",
            "Vigenère": "Keyword [Example: UTAD]:",
            "Vernam / OTP": "Key [Same length as message]:",
            "Transposition": "Keyword [Example: UTAD]:",
        }

        self.key_label.config(text=key_labels.get(cipher_name, "Key:"))

        # Clear results
        self.result_text.config(state="normal")
        self.result_text.delete(1.0, tk.END)
        self.result_text.config(state="disabled")

    def _encrypt(self):
        """Encrypt the message with selected cipher."""
        message = self.message_entry.get()
        key = self.key_entry.get()
        cipher_name = self.cipher_combo.get()

        if not message:
            messagebox.showwarning(
                "Input Required", "Please enter a message to encrypt!"
            )
            return

        try:
            cipher = self.ciphers[cipher_name]
            analysis = cipher.get_analysis(message, key)

            # Display results
            self.result_text.config(state="normal")
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, analysis)
            self.result_text.config(state="disabled")

        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
        except Exception as e:
            messagebox.showerror("Critical Error", f"An unexpected error occurred:\n{e}")


def main():
    """Launch the application."""
    root = tk.Tk()
    app = LabCriptoApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
