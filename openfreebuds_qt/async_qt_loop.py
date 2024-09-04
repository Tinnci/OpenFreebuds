import asyncio
import sys

from PyQt6.QtWidgets import QApplication
from qasync import QEventLoop


def qt_app_entrypoint(WidgetClass):
    def _wrapper(callback):
        def _inner():
            app = QApplication(sys.argv)
            event_loop = QEventLoop(app)
            asyncio.set_event_loop(event_loop)

            app_close_event = asyncio.Event()
            app.aboutToQuit.connect(app_close_event.set)

            widget = WidgetClass(app)
            event_loop.create_task(callback(app, widget))
            event_loop.run_until_complete(app_close_event.wait())
            event_loop.close()

        return _inner

    return _wrapper
