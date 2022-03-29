---
title: "Creating a Custom Tooltip Component in Vue"
date: "2020-08-28"
categories: 
  - "javascript"
---

There are plenty of libraries out there that will have you up and running with a good tooltip solution in minutes. However, if you are like me, you are sick and tired of giant dependency trees that have the distinct possibility of breaking at any time. For that reason, we're going to build a custom single file tooltip component that you can build yourself and tweak to your heart's content. It might take 15 minutes instead of 3... sorry about that.

As it happens, this is also the boilerplate for the tooltip component we use on [Qvault's coding app.](https://app.qvault.io/)

## How to make other custom Vue components

Before we move on, if you are looking for our other custom Vue.js components tutorials you can find them here:

- [Custom select component in Vue](https://qvault.io/2020/09/25/how-to-make-a-custom-select-component-in-vue-js/)
- [Custom toggle switch component in Vue](https://qvault.io/2020/07/21/how-to-create-a-custom-toggle-switch-component-in-vue-js/)
- [Custom slider component in Vue](https://qvault.io/2020/11/24/how-to-make-a-custom-slider-component-in-vue/)
- [Custom checkbox form component in Vue](https://qvault.io/2020/11/25/how-to-create-a-custom-checkbox-form-in-vue/)

## The End Goal

We are building a single file component, as such it will be a single file with the following structure:

```
<template>
  
</template>

<script>

</script>

<style scoped>

</style>
```

At the end of this walkthrough we will have a tooltip component that floats above the target element(s), fades in and out, activates on hover, and is reusable across our entire app. Let's take each section at a time.

## The HTML

```
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

## The JavaScript

```
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

```
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

```
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

```
<Tooltip
  text="Difficulty"
 >
   <span> hover over me </span>
 </Tooltip>
```
