import OpenSSL
import ssl, socket
cert=ssl.get_server_certificate(('downloadplugins.citrix.com', 443))
x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
print(x509.get_notAfter())
