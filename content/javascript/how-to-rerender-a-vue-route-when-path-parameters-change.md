---
title: "How to Rerender a Vue Route When Path Parameters Change"
author: lane
date: "2020-07-07"
categories:
  - "javascript"
images:
  - /img/800/paint-over-dark-628x354-1.webp
---

In single-page apps that use the [Vue Router](https://router.vuejs.org/), it's common to create a path parameter that changes the behavior of a route. Often a problem occurs however when a user alters the path manually in the address bar. Manually changing the URL does **not** rerender the view! This can cause unexpected behavior because _mounted()_ hooks don't fire and nested components don't reload.

## How to Fix It

The solution is to use another Vue hook, [beforeRouteUpdate()](https://router.vuejs.org/guide/advanced/navigation-guards.html#in-component-guards). Let's take the example of the [boot.dev](https://www.boot.dev/) [Playground](https://app.boot.dev/playground/go). The last parameter in the Playground's path is the code language, `js` or `go`. If the boilerplate code were only fetched using a _mounted()_ hook, then when a user changed the path parameter the boilerplate code wouldn't reload.

The reason that it _does_ reload is that the boot.dev SPA also has the following _beforeRouteUpdate()_ hook:

```
beforeRouteUpdate (to, from, next) {
  this.lang = to.params.lang;
  this.setCode();
  next();
}
```

According to the [docs](https://router.vuejs.org/guide/advanced/navigation-guards.html#global-before-guards), the hook receives three parameters:

- **`to`**: the target [Route Object](https://router.vuejs.org/api/#the-route-object) being navigated to.
- **`from`**: the current route being navigated away from.
- **`next`**: this function must be called to **resolve** the hook. The action depends on the arguments provided to `next`:
  - **`next()`**: move on to the next hook in the pipeline. If no hooks are left, the navigation is **confirmed**.
  - **`next(false)`**: abort the current navigation. If the browser URL was changed (either manually by the user or via the back button), it will be reset to that of the `from` route.
  - **`next('/')` or `next({ path: '/' })`**: redirect to a different location. The current navigation will be aborted and a new one will be started. You can pass any location object to `next`, which allows you to specify options like `replace: true`, `name: 'home'` and any option used in [`router-link`'s `to` prop](https://router.vuejs.org/api/#to) or [`router.push`](https://router.vuejs.org/api/#router-push)
  - **`next(error)`**: (2.4.0+) if the argument passed to `next` is an instance of `Error`, the navigation will be aborted and the error will be passed to callbacks registered via [`router.onError()`](https://router.vuejs.org/api/#router-onerror).

In the case of the boot.dev Playground, we are just doing the same operation that the _mounted()_ hook does: we check the language and fetch the boiler plate.

## What If I Want All Routes To Update?

If this is a common problem in your app, you can set your entire [router-view](https://router.vuejs.org/api/#router-view) to re-render when its path changes by providing a key property:

```html
<router-view :key="$route.fullPath" />
```

With the above, you won't need to use the _beforeRouteUpdate()_ hook, and can directly access the now-reactive **this.$route.params.myVar** property. The only problem with this method is that every path in that router will update in the case of a path change. You may not want all that needless re-rendering, but that's a decision for you to make.
