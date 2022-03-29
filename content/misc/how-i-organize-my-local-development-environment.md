---
title: "How I Organize My Local Development Environment"
date: "2021-03-17"
categories: 
  - "golang"
---

When I was just getting into coding, I was _very_ disorganized. I would create a new text file in `My Documents`, work on it, never create a Git repository, accidentally delete it later, you get the idea. Nowadays I'm quite the opposite. To be honest, the thing that made me get my act together was the quite unpopular and now deprecated [GOPATH](https://golang.org/doc/gopath_code) that early versions of Go required developers to work in. I think it was the right move to not force that organization as a requirement, but I actually quite liked the method personally, and still use a version of it to this day.

## Where I store code on my local machine

All the code that I write, fork, and maintain goes under the `~/workspace` directory in the home folder. I only work in Unix environments these days. Within the `workspace` directory, everything is namespaced in the way that the GOPATH used to handle it. For example,

`~/workspace/REMOTE/NAMESPACE/REPO`

For example, my open-source package [go-password-validator](https://github.com/wagslane/go-password-validator) lives in `~/workspace/github.com/wagslane/go-password-validator`.

I like this setup for several reasons.

1. By including `remote` in the path, I'm reminded to always user version control. In fact, any new project gets created on the remote server (usually Github) first, then cloned down to it's proper location.
2. By namespacing this way, it's impossible for me to have collisions with various projects I work on. For example, say I have a personal "image-cacher", but my work also has an "image-cacher" project. If they weren't in different directories I'd have to do something silly.
3. I always know exactly where everything is. Back when I was a student, I would forget where I put different projects or snippets, and that hasn't been a problem for me in a long time.
4. When I'm at work, sometimes I need to work in a few different repositories at the same time. It's really nice to open VS Code at the `namespace` level and see all the projects for the organization.

## How I start new projects

For any new project, the setup process looks something like this.

1. Create a new repository on Github
2. Initialize it with a README.md, and if it's open-source, a license
3. Clone the repo down to my local workspace as described above
4. Change the repo settings to auto-delete head branches (I hate branch-creep)

Because I usually work in Go, I then setup some boilerplate. I have an [entirely separate post](https://qvault.io/2020/10/01/boilerplating-a-new-go-program-microservice/) on that process, so you can check that out if you're interested in Go-specific boilerplate.

## How I develop locally - some of my favorite tools

### VS Code

I use VS Code these days. I'm a huge fan so far, though it would be nice if it wasn't such a memory hog. I only have two real aversions when it comes to trying new editors.

1. I don't like language-specific IDE's or editors. One tool for all my projects thanks.
2. I don't like to become completely dependent on the tool. For example, in school I didn't ever learn how to build my C++ code without Visual Studio. Visual Studio adds project files into your repo and does some magic to make it work. I prefer my editors to mostly just be editors. I'd rather use the command line for building, testing, running, etc.

### REST Client

I'm not a huge fan of Postman and Insomnia just because I don't like having another tool open. I'm a big fan of VS Code plugins. For example, I use this [REST client plugin](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) because it makes it easy for me to save all my test requests as readable text files right in my project.

### Database Client

I primarily work in Postgres and ElasticSearch currently. For Postgres admin management I use [PG Admin 4](https://www.pgadmin.org/download/). I don't love that it's in a browser, but it's fine. If anyone has a recommendation for a better tool though I'm all ears.

[ElasticSearch](https://www.elastic.co/) is easy because it comes with [Kibana](https://www.elastic.co/kibana) out of the box. Kibana is a fantastic ES client.

### Operating System

For the last few years, I've worked primarily on a Macbook Pro with the latest versions of Mac OS. Occasionally I'll use [WSL](https://docs.microsoft.com/en-us/windows/wsl/install-win10) & Ubuntu when I'm on my gaming PC though. The Windows Subsystem for Linux is a lifesaver, I can't stand the Windows command line.

I almost always deploy using Docker on a Linux server (Debian typically), so my local environments of Mac OS and Ubuntu are usually pretty damn close to what's going on in production. I'm usually not writing code that interacts too heavily with the operating system anyhow.

## Bash Profile

I often have to connect to remote databases or APIs using a jump box for security reasons. When this is the case, I fill out my Bash Profile with alias commands that forward local ports to those services. For example:

```
alias ssh_postgres_prod="ssh -L 5433:DATABASE_URL:5432 JUMP_BOX_URL"
alias ssh_postgres_stage="ssh -L 5434:DATABASE_URL:5432 JUMP_BOX_URL"
```

I use different local ports so that I never accidentally connect to one database thinking it's a different one.

### Local scripts

I'm a big fan of small one-off bash scripts. Anytime I find myself doing something monotonous over and over again, I try to write a script to speed it up in the future. "Automate the boring stuff", if you will. If the script is useful generally, I create it's own Git repo within my `~/workspace` for it. If it's scoped to a project, I typically store it in the `scripts` directory of that project. For example, at my full-time job, we often need to update a dependency in all ~20 of our microservices. Running all those upgrade commands and opening pull requests can be tedious. We wrote a script for that:

```
#!/bin/bash

# get github repo list
echo ">> List all repositories you would like to create a PR in, separated by commas" ;
default="example-repo,example-repo-2"
echo ">> Default: $default";
read repos;
if [ -z "$repos" ]
then
   repos="$default"
fi
echo "Using repos: $repos"
IFS=',';
read -a repoarr <<< "$repos"

# get new branch name
echo ">> what will the feature branch name be?";
echo ">> Default: auto-{RANDOM}";
read branch;
if [ -z "$branch" ]
then
   branch="auto-$RANDOM"
fi
echo "Using feature branch: $branch"

# get base branch name
echo ">> what branch is this merging into?" ;
echo ">> Default: master";
read baseBranch;
if [ -z "$baseBranch" ]
then
   baseBranch="master"
fi
echo "Using base branch: $baseBranch"

# get the desired tag of the dependency
echo ">> what tag are we changing to?";
echo ">> Default: latest";
read tag;
echo "Using latest tag";

# clean and move to tmp directory
rm -rf /tmp/pr-generator ;
mkdir /tmp/pr-generator  ;
cd /tmp/pr-generator  ;

# Loop through each repo
for (( n=0; n < ${#repoarr[*]}; n++))
do
  git clone "https://github.com/example-org/${repoarr[n]}" ;
  cd ${repoarr[n]} ; 
  git checkout -b ${branch} ;
  if [ -z "$tag" ]
  then
    go get -u github.com/example-org/example-dependency ;
  else
    go get -u github.com/example-org/example-dependency@${tag} ;
  fi
  echo "<============ MOD VENDOR =============>" ;
  go mod vendor ;
  go mod tidy ;
  go test ./... ;
  echo "<============ GIT COMMANDS =============>" ;
  git add * ;
  git commit -m "auto generated message for ${branch}" ;
  git push -u origin ${branch};
  echo "<============ PR ==============>" ;

  curl --location --request POST "https://api.github.com/repos/example-org/${repoarr[n]}/pulls" \
--header "Authorization: Bearer $GITHUB_ACCESS" \
--header 'Content-Type: application/json' \
--data-raw "{
    \"title\": \"*autogen title* update dependency in ${baseBranch}\",
    \"head\": \"${branch}\",
    \"base\": \"${baseBranch}\"
}";

done
```

Hopefully some of the stuff I do is useful to you, if you think I'm doing something dumb or have your own preferences, please let me know what they are!
