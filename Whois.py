import socket,re,time
count = 0
def whois(domain):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('whois.nic.xin',43))
    s.send(domain)
    v = s.recv(10240)
    v = v.decode()
    return v

def Change(Str):
    Str = str(Str)
    
    Str = Str.replace("'","")
    Str = Str.replace("[","")
    Str = Str.replace("]","")
    return Str

def record(Whois):        
    Phone = re.findall("Registrant Phone: (.*)\r",Whois)
    Email = re.findall("Registrant Email: (.*)\r",Whois)
    Name = re.findall("Admin Name: (.*)\r",Whois)
    Phone = Change(Phone)
    Email = Change(Email)
    Name = Change(Name)
    return Phone,Email,Name

def localtime():
    localtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    return localtime

Domains = open('Domains.txt','rb')

domains = Domains.readlines()
for domain in domains:
#    Domain = bytes(domain)
    Domain = domain.decode()
    Domain = Domain.strip()
    count=count+1
    if (count %1000) ==0:
        time.sleep(100)
        print(count)
        print(localtime())
    try:
        Whois = whois(domain)
        
    except Exception:
        pass
    [Phone,Email,Name] = record(Whois)
    with open('result.txt','a') as f:
        f.writelines([Domain,",",Name,",",Phone,",",Email,"\n"])
        time.sleep(2)
