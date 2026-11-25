from abc import ABC, abstractmethod
from pydantic import BaseModel
from typing import Optional

class Email(BaseModel):
    subject: str
    message: str
    from_: str
    to_: str

    is_spam: bool = False
    is_virus: bool = False
    is_phising: bool = False


class EmailHandler(ABC):

    def __init__(self):
        self.next: Optional[EmailHandler] = None

    def set_next(self, handler):
        self.next = handler
        return handler

    def handle(self, email: Email) -> Email:
        self.handle_request(email)
        if self.next:
            return self.next.handle(email)
        return email

    @abstractmethod
    def handle_request(self, email: Email):
        pass

class SpamHandler(EmailHandler):

    def handle_request(self, email: Email):
        keywords = ['winner', 'lottery', 'free money']
        subject = email.subject.lower()
        if any(keyword in subject for keyword in keywords):
            email.is_spam = True

class VirusHandler(EmailHandler):

    def handle_request(self, email: Email):
        if "virus" in email.message.lower():
            email.is_virus = True

class PhisingHandler(EmailHandler):

    def handle_request(self, email: Email):
        if 'link' in email.message.lower():
            email.is_phising = True

# ----- Client

if __name__ == "__main__":
    email = Email(
        subject = "You win the lottery",
        message = "Welcome to the UNAL lottery. This is not a virus. Please, follow next link and get your prize.",
        from_ = "prizes@unal_edu.co",
        to_ = "me@unal.edu.co"
    )

    spam_filter = SpamHandler()
    virus_scanner = VirusHandler()
    phishing_scanner = PhisingHandler()
    spam_filter.set_next(virus_scanner).set_next(phishing_scanner)

    print("ORIGINAL EMAIL\n", email)
    processed_email = spam_filter.handle(email)
    print("\nPROCESSED EMAIL\n", processed_email)
