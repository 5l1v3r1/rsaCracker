import OpenSSL
import subprocess 

def translate(hexNumber):
    number = hexNumber.replace(':', '')
    return int(number, 16)

if __name__ == "__main__":
    
    encryptedMessage = 'Qe7+h9OPQ7PN9CmF0ZOmD32fwpJotrUL67zxdRvhBn2U3fDtoz4iUGRXNOxwUXdJ2Cmz7zjS0DE8ST5dozBysByz/u1H//iAN+QeGlFVaS1Ee5a/TZilrTCbGPWxfNY4vRXHP6CB82QxhMjQ7/x90/+JLrhdAO99lvmdNetGZjY='
    pemFile = bytes(open('./key.pem').read(), encoding = 'utf-8')
    cert = OpenSSL.crypto.load_privatekey(
        OpenSSL.crypto.FILETYPE_PEM,
        pemFile
    )
    fileString = OpenSSL.crypto.dump_privatekey(OpenSSL.crypto.FILETYPE_TEXT, cert).decode("utf-8")
    print(fileString)
    lines = fileString.split("\n")
    lines.pop()
    values = dict()
    for i in range(0, len(lines)):
        if("publicExponent" in lines[i]):
            values[lines[i]] = lines[i]
            continue
        if(lines[i][0] is not " "):
            tempLines = list(lines[i+1:])
            if(tempLines[0][0] is not " "):
                continue
            key = lines[i]
            hexString = ""
            for line in tempLines:
                if(line[0] is not " "):
                    value = translate(hexString)
                    values[key] = value
                    break
                else:
                    line = line.replace(' ', '') 
                    hexString += line
    for key in values:
        print('\n')
        print('-------------------------------')
        print(key, values[key])
    
    print('-------------------------------')
    newN = values['prime1:'] * values['prime2:']
    print('new modulo N =', newN)

#openssl asn1parse -genconf asn1.cnf -noout -out asn1.der
#openssl rsa -in example.der -text -check 


