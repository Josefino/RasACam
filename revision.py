import io, sys

def getrevision():
  # Extract board revision from cpuinfo file
  myrevision = "0000"
  try:
    with open('/proc/cpuinfo','r', encoding='utf-8') as f:
        for line in f.readlines():
            if "Revision" in line[0:50]:
                length=len(line)
                myrevision = line[11:length-1]
    f.close()
  except:
    myrevision = "0000"
    
  return myrevision
 
a=getrevision()
print ("model:", a)

