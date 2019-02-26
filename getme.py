from git import Repo
import os

print('elo')

Repo.clone_from('https://github.com/mzbro/foo-bar.git', 'sdx', branch='mzbro-patch-1')

if os.path.exists('sdx/somefile.txt'):
    with open('sdx/somefile.txt', 'r') as filezz:
        print('zawartosc: ' + filezz.read().rsplit('.', 1)[0])
