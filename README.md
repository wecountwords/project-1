# project-1: Wiki 
CSCI E-33a project-1 

**Purpose: design a Wikipedia-liek online encyclopedia. **

**Notes for graders**
Index url or access the app on the development server, use http://<ip address or server name>/wiki.  _wiki_ must be all lowercase. 
  
**References for this assignment**
* class lectures & notes
* W3Schools as reference for html / css / python
  * https://www.w3schools.com/python
  * https://www.w3schools.com/css
  * https://www.w3schools.com/html
* Django documentation
* research on the NoneType for testing results returned when using get_entry()
  * https://www.educative.io/edpresso/what-is-the-none-keyword-in-python
* research templating language to support looping through the titles list and creating links to the articles
  * Django docs and class lecture / notes
* pseudo random number generator for getting random articles
  * Python documentation on the random module
* reading on form validating with django -- adding custom error messaging to the django form validation is not implemented in this project
  * Django docs, stackexchange
  * future aspiration will be to master this customization

**Files run through pycodestyle:**
views.py
util.py
urls.py (project and app level)
Templates:
* layout.html
* index.html
* edit.html
* article.html
* add.html
  * One remaining unresolved error I opted to not resolve: a longish placeholder text string for the textarea, more than 79 chars. 


