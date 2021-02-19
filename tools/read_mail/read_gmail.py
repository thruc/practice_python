from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import time

class GmailAPI:

    def __init__(self):
        # If modifying these scopes, delete the file token.json.
        self._SCOPES = 'https://mail.google.com/'
        self.MessageIDList = []

    def ConnectGmail(self):
        store = file.Storage('token.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('credentials_lml.json', self._SCOPES)
            creds = tools.run_flow(flow, store)
        service = build('gmail', 'v1', http=creds.authorize(Http()))

        return service

    def ModifyUnreadMessageList(self,DateFrom,DateTo,MessageFrom):
        try:

            #APIに接続
            service = self.ConnectGmail()
            self.MessageIDList = []

            query = ''
            # 検索用クエリを指定する
            query += 'is:unread ' #未読のみ
            if DateFrom != None and DateFrom !="":
                query += 'after:' + DateFrom + ' '
            if DateTo != None  and DateTo !="":
                query += 'before:' + DateTo + ' '
            if MessageFrom != None and MessageFrom !="":
                query += 'From:' + MessageFrom + ' '
            print("条件 開始日付{0} 終了日付{1} From:{2}".format(DateFrom,DateTo,MessageFrom))

            # メールIDの一覧を取得する(最大500件)
            self.MessageIDList = service.users().messages().list(userId='me',maxResults=500,q=query).execute()
            if self.MessageIDList['resultSizeEstimate'] == 0:
                print("Message is not found")
                return False

            #batchModifyのrequestbody用にIDを抽出
            ids = {
                'ids': [],
                "removeLabelIds": [
                "UNREAD"
                ]
            }
            ids['ids'].extend([str(d['id']) for d in self.MessageIDList['messages']])

            #更新処理
            print()
            print("{0}件既読更新開始".format(len(ids['ids'])))
            service.users().messages().batchModify(userId='me',body=ids).execute()
            print("更新が完了しました")

            return True

        except Exception as e:
            print("エラーが発生しました")
            print(e)
            return False

if __name__ == '__main__':
    gmail = GmailAPI()

    #一度に消せる件数に制限があるので、対象データがなくなるまで繰り返し
    for i in range(100):
        if (gmail.ModifyUnreadMessageList(DateFrom='2000-01-01',DateTo='2021-11-30',MessageFrom=None) == False):
            break
        if len(gmail.MessageIDList['messages']) < 500:
            #処理を抜ける
            break
        else:
            #10秒待つ
            time.sleep(10)
