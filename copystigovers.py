import xml.etree.ElementTree as ET
import argparse

parser = argparse.ArgumentParser(description='copy over status and finding details from one ckl to another')
parser.add_argument('--old' ,'-o', required =True, help='path to the original ckl file') 
parser.add_argument('--new' , '-n', required =True, help='path to the new ckl file')
args = parser.parse_args()

# parse the XML file
tree1 = ET.parse(args.old)
root1 = tree1.getroot()
#details1 = 'this is a test'


tree2 = ET.parse(args.new)
root2 = tree2.getroot()

get_parent = root1.findall('.//VULN')
#num1 = root1.findall('.//VULN/STIG_DATA[VULN_ATTRIBUTE="Vuln_Num"]/ATTRIBUTE_DATA')
#num2 = root2.findall('.//VULN/STIG_DATA[VULN_ATTRIBUTE="Vuln_Num"]/ATTRIBUTE_DATA')

for STIG in root1.findall('.//VULN'):
    num1 = STIG.find('STIG_DATA[VULN_ATTRIBUTE="Vuln_Num"]/ATTRIBUTE_DATA').text
    details1 = STIG.find('FINDING_DETAILS').text
    status1 = STIG.find('STATUS')
    for STIG2 in root2.findall('.//VULN'):
        num2 = STIG2.find('STIG_DATA[VULN_ATTRIBUTE="Vuln_Num"]/ATTRIBUTE_DATA').text
        details2 = STIG2.find('FINDING_DETAILS')
        status2 = STIG2.find('STATUS')
        if num1 in num2:
            details2.text = details1
            status2.text = status1.text
            print(status1.text)
            print('changed'+ num2.text)



tree2.write(args.new)
 
