
---
title: 'Gitea 1.13.5 is released'
categories: 
    - 编程
    - Gitea - 博客
author: Gitea - 博客
comments: false
date: Sun, 21 Mar 2021 00:00:00 GMT
thumbnail: ''
---

<div>   
<p> 6543</p>
<h2>
<a href="https://blog.gitea.io/2021/03/gitea-1.13.5-is-released/">
Gitea 1.13.5 is released
</a>
</h2>
<p>
<i>Sun Mar 21, 2021</i>
by
<b>
<a href="https://github.com/6543">
6543
</a>
</b>
</p>

<p>We are proud to present the release of Gitea version 1.13.5.</p>
<p>We highly encourage users to update to this version for some important bug-fixes.</p>
<p>We have merged <a href="https://github.com/go-gitea/gitea/pulls?q=is%3Apr+milestone%3A1.13.5+is%3Amerged">17</a> pull requests to release this version.</p>
<!-- raw HTML omitted -->
<p>You can download one of our pre-built binaries from our <a href="https://dl.gitea.io/gitea/1.13.5/">downloads page</a> - make sure to select the correct platform! For further details on how to install, follow our <a href="https://docs.gitea.io/en-us/install-from-binary/">installation guide</a>.</p>
<p>We would also like to thank all of our supporters on <a href="https://opencollective.com/gitea">Open Collective</a> who are helping to sustain us financially.</p>
<p><strong>Have you heard? We now have a <a href="https://shop.gitea.io/">swag shop</a>! 👕 🍵</strong></p>
<h2 id="changelog">Changelog</h2>
<h2 id="1135httpsgithubcomgo-giteagiteareleasestagv1135---2021-03-21"><a href="https://github.com/go-gitea/gitea/releases/tag/v1.13.5">1.13.5</a> - 2021-03-21</h2>
<ul>
<li>SECURITY
<ul>
<li>Update to goldmark 1.3.3 (<a href="https://github.com/go-gitea/gitea/pull/15059">#15059</a>) (<a href="https://github.com/go-gitea/gitea/pull/15061">#15061</a>)</li>
<li>Fix another clusterfuzz spotted issue (<a href="https://github.com/go-gitea/gitea/pull/15032">#15032</a>) (<a href="https://github.com/go-gitea/gitea/pull/15034">#15034</a>)</li>
</ul>
</li>
<li>API
<ul>
<li>Fix set milestone on PR creation (<a href="https://github.com/go-gitea/gitea/pull/14981">#14981</a>) (<a href="https://github.com/go-gitea/gitea/pull/15001">#15001</a>)</li>
<li>Prevent panic when editing forked repos by API (<a href="https://github.com/go-gitea/gitea/pull/14960">#14960</a>) (<a href="https://github.com/go-gitea/gitea/pull/14963">#14963</a>)</li>
</ul>
</li>
<li>BUGFIXES
<ul>
<li>Fix bug when upload on web (<a href="https://github.com/go-gitea/gitea/pull/15042">#15042</a>) (<a href="https://github.com/go-gitea/gitea/pull/15055">#15055</a>)</li>
<li>Delete Labels & IssueLabels on Repo Delete too (<a href="https://github.com/go-gitea/gitea/pull/15039">#15039</a>) (<a href="https://github.com/go-gitea/gitea/pull/15051">#15051</a>)</li>
<li>Fix postgres ID sequences broken by recreate-table (<a href="https://github.com/go-gitea/gitea/pull/15015">#15015</a>) (<a href="https://github.com/go-gitea/gitea/pull/15029">#15029</a>)</li>
<li>Fix several render issues (<a href="https://github.com/go-gitea/gitea/pull/14986">#14986</a>) (<a href="https://github.com/go-gitea/gitea/pull/15013">#15013</a>)</li>
<li>Make sure sibling images get a link too (<a href="https://github.com/go-gitea/gitea/pull/14979">#14979</a>) (<a href="https://github.com/go-gitea/gitea/pull/14995">#14995</a>)</li>
<li>Fix Anchor jumping with escaped query components (<a href="https://github.com/go-gitea/gitea/pull/14969">#14969</a>) (<a href="https://github.com/go-gitea/gitea/pull/14977">#14977</a>)</li>
<li>Fix release mail html template (<a href="https://github.com/go-gitea/gitea/pull/14976">#14976</a>)</li>
<li>Fix excluding more than two labels on issues list (<a href="https://github.com/go-gitea/gitea/pull/14962">#14962</a>) (<a href="https://github.com/go-gitea/gitea/pull/14973">#14973</a>)</li>
<li>Don’t mark each comment poster as OP (<a href="https://github.com/go-gitea/gitea/pull/14971">#14971</a>) (<a href="https://github.com/go-gitea/gitea/pull/14972">#14972</a>)</li>
<li>Add “captcha” to list of reserved usernames (<a href="https://github.com/go-gitea/gitea/pull/14930">#14930</a>)</li>
<li>Re-enable import local paths after reversion from #13610 (<a href="https://github.com/go-gitea/gitea/pull/14925">#14925</a>) (<a href="https://github.com/go-gitea/gitea/pull/14927">#14927</a>)</li>
</ul>
</li>
</ul>





  
</div>
            