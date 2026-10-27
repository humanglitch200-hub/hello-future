### A. What is a contact?
contacts = {"prem": {"phone": "111", "email": "pb@.gmail"}}

---
___ Why I picked it:
    Because I have practiced it and did some excersies with it. So, it feels natural and familiar to me.


### B. List every function. 

add_contact(name, phone, email) -- adds or refusese if name exists
find_contact(name) -- returns info or None
delete_contact(name) -- removes or reports not found
list_all --prints every contact
search(term) -- finds contacts whose name contains the term (partial match) 

### C. Menu options.
    1. Add contact
    2. Find contact
    3. Delete contact
    4. List all
    5. Search
    6. Quit 

### Pick Your guards.
for each function, what's the empty- input case? write them:

add_contact — what if name is blank? What if name already exists?
     returns None

     return False

find_contact — what if contacts is empty? What if name isn't there?
     returns None

     retrun None

delete_contact — what if not there?
     return False

search — what if term is blank? What if nothing matches?
     returns None
     
     return []

list_all — what if contacts is empty?
     if contacts is empty return None.

# HUMAN NEVER CAN BECOME KNOWLEDGEFULL.  (LEARNING>>>)
