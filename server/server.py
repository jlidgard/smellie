from SimpleXMLRPCServer import SimpleXMLRPCServer
from config import PORT
from exception_handler import str_wrap_exceptions

REGISTERED_FUNCTIONS = []

class SMELLIEserver:
    def __init__(self):
        '''
         XML-RPC Protocol server hosted on the SNODROP machine on port 5020
        '''
        self.server = SimpleXMLRPCServer(("0.0.0.0", PORT))
        self.register()

    def serve_forever(self):
        self.server.serve_forever()

    def register(self):
        # wrap all the functions available to redirect exceptions to server
        for function in REGISTERED_FUNCTIONS:
            self.server.register_function(str_wrap_exceptions(function))

if __name__ == "__main__":
    s = SMELLIEserver()
    
