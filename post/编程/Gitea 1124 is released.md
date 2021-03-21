
---
title: Gitea 1.12.4 is released
categories: 
    - 编程
    - Gitea - 博客
author: Gitea - 博客
comments: false
date: Fri, 04 Sep 2020 00:00:00 GMT
thumbnail: 
---

<div>   
<p> 6543</p>
<h2>
<a href="https://blog.gitea.io/2020/09/gitea-1.12.4-is-released/">
Gitea 1.12.4 is released
</a>
</h2>
<p>
<i>Fri Sep 4, 2020</i>
by
<b>
<a href="https://github.com/6543">
6543
</a>
</b>
</p>

<p>We are proud to present the release of Gitea version 1.12.4.</p>
<p>We highly encourage users to update to this version for some important bug-fixes.</p>
<p>We have merged <a href="https://github.com/go-gitea/gitea/pulls?q=is%3Apr+milestone%3A1.12.4+is%3Amerged+">24</a> pull requests to release this version.</p>
<p>We would like to give a special thanks to Jeffrey C. Ollie (<a href="https://github.com/jcollie">@jcollie</a>), Osama Hamad (<a href="https://github.com/osamahamad">@osamahamad</a>) and <a href="https://www.redteam-pentesting.de/">RedTeam Pentesting GmbH</a> for reporting security issues that have been patched in this release.</p>
<p>You can download one of our pre-built binaries from our <a href="https://dl.gitea.io/gitea/1.12.4/">downloads page</a> - make sure to select the correct platform! For further details on how to install, follow our <a href="https://docs.gitea.io/en-us/install-from-binary/">installation guide</a>.</p>
<p>We would also like to thank all of our supporters on <a href="https://opencollective.com/gitea">Open Collective</a> who are helping to sustain us financially.</p>
<h2 id="changelog">Changelog</h2>
<h2 id="1124httpsgithubcomgo-giteagiteareleasestagv1124---2020-09-03"><a href="https://github.com/go-gitea/gitea/releases/tag/v1.12.4">1.12.4</a> - 2020-09-03</h2>
<ul>
<li>SECURITY
<ul>
<li>Escape provider name in oauth2 provider redirect (<a href="https://github.com/go-gitea/gitea/pull/12648">#12648</a>) (<a href="https://github.com/go-gitea/gitea/pull/12650">#12650</a>)</li>
<li>Escape Email on password reset page (<a href="https://github.com/go-gitea/gitea/pull/12610">#12610</a>) (<a href="https://github.com/go-gitea/gitea/pull/12612">#12612</a>)</li>
<li>When reading expired sessions - expire them (<a href="https://github.com/go-gitea/gitea/pull/12686">#12686</a>) (<a href="https://github.com/go-gitea/gitea/pull/12690">#12690</a>)</li>
</ul>
</li>
<li>ENHANCEMENTS
<ul>
<li>StaticRootPath configurable at compile time (<a href="https://github.com/go-gitea/gitea/pull/12371">#12371</a>) (<a href="https://github.com/go-gitea/gitea/pull/12652">#12652</a>)</li>
</ul>
</li>
<li>BUGFIXES
<ul>
<li>Fix to show an issue that is related to a deleted issue (<a href="https://github.com/go-gitea/gitea/pull/12651">#12651</a>) (<a href="https://github.com/go-gitea/gitea/pull/12692">#12692</a>)</li>
<li>Expire time acknowledged for cache (<a href="https://github.com/go-gitea/gitea/pull/12605">#12605</a>) (<a href="https://github.com/go-gitea/gitea/pull/12611">#12611</a>)</li>
<li>Fix diff path unquoting (<a href="https://github.com/go-gitea/gitea/pull/12554">#12554</a>) (<a href="https://github.com/go-gitea/gitea/pull/12575">#12575</a>)</li>
<li>Improve HTML escaping helper (<a href="https://github.com/go-gitea/gitea/pull/12562">#12562</a>)</li>
<li>models: break out of loop (<a href="https://github.com/go-gitea/gitea/pull/12386">#12386</a>) (<a href="https://github.com/go-gitea/gitea/pull/12561">#12561</a>)</li>
<li>Default empty merger list to those with write permissions (<a href="https://github.com/go-gitea/gitea/pull/12535">#12535</a>) (<a href="https://github.com/go-gitea/gitea/pull/12560">#12560</a>)</li>
<li>Skip SSPI authentication attempts for /api/internal (<a href="https://github.com/go-gitea/gitea/pull/12556">#12556</a>) (<a href="https://github.com/go-gitea/gitea/pull/12559">#12559</a>)</li>
<li>Prevent NPE on commenting on lines with invalidated comments (<a href="https://github.com/go-gitea/gitea/pull/12549">#12549</a>) (<a href="https://github.com/go-gitea/gitea/pull/12550">#12550</a>)</li>
<li>Remove hardcoded ES indexername (<a href="https://github.com/go-gitea/gitea/pull/12521">#12521</a>) (<a href="https://github.com/go-gitea/gitea/pull/12526">#12526</a>)</li>
<li>Fix bug preventing transfer to private organization (<a href="https://github.com/go-gitea/gitea/pull/12497">#12497</a>) (<a href="https://github.com/go-gitea/gitea/pull/12501">#12501</a>)</li>
<li>Keys should not verify revoked email addresses (<a href="https://github.com/go-gitea/gitea/pull/12486">#12486</a>) (<a href="https://github.com/go-gitea/gitea/pull/12495">#12495</a>)</li>
<li>Do not add prefix on http/https submodule links (<a href="https://github.com/go-gitea/gitea/pull/12477">#12477</a>) (<a href="https://github.com/go-gitea/gitea/pull/12479">#12479</a>)</li>
<li>Fix ignored login on compare (<a href="https://github.com/go-gitea/gitea/pull/12476">#12476</a>) (<a href="https://github.com/go-gitea/gitea/pull/12478">#12478</a>)</li>
<li>Fix incorrect error logging in Stats indexer and OAuth2 (<a href="https://github.com/go-gitea/gitea/pull/12387">#12387</a>) (<a href="https://github.com/go-gitea/gitea/pull/12422">#12422</a>)</li>
<li>Upgrade google/go-github to v32.1.0 (<a href="https://github.com/go-gitea/gitea/pull/12361">#12361</a>) (<a href="https://github.com/go-gitea/gitea/pull/12390">#12390</a>)</li>
<li>Render emoji’s of Commit message on feed-page (<a href="https://github.com/go-gitea/gitea/pull/12373">#12373</a>)</li>
<li>Fix handling of diff on unrelated branches when Git 2.28 used (<a href="https://github.com/go-gitea/gitea/pull/12370">#12370</a>)</li>
</ul>
</li>
</ul>





  
</div>
            