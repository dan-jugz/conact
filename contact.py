import pyperclip
class Contact:
    """
    Class that generates new instances of contacts
    """

    contact_list=[] #empty contact list
    
    def save_contact(self):
        '''
        save_contact method saves contact objects into contact_list
        '''
        Contact.contact_list.append(self)

    def test_save_multiple_contact(self):
            '''
            test_save_multiple_contact to check if we can save multiple contact
            objects to our contact_list
            '''
      
    def __init__(self,first_name,last_name,phone_number,email):
                                 #this are instance variables
        self.first_name=first_name #    first_name: New contact first name.
        self.last_name=last_name #        last_name : New contact last name.
        self.phone_number=phone_number #        number: New contact phone number.
        self.email=email #        email : New contact email address.


    def delete_contact(self):
        '''
        delete_contact method deletes a saved contact from the contact_list
        '''
        Contact.contact_list.remove(self)

    @classmethod
    def find_by_number(cls,number):
        '''
        Method that takes in a number and returns a contact that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            Contact of person that matches the number.
        '''

        for contact in cls.contact_list:
            if contact.phone_number == number:
                return contact

    @classmethod
    def contact_exist(cls,number):
        '''
        Method that checks if a contact exists from the contact list.
        Args:
        number: Phone number to search if it exists
        Returns :Boolean: True or false depending if the contact exists
        '''
        for contact in cls.contact_list:
            if contact.phone_number == number:
                    return True

        return False

    @classmethod
    def display_contacts(cls):
        '''
        method that returns the contact list
        '''
        return cls.contact_list

    @classmethod
    def copy_email(cls,number):
        contact_found = Contact.find_by_number("0791293150")
        pyperclip.copy(contact_found.email)