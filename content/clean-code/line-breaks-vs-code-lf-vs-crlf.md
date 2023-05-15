---
title: "How to Get Consistent Line Breaks in VS Code (LF vs CRLF)"
author: Lane Wagner
date: "2020-06-18"
categories: 
  - "clean-code"
images:
  - /img/800/vscode-preview.webp
---

Have you ever had the problem where you submit a pull request and the diff is much larger than it should be? Maybe the code looks identical, but GitHub tells you it's completely different.

This is typically due to a difference in **line endings**, especially the difference in `LF` vs. `CRLF`. Unix systems like Linux and macOS use `LF`, the line feed character, for line breaks by default. Windows, on the other hand, is special and uses `CR/LF`, carriage return AND line feed characters, by default.

![Michael Scott condescending to the Windows OS](/img/800/12bb747ebc3c94d638257f18ab25d307-300x244.jpg)

Michael Scott On Windows Line Endings

Unless you work on a Windows-only team, the answer is almost always to change all your code to the Unix default of `LF`.

## The Quick Fix for "End of line character is invalid"

If you're here to quickly fix a single file that you're having problems with, you're in luck. At the bottom right of the screen in [VS Code](https://code.visualstudio.com/), click the little button that says `LF` or `CRLF`. After changing it to your preference, Voila, the file you're editing now has the correct line breaks.

![vscode crlf lf line endings switch](/img/800/vscode-crlf-lf-line-endings-switch.jpg)

Click the LF/CRLF button to toggle line endings

## The Big Fix

If you want new files to automatically have the correct line endings, then you can set the following setting in the top level of your settings.json file:

For LF:

```json
{
    "files.eol": "\n",
}
```

CRLF:

```json
{
    "files.eol": "\r\n",
}
```

If you set the above in your global `settings.json` file it will apply to your entire machine. If you just want the settings for the project you are working on, then edit the `settings.json` in the `.vscode` directory at the root of your project: `.vscode/settings.json`.

This setting will not automatically fix all files in your project that have the wrong line endings! It only applies to new ones. To fix the old ones go through and use the manual method as described in the first paragraph.

## What is CRLF?

`CR LF` stands for "Carriage Return, Line Feed" - it's a digital remnant of classic typewriters. With typewriters, you had to push the "carriage" (the thing that holds the paper) back into place, hence "Carriage Return".

When everything went digital, some devices required a "Line Feed" character to terminate lines, so Microsoft decided to just make a new line have _both__ characters so that they would work correctly on all devices.

![](/img/800/typewriter-form-unsplash-with-carriage-300x200.jpeg)

`CR` and `LF` are just bytecodes. Computers store text characters as numbers in binary, just 1's and 0s. Carriage Return (`CR`), is represented in [ASCII](https://en.wikipedia.org/wiki/ASCII) (a common character encoding protocol) as 13, or in binary, `00001101`. Likewise, the line feed character (`LF`) is 10 or `00001010`.

As you can imagine, `CRLF` is just both bytes shoved up next to each other: `0000110100001010`.

![Ascii Table](/img/800/asciifull.gif)
