#!/usr/bin/env python3

# Import of python system libraries.
import os

def generate_ss_cert():
    """
	This function creates a self signed certificate and creates a pem file which is used for the s_server function.
	"""
    sig_alg = "rsa"
    # Create Self Signed Certificate and key
    print("\n[ Creating Self Signed Certificate <{}> ]".format(sig_alg))
    os.system("apps/openssl req -x509 -new -newkey {0} -keyout {0}.key -out {0}.crt -nodes -subj \"/C=US/ST=MA/L=Cambridge/O=Draper/OU=Research/CN=server\" -config 'apps/openssl.cnf' -days 365".format(sig_alg))

def run_server():
    """
	This function opens a SSL/TLS server on port 4444 with provided ciphers.
    """
    sig_alg = "rsa"
    print("\n[ Setting up SSL/TLS Server <{}> ... Listening on port 4433 ]".format(sig_alg))
    os.system("apps/openssl s_server -cert {0}.crt -key {0}.key -HTTP -tls1_3 -accept 4433".format(sig_alg))

def main():
    cert_path = "rsa.crt"
    if not os.path.isfile(cert_path):
        generate_ss_cert()
    run_server()

if __name__ == "__main__":
    main()
