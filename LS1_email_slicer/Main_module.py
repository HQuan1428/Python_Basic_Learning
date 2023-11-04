from Leasson1 import emailProcess, printMsg



def main():
    emails = ['pyd@gmail.com', 'youtube@codexplore.dev',  'liverpool@winner.con']
    for email in emails:
        username, email_domain = emailProcess(email)
        printMsg(username, email_domain)

if __name__ == "__main__":
    main()