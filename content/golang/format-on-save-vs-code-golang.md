---
title: "Format on Save in Go with VS Code [2023]"
author: Lane Wagner
date: "2023-05-26"
categories: 
  - "golang"
images:
  - /img/800/Screen-Shot-2020-06-25-at-8.webp
aliases:
  - /golang/lint-on-save-vs-code-golang/
---

Go has hard opinions about how you should style and format your code. Setting up your VS Code environment to enforce the standard linting and formatting rules can save you a *ton* of time.

I don't like to think about code styling. I like to type a bunch of code with incorrect spacing and press `(ctrl+s)` or `(cmd+s)` to save my code and auto-format it.

## What you'll need

* Make sure you have the latest version of Go installed on your machine (as of the time of writing, 1.20)
* Install the [Official Golang VS Code Plugin](https://code.visualstudio.com/docs/languages/go)

![official golang vs code extension](/img/800/Screen-Shot-2020-06-25-at-8.34.33-AM-1024x310.png)

Next, open your [settings.json](https://code.visualstudio.com/docs/getstarted/settings#_settings-file-locations) file in VS Code. These settings can be specific to a single workspace or to your user account, whichever you prefer.

I use the following settings:

```json
{
    // format all files on save if a formatter is available
    "editor.formatOnSave": true,
    // I use "goimports" instead of "gofmt"
    // because it does the same thing but also formats imports
    "go.formatTool": "goimports",
    // go-specific settings
    "[go]": {
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
            "source.organizeImports": true
        }
    },
    "[go.mod]": {
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
            "source.organizeImports": true
        }
    },
}
```

## Why `goimports` and not `gofmt`?

Simply put, [goimports](https://godoc.org/golang.org/x/tools/cmd/goimports) does everything `gofmt` does but additionally formats import statements. I like that.

## Bonus: Auto-Update, Staticcheck and Vetting

I also have these additional settings to add even more functionality to my VS Code environment. If you find them useful, feel free to use them.

```json
{
    "gopls": {
        "staticcheck": true,
        "analyses": {
            "ST1000": false,
            "ST1018": false
        }
    },
    "go.toolsManagement.autoUpdate": true,
    "go.vetOnSave": "package",
}
```

## Not Working?

If it still isn't working, you likely need to reload your VS Code window and/or install the missing tools that VS Code is prompting you to install via popups in the bottom-right of the editor.

I will do my best to keep this guide up to date. Let me know if it isn't working for you in the [boot.dev Discord](https://boot.dev/community).
