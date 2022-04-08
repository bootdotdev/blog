---
title: "Beautiful Language and Beautiful Code"
date: "2021-06-30"
categories: 
  - "clean-code"
images:
  - /img/800/language.jpeg
---

"Dead Poet's Society" is a classic film, and has become a recent favorite of mine. There's a scene in particular that I enjoy, where Robin William's character explains that it's bad practice to use terms like "very tired" or "very sad", instead we should use descriptive words like "exhausted" or "morose"!

{{< youtube zh79iPi-y-c >}}

I wholeheartedly agree with what's being taught to the students in this scene. It's tiresome to read a novel where the author drones on within the bounds of a lackluster vocabulary. This brings me to the point I wanted to emphasize in this short article:

_Beautiful language and beautiful code are far from the same._

**Beautiful language** doesn't simply communicate instructions from one human to another. Language well-used arouses emotions, illustrates scenery, exposes nuance, and can sing through rhyme and meter. Its purpose isn't purely functional, it's a rich medium of creative expression.

**Beautiful code**, at least by my standards, is purely functional. Its goal is to communicate exactly what it does. Emotion, motif, and narrative be damned. Beautiful code should be written so that machines carry out the instructions as efficiently as possible, and humans grok the instructions as easily as possible. The ideal piece of code is perfectly efficient and can be understood by any human that reads it.

## Why shouldn't code be more like its more expressive counterpart?

If you're a part of [/r/shittyprogramming](https://www.reddit.com/r/shittyprogramming/) on Reddit, you may have noticed several weeks back when the community became interested in writing the most ridiculous and inefficient way to calculate whether or not a given number is even. Here are some highlights.

```js
const isEven = n => 'x'.repeat(n).replace(/xx/g, '') === '';
```

[source](https://www.reddit.com/r/shittyprogramming/comments/ntzyg0/iseven_with_regex_in_javascript/)

```js
function isEven(number) {
	if (0 == number) {
		return true;
	} else if (number < 0) { //I actually don't remember if JS has an absolute value function,
		return !isEven(number+1); // so this is how we handle negative numbers
	} else {
		return !isEven(number-1);
	}
}
```

[source](https://www.reddit.com/r/shittyprogramming/comments/ntmmc6/my_own_iseven_submission/)

```C++
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

char isEvenFile() {
	while (access("/tmp/isEven", F_OK)) ;
	//We have to wait until the other process created the file
	FILE *comms = fopen("/tmp/isEven", "r");
	int c = EOF;
	while (c == EOF)
		c = fgetc(comms);
	//In case we were so fast that the other process didn't write to the file
	for (;;) {
		int newC = fgetc(comms);
		if (newC != ' ')
			//the number has been sent
			c = newC;
		else {
			FILE *out = fopen("/tmp/out", "w+");
			switch (c) {
				case '0': case '2': case '4': case '6': case '8':
					fprintf(out, "b");
					break;
				default:
					fprintf(out, "a");
					//printing a null char would be the end of the string.
					break;
			}
			fflush(out);
			break;
		}
	}
	fclose(comms);
	exit(0);
}

char isEven(int n) {
	char input[10];
	sprintf(input, "%d", n);
	int pid = fork();
	if (pid == -1)
		return 2; //error
	if (pid == 0) {
		isEvenFile();
	}
	else {
		FILE *comms = fopen("/tmp/isEven", "w+");
		fprintf(comms, "%d ", n);
		fflush(comms);
		//send the number to stdin of the child
		while (access("/tmp/out", F_OK | R_OK)) ;
		FILE *out = fopen("/tmp/out", "r");
		int result = EOF;
		while (result == EOF)
			result = fgetc(out);
		//Again, we have to wait until the other process is done
		result = result == 'b';
		fclose(comms);
		fclose(out);
		remove("/tmp/isEven");
		remove("/tmp/out");
		return (char) result;
	}
}
```

[Source](https://www.reddit.com/r/shittyprogramming/comments/nsxeok/ultra_fast_iseven_function/)

[One Redditor](https://www.reddit.com/r/shittyprogramming/comments/nxsxcy/iseven_training_data/) went so far as to apply machine learning to the problem and annotate an "isEven" training set.

My point with all this "isEven" nonsense is that code _can_ be fun, interesting, and entertaining - I'm not trying to say it can't be. I'm doing some mental gymnastics, however, in that I define all these "jokes through code" as normal language. It's a medium through which humans express themselves creatively to one another, just like film, poetry, novels, or blogging.

None of the examples above are actually intended to run in production. If they were, they would be examples of ugly code indeed.
