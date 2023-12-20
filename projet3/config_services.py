import os

def configure_apache():

    # Open the Apache configuration file for editing

    with open('/etc/apache2/apache2.conf', 'a') as f:
        # Add the following line to the end of the file
        f.write('ServerName localhost\n')

    # Restart the Apache service

    os.system('sudo systemctl restart apache2')

def configure_ssh():

    # Open the SSH configuration file for editing

    with open('/etc/ssh/sshd_config', 'a') as f:
        # Add the following lines to the end of the file
        f.write('PermitRootLogin no\n')
        f.write('PasswordAuthentication no\n')

    # Restart the SSH service

    os.system('sudo systemctl restart ssh')

    # Restart the Apache service

    os.system('sudo systemctl restart apache2')

if __name__ == '__main__':
    configure_apache()
    configure_ssh()

