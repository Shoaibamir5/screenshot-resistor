from pynput import keyboard

class KeyboardMonitor:
    def __init__(self, callback):
        self.callback = callback
        self.listener = None
        self.keys_pressed = set()
        self.cmd_pressed = False
        self.shift_pressed = False
        self.s_pressed = False

    def on_press(self, key):
        self.keys_pressed.add(key)
        
        # Track individual key states
        if key in [keyboard.Key.cmd, keyboard.Key.cmd_r]:
            self.cmd_pressed = True
        elif key == keyboard.Key.shift:
            self.shift_pressed = True
        elif hasattr(key, 'char') and key.char and key.char.lower() == 's':
            self.s_pressed = True

        # Check for PrintScreen
        if key == keyboard.Key.print_screen:
            self.callback("PrintScreen")
        
        # Check for Win+Shift+S combination
        if self.cmd_pressed and self.shift_pressed and self.s_pressed:
            self.callback("SnippingTool Shortcut")
            # Reset the S key to prevent multiple triggers
            self.s_pressed = False
        
        # Check for Alt+PrintScreen
        if keyboard.Key.alt in self.keys_pressed and key == keyboard.Key.print_screen:
            self.callback("Alt+PrintScreen")

    def on_release(self, key):
        if key in self.keys_pressed:
            self.keys_pressed.remove(key)
            
        # Update individual key states
        if key in [keyboard.Key.cmd, keyboard.Key.cmd_r]:
            self.cmd_pressed = False
        elif key == keyboard.Key.shift:
            self.shift_pressed = False
        elif hasattr(key, 'char') and key.char and key.char.lower() == 's':
            self.s_pressed = False

    def start(self):
        self.listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release
        )
        self.listener.daemon = True
        self.listener.start()

    def stop(self):
        if self.listener:
            self.listener.stop()