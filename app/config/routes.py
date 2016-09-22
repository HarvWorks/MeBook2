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
routes['GET']['/logout'] = 'MyFaces#logout'
routes['GET']['/dashboard'] = 'MyFaces#dashboard'
routes['GET']['/profile'] = 'MyFaces#edit'
routes['GET']['/profile/<user_id>'] = 'MyFaces#profile'
routes['GET']['/requestfriend/<user_id>'] = 'MyFaces#requestFriend'
routes['GET']['/acceptfriend/<user_id>'] = 'MyFaces#acceptFriend'
routes['GET']['/unfriend/<user_id>'] = 'MyFaces#unfriend'
routes['POST']['/process/<user_id>'] = 'MyFaces#processUser'
routes['GET']['/message'] = 'MyFaces#message'
routes['GET']['/message/<user_id>'] = 'MyFaces#userMessage'
routes['POST']['/message/<user_id>/send'] = 'MyFaces#userMessageSend'
routes['GET']['/ignore/<user_id>'] = 'MyFaces#ignore'
routes['GET']['/cancelrequest/<user_id>'] = 'MyFaces#cancelRequest'
routes['GET']['/newwall_json'] = 'MyFaces#newWall_json'
routes['GET']['/grabMessages/<user_id>'] = 'MyFaces#grabMessages'
