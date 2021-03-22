
---
title: Gitea 1.12.5 is released
categories: 
    - 编程
    - Gitea - 博客
author: Gitea - 博客
comments: false
date: Thu, 01 Oct 2020 00:00:00 GMT
thumbnail: ''
---

<div>   
<p> jolheiser</p>
<h2>
<a href="https://blog.gitea.io/2020/10/gitea-1.12.5-is-released/">
Gitea 1.12.5 is released
</a>
</h2>
<p>
<i>Thu Oct 1, 2020</i>
by
<b>
<a href="https://github.com/jolheiser">
jolheiser
</a>
</b>
</p>

<p>We are proud to present the release of Gitea version 1.12.5.</p>
<p>We highly encourage users to update to this version for some important bug-fixes.</p>
<p>We have merged <a href="https://github.com/go-gitea/gitea/pulls?q=is%3Apr+milestone%3A1.12.5+is%3Amerged">25</a> pull requests to release this version.</p>
<p>You can download one of our pre-built binaries from our <a href="https://dl.gitea.io/gitea/1.12.5/">downloads page</a> - make sure to select the correct platform! For further details on how to install, follow our <a href="https://docs.gitea.io/en-us/install-from-binary/">installation guide</a>.</p>
<p>We would also like to thank all of our supporters on <a href="https://opencollective.com/gitea">Open Collective</a> who are helping to sustain us financially.</p>
<h2 id="changelog">Changelog</h2>
<h2 id="1125httpsgithubcomgo-giteagiteareleasestagv1125---2020-10-01"><a href="https://github.com/go-gitea/gitea/releases/tag/v1.12.5">1.12.5</a> - 2020-10-01</h2>
<ul>
<li>ENHANCEMENTS
<ul>
<li>gitea dump: include version & Check InstallLock (<a href="https://github.com/go-gitea/gitea/pull/12760">#12760</a>) (<a href="https://github.com/go-gitea/gitea/pull/12762">#12762</a>)</li>
</ul>
</li>
<li>BUGFIXES
<ul>
<li>Allow U2F with default settings for gitea in subpath (<a href="https://github.com/go-gitea/gitea/pull/12990">#12990</a>) (<a href="https://github.com/go-gitea/gitea/pull/13001">#13001</a>)</li>
<li>Prevent empty div when editing comment (<a href="https://github.com/go-gitea/gitea/pull/12404">#12404</a>) (<a href="https://github.com/go-gitea/gitea/pull/12991">#12991</a>)</li>
<li>On mirror update also update address in DB (<a href="https://github.com/go-gitea/gitea/pull/12964">#12964</a>) (<a href="https://github.com/go-gitea/gitea/pull/12967">#12967</a>)</li>
<li>Allow extended config on cron settings (<a href="https://github.com/go-gitea/gitea/pull/12939">#12939</a>) (<a href="https://github.com/go-gitea/gitea/pull/12943">#12943</a>)</li>
<li>Open transaction when adding Avatar email-hash pairs to the DB (<a href="https://github.com/go-gitea/gitea/pull/12577">#12577</a>) (<a href="https://github.com/go-gitea/gitea/pull/12940">#12940</a>)</li>
<li>Fix internal server error from ListUserOrgs API (<a href="https://github.com/go-gitea/gitea/pull/12910">#12910</a>) (<a href="https://github.com/go-gitea/gitea/pull/12915">#12915</a>)</li>
<li>Update only the repository columns that need updating (<a href="https://github.com/go-gitea/gitea/pull/12900">#12900</a>) (<a href="https://github.com/go-gitea/gitea/pull/12912">#12912</a>)</li>
<li>Fix panic when adding long comment (<a href="https://github.com/go-gitea/gitea/pull/12892">#12892</a>) (<a href="https://github.com/go-gitea/gitea/pull/12894">#12894</a>)</li>
<li>Add size limit for content of comment on action ui (<a href="https://github.com/go-gitea/gitea/pull/12881">#12881</a>) (<a href="https://github.com/go-gitea/gitea/pull/12890">#12890</a>)</li>
<li>Convert User expose ID each time (<a href="https://github.com/go-gitea/gitea/pull/12855">#12855</a>) (<a href="https://github.com/go-gitea/gitea/pull/12883">#12883</a>)</li>
<li>Support slashes in release tags (<a href="https://github.com/go-gitea/gitea/pull/12864">#12864</a>) (<a href="https://github.com/go-gitea/gitea/pull/12882">#12882</a>)</li>
<li>Add missing information to CreateRepo API endpoint (<a href="https://github.com/go-gitea/gitea/pull/12848">#12848</a>) (<a href="https://github.com/go-gitea/gitea/pull/12867">#12867</a>)</li>
<li>On Migration respect old DefaultBranch (<a href="https://github.com/go-gitea/gitea/pull/12843">#12843</a>) (<a href="https://github.com/go-gitea/gitea/pull/12858">#12858</a>)</li>
<li>Fix notifications page links (<a href="https://github.com/go-gitea/gitea/pull/12838">#12838</a>) (<a href="https://github.com/go-gitea/gitea/pull/12853">#12853</a>)</li>
<li>Stop cloning unnecessarily on PR update (<a href="https://github.com/go-gitea/gitea/pull/12839">#12839</a>) (<a href="https://github.com/go-gitea/gitea/pull/12852">#12852</a>)</li>
<li>Escape more things that are passed through str2html (<a href="https://github.com/go-gitea/gitea/pull/12622">#12622</a>) (<a href="https://github.com/go-gitea/gitea/pull/12850">#12850</a>)</li>
<li>Remove double escape on labels addition in comments (<a href="https://github.com/go-gitea/gitea/pull/12809">#12809</a>) (<a href="https://github.com/go-gitea/gitea/pull/12810">#12810</a>)</li>
<li>Fix “only mail on mention” bug (<a href="https://github.com/go-gitea/gitea/pull/12775">#12775</a>) (<a href="https://github.com/go-gitea/gitea/pull/12789">#12789</a>)</li>
<li>Fix yet another bug with diff file names (<a href="https://github.com/go-gitea/gitea/pull/12771">#12771</a>) (<a href="https://github.com/go-gitea/gitea/pull/12776">#12776</a>)</li>
<li>RepoInit Respect AlternateDefaultBranch (<a href="https://github.com/go-gitea/gitea/pull/12746">#12746</a>) (<a href="https://github.com/go-gitea/gitea/pull/12751">#12751</a>)</li>
<li>Fix Avatar Resize (resize algo NearestNeighbor -> Bilinear) (<a href="https://github.com/go-gitea/gitea/pull/12745">#12745</a>) (<a href="https://github.com/go-gitea/gitea/pull/12750">#12750</a>)</li>
</ul>
</li>
</ul>





  
</div>
            