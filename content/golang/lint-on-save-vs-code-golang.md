---
title: "Lint on Save With VS Code Official Golang Extension"
date: "2020-06-30"
categories: 
  - "golang"
---

Go has hard opinions about how you should style and format your code, and because of this, setting up your VS Code environment to enforce linting on save can be very efficient. The big upside of this is that you don't need to spend hours setting up tools like ESLint, Prettier, JSLint, etc. That said, in order to take advantage of the styling and listing tools available in the toolchain, you need a dev environment that makes them easy to use.

## VS Code - Lint on save

I'm currently a [VS Code](https://code.visualstudio.com/) fan. I don't like to think about code styling. I like to type a bunch of code with incorrect spacing and press `(ctrl+s)` or `(cmd+s)` to save my code and auto-format it.

First, make sure you have the latest version of Go installed on your machine (as of time of writing, 1.14)

Next install the [Official Golang VS Code Plugin](https://code.visualstudio.com/docs/languages/go)

![official golang vs code extension](/img/Screen-Shot-2020-06-25-at-8.34.33-AM-1024x310.png)

Next open your [settings.json](https://code.visualstudio.com/docs/getstarted/settings#_settings-file-locations) file in VS Code. These settings can be specific to in a single project, workspace or your entire machine.

Add the following settings:

```
{
    "go.lintOnSave": "file",
    "go.formatTool": "goimports",
    "go.useLanguageServer": true,
    "[go]": {
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
            "source.organizeImports": true
        }
    },
    "go.docsTool": "gogetdoc"
}
```

If you don't like any of these settings, you can click the pencil icon to the left of the line (assuming you've opened settings.json in VS Code). It will give a dropdown menu with additional options.

## Why goimports and not gofmt?

Simply put, [goimports](https://godoc.org/golang.org/x/tools/cmd/goimports) does everything `gofmt` does but additionally formats import statements. I like that.

## Not Working?

If it still isn't working, you likely need to reload your VS Code window and/or install the missing tools that VS Code is prompting you to install via popups in the bottom-right of the editor.

I will do my best to keep this guide up to date. Let me know if it isn't working for you via [Twitter](https://qvault.io/contact/) or the [Qvault Discord](https://qvault.io/contact/).
