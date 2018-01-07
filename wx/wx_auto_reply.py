import itchat
from itchat.content import *

@itchat.msg_register(TEXT,isFriendChat=True,isGroupChat=True,isMpChat=True)
def simple_reply(msg):
    #print(msg)
    author = itchat.search_friends(nickName='月读')[0]
    print(author)
    author.send("hai")
    return 'I received : %s' % msg['Text']

@itchat.msg_register([PICTURE,RECORDING,ATTACHMENT,VIDEO])
def download_files(msg):
    msg.download(msg.fileName)
    itchat.send('@%s@%s' % (
        'img' if msg['Type'] == 'Picture' else 'fil', msg['FileName']),
        msg['FromUserName'])
    return '%s received' % msg['Type']

@itchat.msg_register(TEXT,isFriendChat=True)
def text_reply(msg):
    print(msg)
    wx_account = msg['FromUserName']
    user_name = itchat.search_friends(userName=wx_account)
    itchat.send("nihao!",toUserName=msg['FromUserName'])
    #msg['User'].send('你号！')

itchat.auto_login(True)
itchat.run(True)