# Django - Studybuddy

One or two paragraphs providing an overview of your project.

Essentially, this part is your sales pitch.

👉 
 
## UX
 
Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:
- As a user type, I want to perform an action, so that I can achieve a goal.

This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included as a pdf file in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.

## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.

- only the owners can update and delete their own information
- only a user can edit their own post
- if user is not logged in. He/she is not allowed to be on the chat room home page
- use conditional template for displaying login and register form
- added login, logout, restricted pages, and registration
- user cannot revisit login page via manual url while logged in already
- only users can view chat activity
- Added activity feed to chat home page
- included delete functionality in activity feed 
- added a rest api functionality for users that wants to retrieve information from the app
 
### Existing Features
- Feature 1 - allows users X to achieve Y, by having them fill out Z
- ...

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
- Another feature idea

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [HTML](https://www.w3schools.com/html/default.asp)
    - The project uses **HTML** to produce the web contents.

- [CSS](https://www.w3schools.com/CSS/default.asp)
    - The project uses **CSS** to create visually pleasing content.

- [Bootstrap 4.4](https://getbootstrap.com/docs/4.4/getting-started/introduction/)
    - The project uses **Bootstrap** version 4.4, frontend design framework, to produce better UI/UX for mobile first development.

- [Python](https://www.python.org/doc/)
    - The project uses **Python** to process server side queries, such as processing payments and user authentications.

- [Django](https://www.djangoproject.com/)
    - The project uses the **Django** , Python Full Stack framework, to simplify and speedup the development of a Full Stack Web Application.

- [Django REST Framework](https://www.django-rest-framework.org/)
    - The project uses **JQuery** to simplify DOM manipulation.

## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

### Bugs Encountered

- Typos in functions and URL routes
    - dealt with these situation during the code along session by evaluating the error report provided by the Django server
    - investigated the source of the errors reported by django and corrected spelling typos

- Flash `message` object from `django.contrib` conflicted with message variable passed in the view for `def room()`, as 
    - Messages were displaying close to the navbar elements instead of the `div` for the chat
    - problem fixed by changing `messages` variable to `room_messages`

- Using `{% include 'activity_component.html' %}` in the **Django base** displayed error loading page after refreshing the server. The Django template engine could not find the required HTML component. results in:

    ```
    TemplateDoesNotExist at /
        activity_component.html
    ```
    - Issue resolved by including the base directory route --> `{% include 'base/activity_component.html' %}`

- submitting a message in the study room doesn't send any data.
    - Updated the form `action` value to ('') and the `method` value to ('POST')
    - added a name attribute of **body** to the `input` element 
    - form updated the room with current message sent after pressing the **enter** key


## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X

