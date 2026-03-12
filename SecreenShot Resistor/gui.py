import tkinter as tk
from tkinter import Label, Button, Checkbutton, IntVar
import threading
import time
import psutil

from plyer import notification
from keymonitor import KeyboardMonitor


class ScreenshotResistorGUI(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Screenshot Resistor")
        self.geometry("400x350")
        self.resizable(True, True)
        
        # Color scheme
        self.bg_color = "#f0f0f0"
        self.accent_color = "#389A38"
        self.warning_color = "#f44336"
        
        self.configure(bg=self.bg_color)
        
        self.protection_var = IntVar()
        self.overlay = None
        self.notification_enabled = IntVar(value=1)
        
        self.create_widgets()
        
        self.monitor = KeyboardMonitor(self.screenshot_detected)
        self.monitor.start()

        threading.Thread(
            target=self.monitor_snipping_tool,
            daemon=True
        ).start()

    def create_widgets(self):
        Label(
            self,
            text="Screenshot Resistor",
            font=("Arial", 16, "bold"),
            bg=self.bg_color,
            fg=self.accent_color
        ).pack(pady=20)
        
        self.status_label = Label(
            self,
            text="● Protection Disabled",
            font=("Arial", 12, "bold"),
            bg=self.bg_color,
            fg=self.warning_color
        )
        self.status_label.pack(pady=15)
        
        Checkbutton(
            self,
            text="Enable Protection",
            variable=self.protection_var,
            command=self.toggle_protection,
            font=("Arial", 11),
            bg=self.bg_color,
            fg="#333333",
            selectcolor=self.bg_color,
            activebackground=self.bg_color,
            activeforeground=self.accent_color
        ).pack(pady=15)
        
        Button(
            self,
            text="❌ Exit",
            command=self.destroy,
            font=("Arial", 10),
            bg=self.warning_color,
            fg="white",
            relief="flat",
            padx=20,
            pady=8
        ).pack(pady=20)
        
        self.warning_label = Label(
            self,
            text="",
            font=("Arial", 14, "bold"),
            bg="#f0f0f0",
            fg="#FF9800",
            pady=10
        )

    def toggle_protection(self):
        if self.protection_var.get():
            self.status_label.config(
                text="● Protection Enabled",
                fg=self.accent_color
            )
        else:
            self.status_label.config(
                text="● Protection Disabled",
                fg=self.warning_color
            )
            self.remove_overlay()

    def screenshot_detected(self, source="Unknown"):
        if not self.protection_var.get():
            return

        self.status_label.config(
            text=f"⚠ {source} Captured!",
            fg="#f39c12"
        )

        if self.notification_enabled.get():
            notification.notify(
                title="Security Alert",
                message=f"Screenshot attempt detected via {source}",
                timeout=4
            )

        self.apply_overlay()
        self.after(1000, self.remove_overlay)

    def apply_overlay(self):
        if self.overlay:
            return

        x = self.winfo_rootx()
        y = self.winfo_rooty()
        width = self.winfo_width()
        height = self.winfo_height()

        self.overlay = tk.Toplevel(self)
        self.overlay.overrideredirect(True)
        self.overlay.attributes("-topmost", True)
        self.overlay.geometry(f"{width}x{height}+{x}+{y}")
        self.overlay.configure(bg="#000000")

        Label(
            self.overlay,
            text="🚫 SCREEN CAPTURE BLOCKED",
            fg="white",
            bg="#000000",
            font=("Arial", 20, "bold")
        ).pack(expand=True)

    def remove_overlay(self):
        if self.overlay:
            self.overlay.destroy()
            self.overlay = None
            
        if self.protection_var.get():
            self.status_label.config(
                text="● Protection Enabled",
                fg=self.accent_color
            )
            self.show_screenshot_warning()

    def monitor_snipping_tool(self):
        snipping_active = False

        while True:
            found = False

            for process in psutil.process_iter(['name']):
                try:
                    name = process.info['name']
                    if name and "SnippingTool" in name:
                        found = True
                        break
                except:
                    pass

            if found and not snipping_active:
                snipping_active = True

                if self.protection_var.get():
                    self.status_label.config(
                        text="⚠ Snipping Tool Detected!",
                        fg="#f39c12"
                    )

                    if self.notification_enabled.get():
                        notification.notify(
                            title="Security Alert",
                            message="Snipping Tool detected. Window protected.",
                            timeout=4
                        )

                    self.apply_overlay()

            elif not found and snipping_active:
                snipping_active = False
                self.remove_overlay()

                if self.protection_var.get():
                    self.status_label.config(
                        text="● Protection Enabled",
                        fg=self.accent_color
                    )

            time.sleep(1)

    def show_screenshot_warning(self):
        self.warning_label.config(text="📸 Screenshot Detected!")
        self.warning_label.pack(fill="x", pady=(10, 0))


if __name__ == "__main__":
    app = ScreenshotResistorGUI()
    app.mainloop()