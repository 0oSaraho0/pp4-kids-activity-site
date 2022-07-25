# Kidsbored

Kidsbored is an activity shareing site for anyone that has to entertain kids for any length of time.  It provides users a clear and simple way to browse and share ideas on things to keep kids entertained.



(images of media screens)


# Table of contents   




# User-Experience-Design

## Site Goals

The site is aimed at anyone that has to entertain children.  Without logging on the user can brows ideas on what the can do.  They will also be able to log on and share ideas of their own and comment on other peoples ideas.  They will also be able to edit and delete their ideas.

## Agile Planning

This project was developed using agile methodologies, delivering small features over 4 sprints spaced out over 5 weeks.Each issue was labeled must have, should have and could have.  The must have's were completed first, then the should have's then then could have's.  It was done this way to ensure a complete website is made with the nice to have features added if there is capasity.

My kanban board was made using github projects.  Each view can be clicked in to obtain furhter information.

(pic of issues and pic of kanan board)


The user stories were grouped into different Epics

Epic 1 - Set up

The base setup of the Django app was done first as nothing else can be completed beofre this is done. I completed the base html and header and footer. I also included deployment in this section.  

Epic 1 user stories

- As a developer, I need to set up the project so that it is ready for implementing core features
- As a developer I want to create a base HTML page so that all pages can use the same format.
- As a user I want to be able to navigate easily around the site easily on my mobile
- As site owner, I want to share social media links.
- As a developer I want to deploy to heroku early to avoid any problems later on

Epic 2 - Database model and admin.

Setting up database model and admin functions and template pages to be able to view the ideas when not logged in

Epic 2 User Stories

- As a developer I want to lay the foundations of the database to enable users to update their own posts later on.
- As a user that is not logged in, I want to be able to browse ideas from other users

Epic 3 - Setting up login signup and logout pages

Epic 3 User Stories

- As a new user, I want to be able to sign up easily and intuitively
- As a returning user, I want to be able to log in easily.
- As a user, I want to be able to log out of the site safely and easily.

Epic 4 - CRUD

Adding CRUD functionality for users adding editing and deleting ideas

Epic 4 User Stories

- As a user, I want to be able to input my own ideas of things to do into the site in an easy and intuitive way so that I can easily share ideas with others
- As a user I want to be able to comment and like other peoples ideas
- As a user, I want to be able to edit ideas I have created
- As a user, I want to be able to delete ideas that I have created
- As the site owner I want to ensure only the creator of an idea can edit or delete it

Epic 5 - Styling

Epic 5 User Stories

- As a user I want the front page to be clear and self-explanatory so I know I am in the right place
- As a developer I want to ensure the styling is correct
- As a developer I want to ensure the forms are all the same style and look good on all devices

Epic 6 - Documentation

Epic 6 Tasks

- Complete Readme documentation
- Complete testing and writeup

## Scope
- Responsive Design
- Home page with information about Kidsbored
- Ability to perform CRUD functionality on ideas
- Restricted features for not loged in users

## Structure

### Ideasbored Features

Navbar

user story - - As a user I want to be able to navigate easily around the site easily from any devise

Navigation Menu

When the user is not logged in the navigation menu links to the Home page Browse Ideas page and the Sign in page

(screen shot of nav bar)

Once the user has signed in the navigation menue changes to Home, Browse Ideas, Create Idea and Log out

(sceen shot of nav bar)

The sign in, log in, log out pages were made using allauth.

on smaller devices the menu options collapse into a button

(screen shot of mobile nav bar)

### Home Page

- 
User Story - As a user I want the front page to be clear and self-explanatory so I know I am in the right place

The front page contains a hero image of some happy children eating icecream.  This will make it evident to the user that the website is for children.

(screen shot of her image)

Under this is information about the site and how to share and brows activity ideas.

(screen shot of welcome text)

### Footer

- User Story: As site owner, I want to share social media links.

The Footer has been added to the bottom of the site and contains links to social media sites so that users can also share their ideas and promote the site via social media.

### Browse Ideas

- User Story: As a user that is not logged in, I want to be able to browse ideas from other users.

Anybody can use the webiste to brows ideas, they are shown in the brows ideas page with the activity title and picture in rows of 3.  The activity Title is a link to open up each actiity with further information about it.

(screen shot of brows ideas page)

### Idea Detail 


- User Story: As a user I want to be able to comment and like other peoples ideas

Each user story opens up to a full page which contains the image, a link to the activity website if applicable, the age range the activity is aimed at, activity cost per person, the location of the activity and a review.

Logged on users can also comment on and like the ideas.

( screen shot of idea detail page)

### Sign in, log in, log out

User Stories
- As a new user, I want to be able to sign up easily and intuitively
- As a returning user, I want to be able to log in easily.
- As a user, I want to be able to log out of the site safely and easily.

Users can sign in and out using various forms and confirmation pages. These forms were made using allauth and edited using bootstrap

(screenshots of signin out pages)

### Create Idea

- User Story: As a user, I want to be able to input my own ideas of things to do into the site in an easy and intuitive way so that I can easily share ideas with others

Once the user is logged in they can create their own idea using the create Idea form.  The forms were made using crispy forms which were used in conjunction with bootstrap.

(screenshot of create idea form)

### Edit and Delete Idea

User Stories
- As a user, I want to be able to edit ideas I have created
- As a user, I want to be able to delete ideas that I have created
- As the site owner I want to ensure only the creator of an idea can edit or delete it

The creator of an idea will be able to view edit and delete icons on their idea detail page.  The edit button will take them to the create idea form but it will lbe pre populated with information that is already saved.  The user can then update the information and save again where they will be redirected back to the ideas page.

The delete button will take the user to a confirmation page asking them to confirm they wish to delete that idea.  Once an idea is deleted all comments will be deleted with it.

The delete and edit views use LoginRequiredMixin and UserPassesTestMixin to ensure that only the idea creator who is logged in can update or delete their idea.

(screensht of edit and delete buttons and edit and delete pages)

## Features left to impliment

- I had planned to add a profile page that the user could add their picture and details about themselves.  This would also show all their ideas in one place for easy editing or deleting. Unfortunately I ran out of time to add this feature 

- Once the profile page was in place I could add an option to show the creators picture as well as name on their ideas.

- I had also planned to add search options on the brows ideas page allowing users to search by Activity name, location, price or age range.

## Wireframes

Home Page

[Home page wireframe](/static/images/home-page-wireframe.png)

















