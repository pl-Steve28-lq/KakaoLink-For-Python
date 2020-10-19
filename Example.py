from KakaoModule import Kakao

KakaoLink = Kakao('Your JS key')
KakaoLink.login('Your ID', 'Your Password')

KakaoLink.send('Room Name', {'Your KakaoLink' : 'Arguments'}, 'custom')
