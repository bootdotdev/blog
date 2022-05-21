---
title: "How to Make a Custom Slider Component in Vue"
author: Lane Wagner
date: "2020-11-24"
categories: 
  - "javascript"
images:
  - /img/800/vue-custom-slider.webp
---

Creating a custom slider component can be tricky, especially if you want to create a lean standalone Vue component. In this quick article, you’ll learn how to build a fully customizable slider component in Vue. Feel free to swap out the majority of the CSS to get the styling you want, but I'll give you a good jumping-off point.

In fact, the component we'll be building is the exact same component that we use in production, and you can see it in action in the signup workflow for our [coding courses](https://boot.dev/).

You can see a [full demo on codesandbox here](https://codesandbox.io/s/custom-vue-slider-component-8esy1). If you're like me, you prefer to build your own lightweight UI components, rather than import a bloaty library that you don't have the ability to modify and change easily.

## The HTML

```html
<template>
  <div>
    <div class="slider-component">
      <div class="slidecontainer">
        <input
          ref="input"
          v-model="currentValue"
          type="range"
          :min="min"
          :max="max"
          class="slider"
          @input="onInput"
        >
      </div>
    </div>
  </div>
</template>
```

That wasn't so bad right? We are building out the data model in such a way the in order to use the component we can sue the built-in `v-model` property.

## The JavaScript

```js
export default {
  props: {
    value: {
      type: Number,
      required: true
    },
    min: {
      type: Number,
      required: true
    },
    max: {
      type: Number,
      required: true
    }
  },
  data(){
    return {
      currentValue: this.value
    };
  },
  methods: {
    onInput() {
      // this.currentValue is a string because HTML is weird
      this.$emit('input', parseInt(this.currentValue));
    }
  }
};
```

Like I mentioned above, this sets up the use of `v-model`. We set the default `currentValue` to the `this.value` prop, and by emitting the current value with the `@input` hook, we are good to go.

{{< cta1 >}}

## The CSS

You may not be here for exactly my styling, but you're probably here so that you can swap out the styling. Feel free to copypasta my CSS and swap it our for your own sutff!

```css
.slider-component .slidecontainer {
	width: 100%;
}

.slider-component .slidecontainer .slider {
	-webkit-appearance: none;
	appearance: none;
	width: 100%;
	height: 4px;
	border-radius: 2px;
	background: #c2c2c2;
	outline: none;
	opacity: 0.7;
	-webkit-transition: .2s;
	transition: opacity .2s;
}

.slider-component .slidecontainer .slider:hover {
	opacity: 1;
}

.slider-component .slidecontainer .slider::-webkit-slider-thumb {
	-webkit-appearance: none;
	appearance: none;
	width: 18px;
	height: 18px;
	background: #D8A22E;
	cursor: pointer;
	border-radius: 50%;
}

.slider-component .slidecontainer .slider::-moz-range-thumb {
	width: 18px;
	height: 18px;
	background: #D8A22E;
	cursor: pointer;
	border-radius: 50%;
}
```

The important thing to note here is that we're overriding the browsers defaults and setting up all of our own stuff.

## Full Component

```html
<template>
  <div>
    <div class="slider-component">
      <div class="slidecontainer">
        <input
          ref="input"
          v-model="currentValue"
          type="range"
          :min="min"
          :max="max"
          class="slider"
          @input="onInput"
        >
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    value: {
      type: Number,
      required: true
    },
    min: {
      type: Number,
      required: true
    },
    max: {
      type: Number,
      required: true
    }
  },
  data(){
    return {
      currentValue: this.value
    };
  },
  methods: {
    onInput() {
      // this.currentValue is a string because HTML is weird
      this.$emit('input', parseInt(this.currentValue));
    }
  }
};
</script>

<style scoped>
.slider-component .slidecontainer {
	width: 100%;
}

.slider-component .slidecontainer .slider {
	-webkit-appearance: none;
	appearance: none;
	width: 100%;
	height: 4px;
	border-radius: 2px;
	background: #c2c2c2;
	outline: none;
	opacity: 0.7;
	-webkit-transition: .2s;
	transition: opacity .2s;
}

.slider-component .slidecontainer .slider:hover {
	opacity: 1;
}

.slider-component .slidecontainer .slider::-webkit-slider-thumb {
	-webkit-appearance: none;
	appearance: none;
	width: 18px;
	height: 18px;
	background: #D8A22E;
	cursor: pointer;
	border-radius: 50%;
}

.slider-component .slidecontainer .slider::-moz-range-thumb {
	width: 18px;
	height: 18px;
	background: #D8A22E;
	cursor: pointer;
	border-radius: 50%;
}
</style>
```
