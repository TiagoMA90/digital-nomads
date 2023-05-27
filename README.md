
# Digital Nomads
- Digital Nomads is a website that allows developers to share their experiences outside the office.
- No desks, no cubicles, no offices.
- It is a platform for nomads in the digital world to share their personal adventures, tips and recommendations when working and exploring the world.

# Live Project
- The live website can be found [here](https://digital-nomad.herokuapp.com/).

# Purpose of the website:
- To provide a platform where users can share their stories as digital nomads.
- To promote the idea that developers can be flexible on the job while working and traveling.
- To create a community and connect users in a "guild" of like-minded people.
- To allow users to share their ideas and help each other both in front and behind the screen.

# Design:
The website was designed with the intent to allow users to browse posts easily and perform all CRUD functionalities. It relied on colors that should be appealing to the user, especially for those who might use the website on a daily basis.

For such, it makes use of a color palette of a mere greenish, brownish, and yellowish blend (COLOR # HERE) for the navigation bar. This gives a rustic feeling and is often associated with the nomadic camper life at the beach, desert, and mountain.

The background is best defined by a grayish white (COLOR # HERE), and the body of the post has a lighter gray (COLOR # HERE), bordered by dashed lines. The buttons in the post borrow the same patterns and render a shadow beneath them to contrast the body. This gives the illusion that the user is writing a post on a piece of paper/document.

[IMG for COLOR PALETTE]

For a website where its functionality consists of writing and reading articles, the fonts used for this website were "Audiowide" and "Staatliches." A choice that should appeal to a user's readability and block them from distractions of a complex design. The fonts and logo on the navigation bar are dyed in white, while the body presents itself with a dark grayish tone that doesn't stand too much from the article. Links in the navigation bar are highlighted by a white tone when hovered, and bold when active. Links change color upon hover, particularly the title of the post, the username in a post/comment, the social media links, and links that redirect to other pages.

Icons were also integrated into the website to give a much more aesthetic touch and association of functionality of the website. The navigation bar, footer, and pages in the body make use of icons. The logo states "Digital Nomads" and is animated by an icon to give the idea that devs are on the move. Red was the chosen color to highlight it from the rest of the name. Both the header and footer have an image attached to them, of somebody networking, to give the impression that they are typing and reading posts. Hence the screen at the top and the hand at the bottom.

The structure of the website is coherent, and the base.html is present on all pages. The skeleton of the body is consistent for all pages.

# Features and Functionality for Non-Registered Users, Registered Users, and Superusers

## Non-Registered Users (Visitors):
- Visitors can read all posts from /home/.
- Visitors can read all users' posts from /username/.
- Visitors can create a user account through /register/.
- Visitors can navigate to the Home/About/Login/Register pages.
- Visitors can navigate through the pagination of /home/ and /username/.
- Visitors can access external links on users' posts/comments and footer.

## Registered Users (CRUD) can do the above as a Visitor, moreover:
- Users can log in/out through the "Log In/Out" functionality.
- Users can create posts through the "Post" functionality.
- Users can update their posts through the "Update" functionality.
- Users can delete their posts through the "Delete" functionality.
- Users can like/dislike all posts through the "Like/Dislike" functionality.
- Users can navigate to the Profile tab and update their "Bio".
- Users can navigate to the Profile tab and upload a profile picture.
- Comments cannot be deleted by anyone except Superusers.

## Superusers can manipulate information through the /admin/ panel:
- CRUD posts.
- Change passwords.
- Create/update/delete users.
- Delete comments.
- Promote users to Superuser.

(ELABORTATE...)

# Design
## Navbar, Header & Favicon
- The Navbar features from left to right the [Logo], [Home], [About], [Login], [Register], and the [Search] fields. Furthermore, for Users who are logged in, the [Post], [Profile], and [Logout] links. The links guide Users to the respective pages and remain "active" when and if on that page, with the exception of [Post].
- The Header features an image that splits in half, sharing the rest with the Footer. The screen of a laptop can be seen together with the Logo of the website.
- On the browser's tab, the Favicon and Logo of the website can be found—a red gear.
- 
<img src="media/readme_img/headernavpanel.png" alt="Navigation & Header">

## Footer
- The Footer is best defined by Bootstrap's template. It features a slogan on the left side and on the right, the Social Media links. At the very bottom, a copyright notice.
- Above the Footer is the rest of the image shared with the Header: the keyboard of a laptop.
- Users can open the Social Media links in new tabs.

<img src="media/readme_img/footerpanel.png" alt="Footer">

## Home: Posts & Pagination
- The homepage displays all of the posts that users create.
- If users are logged in, they are greeted with a message followed by their usernames.
- If no posts are present on the homepage, a message is displayed encouraging users to create a post.
- 
<img src="media/readme_img/nopostspanel.png" alt="No Posts">

- If the forum has been populated with posts, then the posts are displayed and organized in a vertical fashion, with the newest at the top and the oldest at the bottom.
- For each post, the username, picture, date, title, and body (truncated by 50 words) are displayed.
- Every 6 posts, a new page for pagination is created, allowing users to easily navigate from page to page.

<img src="media/readme_img/pagination.png" alt="Pagination">

## About
- The About page renders a small section of advertisement and information about the website. It also encourages users to either Log in or Register an account.

<img src="media/readme_img/aboutpanel.png" alt="About">

## Posts & Comments
- When opening a Post, the details of that particular Post is expanded, allowing Users to read the whole article.
- Users can read and engage with the Post, by leaving Comments and Likes.

<img src="media/readme_img/openpostandcommentpanels.png" alt="Open Posts and Comments">

## Search Field
- Users can use the Search functionality.
- Upon making a valid search, the page should retrieve a list of Threads by a word populated either in the Title, Body or Username of a Post.

<img src="media/readme_img/charactersearch.png" alt="Search Field">

- If no Post exhibit such word, than a template prompts Users to give in a valid word.

<img src="media/readme_img/wrongcharactersearch.png" alt="Search Field">

- Otherwise, if no word was introduced in the search field, Users are requested to input a valid word/character.

<img src="media/readme_img/nocharactersearch.png" alt="Search Field">

## User Profile
- The User profile can be best defined as a "Settings panel" where users can update their personal info.
- The fields that can be updated include Username, Profile picture, E-mail and Bio.

<img src="media/readme_img/profile.png" alt="Profile">

- Upon updating the Bio the User should have an Overview field.

<img src="media/readme_img/overviewpanel.png" alt="Overview">

- If a User created an account, but did not make any Posts, even though made Comments. The User profile still remains inactive. This compels users to Post.

<img src="media/readme_img/usernopostspanel.png" alt="User no Profile">

## Registration & Deletion
- The Registration page requests Users to input a Username, E-mail and Password.

<img src="media/readme_img/registerationpanel.png" alt="Error 404">

## Log in/out
- The Log in page demands Users to input valid credentials, as per registered.

<img src="media/readme_img/loginpanel.png" alt="Log in">

- By Logging out, Users are fired with a farewell message.

<img src="media/readme_img/logoutpanel.png" alt="Log out">

## Deletion

<img src="media/readme_img/deletionpanel.png" alt="Deletion">

<img src="media/readme_img/deletionconfirmedpanel.png" alt="Deleted">

## Error 404
- If a User goes to a non-defined URL, then a 404 Error template is rendered, requesting users to leave that page.

<img src="media/readme_img/404.png" alt="Error 404">

## Planning & Agile:
This project was planned using Agile methodology and MoSCoW prioritization.
For this purpose, the project was illustrated by one milestone titled "Submit the project to CI before Deadline," providing the developer with the freedom to accomplish all issues/tasks flexibly by the deadline.
Throughout the development process, new issues were added/removed, starting from "Todo," progressing to "In Progress," and finally being finalized in "Done."
The issues were assigned to the sole developer, [TiagoMA90](https://github.com/TiagoMA90), and labeled as "could-have," "should-have," and "must-have."
Once completed, the issues were marked as "done," and when all of them were completed, the milestone was closed.

[SCREENSHOTS] (ELABORATE)

## Development Process
The project started out as a forum for Ads of Events, where users could post events taking place at a certain time in a certain location.
Users would open up a thread, give a brief description of the event, target the location with Google Maps API, and set the date. After an event took place, it would be automatically deleted.

In the end, this project was simplified due to deadline limitations and time constraints. It makes good use of familiar concepts such as Create Read Update Delete.
Upon re-creating this project, the developer rethought the idea of a "forum" or "discussion board," similar to [reddit](https://www.reddit.com/), but more focused on the nomadic lifestyle.

## Manual Testing and Website Functionality:

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
- By inputting and retrieving results from the search box.
- By Resetting the password of an account via email.
- By manipulating posts, users, comments, and likes as a superuser in the Admin panel.

By clicking the links in the navigation panel, users are redirected to the assigned pages.
- By clicking on "Home," users are sent to the homepage, where the board of posts can be found. From here, users can browse posts and select one to read.
- By clicking on "About," users are sent to the About page. Within that page, users can read the introduction and the mission goal of the website. Users may navigate to the Registration and Login pages.
- By clicking on "Post," users are redirected to the Post Form, where they must input a title and body to create a thread. Posts are submitted by clicking the Submit Button. (Users must be logged in to post; otherwise, they are prompted to the Login page.)
- Once a post has been successfully created, it can be accessed and read by the entire community.
- Authors of that particular thread can Edit, Delete, Like/Dislike, and Comment on that post. Respectively, these functionalities are achieved by clicking the following icons at the end of the thread: the "Pencil," "Bin," "Heart," and the "Add Comment" links.
- Other users can Like/Dislike and/or Comment on that post by clicking the same icons mentioned above.
- Comments cannot be updated or deleted by anyone once submitted, except by administrators. To submit a comment on the Comment page, users must click the "Submit Comment" button.
- By clicking on "Profile," users are sent to the

Bugs and Excluded features:
- The ckeditor failed to render properly in the body of the Post. Eventually ckeditor was removed from the project altogether, give Users the possibility to write a basic TextField.

[SCREENSHOTS] (ELABORATE)

- This website was developed on Gitpod hosted by GitHub, making use of both Front-end and Back-end.

Errors and Removed functionalities:
- ckeditor - (traces of the code are still visible in the code) - Had trouble with assets such as "brown-paper" & others.
- Imported and uploaded manually, but the interface was unrecognizable. Eventually moved back to models.TextField()

Languages
- HTML (markup language)
- CSS (style sheet language)
- Python (programming language)

Frameworks
- Bootsrap (css framework)
- Django (web framework)

and  and deployed on Heroku.

# Development & Deployment
The project was developed using GitHub and GitPod platforms...
- Navigate to: "Repositories" and create "New".
- Mark the following fields: ✓ Public ✓ Add a README file.
- Select template: "Code-Institute-Org/python-essentials-template".
- Add a Repository name: "digital-nomads".
- ...and create Repository.

... and suffered various executions using the inbuild Terminal.

For Commits on this project, the following commands ran:
- "git add ." <- Stages before commiting.
- "git commit -m "written imperative declaration"" <- Declares changes and updates.
- "git push" <- Push all updates to the GitHub Repository.

To run the server locally (Debug = True), the following command ran:
- python manage.py runserver <- Loads the website on the in-built Terminal.

During development migrations to the database were made.
To make migrations the following commands ran:
- "python manage.py makemigrations" <- Creates a new database migration
- "python manage.py migrate" <- Applies pending migrations

To create a new Django project, in the currenct directory, the followig command ran:
- "django-admin startproject NAMEOFTHEPROJECT ." <- Starts the project

To create the app the following command ran:
- "python3 manage.py startapp blog" <- Creates a folder for the app withing the project

To install Django libraries and Set up:
From the new workspace, navigate to the Terminal and run:

- "pip3 install 'django<4' gunicorn" <-Runs the /admin

To install the supporting libraries the following command ran:
- "pip3 install dj_database_url==0.5.0 psycopg2" <- Installs Python packages and PostgreSQL adapter

To install Cloudinary the following command ran:
- "pip3 install dj3-cloudinary-storage" <- Installs Cloudinary

To install AlAuth the following command ran:
- "pip3 install django-allauth" <- Installs allauth

To istall crispy-forms the following command ran:
- "pip3 install django-crispy-forms==1.14.0"  <- Installs crispy

To install Pillow the following command ran:
- "pip3 install django Pillow" <- Installs Pillow

To install Summernote the following command ran:
- "pip3 install django-summernote" <- Installs summernote((!) Unisntalled/or Ignored by the Developer)

To install Ckeditor, the folowing command ran:
- "pip install django-ckeditor" <- Installs ckeditor((!) Uninstalled/or Ignored by the Developer)

To create or update Requirements.txt, the following command ran:
- "pip3 freeze --local > requirements.txt"  <-Runs the requirements

To install the requirements set on Requirements.txt the following command ran:
- "pip install -r requirements.txt" <- Installs requirements

To clear the cache, the following command ran:
- "pip cache purge" <- Clears the cache

The database is being hosted on ElephantSQL:
- Create an account(with GitHub) and select TinyTurtle plan.
- From Details collect the URL and paste it on Heroku Config Var.

The static files are being hosted on Cloudinary:
- Create and account (with GitHub)
- From the dashboard collect the API Environment variable and paste it on Heroku Config VAR.

...and hosted on Heroku:

- After creating an Heroku Free account, and applying for Student Pack
- Navigate to: "Create new app" add a unique name "digital-nomad" and select "Europe" region. Click "Create App"
- Head over to "Settings" tab and apply the respective config VARs
- Move to "Deploy" section and select "Github" method"
- From here search for the repository name "digitals-nomads", from the GitHub account.
- Hit "Connect" and "Enable Automatic Deploys" to keep the the repository in parallel to Heroku.
- Manually "Deploy Main Branch".
- Upon successful deployment, retrieve the link for the mock terminal.
- The live app can be found here.
