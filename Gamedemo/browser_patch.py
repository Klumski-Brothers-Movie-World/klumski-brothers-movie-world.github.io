# browser_patch.py - Füge das am ANFANG von irgendwas.py ein!

import sys
import os

# === BROWSER COMPATIBILITY PATCHES ===

# 1. Fake __file__ für Pyodide
if '__file__' not in globals():
    __file__ = 'irgendwas.py'

# 2. Fake tkweb für Browser
if os.name == "posix":
    try:
        import tkweb as tk_browser  # ← Geändert zu TkWeb
        from tkweb import messagebox as msg_browser, simpledialog as dlg_browser
        
        # Fake tkweb modules
        sys.modules['tkweb'] = tk_browser
        sys.modules['tkweb.messagebox'] = type('module', (), {
            'showinfo': msg_browser.showinfo,
            'showwarning': msg_browser.showwarning,
            'showerror': msg_browser.showerror,
            'askyesno': msg_browser.askyesno,
        })()
        sys.modules['tkweb.simpledialog'] = type('module', (), {
            'askstring': dlg_browser.askstring,
        })()
        
        print("✅ Browser-Mode aktiv: TkWeb geladen")
    except ImportError as e:
        print(f"❌ Fehler beim Laden von TkWeb: {e}")

# 3. Deaktiviere Packages die nicht im Browser funktionieren
class FakeModule:
    def __getattr__(self, name):
        return lambda *args, **kwargs: None

if os.name == "posix":
    # Diese Module gibt's nicht in Pyodide
    sys.modules['ctypes'] = FakeModule()
    sys.modules['subprocess'] = FakeModule()
    sys.modules['yt_dlp'] = FakeModule()
    
    # Fake YoutubeDL
    class FakeYoutubeDL:
        def __init__(self, *args, **kwargs):
            pass
        def __enter__(self):
            return self
        def __exit__(self, *args):
            pass
        def extract_info(self, *args, **kwargs):
            return {'url': ''}
    
    sys.modules['yt_dlp'].YoutubeDL = FakeYoutubeDL

print("✅ Browser Patches geladen")
