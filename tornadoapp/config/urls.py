from .. import handlers

urls = [
    (r"/|/about", handlers.IndexHandler),
    (r"/work", handlers.WorkHandler),
    (r"/stuff", handlers.StuffHandler),
    (r"/contact", handlers.ContactHandler),
    (r".*", handlers.ErrorHandler)
]