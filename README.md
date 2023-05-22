
# Digital Nomads
- Digital Nomads is a website that allows developers to share their experiences outside the office.
- No desks, no cubicles, no offices.
- It is a platform for nomads in the digital world to share their personal adventurers on the road, tips and recommendations when working and exploring the world in the great outdoors.

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

## Development
The project started out as a forum for Ads of Events, where users could post Events taking place at a certain time in a certain location.
Users would therefore open up a thread give a brief description of the Event, target the location with Google Maps API and set the Date. After an event took place, it ought to be automatically deleted.

In the end, this project was simplified due to dateline limitations and time conciliations. It makes good use of familiar concepts such as Create Read Update Delete.
Upon re-creating this project, the developer resorted the idea of a "forum" or "discussion board", similar to [reddit](https://www.reddit.com/) but more focused on the nomadic lifestyle.

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
