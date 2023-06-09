# Testing:
## Manual testing

Manual testing has been performed for its overall purpose.
The website has proven to exhibit dynamic functionality and responsive interactivity, both in the Front & Back-End.
After consecutive rehearsals and manual testing, the website employed the desired role and met the final goal set by the developer.

Based on the solid foundations of CRUD, testing was performed:
- By navigating and accessing links on the website.
- By Creating, Reading, Updating, and Deleting an account for a registered user.
- By Creating, Reading, Updating, and Deleting posts as a registered user.
- By Creating and Reading comments on a post as a registered user.
- By Liking and Disliking a post as a registered user.
- By Populating the homepage with posts to activate Pagination.
- By navigating through Pagination.
- By inputting and retrieving results from the search box.
- By Resetting the password of an account via email.
- By manipulating posts, users, comments, and likes as a superuser in the Admin panel.

## Functionalities
- By clicking on "Home," users are sent to the homepage, where the board of posts can be found. From here, users can browse posts and select one to read.
- By clicking on "About," users are sent to the About page. Within that page, users can read the introduction and the mission goal of the website. Users may navigate to the Registration and Login pages.
- By clicking on "Post," users are redirected to the Post Form, where they must input a title & body to create a thread. Posts are submitted by clicking the Submit Button. (Users must be logged in to post; otherwise, they are prompted to the Login page.)
- Once a post has been successfully created, it can be accessed and read by the entire community.
- Authors of that particular thread can Edit, Delete, Like/Dislike, and Comment on that post. Respectively, these functionalities are achieved by clicking the following icons at the end of the thread: the "Pencil," "Bin," "Heart," and the "Add Comment" links.
- Other users can Like/Dislike and/or Comment on that post by clicking the same icons mentioned above.
- Comments cannot be updated or deleted by anyone once submitted, except by administrators. To submit a comment on the Comment page, users must click the "Submit Comment" button.
- By clicking on "Profile," users are sent to the

...........................................

...........................................


## Lighthouse & WAVE
This website, under Ingognito mode, was scanned for Performance, Accessibility, Best Practices and SEO for both Desktop and Mobile devices under the Lighthouse function provided by Chrome DevTools, with favorable scores.

Both devices exhibited scores above 90% for Performance, Accessibility and SEO, with the exception for Mobiles on Performance, due to image size and extension uploaded by Users.
Lighthouse failed to run and validate a "error 404" page.

Refer to the links for the templates:
<img src="media/readme_img/lighthousedesktop.png" alt="lighthousedesktop">
<img src="media/readme_img/lighthousemobile.png" alt="lighthousemobile">

