
---
title: Gitea 1.13.0 is released
categories: 
    - 编程
    - Gitea - 博客
author: Gitea - 博客
comments: false
date: Wed, 02 Dec 2020 00:00:00 GMT
thumbnail: https://blog.gitea.io/demos/shop/shirt.png
---

<div>   
<p> jolheiser</p>
<h2>
<a href="https://blog.gitea.io/2020/12/gitea-1.13.0-is-released/">
Gitea 1.13.0 is released
</a>
</h2>
<p>
<i>Wed Dec 2, 2020</i>
by
<b>
<a href="https://github.com/jolheiser">
jolheiser
</a>
</b>
</p>

<p>We are proud to present the release of Gitea version 1.13.0.</p>
<p>As we approach Gitea’s <a href="https://blog.gitea.io/2016/12/release-of-1.0.0/">4th birthday</a>, I just want to give a special thanks to everyone who has been a part of the project, whether it’s the implementation of a feature, or just enjoying the software.<br>
Thank you all!</p>
<p>We have merged an incredible <a href="https://github.com/go-gitea/gitea/pulls?q=is%3Apr+milestone%3A1.13.0+is%3Amerged">649</a> pull requests to release this version.</p>
<!-- raw HTML omitted -->
<p>We would like to give a special thanks to Michael Scherer (<a href="https://github.com/mscherer">@mscherer</a>) for reporting a security issue that was patched in this release.<br>
Thanks to <a href="https://github.com/zeripath">@zeripath</a> for fixing in <a href="https://github.com/go-gitea/gitea/pull/12685">#12685</a></p>
<p>You can download one of our pre-built binaries from our <a href="https://dl.gitea.io/gitea/1.13.0/">downloads page</a> - make sure to select the correct platform! For further details on how to install, follow our <a href="https://docs.gitea.io/en-us/install-from-binary/">installation guide</a>.</p>
<p>❗ As of this version, Gitea supports TLS version 1.2 at <em>minimum</em>. (<a href="https://github.com/go-gitea/gitea/pull/12689">#12689</a>)</p>
<p>❗ Users with a custom favicon will need to provide a <code>favicon.svg</code>. (<a href="https://github.com/go-gitea/gitea/pull/12437">#12437</a>)</p>
<p>❗ Password complexity checks now default to <code>off</code>. (<a href="https://github.com/go-gitea/gitea/pull/12557">#12557</a>)<br>
Alternative methods such as minimum length or checking against HaveIBeenPwned should be considered.</p>
<p>❗ The Webhook shared secret inside the webhook payload has been deprecated and will be removed in 1.14.0: <a href="https://github.com/go-gitea/gitea/issues/11755">https://github.com/go-gitea/gitea/issues/11755</a> please use the secret header that uses an hmac signature to validate the webhook payload.</p>
<p>❗ Git hooks now default to <code>off</code>! (<a href="https://github.com/go-gitea/gitea/pull/13058">#13058</a>)<br>
In your config, you can check the <a href="https://docs.gitea.io/en-us/config-cheat-sheet/#security-security">security</a> section for
<code>DISABLE_GIT_HOOKS</code>. To enable them again, you must set the setting to <code>false</code>.<br>
<strong>WARNING:</strong> Custom git hooks can be used to perform arbitrary code execution on the host operating system.
This enables the users to access and modify this config file and the Gitea database and interrupt the Gitea service.
By modifying the Gitea database, users can gain Gitea administrator privileges.
It also enables them to access other resources available to the user on the operating system that is running the Gitea instance and perform arbitrary actions in the name of the Gitea OS user.
This may be harmful to you website or your operating system.</p>
<p>We would also like to thank all of our supporters on <a href="https://opencollective.com/gitea">Open Collective</a> who are helping to sustain us financially.</p>
<p><strong>Have you heard? We now have a <a href="https://shop.gitea.io/">swag shop</a>! 👕 🍵</strong><br>
Sample images below.</p>
<table>
<thead>
<tr>
<th><img src="https://blog.gitea.io/demos/shop/shirt.png" alt="shirt" referrerpolicy="no-referrer"></th>
<th><img src="https://blog.gitea.io/demos/shop/hoodie.png" alt="hoodie" referrerpolicy="no-referrer"></th>
<th><img src="https://blog.gitea.io/demos/shop/ladies.png" alt="ladies" referrerpolicy="no-referrer"></th>
</tr>
</thead>
</table>
<!-- raw HTML omitted -->
<p>Now, on to the changes!</p>
<h2 id="adopt-repositories-12920httpsgithubcomgo-giteagiteapull12920">Adopt repositories (<a href="https://github.com/go-gitea/gitea/pull/12920">#12920</a>)</h2>
<p>Administrators can now adopt repositories that are on disk, but not yet in Gitea’s database.</p>
<p>An administrator can also allow users to adopt repositories from their settings.</p>
<p><em>Thanks to <a href="https://github.com/zeripath"><strong>@zeripath</strong></a></em></p>
<h2 id="check-passwords-against-haveibeenpwned-12716httpsgithubcomgo-giteagiteapull12716">Check passwords against HaveIBeenPwned (<a href="https://github.com/go-gitea/gitea/pull/12716">#12716</a>)</h2>
<p>A new, optional password policy to check new passwords against <a href="https://haveibeenpwned.com/Passwords">HaveIBeenPwned</a>.</p>
<p><em>Thanks to <a href="https://github.com/jolheiser"><strong>@jolheiser</strong></a></em></p>
<h2 id="add-a-migrate-service-type-switch-page-12697httpsgithubcomgo-giteagiteapull12697">Add a migrate service type switch page (<a href="https://github.com/go-gitea/gitea/pull/12697">#12697</a>)</h2>
<p><img src="https://blog.gitea.io/demos/12697/1.png" alt="migration" referrerpolicy="no-referrer"></p>
<p><em>Thanks to <a href="https://github.com/lunny"><strong>@lunny</strong></a></em><br>
<em>Thanks to <a href="https://github.com/6543"><strong>@6543</strong></a> for gitea2gitea migration (<a href="https://github.com/go-gitea/gitea/pull/12657">#12657</a>)</em></p>
<h2 id="mermaid-js-renderer-12334httpsgithubcomgo-giteagiteapull12334">Mermaid JS renderer (<a href="https://github.com/go-gitea/gitea/pull/12334">#12334</a>)</h2>
<p><img src="https://blog.gitea.io/demos/12334/1.png" alt="mermaid" referrerpolicy="no-referrer"></p>
<p><em>Thanks to <a href="https://github.com/silverwind"><strong>@silverwind</strong></a></em></p>
<h2 id="add-spent-time-to-referenced-issue-in-commit-message-12220httpsgithubcomgo-giteagiteapull12220">Add spent time to referenced issue in commit message (<a href="https://github.com/go-gitea/gitea/pull/12220">#12220</a>)</h2>
<p><img src="https://blog.gitea.io/demos/12220/1.png" alt="time" referrerpolicy="no-referrer"></p>
<p><em>Thanks to <a href="https://github.com/lafriks"><strong>@lafriks</strong></a></em></p>
<h2 id="enable-cloning-via-git-wire-protocol-v2-over-http-12170httpsgithubcomgo-giteagiteapull12170">Enable cloning via Git Wire Protocol v2 over HTTP (<a href="https://github.com/go-gitea/gitea/pull/12170">#12170</a>)</h2>
<p><img src="https://blog.gitea.io/demos/12170/1.gif" alt="v2" referrerpolicy="no-referrer"></p>
<p><em>Thanks to <a href="https://github.com/wmhilton"><strong>@wmhilton</strong></a></em></p>
<h2 id="issue-templates-directory-11450httpsgithubcomgo-giteagiteapull11450">Issue templates directory (<a href="https://github.com/go-gitea/gitea/pull/11450">#11450</a>)</h2>
<table>
<thead>
<tr>
<th><img src="https://blog.gitea.io/demos/11450/1.png" alt="raw" referrerpolicy="no-referrer"></th>
<th><img src="https://blog.gitea.io/demos/11450/2.png" alt="preview" referrerpolicy="no-referrer"></th>
</tr>
</thead>
</table>
<p><em>Thanks to <a href="https://github.com/jolheiser"><strong>@jolheiser</strong></a></em></p>
<h2 id="storage-layer-for-attachments--avatars--lfs-11387httpsgithubcomgo-giteagiteapull11387-11516httpsgithubcomgo-giteagiteapull12516-12518httpsgithubcomgo-giteagiteapull12518">Storage layer for attachments / avatars / LFS (<a href="https://github.com/go-gitea/gitea/pull/11387">#11387</a>, <a href="https://github.com/go-gitea/gitea/pull/12516">#11516</a>, <a href="https://github.com/go-gitea/gitea/pull/12518">#12518</a>)</h2>
<p>Attachments, user avatars, repo avatars and LFS files can now be saved to disk, or served via minio. (More S3-compatible integrations may become available in the future!). Now there is no storage layer only on git data.
See <a href="https://docs.gitea.io/en-us/config-cheat-sheet/#storage-storage">https://docs.gitea.io/en-us/config-cheat-sheet/#storage-storage</a> about how to configure it.</p>
<p><em>Thanks to <a href="https://github.com/lunny"><strong>@lunny</strong></a></em></p>
<p>And also thanks to <em><a href="https://github.com/zeripath"><strong>@zeripath</strong></a></em> for simplifying the configuration <a href="https://github.com/go-gitea/gitea/pull/12978">#12978</a></p>
<h2 id="push-commits-history-comment-on-pr-time-line-11167httpsgithubcomgo-giteagiteapull11167">Push commits history comment on PR time-line (<a href="https://github.com/go-gitea/gitea/pull/11167">#11167</a>)</h2>
<p><img src="https://blog.gitea.io/demos/11167/1.png" alt="commits" referrerpolicy="no-referrer"></p>
<p><em>Thanks to <a href="https://github.com/a1012112796"><strong>@a1012112796</strong></a></em></p>
<h2 id="support-elastic-search-for-code-search-10273httpsgithubcomgo-giteagiteapull10273">Support elastic search for code search (<a href="https://github.com/go-gitea/gitea/pull/10273">#10273</a>)</h2>
<p>Elastic search can now be used as the code search indexer.</p>
<p><em>Thanks to <a href="https://github.com/lunny"><strong>@lunny</strong></a></em></p>
<h2 id="kanban-board-8346httpsgithubcomgo-giteagiteapull8346">Kanban board (<a href="https://github.com/go-gitea/gitea/pull/8346">#8346</a>)</h2>
<p><img src="https://blog.gitea.io/demos/8346/1.png" alt="kanban" referrerpolicy="no-referrer"></p>
<p><em>Thanks to <a href="https://github.com/adelowo"><strong>@adelowo</strong></a></em><br>
<em>Also thanks to <a href="https://github.com/jaqra"><strong>@jaqra</strong></a>, <a href="https://github.com/TsakiDev"><strong>@TsakiDev</strong></a>, <a href="https://github.com/6543"><strong>@6543</strong></a>, and <a href="https://github.com/zeripath"><strong>@zeripath</strong></a> for additional support</em></p>
<h2 id="server-side-syntax-highlighting-for-all-code-12047httpsgithubcomgo-giteagiteapull12047">Server-side syntax highlighting for all code (<a href="https://github.com/go-gitea/gitea/pull/12047">#12047</a>)</h2>
<h3 id="old">Old</h3>
<table>
<thead>
<tr>
<th><img src="https://blog.gitea.io/demos/12047/1o.png" alt="diff-old" referrerpolicy="no-referrer"></th>
<th><img src="https://blog.gitea.io/demos/12047/2o.png" alt="diff-side-old" referrerpolicy="no-referrer"></th>
</tr>
</thead>
</table>
<h3 id="new">New</h3>
<table>
<thead>
<tr>
<th><img src="https://blog.gitea.io/demos/12047/1n.png" alt="diff-new" referrerpolicy="no-referrer"></th>
<th><img src="https://blog.gitea.io/demos/12047/2n.png" alt="diff-side-new" referrerpolicy="no-referrer"></th>
</tr>
</thead>
<tbody>
<tr>
<td><img src="https://blog.gitea.io/demos/12047/3n.png" alt="blame" referrerpolicy="no-referrer"></td>
<td><img src="https://blog.gitea.io/demos/12047/4n.png" alt="comment" referrerpolicy="no-referrer"></td>
</tr>
</tbody>
</table>
<p><em>Thanks to <a href="https://github.com/mrsdizzie"><strong>@mrsdizzie</strong></a></em><br>
<em>Additional thanks to <a href="https://github.com/silverwind"><strong>@silverwind</strong></a> for a <strong>ton</strong> of UI improvements for highlighting</em></p>
<h2 id="changelog">Changelog</h2>
<h2 id="1130httpsgithubcomgo-giteagiteareleasestagv1130---2020-12-01"><a href="https://github.com/go-gitea/gitea/releases/tag/v1.13.0">1.13.0</a> - 2020-12-01</h2>
<ul>
<li>SECURITY
<ul>
<li>Add Allow-/Block-List for Migrate & Mirrors (<a href="https://github.com/go-gitea/gitea/pull/13610">#13610</a>) (<a href="https://github.com/go-gitea/gitea/pull/13776">#13776</a>)</li>
<li>Prevent git operations for inactive users (<a href="https://github.com/go-gitea/gitea/pull/13527">#13527</a>) (<a href="https://github.com/go-gitea/gitea/pull/13536">#13536</a>)</li>
<li>Disallow urlencoded new lines in git protocol paths if there is a port (<a href="https://github.com/go-gitea/gitea/pull/13521">#13521</a>) (<a href="https://github.com/go-gitea/gitea/pull/13524">#13524</a>)</li>
<li>Mitigate Security vulnerability in the git hook feature (<a href="https://github.com/go-gitea/gitea/pull/13058">#13058</a>)</li>
<li>Disable DSA ssh keys by default (<a href="https://github.com/go-gitea/gitea/pull/13056">#13056</a>)</li>
<li>Set TLS minimum version to 1.2 (<a href="https://github.com/go-gitea/gitea/pull/12689">#12689</a>)</li>
<li>Use argon as default password hash algorithm (<a href="https://github.com/go-gitea/gitea/pull/12688">#12688</a>)</li>
<li>Escape failed highlighted files (<a href="https://github.com/go-gitea/gitea/pull/12685">#12685</a>)</li>
</ul>
</li>
<li>BREAKING
<ul>
<li>Set RUN_MODE prod by default (<a href="https://github.com/go-gitea/gitea/pull/13765">#13765</a>) (<a href="https://github.com/go-gitea/gitea/pull/13767">#13767</a>)</li>
<li>Don’t replace underscores in auto-generated IDs in goldmark (<a href="https://github.com/go-gitea/gitea/pull/12805">#12805</a>)</li>
<li>Add Primary Key to Topic and RepoTopic tables (<a href="https://github.com/go-gitea/gitea/pull/12639">#12639</a>)</li>
<li>Disable password complexity check default (<a href="https://github.com/go-gitea/gitea/pull/12557">#12557</a>)</li>
<li>Change PIDFile default from /var/run/gitea.pid to /run/gitea.pid (<a href="https://github.com/go-gitea/gitea/pull/12500">#12500</a>)</li>
<li>Add extension Support to Attachments (allow all types for releases) (<a href="https://github.com/go-gitea/gitea/pull/12465">#12465</a>)</li>
<li>Remove IE11 Support (<a href="https://github.com/go-gitea/gitea/pull/11470">#11470</a>)</li>
</ul>
</li>
<li>FEATURES
<ul>
<li>Adopt repositories (#12920)</li>
<li>Check passwords against HaveIBeenPwned (#12716)</li>
<li>Gitea 2 Gitea migration (#12657)</li>
<li>Support storing Avatars in minio  (#12516)</li>
<li>Allow addition of gpg keyring with multiple keys (#12487)</li>
<li>Add email notify for new release (#12463)</li>
<li>Add Access-Control-Expose-Headers (#12446)</li>
<li>UserProfile Page: Render Description (#12415)</li>
<li>Add command to recreate tables (#12407)</li>
<li>Add mermaid JS renderer (#12334)</li>
<li>Add ssh certificate support (#12281)</li>
<li>Add spent time to referenced issue in commit message (#12220)</li>
<li>Initial support for push options (#12169)</li>
<li>Provide option to unlink a fork (#11858)</li>
<li>Show exact tag for commit on diff view (#11846)</li>
<li>Pause, Resume, Release&Reopen, Add and Remove Logging from command line (#11777)</li>
<li>Issue templates directory (#11450)</li>
<li>Add a storage layer for attachments (#11387)</li>
<li>Add hide activity option (#11353)</li>
<li>Add push commits history comment on PR time-line (#11167)</li>
<li>Support elastic search for code search (#10273)</li>
<li>Kanban board (#8346)</li>
</ul>
</li>
<li>API
<ul>
<li>If User is Admin, show 500 error message on PROD mode too (#13115)</li>
<li>Add Timestamp to Tag list API (#13026)</li>
<li>Return sample message for login error in api context (#12994)</li>
<li>Add IsTemplate option in create repo ui and api (#12942)</li>
<li>GetReleaseByID return 404 if not found (#12933)</li>
<li>Get release by tags endpoint (#12932)</li>
<li>NotificationSubject show Issue/Pull State (#12901)</li>
<li>Expose its limitation settings (#12714)</li>
<li>Add Created & Updated to Milestone (#12662)</li>
<li>Milestone endpoints accept names too (#12649)</li>
<li>Expose Attachment Settings in the API (#12514)</li>
<li>Add Issue and Repo info to StopWatch (#12458)</li>
<li>Add cron running API (#12421)</li>
<li>Add Update Pull HeadBranch Function (#12419)</li>
<li>Add TOTP header to Swagger Documentation (#12402)</li>
<li>Delete Token accept names too (#12366)</li>
<li>Add name filter for GetMilestoneList (#12336)</li>
<li>Fixed count of filtered issues when api request. (#12275)</li>
<li>Do not override API issue pagination with UI settings (#12068)</li>
<li>Expose useful General Repo settings settings (#11758)</li>
<li>Return error when trying to create Mirrors but Mirrors are globally disabled (#11757)</li>
<li>Provide diff and patch API endpoints (#11751)</li>
<li>Allow to create closed milestones (#11745)</li>
<li>Add language Statistics endpoint (#11737)</li>
<li>Add Endpoint to get GetGeneralUI Settings (#11735) & (#11854)</li>
<li>Issue/Pull expose IsLocked Property on API (#11708)</li>
<li>Add endpoint for Branch Creation (#11607)</li>
<li>Add pagination headers on endpoints that support total count from database (#11145)</li>
</ul>
</li>
<li>BUGFIXES
<ul>
<li>Fix bogus http requests on diffs (#13760) (#13761)</li>
<li>Show ‘owner’ tag for real owner (#13689) (#13743)</li>
<li>Validate email before inserting/updating (#13475) (#13666)</li>
<li>Fix issue/pull request list assignee filter (#13647) (#13651)</li>
<li>Gitlab migration support for subdirectories (#13563) (#13591)</li>
<li>Fix logic for preferred license setting (#13550) (#13557)</li>
<li>Add missed sync branch/tag webhook (#13538) (#13556)</li>
<li>Migration won’t fail on non-migrated reactions (#13507)</li>
<li>Fix Italian language file parsing error (#13156)</li>
<li>Show outdated comments in pull request (#13148) (#13162)</li>
<li>Fix parsing of pre-release git version (#13169) (#13172)</li>
<li>Fix diff skipping lines (#13154) (#13155)</li>
<li>When handling errors in storageHandler check underlying error (#13178) (#13193)</li>
<li>Fix size and clickable area on file table back link (#13205) (#13207)</li>
<li>Add better error checking for inline html diff code (#13251)</li>
<li>Fix initial commit page & binary munching problem (#13249) (#13258)</li>
<li>Fix migrations from remote Gitea instances when configuration not set (#13229) (#13273)</li>
<li>Store task errors following migrations and display them (#13246) (#13287)</li>
<li>Fix bug isEnd detection on getIssues/getPullRequests (#13299) (#13301)</li>
<li>When the git ref is unable to be found return broken pr (#13218) (#13303)</li>
<li>Ensure topics added using the API are added to the repository (#13285) (#13302)</li>
<li>Fix avatar autogeneration (#13233) (#13282)</li>
<li>Add migrated pulls to pull request task queue (#13331) (#13334)</li>
<li>Issue comment reactions should also check pull type on API (#13349) (#13350)</li>
<li>Fix links to repositories in /user/setting/repos (#13360) (#13362)</li>
<li>Remove obsolete change of email on profile page (#13341) (#13347)</li>
<li>Fix scrolling to resolved comment anchors (#13343) (#13371)</li>
<li>Storage configuration support <code>[storage]</code> (#13314) (#13379)</li>
<li>When creating line diffs do not split within an html entity (#13357) (#13375) (#13425) (#13427)</li>
<li>Fix reactions on code comments (#13390) (#13401)</li>
<li>Add missing full names when DEFAULT_SHOW_FULL_NAME is enabled (#13424)</li>
<li>Replies to outdated code comments should also be outdated (#13217) (#13433)</li>
<li>Fix panic bug in handling multiple references in commit (#13486) (#13487)</li>
<li>Prevent panic on git blame by limiting lines to 4096 bytes at most (#13470) (#13491)</li>
<li>Show original author’s reviews on pull summary box (#13127)</li>
<li>Update golangci-lint to version 1.31.0 (#13102)</li>
<li>Fix line break for MS teams webhook (#13081)</li>
<li>Fix Issue & Pull Request comment headers on mobile (#13039)</li>
<li>Avoid setting the CONN_STR in queues unless it is meant to be set (#13025)</li>
<li>Remove code-view class from diff view (#13011)</li>
<li>Fix the color of PR comment hyperlinks. (#13009)</li>
<li>(Re)Load issue labels when changing them (#13007)</li>
<li>Fix Media links in org files not liked to media files (#12997)</li>
<li>Always return a list from GetCommitsFromIDs (#12981)</li>
<li>Only set the user password if the password field would have been shown (#12980)</li>
<li>Fix admin/config page (#12979)</li>
<li>Changed width of commit signature avatar (#12961)</li>
<li>Completely quote AppPath and CustomConf paths (#12955)</li>
<li>Fix handling of migration errors (#12928)</li>
<li>Fix anonymous GL migration (#12862)</li>
<li>Fix git open close bug (#12834)</li>
<li>Fix markdown meta parsing (#12817)</li>
<li>Add default storage configurations (#12813)</li>
<li>Show PR settings on empty repos (#12808)</li>
<li>Disable watch and star if not signed in (#12807)</li>
<li>Whilst changing the character set to utf8mb4 we should set ROW_FORMAT=dynamic too (#12804)</li>
<li>Set opengraph attributes on org pages (#12803)</li>
<li>Return error when creating gitlabdownloader failed (#12790)</li>
<li>Add migration for password algorithm change (#12784)</li>
<li>Compare SSH_DOMAIN when parsing submodule URLs (#12753)</li>
<li>Fix editor.commit_empty_file_text locale string (#12744)</li>
<li>Fix wrong poster message for code comment on Pull view (#11721)</li>
<li>Ensure that all migration requests are cancellable (#12669)</li>
<li>Ensure RepoPath is lowercased in gitea serv (#12668)</li>
<li>Do not disable commit changes button on repost (#12644)</li>
<li>Dark theme for line numbers in blame view (#12632)</li>
<li>Fix message when deleting last owner from an organization (#12628)</li>
<li>Use shellquote to unpack arguments to gitea serv (#12624)</li>
<li>Fix signing.wont_sign.%!s(<!-- raw HTML omitted -->) if Require Signing commits but not signed in. (#12581)</li>
<li>Set utf8mb4 as the default charset on MySQL if CHARSET is unset (#12563)</li>
<li>Set context for running CreateArchive to that of the request (#12555)</li>
<li>Prevent redirect back to /user/events (#12462)</li>
<li>Re-attempt to delete temporary upload if the file is locked by another process (#12447)</li>
<li>Mirror System Notice reports are too frequent (#12438)</li>
<li>Do not show arrows on comment diffs on pull comment pages (#12434)</li>
<li>Fix milestone links (#12405)</li>
<li>Increase size of the language column in language_stat (#12396)</li>
<li>Use transaction in V102 migration (#12395)</li>
<li>Only use –exclude on name-rev with git >= 2.13 (#12347)</li>
<li>Add action feed for new release (#12324)</li>
<li>Set NoAutoTime when updating is_archived (#12266)</li>
<li>Support Force-update in Mirror and improve Tracing in mirror (#12242)</li>
<li>Avoid sending “0 new commits” webhooks (#12212)</li>
<li>Fix U2F button icon (#12167)</li>
<li>models/repo_sign.go: break out of loops (#12159)</li>
<li>Ensure that git commit tree continues properly over the page (#12142)</li>
<li>Rewrite GitGraph.js (#12137)</li>
<li>Fix repo API listing stability (#12057)</li>
<li>Add team support for review request (#12039)</li>
<li>Fix 500 error on repos with no tags (#11870)</li>
<li>Fix nil pointer in default issue mail template (#11862)</li>
<li>Fix commit search in all branches (#11849)</li>
<li>Don’t consider tag refs as valid for branch name (#11847)</li>
<li>Don’t add same line code comment box twice (#11837)</li>
<li>Fix visibility of forked public repos from private orgs (#11717)</li>
<li>Fix chardet test and add ordering option (#11621)</li>
<li>Fix number of files, total additions, and deletions on Diff pages (#11614)</li>
<li>Properly handle and return empty string for dangling commits in GetBranchName (#11587)</li>
<li>Include query in sign in redirect (#11579)</li>
<li>Fix Enter not working in SimpleMDE (#11564)</li>
<li>Fix bug about can’t skip commits base on base branch (#11555)</li>
</ul>
</li>
<li>ENHANCEMENTS
<ul>
<li>Only Return JSON for responses (#13511) (#13565)</li>
<li>Use existing analyzer module for language detection for highlighting (#13522) (#13551)</li>
<li>Return the full rejection message and errors in flash errors (#13221) (#13237)</li>
<li>Remove PAM from auth dropdown when unavailable (#13276) (#13281)</li>
<li>Add HostCertificate to sshd_config in Docker image (#13143)</li>
<li>Save TimeStamps for Star, Label, Follow, Watch and Collaboration to Database (#13124)</li>
<li>Improve error feedback for duplicate deploy keys (#13112)</li>
<li>Set appropriate <code>autocomplete</code> attributes on password fields (#13078)</li>
<li>Adding visual cue for “Limited” & “Private” organizations. (#13040)</li>
<li>Fix Pull Request merge buttons on mobile (#13035)</li>
<li>Gitea serv, hooks, manager and the like should always display Fatals (#13032)</li>
<li>CSS tweaks to warning/error segments and misc fixes (#13024)</li>
<li>Fix formatting of branches ahead-behind on narrow windows (#12989)</li>
<li>Add config option to make create-on-push repositories public by default (#12936)</li>
<li>Disable migration items when mirror is selected (#12918)</li>
<li>Add the checkbox quick button to the comment tool bar also (#12885)</li>
<li>Support GH enterprise (#12863)</li>
<li>Simplify CheckUnitUser logic (#12854)</li>
<li>Fix background of signed-commits on arc-green of timeline commits (#12837)</li>
<li>Move git update-server-info to hooks (#12826)</li>
<li>Add ui style for “Open a blank issue” button (#12824)</li>
<li>Use a simple format for the big number on ui (#12822)</li>
<li>Make SVG size argument optional (#12814)</li>
<li>Add placeholder text for bio profile text form (#12792)</li>
<li>Set language via AJAX (#12785)</li>
<li>Show git-pull-request icon for closed pull request (#12742)</li>
<li>Migrate version parsing library to hashicorp/go-version (#12719)</li>
<li>Only use async pre-empt hack if go < 1.15 (#12718)</li>
<li>Inform user about meaning of an hourglass on reviews (#12713)</li>
<li>Add a migrate service type switch page (#12697)</li>
<li>Migrations: Gitlab Add Reactions Support for Issues & MergeRequests (#12695)</li>
<li>Remove duplicate logic in initListSubmits (#12660)</li>
<li>Set avatar image dimensions (#12654)</li>
<li>Rename models.ProtectedBranchRepoID/PRID to models.EnvRepoID/PRID and ensure EnvPusherEmail is set (#12646)</li>
<li>Set setting.AppURL as GITEA_ROOT_URL environment variable during pushes (#12752)</li>
<li>Add postgres schema to the search_path on database connection (#12634)</li>
<li>Git migration UX improvements (#12619)</li>
<li>Add link to home page on swagger ui (#12601)</li>
<li>hCaptcha Support (#12594)</li>
<li>OpenGraph: use repo avatar if exist (#12586)</li>
<li>Reaction picker display improvements (#12576)</li>
<li>Fix emoji replacements, make emoji images consistent (#12567)</li>
<li>Increase clickable area on files table links (#12553)</li>
<li>Set z-index for sticky diff box lower (#12537)</li>
<li>Report error if API merge is not allowed (#12528)</li>
<li>LFS support to be stored on minio (#12518)</li>
<li>Show 2FA info on Admin Pannel: Users List (#12515)</li>
<li>Milestone Issue/Pull List: Add octicons type (#12499)</li>
<li>Make dashboard newsfeed list length a configurable item (#12469)</li>
<li>Add placeholder text for send testing email button in admin/config (#12452)</li>
<li>Add SVG favicon (#12437)</li>
<li>In issue comments, put issue participants also in completion list when hitting @ (#12433)</li>
<li>Collapse Swagger UI tags by default (#12428)</li>
<li>Detect full references to issues and pulls in commit messages (#12399)</li>
<li>Allow common redis and leveldb connections (#12385)</li>
<li>Don’t use legacy method to send Matrix Webhook (#12348)</li>
<li>Remove padding/border-radius on image diffs (#12346)</li>
<li>Render the git graph on the server (#12333)</li>
<li>Fix clone panel in wiki position not always align right (#12326)</li>
<li>Rework ‘make generate-images’ (#12316)</li>
<li>Refactor webhook payload convertion (#12310)</li>
<li>Move jquery-minicolors to npm/webpack (#12305)</li>
<li>Support use nvarchar for all varchar columns when using mssql (#12269)</li>
<li>Update Octicons to v10 (#12240)</li>
<li>Disable search box autofocus (#12229)</li>
<li>Replace code fold icons with octicons (#12222)</li>
<li>Ensure syntax highlighting is the same inside diffs (#12205)</li>
<li>Auto-init repo on license, .gitignore select (#12202)</li>
<li>Default to showing closed Issues/PR list when there are only closed issues/PRs (#12200)</li>
<li>Enable cloning via Git Wire Protocol v2 over HTTP (#12170)</li>
<li>Direct SVG rendering (#12157)</li>
<li>Improve arc-green code colors (#12111)</li>
<li>Allow admin to merge pr with protected file changes (#12078)</li>
<li>Show description on individual milestone view (#12055)</li>
<li>Update the wiki repository remote origin while update the mirror repository’s Clone From URL (#12053)</li>
<li>Server-side syntax highlighting for all code (#12047)</li>
<li>Use Fomantic’s fluid padded for blame full width (#12023)</li>
<li>Use custom SVGs for commit signing lock icon (#12017)</li>
<li>Make tabs smaller (#12003)</li>
<li>Fix sticky diff stats container (#12002)</li>
<li>Move fomantic and jQuery to main webpack bundle (#11997)</li>
<li>Use enry language type to detect special languages (#11974)</li>
<li>Use only first line of commit when creating referenced comment (#11960)</li>
<li>Rename custom/conf/app.ini.sample to custom/conf/app.example.ini for better syntax light on editor (#11926)</li>
<li>Fix double divider on issue sidebar (#11919)</li>
<li>Shorten markdown heading anchors links (#11903)</li>
<li>Add org avatar on top of internal repo icon (#11895)</li>
<li>Use label to describe repository type (#11891)</li>
<li>Make repository size unclickable on repo summary bar (#11887)</li>
<li>Rework blame template and styling (#11885)</li>
<li>Fix icon alignment for show/hide outdated link on resolved conversation (#11881)</li>
<li>Vertically align review icons on repository sidebar (#11880)</li>
<li>Better align items using flex within review request box (#11879)</li>
<li>Only write to global gitconfig if necessary (#11876)</li>
<li>Disable all typographic replacements in markdown renderer (#11871)</li>
<li>Improve label edit buttons labels (#11841)</li>
<li>Use crispEdges rendering for octicon-internal-repo (#11801)</li>
<li>Show update branch item in merge box when it’s necessary (#11761)</li>
<li>Add compare link to releases (#11752)</li>
<li>Allow site admin to disable mirrors (#11740)</li>
<li>Export monaco editor on window.codeEditors (#11739)</li>
<li>Add configurable Trust Models (#11712)</li>
<li>Show full GPG commit status on PR commit history (#11702)</li>
<li>Fix align issues and decrease avatar size on PR timeline (#11689)</li>
<li>Replace jquery-datetimepicker with native date input (#11684)</li>
<li>Change Style of Tags on Comments (#11668)</li>
<li>Fix missing styling for shabox on PR commit history (#11625)</li>
<li>Apply padding to approval icons on PR list (#11622)</li>
<li>Fix message wrapping on PR commit list (#11616)</li>
<li>Right-align status icon on pull request commit history (#11594)</li>
<li>Add missing padding for multi-commit list on PR view (#11593)</li>
<li>Do not show avatar for “{{user}} added X commits” (#11591)</li>
<li>Fix styling and padding for commit list on PR view (#11588)</li>
<li>Style code review comment for arc-green (#11572)</li>
<li>Use default commit message for wiki edits (#11550)</li>
<li>Add internal-repo octicon for public repos of private org (#11529)</li>
<li>Fix dropzone color on arc-green (#11514)</li>
<li>Insert ui divider directly in templates instead of from inside heatmap vue component (#11508)</li>
<li>Move tributejs to npm/webpack (#11497)</li>
<li>Fix text-transform on wiki revisions page (#11486)</li>
<li>Do not show lock icon on repo list for public repos in private org (#11445)</li>
<li>Include LFS when calculating repo size (#11060)</li>
<li>Add check for LDAP group membership (#10869)</li>
<li>When starting new stopwatch stop previous if it is still running (#10533)</li>
<li>Add queue for code indexer (#10332)</li>
<li>Move all push update operations to a queue (#10133)</li>
<li>Cache last commit when pushing for big repository (#10109)</li>
<li>Change/remove a branch of an open issue (#9080)</li>
<li>Sortable Tables Header By Click (#7980)</li>
</ul>
</li>
<li>TESTING
<ul>
<li>Use community codecov drone plugin (#12468)</li>
<li>Add more tests for diff highlighting (#12467)</li>
<li>Don’t put integration test data outside of test folder (#11746)</li>
<li>Add debug option to hooks (#11624)</li>
<li>Log slow tests (#11487)</li>
</ul>
</li>
<li>TRANSLATION
<ul>
<li>Translate two small lables on commit statuse list (#12821)</li>
<li>Make issues.force_push_codes message shorter (#11575)</li>
</ul>
</li>
<li>BUILD
<ul>
<li>Bump min required golang to 1.13 (#12717)</li>
<li>Add ‘make watch’ (#12636)</li>
<li>Extract Swagger CSS to its own file (#12616)</li>
<li>Update eslint config (#12609)</li>
<li>Avoid unnecessary system-ui expansion (#12522)</li>
<li>Make the default PID file compile-time settable (#12485)</li>
<li>Add ‘watch-backend’ (#12330)</li>
<li>Detect version of sed in Makefile (#12319)</li>
<li>Update gitea-vet to v0.2.1 (#12282)</li>
<li>Add logic to build stable and edge builds for gitea snap (#12052)</li>
<li>Fix missing CGO_EXTRA_FLAGS build arg for docker (#11782)</li>
<li>Alpine 3.12 (#11720)</li>
<li>Enable stylelint’s shorthand-property-no-redundant-values (#11436)</li>
</ul>
</li>
<li>DOCS
<ul>
<li>Change default log configuration (#13088)</li>
<li>Add automatic JS license generation (#11810)</li>
<li>Remove page size limit comment from swagger (#11806)</li>
<li>Narrow down Edge version in browser support docs (#11640)</li>
</ul>
</li>
</ul>





  
</div>
            