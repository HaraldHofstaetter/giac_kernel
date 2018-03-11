from ipykernel.kernelbase import Kernel
from pexpect import replwrap, EOF
import pexpect

__version__ = '0.1.0'

def remove_comments(s):
    i = s.find('//')
    if i>=0:
        s = s[0:i]
    return s


class GiacKernel(Kernel):
    implementation = 'Giac'
    implementation_version = __version__ 
    language = 'giac'
    language_version = '1.2.2'
    language_info = {
        'name': 'giac',
        'mimetype': 'text/plain',
        'file_extension': '.xws',
    }
    banner = "Giac kernel"

    def __init__(self, **kwargs):
        Kernel.__init__(self, **kwargs)
        self.latex = False
        self._start_giac()    

    def _start_giac(self):
        self.giacwrapper = replwrap.REPLWrapper('giac', u'>> ', None)

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        code = "".join([remove_comments(x)+' ' for x in code.split('\n')])
        if self.latex:
            code = 'latex('+code.strip()+')'
            output = self.giacwrapper.run_command(code, timeout=None)
            if not silent:
                output = '$'+output[1:output.rfind('"\r\n//')]+'$'
                data = {'text/latex': output}
                content = {'data': data}
                self.send_response(self.iopub_socket, 'display_data', content)
        else:
            output = self.giacwrapper.run_command(code, timeout=None)
            if not silent:
                output = output[:output.rfind('\r\n//')]
                content = {'name': 'stdout', 'text': output}                
                self.send_response(self.iopub_socket, 'stream', content)

        return {'status': 'ok',
                # The base class increments the execution count
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }
               
