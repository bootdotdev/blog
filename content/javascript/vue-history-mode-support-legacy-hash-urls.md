---
title: "Vue History Mode - Support Legacy Hash URLs"
author: Lane Wagner
date: "2020-07-15"
categories: 
  - "javascript"
images:
  - /img/800/history.jpeg
---

When we first launched the [boot.dev's single-page-app](https://boot.dev/), we were using [Vue Router's](https://router.vuejs.org/) default hash routing. Hash routing looks ugly to the end-user, and when you want to be able to share parts of your app via direct link those hashes can get really annoying.

We have since moved to the newer [HTML5 History Mode](https://router.vuejs.org/guide/essentials/history-mode.html) which doesn't have that obnoxious hash in the route. We had a bit of trouble coming up with a clean way to redirect those old hash routes to the new ones, however, so now that we've solved it we will share our findings.

At the time of writing we have the following routes, you probably have something similar:

```js
import Vue from 'vue';
import VueRouter from 'vue-router';
import Courses from '../views/Courses.vue';
import CourseProduct from '../views/CourseProduct.vue';
import Profile from '../views/Profile.vue';
import Exercise from '../views/Exercise.vue';
import Store from '../views/Store.vue';
import Certificates from '../views/Certificates.vue';
import Dashboard from '../views/Dashboard.vue';
import Certificate from '../views/Certificate.vue';
import Login from '../views/Login.vue';
import Playground from '../views/Playground.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Login',
    component: Login
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
    children: [
      {
        path: 'courses',
        name: 'Courses',
        component: Courses
      },
      {
        path: 'course_product/:courseUUID',
        name: 'CourseProduct',
        component: CourseProduct
      },
      {
        path: 'exercise/:courseUUID/:moduleUUID?',
        name: 'Exercise',
        component: Exercise
      },
      {
        path: 'store',
        name: 'Store',
        component: Store
      },
      {
        path: 'profile',
        name: 'Profile',
        component: Profile
      },
      {
        path: 'certificates',
        name: 'Certificates',
        component: Certificates
      }
    ]
  },
  {
    path: '/certificate/:userUUID/:courseUUID',
    name: 'Certificate',
    component: Certificate
  },
  {
    path: '/playground/:lang',
    name: 'Playground',
    component: Playground
  }
];

const router = new VueRouter({
  mode: 'history',
  routes
});

export default router;
```

Our goal is to redirect all of our old hash based (#) routes to the new non-hash versions. For example:

[boot.dev/#/playground/go](https://boot.dev/playground/go) --> [boot.dev/playground/go](https://boot.dev/playground/go)

All we do is add the following to our router:

```js
// Redirect if path begins with a hash (ignore hashes later in path)
router.beforeEach((to, from, next) => {
  // Redirect if fullPath begins with a hash (ignore hashes later in path)
  if (to.fullPath.substr(0, 2) === '/#') {
    const path = to.fullPath.substr(2);
    next(path);
    return;
  }
  next();
});
```

The full code:

```js
import Vue from 'vue';
import VueRouter from 'vue-router';
import Courses from '../views/Courses.vue';
import CourseProduct from '../views/CourseProduct.vue';
import Profile from '../views/Profile.vue';
import Exercise from '../views/Exercise.vue';
import Store from '../views/Store.vue';
import Certificates from '../views/Certificates.vue';
import Dashboard from '../views/Dashboard.vue';
import Certificate from '../views/Certificate.vue';
import Login from '../views/Login.vue';
import Playground from '../views/Playground.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Login',
    component: Login
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
    children: [
      {
        path: 'courses',
        name: 'Courses',
        component: Courses
      },
      {
        path: 'course_product/:courseUUID',
        name: 'CourseProduct',
        component: CourseProduct
      },
      {
        path: 'exercise/:courseUUID/:moduleUUID?',
        name: 'Exercise',
        component: Exercise
      },
      {
        path: 'store',
        name: 'Store',
        component: Store
      },
      {
        path: 'profile',
        name: 'Profile',
        component: Profile
      },
      {
        path: 'certificates',
        name: 'Certificates',
        component: Certificates
      }
    ]
  },
  {
    path: '/certificate/:userUUID/:courseUUID',
    name: 'Certificate',
    component: Certificate
  },
  {
    path: '/playground/:lang',
    name: 'Playground',
    component: Playground
  }
];

const router = new VueRouter({
  mode: 'history',
  routes
});

// Redirect if path begins with a hash (ignore hashes later in path)
router.beforeEach((to, from, next) => {
  // Redirect if fullPath begins with a hash (ignore hashes later in path)
  if (to.fullPath.substr(0, 2) === '/#') {
    const path = to.fullPath.substr(2);
    next(path);
    return;
  }
  next();
});

export default router;
```
