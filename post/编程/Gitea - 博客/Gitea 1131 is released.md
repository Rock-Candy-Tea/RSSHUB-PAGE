
---
title: Gitea 1.13.1 is released
categories: 
    - 编程
    - Gitea - 博客
author: Gitea - 博客
comments: false
date: Mon, 28 Dec 2020 00:00:00 GMT
thumbnail: ''
---

<div>   
<p> techknowlogick</p>
<h2>
<a href="https://blog.gitea.io/2020/12/gitea-1.13.1-is-released/">
Gitea 1.13.1 is released
</a>
</h2>
<p>
<i>Mon Dec 28, 2020</i>
by
<b>
<a href="https://github.com/techknowlogick">
techknowlogick
</a>
</b>
</p>

<p>We are proud to present the release of Gitea version 1.13.1.</p>
<p>We highly encourage users to update to this version for some important security fixes.</p>
<p>We have merged <a href="https://github.com/go-gitea/gitea/pulls?q=is%3Apr+milestone%3A1.13.1+is%3Amerged">33</a> pull requests to release this version.</p>
<!-- raw HTML omitted -->
<p>We would like to give a special thanks to Sebastian Goettsch (<a href="https://github.com/sgoettsch">@sgoettsch</a>) for reporting a security issue that was patched in this release.<br>
Thanks to <a href="https://github.com/zeripath">@zeripath</a> for fixing in <a href="https://github.com/go-gitea/gitea/pull/14154">#14154</a>, and <a href="https://github.com/6543">@6543</a> for fixing another one in <a href="https://github.com/go-gitea/gitea/pull/14031">#14031</a>.</p>
<p>You can download one of our pre-built binaries from our <a href="https://dl.gitea.io/gitea/1.13.1/">downloads page</a> - make sure to select the correct platform! For further details on how to install, follow our <a href="https://docs.gitea.io/en-us/install-from-binary/">installation guide</a>.</p>
<p>We would also like to thank all of our supporters on <a href="https://opencollective.com/gitea">Open Collective</a> who are helping to sustain us financially.</p>
<p><strong>Have you heard? We now have a <a href="https://shop.gitea.io/">swag shop</a>! 👕 🍵</strong></p>
<h2 id="changelog">Changelog</h2>
<h2 id="1131httpsgithubcomgo-giteagiteareleasestagv1131---2020-12-28"><a href="https://github.com/go-gitea/gitea/releases/tag/v1.13.1">1.13.1</a> - 2020-12-28</h2>
<ul>
<li>SECURITY
<ul>
<li>Hide private participation in Orgs (<a href="https://github.com/go-gitea/gitea/pull/13994">#13994</a>) (<a href="https://github.com/go-gitea/gitea/pull/14031">#14031</a>)</li>
<li>Fix escaping issue in diff (<a href="https://github.com/go-gitea/gitea/pull/14153">#14153</a>) (<a href="https://github.com/go-gitea/gitea/pull/14154">#14154</a>)</li>
</ul>
</li>
<li>BUGFIXES
<ul>
<li>Fix bug of link query order on markdown render (<a href="https://github.com/go-gitea/gitea/pull/14156">#14156</a>) (<a href="https://github.com/go-gitea/gitea/pull/14171">#14171</a>)</li>
<li>Drop long repo topics during migration (<a href="https://github.com/go-gitea/gitea/pull/14152">#14152</a>) (<a href="https://github.com/go-gitea/gitea/pull/14155">#14155</a>)</li>
<li>Ensure that search term and page are not lost on adoption page-turn (<a href="https://github.com/go-gitea/gitea/pull/14133">#14133</a>) (<a href="https://github.com/go-gitea/gitea/pull/14143">#14143</a>)</li>
<li>Fix storage config implementation (<a href="https://github.com/go-gitea/gitea/pull/14091">#14091</a>) (<a href="https://github.com/go-gitea/gitea/pull/14095">#14095</a>)</li>
<li>Fix panic in BasicAuthDecode (<a href="https://github.com/go-gitea/gitea/pull/14046">#14046</a>) (<a href="https://github.com/go-gitea/gitea/pull/14048">#14048</a>)</li>
<li>Always wait for the cmd to finish (<a href="https://github.com/go-gitea/gitea/pull/14006">#14006</a>) (<a href="https://github.com/go-gitea/gitea/pull/14039">#14039</a>)</li>
<li>Don’t use simpleMDE editor on mobile devices for 1.13 (<a href="https://github.com/go-gitea/gitea/pull/14029">#14029</a>)</li>
<li>Fix incorrect review comment diffs (<a href="https://github.com/go-gitea/gitea/pull/14002">#14002</a>) (<a href="https://github.com/go-gitea/gitea/pull/14011">#14011</a>)</li>
<li>Trim the branch prefix from action.GetBranch (<a href="https://github.com/go-gitea/gitea/pull/13981">#13981</a>) (<a href="https://github.com/go-gitea/gitea/pull/13986">#13986</a>)</li>
<li>Ensure template renderer is available before storage handler (<a href="https://github.com/go-gitea/gitea/pull/13164">#13164</a>) (<a href="https://github.com/go-gitea/gitea/pull/13982">#13982</a>)</li>
<li>Whenever the password is updated ensure that the hash algorithm is too (<a href="https://github.com/go-gitea/gitea/pull/13966">#13966</a>) (<a href="https://github.com/go-gitea/gitea/pull/13967">#13967</a>)</li>
<li>Enforce setting HEAD in wiki to master (<a href="https://github.com/go-gitea/gitea/pull/13950">#13950</a>) (<a href="https://github.com/go-gitea/gitea/pull/13961">#13961</a>)</li>
<li>Fix feishu webhook caused by API changed (<a href="https://github.com/go-gitea/gitea/pull/13938">#13938</a>)</li>
<li>Fix Quote Reply button on review diff (<a href="https://github.com/go-gitea/gitea/pull/13830">#13830</a>) (<a href="https://github.com/go-gitea/gitea/pull/13898">#13898</a>)</li>
<li>Fix Pull Merge when tag with same name as base branch exist (<a href="https://github.com/go-gitea/gitea/pull/13882">#13882</a>) (<a href="https://github.com/go-gitea/gitea/pull/13896">#13896</a>)</li>
<li>Fix mermaid chart size (<a href="https://github.com/go-gitea/gitea/pull/13865">#13865</a>)</li>
<li>Fix branch/tag notifications in mirror sync (<a href="https://github.com/go-gitea/gitea/pull/13855">#13855</a>) (<a href="https://github.com/go-gitea/gitea/pull/13862">#13862</a>)</li>
<li>Fix crash in short link processor (<a href="https://github.com/go-gitea/gitea/pull/13839">#13839</a>) (<a href="https://github.com/go-gitea/gitea/pull/13841">#13841</a>)</li>
<li>Update font stack to bootstrap’s latest (<a href="https://github.com/go-gitea/gitea/pull/13834">#13834</a>) (<a href="https://github.com/go-gitea/gitea/pull/13837">#13837</a>)</li>
<li>Make sure email recipients can see issue (<a href="https://github.com/go-gitea/gitea/pull/13820">#13820</a>) (<a href="https://github.com/go-gitea/gitea/pull/13827">#13827</a>)</li>
<li>Reply button is not removed when deleting a code review comment (<a href="https://github.com/go-gitea/gitea/pull/13824">#13824</a>)</li>
<li>When reinitialising DBConfig reset the database use flags (<a href="https://github.com/go-gitea/gitea/pull/13796">#13796</a>) (<a href="https://github.com/go-gitea/gitea/pull/13811">#13811</a>)</li>
</ul>
</li>
<li>ENHANCEMENTS
<ul>
<li>Add emoji in label to project boards (<a href="https://github.com/go-gitea/gitea/pull/13978">#13978</a>) (<a href="https://github.com/go-gitea/gitea/pull/14021">#14021</a>)</li>
<li>Send webhook when tag is removed via Web UI (<a href="https://github.com/go-gitea/gitea/pull/14015">#14015</a>) (<a href="https://github.com/go-gitea/gitea/pull/14019">#14019</a>)</li>
<li>Use Process Manager to create own Context (<a href="https://github.com/go-gitea/gitea/pull/13792">#13792</a>) (<a href="https://github.com/go-gitea/gitea/pull/13793">#13793</a>)</li>
</ul>
</li>
<li>API
<ul>
<li>GetCombinedCommitStatusByRef always return json & swagger doc fixes (<a href="https://github.com/go-gitea/gitea/pull/14047">#14047</a>)</li>
<li>Return original URL of Repositories (<a href="https://github.com/go-gitea/gitea/pull/13885">#13885</a>) (<a href="https://github.com/go-gitea/gitea/pull/13886">#13886</a>)</li>
</ul>
</li>
</ul>





  
</div>
            