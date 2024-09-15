# Transmit

Welcome to Transmit, your go-to platform for community-driven content and discussions! Inspired by the popular Reddit model, Transmit brings together users from all walks of life to share, discuss, and vote on topics that matter most to them.

---

## Design

---

### Colour scheme

Transmit colour palette

- The website has 2 main color #004aad and #f15226
- However, most of the page hads white back ground easier to see
- For normal text the default color of the browser is used.
- The colour scheme is consistent throughtout the whole website.

### Typography

---
No External fonts have use.

## Features

---

### General Features on each page

---
All the pages on the website have :

- A favicon which is the centre part of the Trasmit.
- A navbar which allows the users to easily navigate through the site. On mobile devices and on tablet device the navbar is collapsed into a burger icon with a dropdown navbar.
- A footer which contains links to the social media accounts.

#### Home(index) Page

---
The Home Page is card like sections which will show community name post title and content:
- community name should redirect to community detail page
- post title should redirect to post detail page

The Home page provides information about all the post that has been done by all community.


#### Community detail page

---
The Community detail page shows the overview of all the post that has been created within the community
- it has button to join the community
- it has button to create a new post
- It has user name which will redirect to the user profile
- it also has post tile which will redirect user to post detail along side post content


#### Post detail page

---
The Post detail page shows the post user has click in full details with the option of voting and commenting
- it has button to edit/delete the post
- it has user name which will redirect to user profile page
- it has button to upvote/downvote the post
- it has a form to comment on the post
- it has button to edit/delete the comment


#### User profile page
The User profile page shows the post user has made withing any community
- it has user name
- it has community name which will redirect to community detail page
- it has post title which will redirect to post detail page
- it also have draft post which only current user can see

#### Future Features

---

- Draft post will be better render easier to find
- when creating post from the community the community name will be automatically filled
- better UI will be added so user have better understanding about the page
- user will be able to add images, videos, banner and more
- comment will be better so user can comment on other user comment aswell
- community description rules and policy will be added for user to have safe environment#
- community will be able to pick tags and from that their will be a search bar
- logo will be added

---

## Transmit - TESTING DOCUMENTATION

---

## AUTOMATED TESTING

### Django automated testing

- test_forms.py for forms automated testing have been done
- test_views.py for views automated testing have been done
  
### W3C Validator

[W3C](https://validator.w3.org/) was used to validate all HTML pages, as well as the [CSS](https://jigsaw.w3.org/css-validator/#validate_by_uri).
  
- html page W3C HTML Validation - Pass
- style.css CSS Validation - Pass
- script.js JavaScript Validation - Pass

---

## Manual Testing

### Responsiveness

---

Each page has been inspected on variety of devices such as mobile, laptop, desktop. Moreover, they have been tested on multiple browser such as Google, Microsoft edge.

### Validation

- The header section:
  - Transmit has a clickable link to the Home page.
  - Home page has a clickable link to the Home page.
  - My profile has a clickable link to the user profile page.

- The footer section:
  - Facebook Font Awesome has a clickable link to the Facebook page.
  - Instagram Font Awesome has a clickable link to the Instagram page.
  - Twitter(X) Font Awesome has a clickable link to the Twitter(X) page.
  - Youtube Font Awesome has a clickable link to the Youtbe page

## Accessibility

---
Care has been taken throughout the coding to ensure that this website is as accessible friendly as possible. Particular attention has been given to the following points:

- Ensuring sufficient contrast between the text and its respective background.
- Using a bootstrap for the buttons for the buttons and the text input fields.

## Technologies used

#### Frameworks, Libraries & Programs Used

- [Favicon.io](https://favicon.io/) - To create and download the favicon logo.
- [Google HTML/CSS style guide](https://google.github.io/styleguide/htmlcssguide.html) - To create proper pages with rules.
- [Font awesome](https://fontawesome.com/) - for the social media and navbar burger icons.
- [W3C HTML validator](https://validator.w3.org/) - To validate all the HTML file.
- [W3C CSS validator](https://jigsaw.w3.org/css-validator/) - To validate CSS file.
- [Google Dev tools](https://developer.chrome.com/docs/) - to troubleshoot and test issues during the development.
- [MDN webdocs](https://developer.mozilla.org/en-US/) - reference
- [W3C schools](https://www.w3schools.com/) - for resolving code format in CSS and HTML.
- [Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/) - for design and css.

## Deployment

---
 This site was deployed using the following steps:

1. Open GitHub.
2. Select the project to be deployed.
3. Go to 'Settings'.
4. In the Code and Automation section, select Pages.
5. Set Source to 'Deploy from a branch'.
6. Select Main Branch.
7. Set Folder to 'Root'.
8. Under Branch click 'Save'
9. The link to the live website is now displayed at the top of the page.

### Local development

---

#### How to Fork

1. Log in to Github.
2. Go to the repository for this project.
3. At the top right of the page, click the "Fork" button. This will create a copy of the repository under your Github account.

#### How to clone

1. Log in to Github.
2. Go to the repository for this project.
3. Click on the "Code" button, select from HTTPS, SSH or Github CLI.
4. Copy the URL for the repository.
5. Open your terminal or command prompt.
6. Navigate to the directory where you want to clone your repository.
7. Use the `git clone` command followed by the URL that you have copied.


