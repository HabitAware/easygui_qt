from PyQt6 import QtGui
from PyQt6 import QtWidgets as qt_widgets


def get_string(prompt="What is your name? ", title="Title",
               default_response="PyQt", app=None):
    """GUI equivalent of input()."""

    if app is None:
        app = qt_widgets.QApplication([])
    app.dialog = qt_widgets.QInputDialog()
    text, ok = app.dialog.getText(None, title, prompt,
                                  qt_widgets.QLineEdit.EchoMode.Normal,
                                  default_response)
    app.quit()
    if ok:
        return text

if __name__ == '__main__':
    print(get_string())
    app2 = qt_widgets.QApplication([])
    print(get_string(app=app2))
