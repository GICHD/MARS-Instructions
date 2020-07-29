"""
This python code to fetch the IMSMA Report GUID from an MaXML file. 
The output is a guid used in the Published from in MARS

To run the code 
 	`findguid maxml_source_file`
 	
"""
#!/usr/bin/python

import sys
import xml.etree.ElementTree as ET

def fieldGuid(str):
	root = ET.parse(str).getroot()
	for field in root.findall('FieldReport'):
		return field.find('FieldReportInfo').get('reportGUID')


if __name__ == "__main__" :
	if len(sys.argv) >= 1 :
		try:
			if sys.argv[1] is not None:
				if sys.argv[1] == '/?':
					raise IndexError
				filename = sys.argv[1]
				print('IMSMA Report GUID:',fieldGuid(filename))
				print('Copy and past this code in MARS in the form under the IMSMA Report GUID field')
		except NameError:
			print('File does not exist')
		except FileNotFoundError:
			print('File does not exist')
		except ImportError:
			print("Cannot Parse this file, it is not an xml format")
		except IndexError:
			print("usage:\tfindguid maxml_source_file")
			print("\t findguid /? to call this help.")
		except ET.ParseError:
			print('File is missing xml elements, check if file is correct MaXML format!')