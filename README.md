# project-1: Wiki 
CSCI E-33a project-1 

**submitting tegan-wiki.zip for project-1 + the unzipped files in the project which will be found in the wiki directory**

**Purpose: design a Wikipedia-liek online encyclopedia.**

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
 
 **Design decisions**
 * Req 1 - Entry Page
   * the article page and error page use the same template with a conditional to indicate if we show or not show the _page not found_ message
 * Req 2 - Index Page
   * As we only have 1 app for the project, strictly speaking, an app_name in urls.py is not necessary to avoid namespace collisions across apps. As such, I opted not to implement this option. 
 * Req 3 - Search
   * Implemented the search form through the Django forms mechanisms in views.py. 
   * OPEN ITEM: it appears now that I have to send the form in the context of the of the view function that renders each page. I did some research but was unable to identify a straight forward this while utilizing the methods we learned in our Django lecture. Future aspiration: figure out a more elegant way to support the same form across all pages.
   * If the seach term is not in the wiki, then in the view function, we will do the work to create a list of similar items and send that list to the template. This is in lieu of sending the full list to the template and making the decision at time of template rendering.
   * Since it is not a requirement, I strictly adhered to sending back a list of similar items only if search term q is a substring of the entry title. I did not go the other way. So, for example, HTML5 will not have html in its list of similar items but htm will have HTML in its list of similar items.
   * OPEN ITEM: the article title and the markdown title can be different which means we can end up with duplicates with different names. 
 * Req 4 - New Page
   * All article titles are saved with the first latter capitalized to support a more intuitive sort order for the "All Page" list.
   * Duplicate article error is shown as a message returned to the top of the create page. 
   * OPEN ITEM: implement the error via the Django validation and error mechanism for a more standardized mechanism. Future aspiration.
* Req 5 - Edit Page
  * Design assumption: the user should not be able to make changes to the article title, only the markdown.
* Req 6 - Random Page
  * I built a get_random() function in the util.py library to get a random title from the existing titles. It uses the pythong random module. Opted to leave the seed empty to force it to use the system time.
* Req 7 - Markdown to HTML conversion
  * As per the suggestion in the requirements, used the markdown2 module along wiht the safe filter to support successful rending of html.

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


