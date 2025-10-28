import requests
#
class Client():
	def __init__(self):
		self.api="https://zaycev.net/api"
		self.headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36","Accept":"application/json"}
		self.user_id=None
	def login(self,email,password):
		data={"emailOrLogin":email,"password":password}
		req=requests.post(f"{self.api}/external/auth/login",json=data,headers=self.headers)
		self.headers['Cookie']=req.headers['Set-Cookie']
		info=self.account_info()
		self.user_id=info["user"]["personId"]
		return info
	def register(self,email,password,nickname):
		data={"email":email,"password":password,"name":nickname}
		req=requests.post(f"{self.api}/external/auth/registration",json=data,headers=self.headers)
		self.headers['Cookie']=req.headers['Set-Cookie']
		info=self.account_info()
		self.user_id=info["user"]["personId"]
		return info
	def reset_password(self,email):
		return requests.get(f"{self.api}/external/auth/resetPassword/email?email={email}",headers=self.headers).json()
	def account_info(self):
		return requests.get(f"{self.api}/external/auth/info",headers=self.headers).json()
	def playlist(self,id):
		return requests.get(f"{self.api}/external/playlist?personId={self.user_id}&globalId={id}",headers=self.headers).json()
	def genres_pages(self):
		return requests.get(f"{self.api}/external/pages/genres",headers=self.headers).json()
	def track_info(self,id):
		return requests.get(f"{self.api}/external/news/tracks/info?id={id}",headers=self.headers).json()
	def audiobooks_list(self,url:str="new,popular,biznes,biznes-knigi,boeviki",page:int=1,limit:int=6):
		return requests.get(f"{self.api}/external/audiobooks/list/?urls={urls}&page={page}&limit={limit}",headers=self.headers).json()
	def audiobooks_geners(self):
		return requests.get(f"{self.api}/external/audiobooks/genres",headers=self.headers).json()
	def search_musicsets(self,q,page:int=1,limit:int=100):
		return requests.get(f"{self.api}/external/pages/search/musicsets?q={q}&page={page}&limit={limit}",headers=self.headers).json()
	def search_artists(self,q,page:int=1,limit:int=100):
		return requests.get(f"{self.api}/external/pages/search/artists?q={q}&page={page}&limit={limit}",headers=self.headers).json()
	def search_tracks(self,q,page:int=1,limit:int=100):
		return requests.get(f"{self.api}/external/pages/search/tracks?q={q}&page={page}&limit={limit}",headers=self.headers).json()
	def new_pages(self,page:int=1,limit:int=100):
		return requests.get(f"{self.api}/external/pages/new?page={page}&limit={limit}",headers=self.headers).json()
	def pages_musicset(self,query:str="all",page:int=1,limit:int=100):
		return requests.get(f"{self.api}/external/pages/musicset/list?page={page}&limit={limit}&query={query}",headers=self.headers).json()
	def top_pages(self,period:str="day",entity:str="track",page:int=1,limit:int=100):
		return requests.get(f"{self.api}/external/pages/index/top?page={page}&limit={limit}&period={period}&entity={entity}",headers=self.headers).json()