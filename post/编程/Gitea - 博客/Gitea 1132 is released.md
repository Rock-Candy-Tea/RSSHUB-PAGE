
---
title: 'Gitea 1.13.2 is released'
categories: 
    - 编程
    - Gitea - 博客
author: Gitea - 博客
comments: false
date: Mon, 01 Feb 2021 00:00:00 GMT
thumbnail: ''
---

<div>   
<p> jolheiser</p>
<h2>
<a href="https://blog.gitea.io/2021/02/gitea-1.13.2-is-released/">
Gitea 1.13.2 is released
</a>
</h2>
<p>
<i>Mon Feb 1, 2021</i>
by
<b>
<a href="https://github.com/jolheiser">
jolheiser
</a>
</b>
</p>

<p>We are proud to present the release of Gitea version 1.13.2.</p>
<p>We highly encourage users to update to this version for some important bug-fixes.</p>
<p>We have merged <a href="https://github.com/go-gitea/gitea/pulls?q=is%3Apr+milestone%3A1.13.2+is%3Amerged">28</a> pull requests to release this version.</p>
<!-- raw HTML omitted -->
<p>You can download one of our pre-built binaries from our <a href="https://dl.gitea.io/gitea/1.13.2/">downloads page</a> - make sure to select the correct platform! For further details on how to install, follow our <a href="https://docs.gitea.io/en-us/install-from-binary/">installation guide</a>.</p>
<p>We would also like to thank all of our supporters on <a href="https://opencollective.com/gitea">Open Collective</a> who are helping to sustain us financially.</p>
<p><strong>Have you heard? We now have a <a href="https://shop.gitea.io/">swag shop</a>! 👕 🍵</strong></p>
<h2 id="changelog">Changelog</h2>
<h2 id="1132httpsgithubcomgo-giteagiteareleasestagv1132---2021-02-01"><a href="https://github.com/go-gitea/gitea/releases/tag/v1.13.2">1.13.2</a> - 2021-02-01</h2>
<ul>
<li>SECURITY
<ul>
<li>Prevent panic on fuzzer provided string (<a href="https://github.com/go-gitea/gitea/pull/14405">#14405</a>) (<a href="https://github.com/go-gitea/gitea/pull/14409">#14409</a>)</li>
<li>Add secure/httpOnly attributes to the lang cookie (<a href="https://github.com/go-gitea/gitea/pull/14279">#14279</a>) (<a href="https://github.com/go-gitea/gitea/pull/14280">#14280</a>)</li>
</ul>
</li>
<li>API
<ul>
<li>If release publisher is deleted use ghost user (<a href="https://github.com/go-gitea/gitea/pull/14375">#14375</a>)</li>
</ul>
</li>
<li>BUGFIXES
<ul>
<li>Internal ssh server respect Ciphers, MACs and KeyExchanges settings (<a href="https://github.com/go-gitea/gitea/pull/14523">#14523</a>) (<a href="https://github.com/go-gitea/gitea/pull/14530">#14530</a>)</li>
<li>Set the name Mapper in migrations (<a href="https://github.com/go-gitea/gitea/pull/14526">#14526</a>) (<a href="https://github.com/go-gitea/gitea/pull/14529">#14529</a>)</li>
<li>Fix wiki preview (<a href="https://github.com/go-gitea/gitea/pull/14515">#14515</a>)</li>
<li>Update code.gitea.io/sdk/gitea v0.13.1 -> v0.13.2 (<a href="https://github.com/go-gitea/gitea/pull/14497">#14497</a>)</li>
<li>ChangeUserName: rename user files back on DB issue (<a href="https://github.com/go-gitea/gitea/pull/14447">#14447</a>)</li>
<li>Fix lfs preview bug (<a href="https://github.com/go-gitea/gitea/pull/14428">#14428</a>) (<a href="https://github.com/go-gitea/gitea/pull/14433">#14433</a>)</li>
<li>Ensure timeout error is shown on u2f timeout (<a href="https://github.com/go-gitea/gitea/pull/14417">#14417</a>) (<a href="https://github.com/go-gitea/gitea/pull/14431">#14431</a>)</li>
<li>Fix Deadlock & Delete affected reactions on comment deletion (<a href="https://github.com/go-gitea/gitea/pull/14392">#14392</a>) (<a href="https://github.com/go-gitea/gitea/pull/14425">#14425</a>)</li>
<li>Use path not filepath in routers/editor (<a href="https://github.com/go-gitea/gitea/pull/14390">#14390</a>) (<a href="https://github.com/go-gitea/gitea/pull/14396">#14396</a>)</li>
<li>Check if label template exist first (<a href="https://github.com/go-gitea/gitea/pull/14384">#14384</a>) (<a href="https://github.com/go-gitea/gitea/pull/14389">#14389</a>)</li>
<li>Fix migration v141 (<a href="https://github.com/go-gitea/gitea/pull/14387">#14387</a>) (<a href="https://github.com/go-gitea/gitea/pull/14388">#14388</a>)</li>
<li>Use Request.URL.RequestURI() for fcgi (<a href="https://github.com/go-gitea/gitea/pull/14347">#14347</a>)</li>
<li>Use ServerError provided by Context (<a href="https://github.com/go-gitea/gitea/pull/14333">#14333</a>) (<a href="https://github.com/go-gitea/gitea/pull/14345">#14345</a>)</li>
<li>Fix edit-label form init (<a href="https://github.com/go-gitea/gitea/pull/14337">#14337</a>)</li>
<li>Fix mailIssueCommentBatch for pull request (<a href="https://github.com/go-gitea/gitea/pull/14252">#14252</a>) (<a href="https://github.com/go-gitea/gitea/pull/14296">#14296</a>)</li>
<li>Render links for commit hashes followed by comma (<a href="https://github.com/go-gitea/gitea/pull/14224">#14224</a>) (<a href="https://github.com/go-gitea/gitea/pull/14227">#14227</a>)</li>
<li>Send notifications for mentions in pulls, issues, (code-)comments (<a href="https://github.com/go-gitea/gitea/pull/14218">#14218</a>) (<a href="https://github.com/go-gitea/gitea/pull/14221">#14221</a>)</li>
<li>Fix avatar bugs (<a href="https://github.com/go-gitea/gitea/pull/14217">#14217</a>) (<a href="https://github.com/go-gitea/gitea/pull/14220">#14220</a>)</li>
<li>Ensure that schema search path is set with every connection on postgres (<a href="https://github.com/go-gitea/gitea/pull/14131">#14131</a>) (<a href="https://github.com/go-gitea/gitea/pull/14216">#14216</a>)</li>
<li>Fix dashboard issues labels filter bug (<a href="https://github.com/go-gitea/gitea/pull/14210">#14210</a>) (<a href="https://github.com/go-gitea/gitea/pull/14214">#14214</a>)</li>
<li>When visit /favicon.ico but the static file is not exist return 404 but not continue to handle the route (<a href="https://github.com/go-gitea/gitea/pull/14211">#14211</a>) (<a href="https://github.com/go-gitea/gitea/pull/14213">#14213</a>)</li>
<li>Fix branch selector on new issue page (<a href="https://github.com/go-gitea/gitea/pull/14194">#14194</a>) (<a href="https://github.com/go-gitea/gitea/pull/14207">#14207</a>)</li>
<li>Check for notExist on profile repository page (<a href="https://github.com/go-gitea/gitea/pull/14197">#14197</a>) (<a href="https://github.com/go-gitea/gitea/pull/14203">#14203</a>)</li>
</ul>
</li>
</ul>





  
</div>
            