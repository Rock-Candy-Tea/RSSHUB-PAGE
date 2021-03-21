
---
title: Gitea 1.13.4 is released
categories: 
    - 编程
    - Gitea - 博客
author: Gitea - 博客
comments: false
date: Wed, 10 Mar 2021 00:00:00 GMT
thumbnail: 
---

<div>   
<p> lunny</p>
<h2>
<a href="https://blog.gitea.io/2021/03/gitea-1.13.4-is-released/">
Gitea 1.13.4 is released
</a>
</h2>
<p>
<i>Wed Mar 10, 2021</i>
by
<b>
<a href="https://github.com/lunny">
lunny
</a>
</b>
</p>

<p>We are proud to present the release of Gitea version 1.13.4.</p>
<p>We highly encourage users to update to this version for some important bug-fixes.</p>
<p>We have merged <a href="https://github.com/go-gitea/gitea/pulls?q=is%3Apr+milestone%3A1.13.4+is%3Amerged">8</a> pull requests to release this version.</p>
<p>You can download one of our pre-built binaries from our <a href="https://dl.gitea.io/gitea/1.13.4/">downloads page</a> - make sure to select the correct platform! For further details on how to install, follow our <a href="https://docs.gitea.io/en-us/install-from-binary/">installation guide</a>.</p>
<p>We would like to give a special thanks to Septatrix for reporting a security issue that was patched in this release.</p>
<p>We would also like to thank all of our supporters on <a href="https://opencollective.com/gitea">Open Collective</a> who are helping to sustain us financially.</p>
<p><strong>Have you heard? We now have a <a href="https://shop.gitea.io/">swag shop</a>! 👕 🍵</strong></p>
<h2 id="changelog">Changelog</h2>
<h2 id="1134httpsgithubcomgo-giteagiteareleasestagv1134---2021-03-09"><a href="https://github.com/go-gitea/gitea/releases/tag/v1.13.4">1.13.4</a> - 2021-03-09</h2>
<ul>
<li>SECURITY
<ul>
<li>Fix issue popups (<a href="https://github.com/go-gitea/gitea/pull/14898">#14898</a>) (<a href="https://github.com/go-gitea/gitea/pull/14899">#14899</a>)</li>
</ul>
</li>
<li>BUGFIXES
<ul>
<li>Fix race in LFS ContentStore.Put(…) (<a href="https://github.com/go-gitea/gitea/pull/14895">#14895</a>) (<a href="https://github.com/go-gitea/gitea/pull/14913">#14913</a>)</li>
<li>Fix a couple of issues with a feeds (<a href="https://github.com/go-gitea/gitea/pull/14897">#14897</a>) (<a href="https://github.com/go-gitea/gitea/pull/14903">#14903</a>)</li>
<li>When transfering repository and database transaction failed, rollback the renames (<a href="https://github.com/go-gitea/gitea/pull/14864">#14864</a>) (<a href="https://github.com/go-gitea/gitea/pull/14902">#14902</a>)</li>
<li>Fix race in local storage (<a href="https://github.com/go-gitea/gitea/pull/14888">#14888</a>) (<a href="https://github.com/go-gitea/gitea/pull/14901">#14901</a>)</li>
<li>Fix 500 on pull view page if user is not loged in (<a href="https://github.com/go-gitea/gitea/pull/14885">#14885</a>) (<a href="https://github.com/go-gitea/gitea/pull/14886">#14886</a>)</li>
</ul>
</li>
<li>DOCS
<ul>
<li>Fix how lfs data path is set (<a href="https://github.com/go-gitea/gitea/pull/14855">#14855</a>) (<a href="https://github.com/go-gitea/gitea/pull/14884">#14884</a>)</li>
</ul>
</li>
</ul>





  
</div>
            