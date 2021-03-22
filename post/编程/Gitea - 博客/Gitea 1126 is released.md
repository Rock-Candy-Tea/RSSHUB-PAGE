
---
title: Gitea 1.12.6 is released
categories: 
    - 编程
    - Gitea - 博客
author: Gitea - 博客
comments: false
date: Mon, 16 Nov 2020 00:00:00 GMT
thumbnail: ''
---

<div>   
<p> gary-kim</p>
<h2>
<a href="https://blog.gitea.io/2020/11/gitea-1.12.6-is-released/">
Gitea 1.12.6 is released
</a>
</h2>
<p>
<i>Mon Nov 16, 2020</i>
by
<b>
<a href="https://github.com/gary-kim">
gary-kim
</a>
</b>
</p>

<p>We are proud to present the release of Gitea version 1.12.6.</p>
<p>We highly encourage users to update to this version as it contains some important security and bug fixes.</p>
<p>We have merged <a href="https://github.com/go-gitea/gitea/pulls?q=is%3Apr+milestone%3A1.12.6+is%3Amerged">27</a> pull requests to release this version.</p>
<p>We would like to give a special thanks to <a href="https://github.com/stypr">stypr</a> of Flatt Security Inc. for reporting security issues that have been patched in this release.</p>
<p>You can download one of our pre-built binaries from our <a href="https://dl.gitea.io/gitea/1.12.6/">downloads page</a> - make sure to select the correct platform! For further details on how to install, follow our <a href="https://docs.gitea.io/en-us/install-from-binary/">installation guide</a>.</p>
<p>We would also like to thank all of our supporters on <a href="https://opencollective.com/gitea">Open Collective</a> who are helping to sustain us financially.</p>
<h2 id="changelog">Changelog</h2>
<h2 id="1126httpsgithubcomgo-giteagiteareleasestagv1126---2020-11-11"><a href="https://github.com/go-gitea/gitea/releases/tag/v1.12.6">1.12.6</a> - 2020-11-11</h2>
<ul>
<li>SECURITY
<ul>
<li>Prevent git operations for inactive users (<a href="https://github.com/go-gitea/gitea/pull/13527">#13527</a>) (<a href="https://github.com/go-gitea/gitea/pull/13537">#13537</a>)</li>
<li>Disallow urlencoded new lines in git protocol paths if there is a port (<a href="https://github.com/go-gitea/gitea/pull/13521">#13521</a>) (<a href="https://github.com/go-gitea/gitea/pull/13525">#13525</a>)</li>
</ul>
</li>
<li>BUGFIXES
<ul>
<li>API should only return Json (<a href="https://github.com/go-gitea/gitea/pull/13511">#13511</a>) (<a href="https://github.com/go-gitea/gitea/pull/13564">#13564</a>)</li>
<li>Fix before and since query arguments at API (<a href="https://github.com/go-gitea/gitea/pull/13559">#13559</a>) (<a href="https://github.com/go-gitea/gitea/pull/13560">#13560</a>)</li>
<li>Prevent panic on git blame by limiting lines to 4096 bytes at most (<a href="https://github.com/go-gitea/gitea/pull/13470">#13470</a>) (<a href="https://github.com/go-gitea/gitea/pull/13492">#13492</a>)</li>
<li>Fix link detection in repository description with tailing ‘_’ (<a href="https://github.com/go-gitea/gitea/pull/13407">#13407</a>) (<a href="https://github.com/go-gitea/gitea/pull/13408">#13408</a>)</li>
<li>Remove obsolete change of email on profile page (<a href="https://github.com/go-gitea/gitea/pull/13341">#13341</a>) (<a href="https://github.com/go-gitea/gitea/pull/13348">#13348</a>)</li>
<li>Fix permission check on get Reactions API endpoints (<a href="https://github.com/go-gitea/gitea/pull/13344">#13344</a>) (<a href="https://github.com/go-gitea/gitea/pull/13346">#13346</a>)</li>
<li>Add migrated pulls to pull request task queue (<a href="https://github.com/go-gitea/gitea/pull/13331">#13331</a>) (<a href="https://github.com/go-gitea/gitea/pull/13335">#13335</a>)</li>
<li>API deny wrong pull creation options (<a href="https://github.com/go-gitea/gitea/pull/13308">#13308</a>) (<a href="https://github.com/go-gitea/gitea/pull/13327">#13327</a>)</li>
<li>Fix initial commit page & binary munching problem (<a href="https://github.com/go-gitea/gitea/pull/13249">#13249</a>) (<a href="https://github.com/go-gitea/gitea/pull/13259">#13259</a>)</li>
<li>Fix diff parsing (<a href="https://github.com/go-gitea/gitea/pull/13157">#13157</a>) (<a href="https://github.com/go-gitea/gitea/pull/13136">#13136</a>) (<a href="https://github.com/go-gitea/gitea/pull/13139">#13139</a>)</li>
<li>Return error 404 not 500 from API if team does not exist (<a href="https://github.com/go-gitea/gitea/pull/13118">#13118</a>) (<a href="https://github.com/go-gitea/gitea/pull/13119">#13119</a>)</li>
<li>Prohibit automatic downgrades (<a href="https://github.com/go-gitea/gitea/pull/13108">#13108</a>) (<a href="https://github.com/go-gitea/gitea/pull/13111">#13111</a>)</li>
<li>Fix GitLab Migration Option AuthToken (<a href="https://github.com/go-gitea/gitea/pull/13101">#13101</a>)</li>
<li>GitLab Label Color Normalizer (<a href="https://github.com/go-gitea/gitea/pull/12793">#12793</a>) (<a href="https://github.com/go-gitea/gitea/pull/13100">#13100</a>)</li>
<li>Log the underlying panic in runMigrateTask (<a href="https://github.com/go-gitea/gitea/pull/13096">#13096</a>) (<a href="https://github.com/go-gitea/gitea/pull/13098">#13098</a>)</li>
<li>Fix attachments list in edit comment (<a href="https://github.com/go-gitea/gitea/pull/13036">#13036</a>) (<a href="https://github.com/go-gitea/gitea/pull/13097">#13097</a>)</li>
<li>Fix deadlock when deleting team user (<a href="https://github.com/go-gitea/gitea/pull/13093">#13093</a>)</li>
<li>Fix error create comment on outdated file (<a href="https://github.com/go-gitea/gitea/pull/13041">#13041</a>) (<a href="https://github.com/go-gitea/gitea/pull/13042">#13042</a>)</li>
<li>Fix repository create/delete event webhooks (<a href="https://github.com/go-gitea/gitea/pull/13008">#13008</a>) (<a href="https://github.com/go-gitea/gitea/pull/13027">#13027</a>)</li>
<li>Fix internal server error on README in submodule (<a href="https://github.com/go-gitea/gitea/pull/13006">#13006</a>) (<a href="https://github.com/go-gitea/gitea/pull/13016">#13016</a>)</li>
</ul>
</li>
</ul>





  
</div>
            