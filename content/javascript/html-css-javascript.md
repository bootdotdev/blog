---
title: "HTML vs CSS vs JavaScript Explained"
author: Jamie Dunmore
date: "2021-09-27"
categories: 
  - "misc"
images:
  - /img/800/HTML-vs-CSS-vs-JavaScript-min.webp
---

HTML, CSS, and JavaScript are the most important tools in your arsenal for all your web design escapades. Rather than compete, they complement and augment each other, and their power expounds when they're combined -- like internet Power Rangers.

JavaScript brings HTML to life, CSS makes HTML beautiful, and HTML gives JavaScript and CSS their structure on a web page. Here we'll run through the major differences between HTML, CSS, and JavaScript as programming languages.

![](/img/800/HTML-CSS-JavaScript-power-rangers-min.jpg)

When they combine forces they're unstoppable -- the internet's Power Rangers.

## What are HTML, CSS and JavaScript?

Here's a TL;DR mixed in with a Frankenstein reference, if that's your thing.

Imagine you're building your own version of Frankenstein's monster.

You need bones (the structure), skin (the aesthetics), and you need to make it come to life (the interactivity).

That's how you build a webpage, too:

![building a webpage with HTML, CSS and JavaScript](/img/800/Building-a-webpage-with-HTML-CSS-and-JavaScript-min-1024x576.png)

### HTML

HTML makes up this web page's skeleton and structure, and almost every other web page you’ll ever visit. It’s a markup language that "marks up" and forms the backbone to online content, putting the site structure in place for the web browser to understand.

HTML, or Hypertext Markup Language, was first proposed and published in 1993, though its roots trace back to proposals by Sir Tim Berners-Lee in 1989 for an internet hypertext system. It’s developed by WHATWG, with the latest version, HTML5, currently in place.

### CSS

Whereas HTML makes up the structure, or bones, of the site, CSS adds the skin - the aesthetics you see and navigate. The CSS on a webpage designs it and makes it look more attractive for the visitor reading the page.

CSS, or Cascading Style Sheets, shape the HTML and affects how it's displayed to the website visitor. These forms of styling include font color, background color, border-radius (rounded corners on boxes), the position of columns, hue, opacity, and separation. New CSS features even allow for animations, flexbox gaps, and much more responsive design.

### JavaScript

JavaScript (JS) is another key language for web page design and inserts dynamic text into HTML client-side.

It’s a scripting language rather than a markup language, and was first released two years after HTML in 1995, developed by Brendan Eich of Netscape, a now-defunct web browser. JavaScript is maintained by the ECMA and as of 2021, the 12th version of ECMA is active.

The main three languages used in web page development are HTML, CSS, and JavaScript. In general:

> HTML provides the structure, CSS provides the presentation and formatting, and JavaScript makes the elements dynamic and controls their behavior.

{{< cta1 >}}

## HTML, CSS & JavaScript: What do they do?

HTML gives structure to web pages using each different element, and can also affect font, color, hyperlinks, and images. HTML files have either `.html` or `.htm` extensions when stored.

You would use HTML to tell the browser which of the content on your site is the title, which is your H2 and H3 headings, and any images or tables you have on your web page.

CSS is inserted into HTML using the `<style>` element, and affects how the HTML looks and where it is positioned. Some other examples of CSS are:

- Changing the sizes, colors and shading in tables
- Changing the styles, size or color of bullet pointed lists (like this one)
- Changing link color and style (our buttons are `#c08f54` to match our brand color)
- Switching to italics or bold text to _really make_ **your point**

CSS doesn't make web pages interactive or dynamic, however, but better styles HTML for aesthetics and presentation, giving it a better structure.

JavaScript can be added to these pages to more them more dynamic and interactive. For example, JavaScript can make buttons clickable to take you to your chosen destination, and lets you design on-page calculators and other widgets. It doesn’t replace HTML, it complements it to create dynamic and interactive content.

HTML elements include `<p>` paragraph tags, `<h1>` and other heading tags, and many other elements for structuring web pages. JavaScript doesn't use tags, instead it uses functions and data structures to manipulate the code. However, you need to use the `<script>` element to insert JavaScript into HTML.

**An example of HTML, CSS & JavaScript uses**

HTML is used to create the static structure of a page. For example, if I wanted the H3 heading of a new boot.dev page to say "Boot.dev is the best computer science education site", with a paragraph underneath reinforcing this by saying "And if you disagree, try out our courses and be convinced!", you could easily implement this structure with the following HTML code:

```
<h3> Boot.dev is the best computer science education site </h3>

<p> And if you disagree, try out our courses and be convinced! </p>
```

And it would render the following on a web page:

![](/img/800/HTML-example-web-page.jpeg)

However, this content is the boring HTML default, and you may want to style it differently. You can make the content look better by adding styling via CSS, and by adding JavaScript you can make the content interactive.

CSS can then be added to format and style the content (and any other elements on the page).

A very basic simplistic example would be to change the color of the H3 heading title text to white on a black background, change the paragraph text to blue, and the background color to grey, by writing the following CSS:

```
body {
  background-color: lightgrey;
  color: blue;
}

h3 {
  background-color: black;
  color: white;
}
```

So that your original HTML changes to:

![](/img/800/CSS-example-code.jpeg)

This obviously doesn't look great yet, but shows how CSS changes the style of your content.