This website, under Ingognito mode, was scanned for Errors, Contrast Errors, Alerts, Features, Structural Elements and Aria for both Desktop with Chromes extension [Wave](https://wave.webaim.org/).

After several tests and corrections, the website went under examination for all its pages and retrieved no Errors, whatsoever.
The website is responsive and displays a pleasing style to the viewers, with colors contrasting each other. Aria labels have been applied together with Structural Elements and Features.

It retrieved Alerts however, for Redundant links (example links found in the navigation bar from base.html also found in the body of a page.), Suspicious alternative text and Skipped heading level.

Refer to the templates names:
<img src="media/readme_img/wave.png" alt="wave">

In order to achieve auspicious ratings, the website underwent various changes on its styling in order to please both WAVE and Lighthouse 
...........................................

## Validation 
Via URL of the deployed website on Heroku, all pages were validated through validator.w3.org & jigsaw.w3.org.
No errors or warnings were found whatsoever, after several corrections have been applied with the exception of /register/

The website went under various editions in order to comply with markup validity.
Refer to the following links:
[home](https://validator.w3.org/nu/?doc=https%3A%2F%2Fdigital-nomad.herokuapp.com%2F)
[/about/](https://validator.w3.org/nu/?doc=https%3A%2F%2Fdigital-nomad.herokuapp.com%2Fabout%2F)
[/login/](https://validator.w3.org/nu/?doc=https%3A%2F%2Fdigital-nomad.herokuapp.com%2Flogin%2F)
[/logout/](https://validator.w3.org/nu/?doc=https%3A%2F%2Fdigital-nomad.herokuapp.com%2Flogout%2F)
[/register/](https://validator.w3.org/nu/?doc=https%3A%2F%2Fdigital-nomad.herokuapp.com%2Fregister%2F)
[/post/new/](https://validator.w3.org/nu/?doc=https%3A%2F%2Fdigital-nomad.herokuapp.com%2Fpost%2Fnew%2F)
[/post/update/](https://validator.w3.org/nu/?doc=https%3A%2F%2Fdigital-nomad.herokuapp.com%2Fpost%2F68%2Fupdate)
[/user/user/](https://validator.w3.org/nu/?doc=https%3A%2F%2Fdigital-nomad.herokuapp.com%2Fuser%2Fuser)

The Developer investigated the error, but found no solution, as "xt-muted"><ul><li>Yo" is not found int the /register/ template.
When time allows, the error ought to suffer a correction.
<img src="media/readme_img/registererror.png" alt="register error">

Otherwise, the .html template structure and format passed through the official [W3validator](https://validator.w3.org/) with no issues.
[See the report](https://validator.w3.org/nu/?doc=https%3A%2F%2Fdigital-nomad.herokuapp.com%2F)
<img src="media/readme_img/w3validator.png" alt="w3validator">

The .css styling file was tested and validated through [W3jigsaw](https://jigsaw.w3.org/css-validator/) with no issues.
[See the report](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fdigital-nomad.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
<img src="media/readme_img/jigsawvalidator.png" alt="jigsawvalidator">

The .py models, views and urls format were tested and validated through [Pep8CI](https://pep8ci.herokuapp.com/)
<img src="media/readme_img/cilinter.png" alt="pep8 ci linter">

- This website was developed on Gitpod hosted by GitHub, making use of both Front-end and Back-end.

Bugs, Errors and Removed functionalities:
- The ckeditor failed to render properly in the body of the Post. Eventually ckeditor was removed from the project altogether, giving Users the possibility to write a basic TextField.
- After getting it to work, the layout of the tool box felt off. After stylizing with on .css it failed to render properly. on Heroku. The localserver everything worked fine.
- The developer would like to re-implement if when time allows.

# Errors & Bugs
## Bug while Spaming
Upon manual testing, if a User creates a Post and the Post is submitted & written while spaming the same character/different characters but in the same paragraph, without a single space. The Title and Body exhibit a bug, where the text crosses over to the right side of the border of the Post model. (The same error was found, with ckeditor installed)
- Solution: Unsolved. No solution was founded The Posts should be written by s Human. (Ought to be fixed in the future, when time is available, perhaps post-assessment)

<img src="media/readme_img/bugontype.png" alt="Bug while spaming a letter">

## Missing "etag" and assets"
Upon deploying the project to Heroku, the static files were either corrupted or missing. The ckeditor in particluar exhibited many errors and this resulted in frustration utltimatly leading the developer to abandon this type of RichTextEditor for the time being (Ought to be implemented in the future, perhaps post-assessment). After ckeditor suffered a successful fupload forits assets from the local static files to cloudinary, the developer still insisted on keeping the Posts model simple with TextField for the time being.
- Solution: Solved by deleting the static folder in Cloudinary, running "pip cache purge" in the terminal of working environment of GitPod and re-deploying on Heroku.

<img src="media/readme_img/collectstaticerror.png" alt="Example of collectstaticerror">

## Building Image
Upon opening booting the working environment, the repository displayed the same error over and over when trying to access the project on GitPod. This error is persistent and hass been documented since the developers CI-PP3(Python).
- Solution: Unsolved. Hit "Continue with Default Image".

<img src="media/readme_img/imagebuild.png" alt="Image Build error">

## Responsivness
The website was tested through Chrome Developer tools for the following devices:

iPhone SE
iPhone XR
iPhone 12 Pro
Pixel 5
Samsung Galaxy S8+
Samsung Galaxy S20 Ultra
iPad Air
iPad Mini
Surface Pro 7
Surface Duo
Galaxy Fold
Samsung Galaxy A51