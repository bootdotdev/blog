---
title: "Creating a Custom Tooltip Component in Vue"
author: Lane Wagner
date: "2020-08-28"
categories: 
  - "javascript"
images:
  - /img/800/Copy-of-Bcrypt.webp
---

There are plenty of libraries out there that will have you up and running with a good tooltip solution in minutes. However, if you are like me, you are sick and tired of giant dependency trees that have the distinct possibility of breaking at any time. For that reason, we're going to build a custom single file tooltip component that you can build yourself and tweak to your heart's content. It might take 15 minutes instead of 3... sorry about that.

As it happens, this is also the boilerplate for the tooltip component we use on [boot.dev's coding app.](https://boot.dev/)

## The End Goal

We are building a single file component, as such it will be a single file with the following structure:

```html
<template>
  
</template>

<script>

</script>

<style scoped>

</style>
```

At the end of this walkthrough we will have a tooltip component that floats above the target element(s), fades in and out, activates on hover, and is reusable across our entire app. Let's take each section at a time.

## The HTML

```html
<template>
  <div class="tooltip-box">
    <slot />
    <div
      class="tooltip"
    >
      <span
        class="text"
      >{{ text }}</span>
    </div>
  </div>
</template>
```

Fairly simple setup here. We need:

- An outer `tooltip-box` to encapsulate the entire component and ensure positioning.
- A slot tag to inject the child component (whatever is hovered over to show the tooltip).
- A `span` that will house the text of our tooltip.

{{< cta1 >}}

## The JavaScript

```js
export default {
  props: { 
    text: {
      type: String,
      required: true
    }
  }
};
```

Pretty straightforward, all we need is a required prop for our users to specify what they want the tooltip to say.

## The CSS

```css
.tooltip-box { 
  position: relative;
  display: inline-block;
}

.tooltip-box:hover .tooltip{
  opacity: 1;
}

.tooltip { 
  color: #ffffff;
  text-align: center;
  padding: 5px 0;
  border-radius: 2px;
  
  width: 120px;
  bottom: 100%;
  left: 50%;
  margin-left: -60px;

  opacity: 0;
  transition: opacity 1s;

  position: absolute;
  z-index: 1;

  background: #a782e8;
}

.text::after {
  content: " ";
  position: absolute;
  top: 100%;
  left: 50%;
  margin-left: -5px;
  border-width: 5px;
  border-style: solid;
  border-color: #a782e8 transparent transparent transparent;
}
```

The CSS is certainly the most interesting part. A couple key points:

- We need to ensure the top-level element, `tooltip-box` is positioned relatively so that our absolute positioning works.
- We use an opacity transition to fade the tooltip in and out of view.
- The `z-index` property ensures that the tooltip is on top of whatever it needs to hover over.
- The `.text::after` property creates the little triangle pointer at the bottom of the tooltip

The full component:

```html
<template>
  <div class="tooltip-box">
    <slot />
    <div
      class="tooltip"
    >
      <span
        class="text"
      >{{ text }}</span>
    </div>
  </div>
</template>

<script>
export default {
  props: { 
    text: {
      type: String,
      required: true
    }
  }
};
</script>

<style scoped>
.tooltip-box { 
  position: relative;
  display: inline-block;
}

.tooltip-box:hover .tooltip{
  opacity: 1;
}

.tooltip { 
  color: #ffffff;
  text-align: center;
  padding: 5px 0;
  border-radius: 2px;
  
  width: 120px;
  bottom: 100%;
  left: 50%;
  margin-left: -60px;

  opacity: 0;
  transition: opacity 1s;

  position: absolute;
  z-index: 1;

  background: #a782e8;
}

.text::after {
  content: " ";
  position: absolute;
  top: 100%;
  left: 50%;
  margin-left: -5px;
  border-width: 5px;
  border-style: solid;
  border-color: #a782e8 transparent transparent transparent;
}
</style>
```

And how to use it:

```html
<Tooltip
  text="Difficulty"
 >
   <span> hover over me </span>
 </Tooltip>
```
