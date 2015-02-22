tornadwwo
=========

Non-blocking API for World Weather Online.

The official one is at https://github.com/WorldWeatherOnline/pywwo and kind of outdated.

**You need to use IPython QT Console or Spyder** to use it, or use it **inside Tornado IOLoop (or you will have the `response` missing!)**, Check this [StackOverflow Answer](http://stackoverflow.com/questions/27284172/ipython-dont-execute-codes-like-python).

Usage
=========

Since this is an alpha version, and needs lot of tweaks, the usage is really easy and for tests.

1. This will only work for Free API key, this is what i can test.
2. I did it to understand Tornado `AsyncHTTPClient`
3. LONG TODO LIST...

`from tornadwwo import wwo`

`wwo.forecast('your free api key', 'azazga') # Azazga is a town...`
 
`response = wwo.response # this will return a raw result, if you want a formatted one:`

`formatted-result = wwo.get_result() # this will the type of result (json, xml, csv, tab)`

`result = wwo.result `

and this is how to run it directly from Tornado (without IPython QT or Spyder)

    # -*- coding: utf-8 -*-
    import tornado.ioloop
    import tornado.web
    from tornadwwo import wwo


    class MainHandler(tornado.web.RequestHandler):
        def get(self):
            wwo.forecast('your free api key', q='azazga')
            self.write(str(wwo.response))

    application = tornado.web.Application([
        (r"/", MainHandler),
    ])

    if __name__ == "__main__":
        application.listen(8888)
        tornado.ioloop.IOLoop.instance().start()

**Note:

If you get a blank response while you work on a project, think about blocking it with Tornado:

`yield tornado.gen.Task(ioloop.IOLoop.instance().add_timeout, time.time() + 1)`
