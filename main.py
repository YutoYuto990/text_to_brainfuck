def getfactor(num,k=10):
  ret=[]
  for i in range(1,abs(num)+1):
    if num%i==0:
      if abs(int(num/i)-i)<k:
        ret+=[i,int(num/i)]
        break
  return ret
def getthebestfactor(num,k=10):
  for i in range(10):
    val=getfactor(num-i,k)
    if val:
      ret=[val[0],val[1],i]
      break
  return ret
def getfinfactor(num,k=10):
  t=getthebestfactor(num,k)
  if (t[0]<=10 and t[1]<=10):
    return t
  else:
    a,b=getthebestfactor(t[0],4),getthebestfactor(t[1],4)
    return [a,b,t[2]]
def numtbf(val:list):
  ret=""
  if isinstance(val[0],int):
    if val[0]==1 and val[1]>=0:
      ret+="+"*val[1]
    elif val[0]==1 and val[1]<0:
      ret+="-"*abs(val[1])
    else:
      ret+="+"*val[0]+"[>"+"+"*val[1]+"<-]>"+"+"*val[2]
  else:
    ret+=numtbf(val[0])+"[>"+numtbf(val[1])+"<<-]>>"+"+"*val[2]
  return ret
def get_brain_fuck(text):
  ret=""
  codes=[ord(i) for i in text if ord(i)<1000]
  val=[codes[0]]
  for i in range(1,len(codes)):
    if codes[i]-codes[i-1]>=-10 and codes[i]-codes[i-1]!=0:
      val.append(codes[i]-codes[i-1])
    elif codes[i]-codes[i-1]==0:
      val.append(0)
    else:
      val.append(codes[i])
  for i,v in enumerate(val):
    if v==0:
      ret+="."
    elif codes[i]==v and v>=10:
      ret+=">"+numtbf(getfinfactor(v))+"."
    elif codes[i]!=v and v>=10:
      ret+="<"+numtbf(getfinfactor(v))+"."
    else:
      ret+=numtbf(getfinfactor(v))+"."
  return ret
