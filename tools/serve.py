#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import http.server as s
from urllib.parse import urlparse
from urllib.parse import parse_qs

class MyHandler(s.BaseHTTPRequestHandler):
    def do_POST(self):
        # urlパラメータを取得
        parsed = urlparse(self.path)
        # urlパラメータを解析
        params = parse_qs(parsed.query)
        # body部を取得
        content_len  = int(self.headers.get("content-length"))
        req_body = ""
        if content_len:
            req_body = self.rfile.read(content_len).decode("unicode-escape")
        # リクエスト内容まとめ
        msg  = "method: " + self.command + "\n"
        msg += "body  : " + req_body + "\n"
        print(msg)
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')

    def do_GET(self):
        # urlパラメータを取得
        parsed = urlparse(self.path)
        # urlパラメータを解析
        params = parse_qs(parsed.query)
        # リクエスト内容まとめ
        msg  = "method: " + self.command + "\n"
        msg += "params: " + str(params) + "\n"
        print(msg)
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
    
        
host = 'localhost'
port = 8888
httpd = s.HTTPServer((host, port), MyHandler)
print('サーバを起動しました。ポート:%s' % port)
httpd.serve_forever()
