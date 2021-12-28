from unicodedata import normalize

f=open('/tmp/group.txt')
group=f.readlines()
f.close()

def tg_count(tg_num):
  count=0
  global group
  for line in group:
    newlines=line.split('},')
    for item in newlines:
        if (item.find(','+str(tg_num)+',')>0): count+=1
  return count

f = open('/tmp/data.json')
content = f.readlines()
f.close()

content=[x.strip() for x in content]
content = content[1:]
content = content[:-1]
content = [normalize('NFKD',x.decode('unicode-escape')).encode('ascii','ignore') for x in content]
f = open("/tmp/TGList.txt","wb+")
first_time = True
j=0
for line in content:
  j=j+1
  print "\rProcessing line" + str(j),
  line=line.replace("\/"," ")
  line=line.replace("Provincial","")
  line=line.replace("Regional","Reg-")
  #delete line feed
  line=line.replace("\n","")
  line=line.replace("\r","")
  #delete json simbols
  line=line.replace('"','')
  line=line.replace(',','')
  line=line.split(':')
  i=line[0]
  val=int(i)
  # Include Spanish Multimode TG
  if first_time and val>2140:
    c=tg_count(214011)
    tmp="214011;0;" + str(c) + ";EXTREMADURA;EXTREMADURA"
    f.write(tmp+'\n')
    c=tg_count(21480)
    tmp="21480;0;" + str(c) + ";SPAIN INFORMATION BEACON;INFORMATION BEACON"
    f.write(tmp+'\n')
    c=tg_count(214001)
    tmp="214001;0;" + str(c) + ";ANDALUCIA;ANDALUCIA"
    f.write(tmp+'\n')
    c=tg_count(214012)
    tmp="214001;0;" + str(c) + ";GALICIA;GALICIA"
    f.write(tmp+'\n')    
    first_time = False
  #process special TG
  if (val>=4000) and (val<=5000):
    b='1'
  else:
    b='0'
  if val==9990: b=2
  if (val>90) and (val!=4000) and (val!=5000) and (val!=9990):
    c=tg_count(val)
  else:
    c=0
  #write final lines
  line=line[0]+';'+ str(b)+';'+str(c)+';'+line[1]+';'+line[1]
  line=line.replace(' ','')
  f.write(line+'\n')

f.close()
