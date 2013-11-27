# -*- coding: utf-8 -*-
import web
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
import apiinstances
from sqlalchemy.orm import scoped_session, sessionmaker
from model.dbmodel import engine


#urls 定向配置
urls = (
    "/mytest","mytest",
    "/", "Index",
)

#模板定向
render = web.template.render(os.path.abspath(os.path.dirname(__file__)) + '/templates/', base="base")
#域名获取
realhome = web.ctx.get("realhome", "/lsgoapi")

#接口索引页面
class Index():
    def GET(self):
        web.header('Content-Type', 'text/html')
        #b = dict(zip(urls[0::2], urls[1::2]))
        #for item in b:
        #    yield """<a href="%s" >%s</a><br>""" % (item, b[item].lower())
        return render.index(urls[0::2], urls[0::2], realhome)

#测试页面 显示web 服用器各种参数
class mytest():
    count = 0
    def GET(self):
        return web.ctx.__dict__

#输出http头全局配置为 application/json  勾子
def setheader_json():
    web.header('Content-Type', 'application/json')

#get a new sqlalchemy session for the web.ctx.orm
def load_sqla(handler):
    web.ctx.orm = scoped_session(sessionmaker(engine))
    try:
        return handler()
    except web.HTTPError:
        web.ctx.orm.commit()
        raise
    except:
        web.ctx.orm.rollback()
        # debug only
        #return '{"code": 11, "ermsg": u"系统错误"}'
        #raise
    finally:
        web.ctx.orm.commit()
        web.ctx.orm.close()

app = web.application(urls, globals())
#输出http头全局配置为 application/json  勾子
app.add_processor(web.loadhook(setheader_json))

app.add_processor(load_sqla)
#使用服务器使用 mode_wsgi  运行
application = app.wsgifunc()

web.config.debug = True
if __name__ == "__main__":
    app.run()
