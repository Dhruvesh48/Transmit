# Transmit

Welcome to Transmit, your go-to platform for community-driven content and discussions! Inspired by the popular Reddit model, Transmit brings together users from all walks of life to share, discuss, and vote on topics that matter most to them.

![Screenshot of all the pages and responsiveness of the project](/docs/home-page-responsive-image.png)
Visit the deployed site here :[Medical History](https://dhruvesh48.github.io/Project-1-html-css/)

---

## Design

---

### Colour scheme

Transmit colour palette

![Colour palette](docs/colour-palette.png)

- The website has 2 main color #004aad and #f15226
- However, most of the page had white back ground easier to see
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

![Home page image](docs/home-page-responsive-image.png)

#### Community detail page

---
The Community detail page shows the overview of all the post that has been created within the community
- it has button to join the community
- it has button to create a new post
- It has user name which will redirect to the user profile
- it also has post tile which will redirect user to post detail along side post content

![More topic page image](docs/more-topic-responsive-page.png)

#### Post detail page

---
The Post detail page shows the post user has click in full details with the option of voting and commenting
- it has button to edit/delete the post
- it has user name which will redirect to user profile page
- it has button to upvote/downvote the post
- it has a form to comment on the post
- it has button to edit/delete the comment

![Sign up page image](docs/signup-responsive-page.png)

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
  
### W3C Validator

[W3C](https://validator.w3.org/) was used to validate all HTML pages, as well as the [CSS](https://jigsaw.w3.org/css-validator/#validate_by_uri).
  
- [Home page W3C HTML Validation](docs/home-page-HTML-validator.png) - Pass
- [More-topic page W3C HTML Validation](docs/more-topic-HTML-validator.png) - Pass
- [sign up page W3C HTML Validation](docs/signup-HTML-validator.png) - Pass
- [style.css CSS Validation](docs/CSS-validator.png) - Pass

---


### Desktop Results

- Home page

  ![Home Page Lighthouse testing desktop](docs/home-page-desktop-lighthouse.png)
- More-topic page

  ![more-topic page Lighthouse testing desktop](docs/more-topic-desktop-lighthouse.png)
- Sign up page

  ![sign up page Lighthouse testing desktop](docs/signup-desktop-lighthouse.png)

### Mobile Results

- Home page

  ![Home Page Lighthouse testing desktop](docs/home-page-mobile-lighthouse.png)
- More-topic page

  ![more-topic page Lighthouse testing desktop](docs/more-topic-mobile-lighthouse.png)
- Sign up page

  ![sign up page Lighthouse testing desktop](docs/signup-mobile-lighthouse.png)

## Manual Testing

### Responsiveness

---

Each page has been inspected on variety of devices such as mobile, laptop, desktop. Moreover, they have been tested on multiple browser such as Google, Microsoft edge.

![Medical History responsiveness include all pages](docs/Multiple-page-responsive.png)

- Home page Mobile device
  
![Home page Mobile device](docs/home-page-mobile-device.png)

- More topic page Mobile device

![More topic page Mobile device](docs/more-topic-mobile-page.png)

- Sign up page Mobile device

![Sign up page Mobile device](docs/signup-mobile-page.png)

- Home page Desktop device
  
![Home page Desktop device](docs/home-desktop-page.png)

- More topic page Desktop device

![More topic page Desktop device](docs/more-topic-desktop-page.png)

- Sign up page Desktop device

![Sign up page Desktop device](docs/signup-desktop-page.png)

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
- [ui.dev](https://ui.dev/amiresponsive) - To create views of the website on different viewing devices.
- [Google Fonts](https://fonts.google.com/) - for importing the font families used.
- [Font awesome](https://fontawesome.com/) - for the social media and navbar burger icons.
- [W3C HTML validator](https://validator.w3.org/) - To validate all the HTML file.
- [W3C CSS validator](https://jigsaw.w3.org/css-validator/) - To validate CSS file.
- [Google Dev tools](https://developer.chrome.com/docs/) - to troubleshoot and test issues during the development.
- [MDN webdocs](https://developer.mozilla.org/en-US/) - reference
- [W3C schools](https://www.w3schools.com/) - for resolving code format in CSS and HTML.
- [Huemint](https://huemint.com/brand-intersection/) - for choosing the color palettes.
- [Compress-or-Die](https://compress-or-die.com/webp) - for compressing the image and changing its format to webp.
- [Flaticon](https://www.flaticon.com/free-icons/injection) - for favicon icon image.

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

## Credits

### Content

- The text in index.html in the section First rabies vaccine the first opening section about Louis Pasteur and the boy is taken from [CDC](https://www.cdc.gov/mmwr/preview/mmwrhtml/00000572.htm#:~:text=On%20July%206%2C%201885%2C%20Louis,rabid%20dog%202%20days%20before)

### Media

- Home page
  - Starting image and First vaccination section image is from [wikipedia](https://en.wikipedia.org/wiki/Edward_Jenner)
  - Vaccination section image is from [Queen Camel Medical Centre](https://www.queencamelmedicalcentre.co.uk/flu-and-covid-vaccinations/)
  - Variolation section image is from [Journal of Trauma and Injury](https://www.jtraumainj.org/journal/view.php?number=1218)
  - First rabies vaccine section image is from [PBS](https://www.pbs.org/newshour/health/louis-pasteurs-risky-move-to-save-a-boy-from-almost-certain-death)
  - Development of Vaccines section image is from [Understanding Animal Research](https://www.understandinganimalresearch.org.uk/resources/infographics/history-of-vaccines-timeline)
  - Elimination Efforts section image is from [Freepik](https://www.freepik.com/vectors/virus-eradication/5)

- More topic page
  - History of Pandemics section image is from [My Bio source](https://www.mybiosource.com/learn/history-of-pandemics/)
  - First medical drug section image is from [ATSE](https://www.atse.org.au/news-and-events/article/what-was-the-first-medicine-to-be-invented-in-a-laboratory/)
  - Development in surgery section image is from [LP FERGUSSON](https://lpfergusson.com/2016/05/13/barber-surgeons/)
  - History of child birth section image is from [The Guardian](https://www.theguardian.com/books/2021/jan/26/i-enjoyed-researching-the-bloody-history-of-childbirth-then-i-had-a-baby-outlawed-anna-north)
  - Development in health care section image is from [NIHR](https://bepartofresearch.nihr.ac.uk/articles/history-healthcare-research/)
  - More updates coming soon section image is from [The Fortis Lite](https://panel.com.sg/portfolio/more-coming-soon/)

- Sign up page
  - Background image is from [The Royal Society of Medicine](https://www.rsm.ac.uk/sections/history-of-medicine-society/)
