---
layout: farshid_default
title: "Shell, Vim & Developer Tools Quick Reference"
date_modified: 2025-06-19
categories: [dev-tools, shell]
tags: [shell, vim, terminal, grep, fzf, tldr, Linux]
description: "Quick reference for shell basics, vim commands, and essential developer CLI tools like ripgrep, fzf, and broot."
excerpt: "Shell essentials: echo, pipes, redirects, vim basics, and must-know CLI tools for efficient development."
author: "Dr. Farshid Pirahansiah"
---

- [NeoHtop](https://github.com/Abdenasser/neohtop)
- 


- The Shell
    - echo
        - "" \ 
        - $PATH
        - cd -
        
        - ctrl+L to clean 
        - ctrl+r

        - >> append
        - output into | input
        - # into root or sudo su
        - xdg-open opent the file with reletive app
        - foo=bar ; must be without space 
        - echo "value is $foo" -> value is bar
        - echo 'value is $foo' -> value is $foo
        - mcd () {
            mkdir -p "$1"
            cv "$1"
        }
        source mcd.sh
        !!
<!--  -->
command + /
option+shif+a




#!/usr/bin/env python
import sys
for arg in reversed(sys.argv[1:]):
    print(arg)

# tools
tldr
locate 
grep 
ripgrep = rg
fzf
broot
nnn


# vim
 i
 esc
 r
 k
 s-v
 c-v
 :
