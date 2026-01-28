---
title: "Migrating From Vue-CLI & Webpack to Vitejs"
author: lane
date: "2021-04-26"
categories: 
  - "javascript"
  - "open-source"
images:
  - /img/800/ruinreborn_fantasy_art_simple_background_butterfly_migration__cc9524c3-41af-48fe-ac97-ac8eed7a845c_1.png.webp
---

[Boot.dev's web app that hosts all of my coding courses](https://www.boot.dev/) is a single-page application written in Vue 2, with plans to migrate to Vue 3 _soon™©®_. In the meantime, I happened across a cool new tooling app called [Vite](https://github.com/vitejs/vite) that promised a few things that caught my attention.

- Nearly instant development server startup time
- Hot module replacement out of the box
- Simple configuration
- Out-of-the-box support for ES modules

This particularly resonated with me because my (fairly) simple app's development server took over 10 seconds to start up with the [Vue-cli](https://cli.vuejs.org/) and [Webpack](https://webpack.js.org/), and I've spent many hours in the past trying to configure Webpack and [Babel](https://babeljs.io/), when I just needed basic Vue configurations. Let's look at some quick anecdotal comparisons before I dive into the migration guide, so you can see if the benefits of switching are worth it for you.


|                            | Vite                      | Vue-cli + Webpack |
| -------------------------- | ------------------------- | ----------------- |
| Dev server start time      | ~600ms                    | ~10,000ms         |
| HMR time                   | Unsure, appears _instant_ | ~2,000ms          |
| Production build time      | ~15s                      | ~22s              |
| Number of bundled JS files | 29 JS modules             | 18 JS Modules     |
| Average JS bundle size     | ~29kb                     | ~61kb             |
| Total JS bundle size       | ~840kb                    | ~1098kb           |


Vite vs Vue-cli + Weback

Additionally, to get the 18 modules shown above using the Vue cli and webpack, I had to add comment annotations to my `routes.js` file. Out of the box the Vue-cli makes one giant bundle, which is much worse for page performance reasons. Vite splits the bundle along module lines out-of-the-box without the need for those annoying annotations.

## Migration Guide

Let's go through the major steps of actually moving a project in Vue 2 from the Vue CLI to Vite.

### Step 1 - dependencies

All `@vue-cli...` dependencies need to go. For me that meant removing the following.

```
- "@vue/cli-plugin-babel": "^4.5.6",
- "@vue/cli-plugin-eslint": "^4.5.6",
- "@vue/cli-service": "^4.5.6",
```

These were replaced with Vite and its plugin for Vue.

```
+ "vite": "^2.2.1",
+ "vite-plugin-vue2": "^1.4.4",
+ "@vue/compiler-sfc": "^3.0.11",
```

Next, Vite supports `sass` out of the box, so I could remove my old dependencies.

```
- "node-sass": "^4.12.0",
- "sass-loader": "^10.0.2",
```

And I replaced them with the bare-bones `sass` compiler, because Vite requires it to be available.

```
+ "sass": "^1.32.11",
```

Finally, because Vite only supports modern browsers (sorry if you have to support legacy stuff, Vite might not be for you) I removed babel dependencies and my `babel.config.js` file.

```
- "babel-eslint": "^10.1.0",
- "babel-runtime": "^6.26.0"
```

### Moving index.html

Vite doesn't store `index.html` in the `public` folder like you're used to, instead it goes right in the root of your project, so move it there. Vite also needs an additional entry point.

```html
<body>
  <noscript>
    <strong>
      We're sorry but this app doesn't work properly without JavaScript enabled. Please enable it to continue.
    </strong>
  </noscript>
  <div id="app"></div>

  <!-- this new script is for vite -->
  <script type="module" src="/src/main.js"></script>
</body>
```

You'll also need to move your static asset references to use a simple `/` rather than `<%= BASE_URL %>`.

```html
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
<link rel="manifest" href="/site.webmanifest">
```

### Vite Config

Here is the `vite.config.js` I settled on, it goes in the root of the project.

```js
import { defineConfig } from 'vite';
import { createVuePlugin } from 'vite-plugin-vue2';
import path from 'path';

export default defineConfig({
  plugins: [ createVuePlugin() ],
  server: {
    port: 8080
  },
  resolve: {
    alias: [
      {
        find: '@',
        replacement: path.resolve(__dirname, 'src')
      }
    ]
  },
  build: {
    chunkSizeWarningLimit: 600,
    cssCodeSplit: false
  }
});
```

The `resolve` block lets me import components using `@` as the root of the `src` directory. For example, `import Tooltip from '@/components/Tooltip.vue';`.

The `build` block does a couple of things, first, it increases the chunk size warning limit from the default of 500kb to 600kb. I did that just because I have a really heavy code editor component and I don't want to see the warning every time.

Secondly, my site **completely broke** when I let Vite split my .`css` files the way it wanted to. This actually makes me sad because I'd rather have my users only load the CSS they need as they need them. If anyone has had a similar problem please let me know how you solved it.

### .vue extensions

Vite explicitly requires that all `.vue` imports include the `.vue` in the path. This can be a bit tedious if you haven't been using the extensions. All your imports need to be updated from `import Tooltip from '@/components/Tooltip'` to `import Tooltip from '@/components/Tooltip.vue'`.

### Webpack chunking for lazy-loaded routes

If previously you used comment annotations in Webpack to break up your bundle, you don't need to do that anymore! Just remove them.

`const Courses = () => import(/* webpackChunkName: "Courses" */ '@/views/Courses.vue');`

becomes

`const Courses = () => import('@/views/Courses.vue');`

### Yarn Scripts

I use the following three scripts.

```
"serve": "vite --open",
"preview": "vite preview --open --port 8080",
"build": "vite build --out-dir dist",
"lint": "eslint src",
"lint:fix": "eslint src --fix"
```

- `yarn serve` starts a development server and open your preferred browser.
- `yarn build` builds the production files and stores them in `dist`
- `yarn preview` serves the production files locally for testing
- `yarn lint` runs `eslint` and reports problems. You probably were using `vue-cli-service lint` before, which just ran `eslint` under the hood.

### Node environment

Vite is strict when it comes to `Node.js` code being slipped into your front-end bundle. I ran into an issue where a dependency I had required `global` to be defined. Obviously, the best thing is to not require dependencies like that, but in my case I needed it so I added a little shim in `index.html`.

```html
<!-- polyfill global because shit dependencies -->
  <script>
    const global = globalThis;
  </script>
<!-- end polyfill -->
```

## Vue 3

My next migration will likely be to Vue 3, hopefully sometime this year. I've really just been holding out for a bit more stability, and for a few of my dependencies to support the new major version.
