function add_contact(phone_book, name, number) {
  /*
    This function allows to store a new contact in the phone book
    :param phone_book: the phone book (dictionary)
    :param name: the name of the contact (a string)
    :param number: the cell number of the contact (a string)
  */
  phone_book[name] = number;
}

function search_contact(phone_book, name) {
  /*
    This functions allows to search for a contact. It should print a meaningful message, e.g.:
    "Contact "Alice" found: 010-1111-2222" OR
    "Contact Alice not found!"
    This function should also return the boolean value True if the contact is found, False otherwise
    :param phone_book: the phone book (dictionary)
    :param name: the name of the contact to search 
  */

  if (phone_book.hasOwnProperty(name)) {
    console.log(`Contact "${name}" found: ${phone_book[name]}`);
    return true;
  } else {
    console.log(`Contact ${name} not found`);
    return false;
  }
}

function delete_contact(phone_book, name) {
  /*
    This function deletes a contact from the phone book (note: you should manage also the case in which the
    contact to delete is not in the phone book!)
    :param phone_book: the phone book (dictionary)
    :param name: he name of the contact to search
  */
  if (phone_book.hasOwnProperty(name)) {
    delete phone_book[name];
  } else {
    console.log("Contact is not in phone book");
  }
}

function count_contacts(phone_book) {
  /*
    This function counts the number of contacts in the phone book and prints a message, e.g.:
    "The number of contacts is: 25"
    :param phone_book: the phone book (dictionary)
  */
  console.log(Object.entries(phone_book).length);
}

function print_phone_book(phone_book) {
  /*
    This function prints on the console the content of the entire phone book
    :param phone_book: the phone book (dictionary)
  */
  for (let i in phone_book) {
    console.log(i + ": " + phone_book[i]);
  }
}

let phone_book = {
  John: "010-6787-990011",
  Jin: "010-4455-7788",
  Bob: "010-8872-0011"
};

print_phone_book(phone_book); // print the phone book content
add_contact(phone_book, "Alice", "010-7865-8899"); // add one entry
search_contact(phone_book, "Jiyoung"); // search for Jyoung's number
search_contact(phone_book, "Jin"); // search for Jin's number
count_contacts(phone_book); // should output 4
delete_contact(phone_book, "Bob"); // delete Bob from the phone book
delete_contact(phone_book, "Alice");
add_contact(phone_book, "Marco", "010-9988-6677");
count_contacts(phone_book); // should output 3
print_phone_book(phone_book);
