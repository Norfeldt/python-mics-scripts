# coding: utf-8
import win32com.client
import pywintypes
import urllib2, nltk, base64


def getNNContactInfo(initials):
	url = "http://phonebook.novo.dk/phonebook/pers.asp?initials=" + initials.lower()
	user = 'np-lanq'
	pwd = base64.b64decode('MTIzOTg3Tm41')

	request = urllib2.Request(url)
	base64string = base64.encodestring( '%s:%s' % (user, pwd) )
	request.add_header("Authorization", "Basic %s" % base64string)
	htmlCode = urllib2.urlopen(request).read()

	raw = nltk.clean_html(htmlCode)
	text = " ".join( raw.split() ).decode('latin-1')
	
	initials, name, email ,mobile, phone , address = None, None, None, None, None, None
	
	initials = text.split("Person Information Page Initials Phone Mobile phone")[1].split()[0]
	name = text.split("Name ")[1].split(" Dep. No.")[0]
	email = initials + "@novonordisk.com"
	_mobile = text.split("307")
	mobile = "+45307" +  _mobile[1].split()[0] if len(_mobile) >1 else ""
	_phone = text.split("444")
	phone = "+45444" +  _phone[1].split()[0] if "307" not in _phone[1].split()[0] else ""
	address = text.split("(Map) ")[1].split(" Address")[0]
	
	return [initials, name, email ,mobile, phone , address]

Outlook = win32com.client.Dispatch("Outlook.Application")
ns = Outlook.GetNamespace("MAPI")
profile = ns.Folders.Item("LANQ@NNEPHARMAPLAN.COM")
contacts = profile.Folders.Item("Contacts")

for i in range(len(contacts.Items)):
	contact = contacts.Items[ i+1 ]
	try:
		email = contact.Email1Address
	
		if len(email.split('@')) < 2 or email.split('@')[1].lower() != 'novonordisk.com':
			continue
		initials = contact.Email1Address.split('@')[0]
		print initials
		person = getNNContactInfo(initials)
		print person[1]
		contact.FirstName = person[1]
		contact.LastName = person[0]
		contact.BusinessTelephoneNumber = person[4]
		contact.MobileTelephoneNumber = person[3]
		contact.MailingAddressStreet = person[5]
		contact.Email1Address = person[2]
		contact.Save()
		print 'Done'
		print
		
	except:
		pass