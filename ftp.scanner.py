import ftplib

def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous')
        print('\n [+] ' + hostname + ' FTP anonymous Login Succeeded.')
        ftp.quit()
        return True 
    
    except Exception:
        print('\n [+] ' + hostname + ' FTP anonymous Login Fails.')
        return False
    
    
    if __name__ == '__main__':
        anonLogin('185.199.103.142')
        
    