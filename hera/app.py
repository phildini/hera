import asyncio
import subprocess
import toga
from toga.style.pack import Pack, ROW, CENTER, COLUMN
import time
import sys
import os
from pathlib import Path
from urllib.parse import quote

class Notebook(toga.Document):
    def __init__(self, filename, app):
        super().__init__(filename=filename, document_type='Jupyter Notebook', app=app)

        self.window = toga.Window(title=filename, size=(768,768))
        self.window.on_close = self.close_window
        self.webview = toga.WebView(style=Pack(flex=1))
        self.window.content = self.webview

    def close_window(self):
        self.proc.kill()

    def read(self):
        asyncio.ensure_future(self.start_jupyter(self.filename))

    def show(self):
        self.window.show()

    async def start_jupyter(self, filename):
        filename = Path(filename)
        command = '{} -m notebook --NotebookApp.token="" --NotebookApp.open_browser=False --notebook-dir="{}"'.format(sys.executable, filename.parent)
        self.proc = await asyncio.create_subprocess_shell(
            command,
            stdin=None,
            stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE,
        )
        line = await self.proc.stderr.readline()
        while line:
            line = line.strip().decode('utf-8')
            if 'http' in line:
                url = line.split(' ')[-1]
                url = "{}notebooks/{}".format(url, quote(filename.name))
                self.webview.url = url
            line = await self.proc.stderr.readline()


class Hera(toga.DocumentApp):

    def __init__(self):
        resource_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        super().__init__(
            'Hera',
            app_id='net.phildini.Hera',
            icon=toga.Icon(os.path.join(resource_dir, 'Hera.icns')),
            document_types={'ipynb': Notebook},
        )

    def startup(self):
        pass

def main():
    Hera().main_loop()


if __name__ == '__main__':
    main()