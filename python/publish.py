import ftplib
import shutil
import json
import os

# This script manages the compiling, renaming, and uploading of my thesis.
# Fraser Parlane 20220810


def get_session():
    """
    Get FTP session object
    :return: session
    """

    with open('credentials.json') as f:
        creds = json.load(f)
    session = ftplib.FTP(
        'fraserparlane.com',
        creds['username'],
        creds['password'],
    )
    session.cwd('demo.parlane.ca')
    return session


def get_paths():
    """
    Get paths to upload
    :return: paths
    """
    paths = []


def upload_website_to_ftp():
    """
    Upload the index.html file to the public FTP.
    :return: None
    """

    # Get FTP session
    session = get_session()
    with open('index.html', 'rb') as html:
        session.storbinary('STOR index.html', html)



if __name__ == '__main__':
    upload_website_to_ftp()