
# Digital Nomads
- Digital Nomads is a website that allows developers to share their experiences outside the office.
- No desks, no cubicles, no offices.
- It is a platform for nomads in the digital world to share their personal adventures, tips and recommendations when working and exploring the world.

# Live Project
- The live website can be found [here](https://digital-nomad.herokuapp.com/).

# Purpose of the website.
- To provide a platform where users can share their stories as Digital nomads.
- To promote the idea that Developers can be flexible on the job, while working and traveling.
- To create a community and connect users in a "guild" of like minded people.
- To allow users to share their ideas and help each other both in front and behind the screen.

# Features and Functionality for non-reg./reg Users & Superusers

## Non-Registered Users (Visitors)
- Visitors can read all posts from /home/.
- Visitors can read all users posts from /username/
- Visitors can create a User account through /register/
- Visitors can navigate to the Home/About/Login/Register pages
- Visitors can navigate through the pagination of /home/ and /username/
- Visitors can access external links on users posts/comments and footer.

## Registered Users (CRUD) can do the above as a Visitor, moreover:
- Users can Log In/Out through the "Log In/Out" functionality".
- Users can create posts through the "Post" functionality.
- Users can update their posts through the "Update" functionality.
- Users can delete their posts through the "Delete" functionality.
- Users can like/dislike all posts through the "Like/Dislike" functionality.
- Users can navigate to the Profile tab and update their "Bio".
- Users can navigate to the Profile tab and upload a Profile pipcture.

- Comments cannot be deleted by anyone, except Superusers.

## Superusers can manipulate information through the /admin/ panel.
- CRUD posts
- Change Password passwords
- Create/Update/Delete users
- Delete Comments
- Promote Users to Superuser

(ELABORTATE...)

# Design
## Navbar, Header & Favicon
- The Navbar features from left to right the [Logo], [Home], [About], [Login], [Register] and the [Search] fields. Furthermore for Users who are logged in, the [Post], [Profie] and [Logout] links. The links guide Users to the respective pages and remain "active" when and if on that page, with the exception of [Post].
- The Header features an image that splits in half, sharing the rest with the Footer. The screen of a Laptop can be seen together with the Logo of the website.
- On the browsers tab, the Favicon and Logo of the website can be found. A red gear.

<img src="media/readme_img/headernavpanel.png" alt="Navigation & Header">

## Footer
- The Footer is best defined by Bootstraps template. It features a Slogan on the left side and on the right the Social Media links. At the very bottom, a copyright notice.
- Above the Footer is the rest of the image shared with the Header. The keyboard of a laptop.
- Users can open the Social Media links in new tabs.

<img src="media/readme_img/footerpanel.png" alt="Footer">

## Home: Posts & Pagination
- The Homepage renders all of the Posts that Users create.
- If Users are logged in, then they are greeted with a message followed by their Usernmes.
- If no Posts are present in the board of Home, then the Homepage displays a message encouraging Users to create a Post.

<img src="media/readme_img/nopostspanel.png" alt="No Posts">

- If the Forum has been populated with Posts, then the Posts are displayed and organized in a vertical fashion, with the newst at the top and the oldest at the bottom.
- Per Post the Username, Picture, Date, Title, and Body truncated by 50 words are displayed.
- For every 6 posts, a new page for Pagination is created and Users can easily navigate from page to page.

<img src="media/readme_img/pagination.png" alt="Pagination">

## About
- The About page renders a small section of advertisement and information about the website. It also encourages users to either Log in or Register an account.

<img src="media/readme_img/aboutpanel.png" alt="About">

## Posts & Comments
- When Opening a Post, the details of that particlar Post is expanded, allowing Users to read the whole article.
- Users can read and engage with the Post, by leaving Comments and Likes.

<img src="media/readme_img/openpostandcommentpanels.png" alt="Open Posts and Comments">

## Search Field
- Users can use the Search functionality.
- Upon making a valid search, the page should retrieve a list of Threads, by a word populated either in the Title, Body or Username of a Post.

<img src="media/readme_img/charactersearch.png" alt="Search Field">

- If no Post exhibit such word, than a template prompts users to give in a valid word.

<img src="media/readme_img/wrongcharactersearch.png" alt="Search Field">

- Otherwise, if not character was introduced in the search field, Users are requested to input a valid character.

<img src="media/readme_img/nocharactersearch.png" alt="Search Field">

## User Profile
- The User profile can be best defined as a "Settings panel", where users can update their personal info.
- The fields that can be updated include Username, Profile picture, E-mail and Bio.

<img src="media/readme_img/profile.png" alt="Profile">
s
- Upon updating the Bio the User should have an Overview field.

<img src="media/readme_img/overviewpanel.png" alt="Overview">

- If a User created an account, but did not make any Posts, even though made Comments. The User profile remains inactive.

<img src="media/readme_img/usernopostspanel.png" alt="User no Profile">

## Registration & Deletion
- The Registration page requests that Users input a Username, E-mail and Password.

<img src="media/readme_img/registerationpanel.png" alt="Error 404">

## Log in/out
- The Log in page demands Users to input valid credentials, as per registered.

<img src="media/readme_img/loginpanel.png" alt="Log in">

- By Logging out, Users are fired with a Goodbye message.

<img src="media/readme_img/logoutpanel.png" alt="Log out">

## Deletion

<img src="media/readme_img/deletionpanel.png" alt="Deletion">

<img src="media/readme_img/deletionconfirmedpanel.png" alt="Deleted">

## Error 404
- If a User goes to a non-defined URL, then a 404 Error template is rendered, requesting users to leave that page.

<img src="media/readme_img/404.png" alt="Error 404">


Navbar items Home, About, Regions, Logo, Search, Bucket List, Write Post, Logout and Profile are available for registered users.
The Navbar is fixed to the top of the screen even when the user is scrolling down the page to allow easier navigation.
The logo is linked to the Homepage and each menu item is linked to each page respectively to allow easier navigation.
The search bar allows users to easily search for a keyword they are looking for.
The navigation menu collapses on small/medium devices to optimise the menu for smaller screen sizes, as per Bootstrap.

## Development Process
The project started out as a forum for Ads of Events, where users could post Events taking place at a certain time in a certain location.
Users would therefore open up a thread give a brief description of the Event, target the location with Google Maps API and set the Date. After an event took place, it ought to be automatically deleted.

In the end, this project was simplified due to dateline limitations and time conciliations. It makes good use of familiar concepts such as Create Read Update Delete.
Upon re-creating this project, the developer resorted the idea of a "forum" or "discussion board", similar to [reddit](https://www.reddit.com/) but more focused on the nomadic lifestyle.

## Features

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
