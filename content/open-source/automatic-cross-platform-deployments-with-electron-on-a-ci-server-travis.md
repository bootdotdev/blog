---
title: "Automatic Cross-Platform Deployments with Electron on a CI Server (Travis)"
author: Lane Wagner
date: "2019-08-08"
categories: 
  - "open-source"
images:
  - /img/800/electron2.webp
---

This is a tutorial on how to set up an Electron app on [Travis CI](https://travis-ci.org/), so that new versions are deployed to [Github Releases](https://help.github.com/en/articles/creating-releases) with a simple pull request.

## Boilerplate

I created a [boilerplate repo](https://github.com/lane-c-wagner/electron-ci-boilerplate) that has all the necessary configuration to deploy a minimalistic app to Github releases. If you get lost during the tutorial you can look to that as an example. Also, if you don't have an electron app yet and just want to start with it as an example feel free.

## Electron Builder

We need a package that will handle packing the app into an executable and deploying to Github releases. [Electron Builder](https://github.com/electron-userland/electron-builder) is a fantastic npm package that handles building, signing, notarizing, and deploying an electron app on all three operating systems. Add it using yarn ([recommended by Electron Builder](https://www.npmjs.com/package/electron-builder#installation)):

```bash
yarn add electron-builder --dev
```

Electron Builder uses your app's package.json file for most configuration.

```json
{
  "name": "{APP_NAME}",
  "version": "{VERSION_NUMBER}",
  "description": "A minimal Electron application that deploys on CI servers",
  "main": "main.js",
  "scripts": {
    "start": "electron .",
    "release": "electron-builder",
    "test": "echo success"
  },
  "repository": "https://github.com/{USER_NAME}/{REPO_NAME}",
  "keywords": [
    "electron",
    "ci",
    "travis",
    "tutorial",
    "demo"
  ],
  "author": "{USER_NAME}",
  "build": {
    "appId": "{APP_ID}",
    "publish": "github",
    "dmg": {
      "contents": [
        {
          "x": 110,
          "y": 150
        },
        {
          "x": 240,
          "y": 150,
          "type": "link",
          "path": "/Applications"
        }
      ]
    },
    "appImage": {
      "license": "LICENSE"
    },
    "nsis": {
      "createDesktopShortcut": "always",
      "license": "LICENSE"
    }
  },
  "devDependencies": {
    "electron": "^4.0.1",
    "electron-builder": "^21.2.0"
  }
}
```

Replace all the configuration variables with your own values. The configuration variables are all caps in {BRACKETS}.

You should have a license file named LICENSE at the root of your directory, as well as a copy called license\_en.txt in your build folder (build/license\_en.txt). Electron builder uses those licenses as the license agreement for the installers.

Good practice for an appId is a reverse domain name. For example, ours is _dev.boot_.

You can setup your test script to actually run tests if you want, the above just prints "success" to the screen. We will configure Travis to run those tests on the CI server.

At this point you should be able to run

```bash
yarn release --publish never
```

which will build and package your app locally into the _dist_ directory. However, it will only build the package for your local operating system, which is expected.

## Travis CI

![travis ci](/img/800/TravisCI-Full-Color.png)

Navigate to [https://travis-ci.org/](https://travis-ci.org/) and sign up using your Github account. Once signed in you should be able to select which repository you want to connect to Travis.

Copy this code into _.travis.yml_ at the root of your repository:

```yaml
language: node_js

node_js:
  - '11.6.0'

# Always run two parallel builds: one on mac and one on linux
# the linux build will use wine to be able to build windows and
# linux apps
matrix:
  include:
    - os: osx
      osx_image: xcode10.2
      language: node_js
      node_js: "11.6.0"
      env:
        - ELECTRON_CACHE=$HOME/.cache/electron
        - ELECTRON_BUILDER_CACHE=$HOME/.cache/electron-builder

    - os: linux
      dist: trusty
      sudo: required
      services: docker
      language: generic

notifications:
  email: false

# cache some files for faster builds
cache:
  yarn: true
  directories:
    - node_modules
    - $HOME/.cache/electron
    - $HOME/.cache/electron-builder

# add git lfs for large file support
before_install:
  - |
    if [ "$TRAVIS_OS_NAME" == "osx" ]; then
      mkdir -p /tmp/git-lfs && curl -L https://github.com/github/git-lfs/releases/download/v2.3.1/git-lfs-$([ "$TRAVIS_OS_NAME" == "linux" ] && echo "linux" || echo "darwin")-amd64-2.3.1.tar.gz | tar -xz -C /tmp/git-lfs --strip-components 1
      export PATH="/tmp/git-lfs:$PATH"
    fi
before_script:
  - git lfs pull

# on PRs and merges to master and prod run tests and build the app
script:
  - |
    if [ "$TRAVIS_OS_NAME" == "linux" ]; then
      docker run --rm \
        -v ${PWD}:/project \
        -v ~/.cache/electron:/root/.cache/electron \
        -v ~/.cache/electron-builder:/root/.cache/electron-builder \
        electronuserland/builder:wine \
        /bin/bash -c "yarn --link-duplicates --pure-lockfile && yarn test"
    else
      yarn test
    fi
# only deploy to github on a merge to the prod branch
deploy:
  provider: script
  script: bash deploy.travis.sh
  skip_cleanup: true
  on:
    branch: prod
    
before_cache:
  - rm -rf $HOME/.cache/electron-builder/wine

# only run this script on pull requests and merges into 
# the 'master' and 'prod' branches
branches:
  only:
  - master
  - prod
```

The comments in the above file should explain what each step does, but the basic idea is to _yarn test_ on each pull request to verify that a pull request doesn't break the app. Then, once code is merged into the prod branch, we trigger the following deploy script to build and push our code to Github Releases:

Copy this file to _deploy.travis.sh_

```bash
#! /bin/bash
if [ "$TRAVIS_OS_NAME" == osx ]; then
    # deploy on mac
    yarn release
else
    # deploy on windows and linux
    docker run --rm -e GH_TOKEN -v "${PWD}":/project -v ~/.cache/electron:/root/.cache/electron -v ~/.cache/electron-builder:/root/.cache/electron-builder electronuserland/builder:wine /bin/bash -c "yarn --link-duplicates --pure-lockfile && yarn release --linux AppImage --win"
fi
```

In order for your _.travis.yml_ script to have permission to upload code to Github Releases, then you will need to set an environment variable that contains an API token.

In Github Navigate to your personal settings / Developer Settings / Generate New Token. Then go to your repository settings in Travis and you can add an environment variable. The variable name is GH\_TOKEN and the token is the one you created on Github. Make sure to keep the variable private (the default) on Travis so that it won't print the token in the logs.

## Done!

Now all pull requests to master and prod should run tests, and all code merged into the prod branch should trigger a new release. The released assets and downloadable installers will be published to your Github repository under the [releases tab](https://github.com/lane-c-wagner/electron-ci-boilerplate/releases).

The release will be a draft so after each deployment you need to go in manually and convert from a draft to a published release, which is just the click of a button.

## Confused?

If you get lost feel free to keep looking back at the [working example repo](https://github.com/lane-c-wagner/electron-ci-boilerplate) and also make sure to look at the logged errors in Travis.
