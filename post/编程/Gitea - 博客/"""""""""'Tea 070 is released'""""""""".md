
---
title: """""""""'Tea 0.7.0 is released'"""""""""
categories: 
    - 编程
    - Gitea - 博客
author: Gitea - 博客
comments: false
date: Fri, 12 Mar 2021 00:00:00 GMT
thumbnail: 'https://blog.gitea.io/demos/13972/1.gif'
---

<div>   
<p> 6543</p>
<h2>
<a href="https://blog.gitea.io/2021/03/tea-0.7.0-is-released/">
Tea 0.7.0 is released
</a>
</h2>
<p>
<i>Fri Mar 12, 2021</i>
by
<b>
<a href="https://github.com/6543">
6543
</a>
</b>
</p>

<p>We are proud to present the release of <code>tea</code> version 0.7.0,
a CLI tool that allows you to work with pull requests, issues and more in your terminal.</p>
<p>You can download prebuilt binaries from <a href="https://dl.gitea.io/tea/0.7.0">dl.gitea.io/tea</a>,
for more options look at the <a href="https://gitea.com/gitea/tea#installation">README.md</a>.</p>
<p><strong>Have you heard? We now have a <a href="https://shop.gitea.io/">swag shop</a>! 👕 🍵</strong></p>
<h2 id="demo">Demo</h2>
<p><img src="https://blog.gitea.io/demos/13972/1.gif" alt="demo gif" referrerpolicy="no-referrer"></p>
<h2 id="review-feature">Review Feature</h2>
<p><img src="https://blog.gitea.io/demos/13972/2.gif" alt="review gif" referrerpolicy="no-referrer"></p>
<p><em>Thanks to <a href="https://github.com/noerw">@noerw</a></em></p>
<h2 id="changelog">Changelog</h2>
<h2 id="v070httpsgiteacomgiteateareleasestagv070---2021-03-12"><a href="https://gitea.com/gitea/tea/releases/tag/v0.7.0">v0.7.0</a> - 2021-03-12</h2>
<ul>
<li>BREAKING
<ul>
<li><code>tea issue create</code>: move <code>-b</code> flag to <code>-d</code> (<a href="https://gitea.com/gitea/tea/pulls/331">#331</a>)</li>
<li>Drop <code>tea notif</code> shorthand in favor of <code>tea n</code> (<a href="https://gitea.com/gitea/tea/pulls/307">#307</a>)</li>
</ul>
</li>
<li>FEATURES
<ul>
<li>Add commands for reviews (<a href="https://gitea.com/gitea/tea/pulls/315">#315</a>)</li>
<li>Add <code>tea comment</code> and show comments of issues/pulls (<a href="https://gitea.com/gitea/tea/pulls/313">#313</a>)</li>
<li>Add interactive mode for <code>tea milestone create</code> (<a href="https://gitea.com/gitea/tea/pulls/310">#310</a>)</li>
<li>Add command to install shell completion (<a href="https://gitea.com/gitea/tea/pulls/309">#309</a>)</li>
<li>Implement PR closing and reopening (<a href="https://gitea.com/gitea/tea/pulls/304">#304</a>)</li>
<li>Add interactive mode for <code>tea issue create</code> (<a href="https://gitea.com/gitea/tea/pulls/302">#302</a>)</li>
</ul>
</li>
<li>BUGFIXES
<ul>
<li>Introduce workaround for missing pull head sha (<a href="https://gitea.com/gitea/tea/pulls/340">#340</a>)</li>
<li>Don’t exit if we can’t find a local repo with a remote matching to a login (<a href="https://gitea.com/gitea/tea/pulls/336">#336</a>)</li>
<li>Don’t push before creating a pull (<a href="https://gitea.com/gitea/tea/pulls/334">#334</a>)</li>
<li>InitCommand() robustness (<a href="https://gitea.com/gitea/tea/pulls/327">#327</a>)</li>
<li><code>tea comment</code>: handle piped stdin (<a href="https://gitea.com/gitea/tea/pulls/322">#322</a>)</li>
</ul>
</li>
<li>ENHANCEMENTS
<ul>
<li>Allow checking out PRs with deleted head branch (<a href="https://gitea.com/gitea/tea/pulls/341">#341</a>)</li>
<li>Markdown renderer: detect terminal width, resolve relative URLs (<a href="https://gitea.com/gitea/tea/pulls/332">#332</a>)</li>
<li>Add more issue / pr creation parameters (<a href="https://gitea.com/gitea/tea/pulls/331">#331</a>)</li>
<li>Improve <code>tea time</code> (<a href="https://gitea.com/gitea/tea/pulls/319">#319</a>)</li>
<li><code>tea pr checkout</code>: dont create local branches (<a href="https://gitea.com/gitea/tea/pulls/314">#314</a>)</li>
<li>Add <code>tea issues --fields</code>, allow printing labels (<a href="https://gitea.com/gitea/tea/pulls/312">#312</a>)</li>
<li>Add more command shorthands (<a href="https://gitea.com/gitea/tea/pulls/307">#307</a>)</li>
<li>Show PR CI status (<a href="https://gitea.com/gitea/tea/pulls/306">#306</a>)</li>
<li>Make PR workflow helpers more robust (<a href="https://gitea.com/gitea/tea/pulls/300">#300</a>)</li>
</ul>
</li>
</ul>





  
</div>
            