from sendEmail import sendEmail

if __name__ == "__main__":
	gmail_username = 'example@gmail.com'
	gmail_password = 'yourpassword'
	emailfrom = gmail_username
	emailto = ['myfriend1@gmail.com','myfriend2@gmail.com']
	filesToSend = ['testFile1.txt', 'testFile2.txt']
	subject = 'Test Files'
	body = 'Here are our test files.\nThank you very much.'
	
	sendEmail(emailfrom, 
			emailto, 
			subject, 
			body, 
			filesToSend, 
			gmail_username, 
			gmail_password)