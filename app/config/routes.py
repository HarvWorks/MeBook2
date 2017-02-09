"""
    Routes Configuration File

    Put Routing rules here
"""
from system.core.router import routes

routes['default_controller'] = 'MyFaces'
routes['GET']['/register'] = 'MyFaces#register'
routes['GET']['/login'] = 'MyFaces#login'
routes['POST']['/process'] = 'MyFaces#process'
routes['GET']['/wall'] = 'MyFaces#wall'
routes['POST']['/wall/post'] = 'MyFaces#postWall'
routes['GET']['/wall/post/<message_id>'] = 'MyFaces#delPost'
routes['POST']['/wall/post/<message_id>'] = 'MyFaces#editPost'
routes['POST']['/wall/comment/<message_id>'] = 'MyFaces#postComment'
routes['GET']['/wall/comment/<comment_id>'] = 'MyFaces#delComment'
routes['POST']['/wall/comment_edit/<comment_id>'] = 'MyFaces#editComment'
routes['GET']['/logout'] = 'MyFaces#logout'
routes['GET']['/dashboard'] = 'MyFaces#dashboard'
routes['GET']['/profile'] = 'MyFaces#edit'
routes['GET']['/profile/<user_id>'] = 'MyFaces#profile'

routes['POST']['/process/<user_id>'] = 'MyFaces#processUser'

routes['POST']['/ignore/<user_id>'] = 'MyFaces#ignore'
routes['POST']['/requestfriend/<user_id>'] = 'MyFaces#requestFriend'
routes['POST']['/acceptfriend/<user_id>'] = 'MyFaces#acceptFriend'
routes['POST']['/cancelrequest/<user_id>'] = 'MyFaces#cancelRequest'
routes['POST']['/unfriend/<user_id>'] = 'MyFaces#unfriend'

routes['GET']['/message'] = 'MyFaces#message'
routes['GET']['/message/<user_id>'] = 'MyFaces#userMessage'
routes['POST']['/message/<user_id>/send'] = 'MyFaces#userMessageSend'
routes['GET']['/newwall_json'] = 'MyFaces#newWall_json'
routes['GET']['/grabMessages/<user_id>'] = 'MyFaces#grabMessages'
routes['POST']['/search'] = 'MyFaces#search'
routes['GET']['/grabfriends'] = 'MyFaces#grabFriends'
