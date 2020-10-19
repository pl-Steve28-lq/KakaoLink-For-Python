# KakaoLink-For-Python
KakaoLink Module implemented with Python!


## Usage Example
```Python
from KakaoModule import Kakao
#Import KakaoLink Module

KakaoLink = Kakao('Your JS key') #Initialize KakaoLink
KakaoLink.login('Your ID', 'Your Password') #Login your Account

KakaoLink.send('Room Name', {'Your KakaoLink' : 'Arguments'}, 'custom')
#Send KakaoLink with Arguments
```
