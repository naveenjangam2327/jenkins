import re
import xml.etree.ElementTree as ET
import xml.dom.minidom
from xml.etree import ElementTree
y="C:\\Users\\J.NAVEEN KUMAR\\Desktop\\vs.log";
f= open(y)
s=f.readlines()
l=[]
res=[]
l1=[]
l2=[]
l3=[]
l4=[]
l5=[]
#del str
count=0
for i in s:
    if "rules violated" in i:
        l.append(i)
for i in l:
    for j in i.split():
        if j.isdigit():
            res.append(j)
for i in res:
    count=count+int(i)
for i in s:
    if (("rule" and "times") in i):
        l1.append(i)
    elif (("rule" and "time") in i):
        l1.append(i)
for i in l1:
    if "User" not in i:
        result = re.findall(r"[-+]?\d*\.\d+|\d+", i)
        l2.append(float(result[0]))
        l3.append(int(result[1]))
for i in range (len(l2)):
    if(l2[i] not in l4):
        l4.append(l2[i])
        l5.append(l3[i])
    else:
        ind=l4.index(l2[i])
        l5[ind]=l5[ind]+l3[i]

def create_xml(): 
    root = ET.Element("root")
    student1 = ET.SubElement(root,"build_id")
    assignment1 = ET.SubElement(root,"job_name")
    student1.text = "101"
    assignment1.text = "Report"
    for a in range(len(l5)):
        result = ET.SubElement(root,"rule_violated")
        student = ET.SubElement(result,"rule_number")
        assignment = ET.SubElement(result,"Violation_count")
        
        student.text = str(l4[a])
        assignment.text = str(l5[a])
    assignment2 = ET.SubElement(root,"total_violation")
    assignment2.text = str(count)
    tree=ET.ElementTree(root)
    tree.write("test.xml")
create_xml()
with open('test.xml') as xmldata:
    xml = xml.dom.minidom.parseString(xmldata.read())
    xml_pretty_str = xml.toprettyxml()
f = open("test1.xml", "a")
f.write(xml_pretty_str)
f.close()