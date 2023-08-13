---
title: "Keyup and Keydown Event Handlers in Vue 3"
author: Lane Wagner
date: "2022-09-04"
categories: 
  - "javascript"
  - "vue"
images:
  - /img/800/photo-1555532538-dcdbd01d373d.avif.webp
---

I recently spent *far too long* fighting with Vue's `keyup` and `keydown` functionality while building [Boot.dev's](https://boot.dev) front-end. I wanted to handle `ctrl+period` keyboard events and it took me *forever* to find the part of the documentation that addressed my use case. Hopefully, this guide can save you some time!

**Take note: This guide is for Vue 3! If you're on Vue 2, find a different guide.**

## @keyup and @keydown

Some default keypress scenarios are quite simple. For example, want to capture when someone presses the "enter" key? You can do:

```html
<input @keyup.enter="onPressEnter" />

```

Or maybe you want your event to fire when the key is *pressed*, rather than when it's *released*:

```html
<input @keydown.enter="onPressEnter" />
```

Keep in mind that the `onPressEnter` needs to be defined and exposed to your template! If you're on the options API, that means it should be defined as a method, and if you're using `setup()`, it means you should be returning it from the `setup()` function.

## Which keys work?

According [to the docs](https://vuejs.org/guide/essentials/event-handling.html#key-modifiers), aliases are provided for common keys:

* `.enter`
* `.tab`
* `.delete` (captures both "Delete" and "Backspace" keys)
* `.esc`
* `.space`
* `.up`
* `.down`
* `.left` 
* `.right`

But what if you want to capture a *different* key?

Turns out that can use the `kebab-case` name for any key you want to use as a modifier. For example:

```html
<input @keyup.a="onPressA" />
<input @keyup.page-down="onPressPageDown" />
```

It even works for *some* punctuation characters like the comma:

```html
<input @keyup.,="onPressComma" />
```

Now we get to my problem:

> What if I want to capture an event on the period key?

The following does **not** work:

```html
<input @keyup..="onPressPeriod" />
```

Instead, you need to write a handler that captures *all* the "keydown" and "keyup" events and watch manually for the right property:

```html
<input @keyup="onPress" />
```

```js
const onPress = (e) => {
  if (e.key !== ".") {
    // guard against non-period presses
    return;
  }
  onPressPeriod()
};
```

## System Modifiers

The topic of "system modifiers" or "key combinations" is [explained well in the docs](https://vuejs.org/guide/essentials/event-handling.html#key-modifiers), so I won't spend much time on it. The four options available to you are:

* `.ctrl`
* `.alt`
* `.shift`
* `.meta` (The "meta" key is "command" on Apple keyboards and the "windows" key on Windows keyboards)

If you want to fire an event on `ctrl+enter` you can just chain the modifier:

```html
<input @keyup.ctrl.enter="onPressEnter" />
```

## Event modifiers

```html
<input @keyup.ctrl.stop="onPressCtrl" />
```

Syntactically, event modifiers are chained onto the `@keyup` keyword as well. Your options include:

* `.stop` - Stop the event's propagation to other handlers
* `.prevent` - Prevent default handling of the event (like a page reload for a form submission)
* `.self` - Only fire events for this element, not children
* `.capture` - Handle the event here before handling it at the child level
* `.once` - Trigger this event once at most
* `.passive` - Process the default behavior immediately, and also handle it here without blocking

## .exact modifier

If you want to fire your handler when the exact keys you've specified are pressed, use the `.exact` modifier.

```html
<!-- this will fire even if alt or another key is also pressed -->
<button @keyup.ctrl="onPressCtrl">A</button>
```

```html
<!-- this will fire if ONLY ctrl is pressed -->
<input @keyup.ctrl.exact="onPressCtrl" />
```

## Mouse button modifiers, don't let them fool you

At first, I assumed that `.left` and `.right` referred to the arrow keys, while in reality they refer to the mouse buttons. All three of the following modifiers can be used to restrict the event to the three mouse buttons.

* `.left`
* `.right`
* `.middle`
