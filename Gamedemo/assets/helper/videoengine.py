from math import e


def block_task_manager():
    """Blockiert Task-Manager und andere System-Tastenkombinationen 😈"""
    import win32api
    import win32con
    
    def hook_callback(nCode, wParam, lParam):
        if nCode >= 0:
            # Hole Tastatur-Event
            kb = win32api.GetKeyState
            
            # STRG+ALT+ENTF blockieren (Task Manager)
            if (kb(win32con.VK_CONTROL) & 0x8000) and (kb(win32con.VK_MENU) & 0x8000) and (kb(win32con.VK_DELETE) & 0x8000):
                return 1  # Blockiere!
            
            # STRG+SHIFT+ESC blockieren (Task Manager direkt)
            if (kb(win32con.VK_CONTROL) & 0x8000) and (kb(win32con.VK_SHIFT) & 0x8000) and (kb(win32con.VK_ESCAPE) & 0x8000):
                return 1
            
            # ALT+TAB blockieren (Fenster wechseln)
            if (kb(win32con.VK_MENU) & 0x8000) and (kb(win32con.VK_TAB) & 0x8000):
                return 1
            
            # ALT+ESC blockieren
            if (kb(win32con.VK_MENU) & 0x8000) and (kb(win32con.VK_ESCAPE) & 0x8000):
                return 1
            
            # STRG+C blockieren
            if (kb(win32con.VK_CONTROL) & 0x8000) and (kb(0x43) & 0x8000):  # C = 0x43
                return 1
            
            # ESC alleine blockieren
            if kb(win32con.VK_ESCAPE) & 0x8000:
                return 1
        
        return win32api.CallNextHookEx(None, nCode, wParam, lParam)
    
    try:
        import win32gui
        hm = win32api.GetModuleHandle(None)
        hook_id = win32api.SetWindowsHookEx(win32con.WH_KEYBOARD_LL, hook_callback, hm, 0)
        return hook_id
    except:
        print("⚠️ Warnung: Konnte Tastatur-Hook nicht setzen")
        return None


def fake_shutdown_sequence():
    import tkweb as tk, time

    win = tk.Tk()
    win.configure(bg="black")
    win.attributes("-fullscreen", True)
    win.attributes("-topmost", True)

    label = tk.Label(
        win,
        text="System shutdown in 10 seconds…",
        fg="white",
        bg="black",
        font=("Segoe UI", 28)
    )
    label.pack(expand=True)

    for i in range(10, 0, -1):
        label.config(text=f"System shutdown in {i} seconds…")
        win.update()
        time.sleep(1)

    # Dramatische Pause 😈
    label.config(text="Shutting down…")
    win.update()
    time.sleep(2)

    # Fake-Abbruch
    label.config(text="Shutdown aborted.")
    win.update()
    time.sleep(2)

    # Extra-Gaslighting 😭
    label.config(text="Restoring system state…")
    win.update()
    time.sleep(2)

    win.destroy()


def play_fullscreen_video(video_path):
    """Spielt Video im Vollbild ab mit VLC - RICHTIG SCARY! 😈
    
    Nutzt VLC statt pygame, damit pygame für dein Spiel (soundengine.py) frei bleibt!
    """
    import subprocess
    import os
    
    try:
        # Blockiere System-Tastenkombinationen
        hook_id = block_task_manager()
        
        # VLC Pfade (versuche mehrere mögliche Installationsorte)
        possible_vlc_paths = [
            r"C:\Program Files\VideoLAN\VLC\vlc.exe",
            r"C:\Program Files (x86)\VideoLAN\VLC\vlc.exe",
            "vlc",  # Falls in PATH
        ]
        
        vlc_path = None
        for path in possible_vlc_paths:
            if path == "vlc" or os.path.exists(path):
                vlc_path = path
                break
        
        if not vlc_path:
            print("❌ FEHLER: VLC nicht gefunden!")
            print("Installiere VLC von: https://www.videolan.org/vlc/")
            return False
        
        # Starte VLC im Vollbild mit allen scary options
        vlc_args = [
            vlc_path,
            video_path,
            "--fullscreen",           # Vollbild
            "--no-video-title-show",  # Kein Titel
            "--no-osd",               # Kein On-Screen-Display
            "--play-and-exit",        # Schließe nach Abspielen
            "--no-qt-privacy-ask",    # Keine Privacy-Fragen
            "--qt-start-minimized",   # Minimiert starten
            "--no-qt-system-tray",    # Kein System Tray
            "--no-video-deco",        # Keine Fenster-Dekoration
            "--no-embedded-video",    # Kein embedded player
        ]
        
        print(f"🎬 Starte VLC im Vollbild...")
        
        # Starte VLC und warte bis es fertig ist
        process = subprocess.Popen(
            vlc_args,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        
        # Warte bis VLC fertig ist (Video zu Ende)
        process.wait()
        
        print("✅ Video fertig!")
        
        # Entferne Tastatur-Hook
        if hook_id:
            try:
                import win32api
                win32api.UnhookWindowsHookEx(hook_id)
            except:
                pass
        
        return True
        
    except FileNotFoundError:
        print("❌ FEHLER: VLC nicht gefunden oder nicht ausführbar!")
        print("Installiere VLC von: https://www.videolan.org/vlc/")
        return False
        
    except Exception as e:
        print(f"❌ Fehler beim Video-Abspielen: {e}")
        # Entferne Hook bei Fehler
        if 'hook_id' in locals() and hook_id:
            try:
                import win32api
                win32api.UnhookWindowsHookEx(hook_id)
            except:
                pass
        return False


def runhack():
    import os, time, sys, tkweb as tk
    from tkweb import messagebox

    # 1) GUI-Warnung ZUERST! 🚨
    root = tk.Tk()
    root.withdraw()

    messagebox.showerror(
        "Security Violation",
        "Nice try, pirate.\n\n"
        "Diese Kopie ist nicht autorisiert.\n\n"
        "Ein Vorfallbericht wurde erstellt.\n\n"
        "Der Computer wird jetzt heruntergefahren."
    )
    
    root.destroy()  # Schließe tkweb komplett
    time.sleep(0.5)  # Kurze Pause

    # 2) Fake-Hack-Video 😈 - NACH der Messagebox!
    try:
        # Relativer Pfad vom sourcecode-Ordner aus (eine Ebene hoch, dann zu assets)
        video = os.path.join(os.path.dirname(__file__), "..", "..", "assets", "video", "inital-start-up.webm")
        video = os.path.abspath(video)  # Konvertiere zu absolutem Pfad
        
        # Prüfe ob Video existiert
        if os.path.exists(video):
            print(f"📁 Spiele Video ab: {video}")
            success = play_fullscreen_video(video)  # Vollbild-Video mit VLC!
            
            if not success:
                print("⚠️ Fallback: Öffne mit Standard-Player...")
                os.startfile(video)
                time.sleep(5)  # Warte länger für externen Player
        else:
            print(f"❌ FEHLER: Video nicht gefunden: {video}")
            print(f"📂 Aktuelle Position: {os.path.dirname(__file__)}")
            
    except Exception as e:
        print(f"❌ Fehler beim Abspielen des Videos: {e}")

    time.sleep(1)  # Kurze Pause nach Video

    # 3) Fake-Shutdown-Sequenz 💀
    fake_shutdown_sequence()

    # 4) Exit 😌
    sys.exit(1)
if __name__ == "__main__":
    runhack()