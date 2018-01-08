import itchat

itchat.auto_login(True)

friends = itchat.search_friends(name='此如犹树')

itchat.send_file('wx_word.py',toUserName=friends[0]['UserName'])

#消息注册 @itchat.register(TEXT,isFriendChat=True,isGroupChat=True,isMpChat=True)

#文字 itchat.content.TEXT
#图片 itchat.content.PICTURE
#语音 itchat.content.RECORDING
#名片 itchat.content.CARD

#登录 itchat.auto_login(True)
#登出 itchat.logout()

#获取所有的朋友 itchat.get_friends()
#获取所有的群聊 itchat.get_chatrooms()
#获取所有的公众号 itchat.get_mps()

#搜索功能
#搜索朋友 itchat.search_friends(self,name=None,userName=None,nickName=None)
#搜索公众号 itchat.search_mps(self,name=None,userName=None)
#搜索群聊 itchat.search_chatrooms(self,name=None,userName=None)




#UserName是指的一个标识。不仅用户有，群聊也有，公众号也有，所以这一句可以给三种'用户'发送消息。
#发送消息 itchat.send(message,UserName)

#发送消息 send_msg  itchat.send_msg("hi",toUserName=None)
#发送文件 send_file itchat.send_file(file_path,toUserName=None)
#发送图片 send_img itchat.send_img(img_path,toUserName=None)
#发送流媒体 send_video itchat.send_video(video_path,toUserName=None)