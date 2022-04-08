---
title: "How To Cache Images - React Native Expo (Managed)"
author: Lane Wagner
date: "2020-02-04"
categories: 
  - "javascript"
images:
  - /img/800/photo-1571858253340-84d2811a8d7e.jpeg
---

Caching images in React Native can be easy, even if you are using Expo's managed workflow. The problem many devs run into is that React Native only supports [caching images on IOS](https://facebook.github.io/react-native/docs/images#cache-control-ios-only) out of the box.

Other popular community packages that work on Android contain native code, and as such don't work with [Expo's managed workflow](https://docs.expo.io/introduction/managed-vs-bare/?redirected). For this reason, I open-sourced the code I'm using on my latest project. Behold, [react-native-expo-cached-image](https://www.npmjs.com/package/react-native-expo-cached-image)!

## Quick Start

Install the module:

```bash
yarn add react-native-expo-cached-image
```

Import the component:

```js
import CachedImage from 'react-native-expo-cached-image';
```

Use the component in a render() method:

```html
<CachedImage
  isBackground
  source={{ uri: 'https://boot.dev/wp-content/uploads/2019/05/QVault-app.png' }}
/>
```

The CachedImage component has the same props and API as React Native's [Image](https://facebook.github.io/react-native/docs/image) and [ImageBackground](https://facebook.github.io/react-native/docs/imagebackground) components. To use CachedImage as a background image, just pass in the _isBackground_ prop:

```html
<CachedImage
  isBackground
  source={{ uri: 'https://boot.dev/wp-content/uploads/2019/05/QVault-app.png' }}
/>
```

{{< cta1 >}}

## What Is It Doing?

CachedImage keeps it simple. It downloads the image to the user's local filesystem using the [SHA-256](/cryptography/how-sha-2-works-step-by-step-sha-256/) hash of the URI. Then, on subsequent renders and app uses, it loads the image from the filesystem if it exists. This saves the user from using unnecessary data and experiencing slow load times.

Tip: In order to bust the cache, you can append a query string or anchor text to the URI.

[Link to the Github](https://github.com/lane-c-wagner/react-native-expo-cached-image)

## Code

![programmer with three screens](/img/800/photo-1550439062-609e1531270e-1024x683.jpg)

[max\_duz](https://unsplash.com/@max_duz)

As of writing, here is the code, feel free to just copypasta it if you don't want to install the dependency:

```js
import React, { Component } from 'react';
import { View, Image, ImageBackground } from 'react-native';
import * as FileSystem from 'expo-file-system';
import * as Crypto from 'expo-crypto';

export default class CachedImage extends Component {
  state = {
    imgURI: ''
  }

  async componentDidMount() {
    const filesystemURI = await this.getImageFilesystemKey(this.props.source.uri);
    await this.loadImage(filesystemURI, this.props.source.uri);
  }

  async componentDidUpdate() {
    const filesystemURI = await this.getImageFilesystemKey(this.props.source.uri);
    if (this.props.source.uri === this.state.imgURI ||
      filesystemURI === this.state.imgURI) {
      return null;
    }
    await this.loadImage(filesystemURI, this.props.source.uri);
  }

  async getImageFilesystemKey(remoteURI) {
    const hashed = await Crypto.digestStringAsync(
      Crypto.CryptoDigestAlgorithm.SHA256,
      remoteURI
    );
    return `${FileSystem.cacheDirectory}${hashed}`;
  }

  async loadImage(filesystemURI, remoteURI) {
    try {
      // Use the cached image if it exists
      const metadata = await FileSystem.getInfoAsync(filesystemURI);
      if (metadata.exists) {
        this.setState({
          imgURI: filesystemURI
        });
        return;
      }

      // otherwise download to cache
      const imageObject = await FileSystem.downloadAsync(
        remoteURI,
        filesystemURI
      );
      this.setState({
        imgURI: imageObject.uri
      });
    }
    catch (err) {
      console.log('Image loading error:', err);
      this.setState({ imgURI: remoteURI });
    }
  }

  render() {
    return (
      <View>
        {this.props.isBackground ? (
          <ImageBackground
            {...this.props}
            source={this.state.imgURI ? { uri: this.state.imgURI } : null}
          >
            {this.props.children}
          </ImageBackground>
        ) : (
          <Image
            {...this.props}
            source={this.state.imgURI ? { uri: this.state.imgURI } : null}
          />
        )}
      </View>
    );
  }
}
```
