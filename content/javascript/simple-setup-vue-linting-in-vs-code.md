---
title: "Simple Setup - Vue Linting in VS Code"
author: Lane Wagner
date: "2020-06-17"
categories: 
  - "javascript"
images:
  - /img/Microsoft.webp
---

I'm a [gopher](https://blog.golang.org/gopher) by nature, so I expect consistent styling and linting in my codebases. More importantly, I don't like to think about styling. I like to type haphazardly and then have my editor apply styles automatically on save (`ctrl+s`, `cmd+s`). If you are the same way, hopefully, this will help you in your next Vue.js project.

## VS Code - Download and Plugin

[Download VS Code](https://code.visualstudio.com/download)

After downloading VS Code, we are going to use 2 plugins. [Vue 2 Snippets](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint) [](https://marketplace.visualstudio.com/items?itemName=octref.vetur)and [Eslint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint). Vue 2 Snippets will basically just provide some Vue specific auto completes, but Eslint will do the more important work of linting our code.

![](/img/Microsoft.VisualStudio.Services.Icons-2-150x150.png)

You will also want to add the following to your project using our package manager's **devDependencies** if you don't already have them:

```bash
yarn add eslint --dev
yarn add eslint-plugin-import --dev
yarn add eslint-plugin-node --dev
yarn add eslint-plugin-promise --dev
yarn add eslint-plugin-standard --dev
yarn add eslint-plugin-vue --dev
yarn add @vue/eslint-config-standard --dev
yarn add babel-eslint --dev
```

## Configuring the settings

Now that everything is installed, we just need to do some final setup. VS Code has a GUI for setting preferences, but I tend to just use the JSON file for simplicity sake. In the root of your project ensure that you have a **.vscode** folder, and inside of that folder there is a **settings.json** file. VS Code will use these settings automatically for this directory.

Paste in these configurations:

```json
{
  "files.eol": "\n",
  "editor.codeActionsOnSave": {
    "source.fixAll": true
  },
  "eslint.options": {
    "configFile": ".eslintrc.json"
  },
  "eslint.alwaysShowStatus": true,
  "eslint.format.enable": true,
  "eslint.packageManager": "yarn"
}
```

This accomplishes several important things.

- It specifies that we will use a **.eslintrc.json** file in the root of our project to configure linting settings, but
- Tells VS Code we use yarn. (Chane **yarn** to **npm** if that's what you use)
- Fixes all linting errors on save (to the best of its ability)
- Forces all line endings to UNIX style (LF) instead of Windows (CRLF)

## ESLint Config

We need to set our linting rules:

```json
{
  "root": true,
  "env": {
    "node": true,
    "mocha": true
  },
  "extends": [
    "eslint:recommended",
    "plugin:vue/recommended"
  ],
  "rules": {
    "comma-dangle": "error",
    "quotes": [
      "error",
      "single"
    ],
    "linebreak-style": [
      "error",
      "unix"
    ],
    "array-bracket-spacing": [
      "error",
      "always"
    ],
    "semi": [
      "error",
      "always"
    ],
    "eol-last": [
      "error",
      "always"
    ],
    "indent": [
      "error",
      2
    ]
  },
  "parserOptions": {
    "parser": "babel-eslint",
    "sourceType": "module",
    "allowImportExportEverywhere": true,
    "ecmaVersion": 2019
  }
}
```

You can obviously change this but this is my boilerplate for Vue CLI projects. This will do things like enforce consistent tab sizes, semicolon usage and array spacing.

## Done!

If you have any questions or if you've noticed that this article has become obsolete please leave a comment and let me know.
