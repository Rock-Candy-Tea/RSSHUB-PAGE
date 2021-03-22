
---
title: """""""""'Gitea 1.13.3 is released'"""""""""
categories: 
    - 编程
    - Gitea - 博客
author: Gitea - 博客
comments: false
date: Fri, 05 Mar 2021 00:00:00 GMT
thumbnail: ''
---

<div>   
<p> 6543</p>
<h2>
<a href="https://blog.gitea.io/2021/03/gitea-1.13.3-is-released/">
Gitea 1.13.3 is released
</a>
</h2>
<p>
<i>Fri Mar 5, 2021</i>
by
<b>
<a href="https://github.com/6543">
6543
</a>
</b>
</p>

<p>We are proud to present the release of Gitea version 1.13.3.</p>
<p>We highly encourage users to update to this version for some important bug-fixes.</p>
<p>We have merged <a href="https://github.com/go-gitea/gitea/pulls?q=is%3Apr+milestone%3A1.13.3+is%3Amerged">21</a> pull requests to release this version.</p>
<p>You can download one of our pre-built binaries from our <a href="https://dl.gitea.io/gitea/1.13.3/">downloads page</a> - make sure to select the correct platform! For further details on how to install, follow our <a href="https://docs.gitea.io/en-us/install-from-binary/">installation guide</a>.</p>
<p>❗ Password hashing algorithm default has changed back to pbkdf2 from argon2. (<a href="https://github.com/go-gitea/gitea/pull/14673">#14673</a>)</p>
<p>We would also like to thank all of our supporters on <a href="https://opencollective.com/gitea">Open Collective</a> who are helping to sustain us financially.</p>
<p><strong>Have you heard? We now have a <a href="https://shop.gitea.io/">swag shop</a>! 👕 🍵</strong></p>
<h2 id="changelog">Changelog</h2>
<h2 id="1133httpsgithubcomgo-giteagiteareleasestagv1133---2021-03-05"><a href="https://github.com/go-gitea/gitea/releases/tag/v1.13.3">1.13.3</a> - 2021-03-05</h2>
<ul>
<li>BREAKING & SECURITY
<ul>
<li>Turn default hash password algorithm back to pbkdf2 from argon2 until we find a better one (<a href="https://github.com/go-gitea/gitea/pull/14673">#14673</a>) (<a href="https://github.com/go-gitea/gitea/pull/14675">#14675</a>)</li>
</ul>
</li>
<li>BUGFIXES
<ul>
<li>Fix paging of file commit logs (<a href="https://github.com/go-gitea/gitea/pull/14831">#14831</a>) (<a href="https://github.com/go-gitea/gitea/pull/14879">#14879</a>)</li>
<li>Print useful error if SQLite is used in settings but not supported (<a href="https://github.com/go-gitea/gitea/pull/14476">#14476</a>) (<a href="https://github.com/go-gitea/gitea/pull/14874">#14874</a>)</li>
<li>Fix display since time round (<a href="https://github.com/go-gitea/gitea/pull/14226">#14226</a>) (<a href="https://github.com/go-gitea/gitea/pull/14873">#14873</a>)</li>
<li>When Deleting Repository only explicitly close PRs whose base is not this repository (<a href="https://github.com/go-gitea/gitea/pull/14823">#14823</a>) (<a href="https://github.com/go-gitea/gitea/pull/14842">#14842</a>)</li>
<li>Set HCaptchaSiteKey on Link Account pages (<a href="https://github.com/go-gitea/gitea/pull/14834">#14834</a>) (<a href="https://github.com/go-gitea/gitea/pull/14839">#14839</a>)</li>
<li>Fix a couple of CommentAsPatch issues.  (<a href="https://github.com/go-gitea/gitea/pull/14804">#14804</a>) (<a href="https://github.com/go-gitea/gitea/pull/14820">#14820</a>)</li>
<li>Disable broken OAuth2 providers at startup (<a href="https://github.com/go-gitea/gitea/pull/14802">#14802</a>) (<a href="https://github.com/go-gitea/gitea/pull/14811">#14811</a>)</li>
<li>Repo Transfer permission checks (<a href="https://github.com/go-gitea/gitea/pull/14792">#14792</a>) (<a href="https://github.com/go-gitea/gitea/pull/14794">#14794</a>)</li>
<li>Fix double alert in oauth2 application edit view (<a href="https://github.com/go-gitea/gitea/pull/14764">#14764</a>) (<a href="https://github.com/go-gitea/gitea/pull/14768">#14768</a>)</li>
<li>Fix broken spans in diffs (<a href="https://github.com/go-gitea/gitea/pull/14678">#14678</a>) (<a href="https://github.com/go-gitea/gitea/pull/14683">#14683</a>)</li>
<li>Prevent race in PersistableChannelUniqueQueue.Has (<a href="https://github.com/go-gitea/gitea/pull/14651">#14651</a>) (<a href="https://github.com/go-gitea/gitea/pull/14676">#14676</a>)</li>
<li>HasPreviousCommit causes recursive load of commits unnecessarily (<a href="https://github.com/go-gitea/gitea/pull/14598">#14598</a>) (<a href="https://github.com/go-gitea/gitea/pull/14649">#14649</a>)</li>
<li>Do not assume all 40 char strings are SHA1s (<a href="https://github.com/go-gitea/gitea/pull/14624">#14624</a>) (<a href="https://github.com/go-gitea/gitea/pull/14648">#14648</a>)</li>
<li>Allow org labels to be set with issue templates (<a href="https://github.com/go-gitea/gitea/pull/14593">#14593</a>) (<a href="https://github.com/go-gitea/gitea/pull/14647">#14647</a>)</li>
<li>Accept multiple SSH keys in single LDAP SSHPublicKey attribute (<a href="https://github.com/go-gitea/gitea/pull/13989">#13989</a>) (<a href="https://github.com/go-gitea/gitea/pull/14607">#14607</a>)</li>
<li>Fix bug about ListOptions and stars/watchers pagnation (<a href="https://github.com/go-gitea/gitea/pull/14556">#14556</a>) (<a href="https://github.com/go-gitea/gitea/pull/14573">#14573</a>)</li>
<li>Fix GPG key deletion during account deletion (<a href="https://github.com/go-gitea/gitea/pull/14561">#14561</a>) (<a href="https://github.com/go-gitea/gitea/pull/14569">#14569</a>)</li>
</ul>
</li>
</ul>





  
</div>
            