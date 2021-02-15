import os
import subprocess
import time

from flask import Flask, request
from flask_restful import Resource, Api, reqparse

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# import db_pack.alpaca.alpaca_daily as alpaca_daily
# import db_pack.alpaca.alpaca_minute as alpaca_minute
# import db_pack.alpaca.alpaca_symbol_loader as alpaca_symbol_loader

# import db_pack.oanda.oanda_daily as oanda_daily
# import db_pack.oanda.oanda_minute as oanda_minute
# import db_pack.oanda.oanda_symbol_loader as oanda_symbol_loader

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()

# class load_symbols(Resource):
#     def get(self,vendor):
#         if vendor=='alpaca':
#             alpaca_symbol_loader.main()
#             return {'Success':'Alpaca Symbols Loaded'}
#         elif vendor=='oanda':
#             oanda_symbol_loader.main()
#             return {'Success':'Oanda Symbols Loaded'}

# class load_daily_data(Resource):
#     def get(self,vendor):
#         if vendor=='alpaca':
#             alpaca_daily.main()
#             return {'Success':'Alpaca Daily Data Loaded'}
#         elif vendor=='oanda':
#             oanda_daily.main()
#             return {'Success':'Oanda Daily Data Loaded'}


# class load_minute_data(Resource):
#     def get(self,vendor):
#         if vendor=='alpaca':
#             alpaca_minute.main()
#             return {'Success':'Alpaca Minute Data Loaded'}
#         elif vendor=='oanda':
#             oanda_minute.main()
#             return {'Success':'Oanda Minute Data Loaded'}

# class load_indicator_data(Resource):
#     def get(self,vendor):
#         cmd_str="""python q_pack/q_run/run_BT.py --todate='2020-03-31'"""
#         subprocess.run(cmd_str, shell=True)
#         return {'Success':'Indicator Data Loaded'}

# class test(Resource):
#     def get(self,vendor):
#         cmd_str="""echo poda'"""
#         subprocess.run(cmd_str, shell=True)
#         return {'Success':'Test'}


# api.add_resource(load_symbols,'/load_symbols/<string:vendor>')
# api.add_resource(load_daily_data,'/load_daily_data/<string:vendor>')
# api.add_resource(load_minute_data,'/load_minute_data/<string:vendor>')
# api.add_resource(load_indicator_data,'/load_indicator_data/<string:vendor>')
# api.add_resource(test,'/test/<string:vendor>')

class HelloWorld(Resource):
    def get(self):
        return {'about':'Hellooo World'}

    def post(self):
        some_json=request.get_json()
        return{'you sent':some_json}, 201

class zerodha_api(Resource):
    # def get(self,userid,password,pin):
    def get(self):
        parser.add_argument('userid', type=str)
        parser.add_argument('password', type=str)
        parser.add_argument('pin', type=str)
        parser.add_argument('url', type=str)
        args = parser.parse_args()

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(chrome_options=chrome_options)
        # driver.implicitly_wait(10)
        # self.driver.quit()
        # try:
        driver.get(args['url'])
        time.sleep(3)
        username_textbox= driver.find_element_by_id("userid")
        username_textbox.send_keys(args['userid'])
        password_textbox= driver.find_element_by_id("password")
        password_textbox.send_keys(args['password'])
        driver.find_element_by_css_selector(".button-orange").click()

        time.sleep(3)
        pin_textbox= driver.find_element_by_id("pin")
        pin_textbox.send_keys(args['pin'])
        driver.find_element_by_css_selector(".button-orange").click()
        # driver.implicitly_wait(10)
        time.sleep(3)
        url = driver.current_url

        return url

        # except:
        #     return {'something is':' wrong'}

# https://stackoverflow.com/questions/30779584/flask-restful-passing-parameters-to-get-request - Take a look at this if you want to pass multiple parameters


# class Multi(Resource):
#     def get(self,num):
#         return {'result':num*10}

api.add_resource(HelloWorld,'/')
api.add_resource(zerodha_api,'/zerodha_api/')

# api.add_resource(Multi,'/mulit/<int:num>')



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',port=8060)
            # port=int(os.environ.get(
            #          'PORT', 8080)))