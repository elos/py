This repository holds python modules for interacting with elos.

# Setup

## Ruby

Mac OS X has Ruby installed. Ruby is the root of the dependency tree of programs
that we will now install to properly set up a Python environment.

## Homebrew

Mac OS X lacks a package manager, [Homebrew](https://brew.sh) serves this need.
Install homebrew:
```bash
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

##  Set up path
Unix-like operating systems use the `$PATH` environment variable to resolve
which binary to run when you type the name of a program into the shell.

`ls`, `cd`, `mkdir` are all programs. And are all in /bin. The system root
folder for program binaries.

So we installed Homebrew, the package manager, to handle installing third party
binaries. We must instruct the operating system where to look for additional
program names. We add homebrew to the front of our path so if that the
operating system first checks there.

Add to your ~/.bash_profile or ~/.profile:
```bash
export PATH=/usr/local/bin:/usr/local/sbin:$PATH
```

## Install Python
Install Python 2.7:
```bash
$ brew install
```

Use pip to manage python modules (homebrew installs
the `pip` command for you.

## Virtual env
Python has bad tooling. Therefore it uses the global environment to
resolve all dependencies. The implications of this decision include
the inability to work on several projects requiring different versions
of the same package at once. This becomes exceedingly ridiculous, espcially
as the packages you rely on may rely on other packages, etc.

Virtualenv is a tool for managing virtual python environments and solves
this issue. Use pip to install virtualenv:
```bash
$ pip install virtualenv
```