CSS does far more than just changing text and background colors, with new features being released all the time and now even supporting animations - you can do almost anything with CSS for web design.

JavaScript can then be added to bring these styled pages (via the CSS) pages to life. This could be as simple as making a button clickable, taking a customer to the checkout page, or for clicking to read another news article, or inputting a math sum into an online calculator that returns the answer to any numbers you select.

You can create more complex calculators fairly easily by adding more elements within a JavaScript function, such as developing an interest rate calculator based on inputs of the original starting amount invested, based on a certain interest rate, and based on a certain amount of time. 

## HTML vs CSS vs JavaScript: Which is easier to learn?

HTML is much easier to learn than JavaScript and is considered the easiest language to learn. You can learn most of HTML from a complete beginner level to coding your own (basic) HTML in just a day or two, but just knowing HTML won't land you a coding job.

You can't learn CSS without already understanding HTML - the two are an inseparable married couple. They're nothing without each other - CSS needs HTML to give it structure, HTML needs CSS to make it look pretty.

CSS is more complex, with far more options and factors at play. You could easily spend a few months getting to grips with some of CSS' wide range of uses and code a few of your own basic web design projects.

For web design work you'll need strong HTML and CSS skills, as well as good command of JavaScript, and potentially extras such as JavaScript libraries (like Node.js, React, and Vue.js), and perhaps skills in languages like PHP, Python, Ruby, or SQL.

JavaScript is a true programming language that follows programming logic, and is, therefore, more complex. CSS might be hard to master, but without logic, errors are less troublesome. JavaScript will likely take longer to grasp than CSS, but both are notably more difficult than HTML.

Despite this, JavaScript and Python are still considered two of the easiest programming languages to learn and are recommended for beginners. Compared to languages like C++ and Java, both Python and JavaScript have far shallower learning curves.

### HTML: Is it a programming language? The debate

HTML’s lack of executable logic has led to intense debates around whether it is a programming language or not. 

HTML isn’t executable; it marks up pages with tags for the browser to infer the purpose for the viewer. As a markup language, you can’t carry out executable tasks in HTML, for example, you couldn’t add two numbers together.

A quote from [this art](https://ischool.syr.edu/why-html-is-not-a-programming-language/#:~:text=HTML%20is%20used%20for%20structural,web%20page%2C%20not%20functional%20ones.&text=Programming%20languages%20have%20functional%20purposes,HTML%20contains%20no%20programming%20logic.)[i](https://ischool.syr.edu/why-html-is-not-a-programming-language/#:~:text=HTML%20is%20used%20for%20structural,web%20page%2C%20not%20functional%20ones.&text=Programming%20languages%20have%20functional%20purposes,HTML%20contains%20no%20programming%20logic.)[cle](https://ischool.syr.edu/why-html-is-not-a-programming-language/#:~:text=HTML%20is%20used%20for%20structural,web%20page%2C%20not%20functional%20ones.&text=Programming%20languages%20have%20functional%20purposes,HTML%20contains%20no%20programming%20logic.) on the Syracuse University School of Information Studies elaborates:

> "Programming languages have functional purposes. HTML, as a markup language doesn’t really "do" anything in the sense that a programming language does. HTML contains no programming logic."

Therefore, without programming logic, some do not consider it a programming language. Nevertheless, when you write in HTML you are still coding, and HTML5 brings a wealth of new extras like geolocation and multimedia to web page design, so HTML’s importance shouldn’t be questioned, whether you agree or disagree with it being a programming language.

{{< cta2 >}}

## Differences between HTML, CSS and JavaScript, and how they work together

HTML can combine JavaScript within scripts that convert HTML's static form into dynamic content by modifying the web page contents without reloading the page. However, the reverse cannot occur. JavaScript doesn't really embed HTML.

HTML tells the web page what it should display rather than how it should display it, whereas JavaScript instructs the web page on how exactly the data and content should be displayed. 

## HTML vs JavaScript: Browser compatibility

HTML is compatible with all browsers, whereas JavaScript can occasionally run into compatibility issues due to different versions of the language being supported by different browsers. Additionally, some browsers (or their users), turn off JavaScript completely, which unsurprisingly breaks most websites.

However, all major browsers support dynamic JavaScript content and unless you use an outdated or extremely niche browser, you'll never run into any JS compatibility issues.

## HTML vs JavaScript: server-side or client-side

HTML is typically rendered from the server-side as it is static and therefore doesn't need anything client-side. It’s usually processed by the server before it’s ever sent to the user. That said, new front-end frameworks like React and Vue actually render the HTML in the JavaScript code on the front-end, which is still a relatively new idea.

JavaScript is a client-side scripting language where it is internally compiled and then interpreted before the scripts or functions are executed client-side. Because JavaScript is run on the user’s machine, it’s not secure -- you should never process passwords or any other sensitive data in JavaScript.

{{< cta3 >}}

## HTML vs CSS vs JavaScript: Add-ons and libraries

What you see is what you get with HTML - it has no supporting libraries.

With JavaScript, however, you have a wide variety of libraries and frameworks for different uses, such as React, Ember, Vue, Svelte, and Angular.

Even CSS has a number of great supporting frameworks - Tailwind, Bootstrap, Foundation, and CSS Wand, for example - aiding front-end development.
