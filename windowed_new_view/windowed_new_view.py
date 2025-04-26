from krita import *

class WindowedNewView(Extension):

    def __init__(self, parent):
        super().__init__(parent)

    def createNewView(self):
        # Get the current document and active view
        doc = Krita.instance().activeDocument()

        # When no image is open, break
        if doc is None:
            return

        # Create a new view for current document
        new_view = Krita.instance().activeWindow().addView(doc)

        # Get the active subwindow
        subWindow = new_view.window().qwindow().centralWidget().currentWidget().activeSubWindow()

        # Show windowed subwindow
        subWindow.showNormal()

        # Check the 'Always on top' option
        menu = subWindow.children()[0]
        menu.actions()[5].trigger()

    # Krita.instance() exists, so do any setup work
    def setup(self):
        pass

    # called after setup(self)
    def createActions(self, window):
        action = window.createAction("pykrita_openWindowedNewView", "Open windowed new view")
        action.triggered.connect(self.createNewView)

Krita.instance().addExtension(WindowedNewView(Krita.instance()))