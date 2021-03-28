"""file for ifm LDAP server setup and usage."""
# from ldap3 import *
# from django.conf import settings
#
#
# def check_credentials(username, password):
#     """function for ifm ldap server request and response check."""
#     try:
#         server = Server(settings.IFM_LDAP_SERVER, get_info=ALL) # setup for request.
#         conn = Connection(server, user="INTRAIFM\\" + username, password=password, authentication=NTLM, auto_bind=True)
#         if conn.bind():
#             message = "loggedin"
#             return message
#         else:
#             message = 'invalid_login'
#             return message
#     except:
#         message = "User login failed !"
#         return message
