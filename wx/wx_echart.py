from echarts import Echart,Legend,Pie
import itchat

itchat.login()

friends = itchat.get_friends(update=True)[0:]

male = female = other = 0

for i in friends[1:]:
    sex = i["Sex"]
    if sex == 1:
        male+=1
    elif sex ==2:
        female +=1
    else:
         other +=1
total = len(friends[1:])
chart = Echart('%sfrends' % (friends[0]['NickName']), 'from WeChat')
chart.use(Pie('WeChat',
              [{'value': male, 'name': u'man %.2f%%' % (float(male) / total * 100)},
               {'value': female, 'name': u'woman %.2f%%' % (float(female) / total * 100)},
               {'value': other, 'name': u'other %.2f%%' % (float(other) / total * 100)}],
              radius=["50%", "70%"]))
chart.use(Legend(["male", "female", "other"]))
del chart.json["xAxis"]
del chart.json["yAxis"]
chart.plot(persist=True)