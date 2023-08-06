import gi
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.0')
from gi.repository import Gtk, WebKit2

class HTMLViewer(Gtk.Window):
    def __init__(self):
        super().__init__(title="Simple HTML Viewer")  # Set window title

        self.set_default_size(800, 600)  # Set default window size

        self.init_ui()

    def init_ui(self):
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)  # Create a vertical box
        self.add(self.box)

        self.init_text_area()
        self.init_web_view()

        self.show_all()

    def init_text_area(self):
        scrolled_window = Gtk.ScrolledWindow()  # Create a scrolled window
        self.textarea = Gtk.TextView()  # Create a text area
        self.textarea.connect("key-release-event", self.update_output)  # Connect key-release event to the update function
        self.textarea.set_size_request(-1, 300)  # Set a fixed height
        scrolled_window.add(self.textarea)  # Add TextView to ScrolledWindow
        self.box.pack_start(scrolled_window, True, True, 0)  # Add ScrolledWindow to the box

    def init_web_view(self):
        self.webview = WebKit2.WebView()  # Create a WebView
        self.box.pack_start(self.webview, True, True, 0)  # Add WebView to the box

    def update_output(self, widget, event):
        html_code = self.textarea.get_buffer().get_text(
            self.textarea.get_buffer().get_start_iter(), self.textarea.get_buffer().get_end_iter(), False
        )  # Get text from TextView
        self.webview.load_html(html_code, "file:///")  # Load HTML content into WebView

if __name__ == "__main__":
    win = HTMLViewer()
    win.connect("destroy", Gtk.main_quit)  # Connect function to window close
    Gtk.main()  # Run event loop