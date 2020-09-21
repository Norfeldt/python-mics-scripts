import sys
import win32com.client

olFolderTodo = 28

outlook = win32com.client.Dispatch("Outlook.Application")
ns = outlook.GetNamespace("MAPI")
todo_folder = ns.GetDefaultFolder(olFolderTodo)
todo_items = todo_folder.Items

def print_encoded(s):
    print s.encode(sys.stdout.encoding, 'replace')

for i in range(1, 1 + len(todo_items)):
    item = todo_items[i]
    if item.__class__.__name__ == '_MailItem':
		if u'Completed: {0}'.format(item.TaskCompletedDate) != u'Completed: 01/01/01 00:00:00':
			continue		
		print_encoded(u'Email: {0}. Due: {1}'.format(item.Subject, item.TaskDueDate))
		# print_encoded(u'Flag: {0}. TaskCompletedDate: {1}'.format(item.FlagRequest, item.TaskCompletedDate)) #DEBUG
		print
		
    elif item.__class__.__name__ == '_ContactItem':
		continue # DEBUG
        #print_encoded(u'Contact: {0}. Due: {1}. Complete: {2}'.format(item.FullName, item.TaskDueDate, item.Complete))
    elif item.__class__.__name__ == '_TaskItem':
		if item.Complete == True:
			continue
		print_encoded(u'Task: {0}. Due: {1}. Complete: {2}'.format(item.Subject, item.DueDate, item.Complete))
		print
		
    else:
        print_encoded(u'Unknown Item type: {0}'.format(item))