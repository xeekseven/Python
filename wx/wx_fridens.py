import itchat
itchat.login()

itchat.send(u'你好','filehelper')
friends = itchat.get_friends(update=True)[0:]
male = female =other= 0

for i in friends[1:]:
    sex = i["Sex"]
    if sex==1:
        male+=1
    elif sex==2:
        female+=1
    else:
        other+=1
total = len(friends[1:])
print(u"男性好友：%.2f%%" % (float(male) / total * 100))
print(u"女性好友：%.2f%%" % (float(female) / total * 100))
print(u"其他：%.2f%%" % (float(other) / total * 100))