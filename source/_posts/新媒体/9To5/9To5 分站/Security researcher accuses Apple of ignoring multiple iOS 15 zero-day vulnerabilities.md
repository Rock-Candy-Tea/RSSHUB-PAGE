
---
title: 'Security researcher accuses Apple of ignoring multiple iOS 15 zero-day vulnerabilities'
categories: 
 - 新媒体
 - 9To5
 - 9To5 分站
headimg: 'https://i1.wp.com/9to5mac.com/wp-content/uploads/sites/6/2021/07/apple-security.jpg?resize=1200%2C628&quality=82&strip=all&ssl=1'
author: 9To5
comments: false
date: Fri, 24 Sep 2021 13:01:49 GMT
thumbnail: 'https://i1.wp.com/9to5mac.com/wp-content/uploads/sites/6/2021/07/apple-security.jpg?resize=1200%2C628&quality=82&strip=all&ssl=1'
---

<div>   
<img src="https://i1.wp.com/9to5mac.com/wp-content/uploads/sites/6/2021/07/apple-security.jpg?resize=1200%2C628&quality=82&strip=all&ssl=1" referrerpolicy="no-referrer">
<p>Apple overhauled its security bounty program back in 2019 by making it open to anyone, increasing payouts, and more. However, the program has seen a good amount of <a href="https://9to5mac.com/2021/09/09/apple-bug-bounty-program-complaints-reform/">criticism from the infosec community</a>. Now another security researcher has shared their experience claiming that Apple didn’t give them credit for one zero-day flaw they reported which was fixed and that there are three more zero-day vulnerabilites in <a href="https://9to5mac.com/guides/ios-15/">iOS 15</a>.</p>
<p><span id="more-756456"></span>
</p>
<p>Security researcher illusionofchaos shared their experience in a <a href="https://habr.com/en/post/579714/">blog post</a> including the claim that Apple has known about and is ignoring three zero-day vulnerabilities since March and they are in iOS 15.</p>
<blockquote class="wp-block-quote">
<p>I want to share my frustrating experience participating in Apple Security Bounty program. I’ve reported four 0-day vulnerabilities this year between March 10 and May 4, as of now three of them are still present in the latest iOS version (15.0) and <a href="https://github.com/illusionofchaos/ios-analyticsd-pre14.7-exploit">one was fixed in 14.7</a>, but Apple decided to cover it up and not list it on the security content page. When I confronted them, they apologized, assured me it happened due to a processing issue and promised to list it on the security content page of the next update. There were three releases since then and they broke their promise each time.</p>
</blockquote>
<p>illusionofchaos says they asked Apple again for an explanation including that they would make their research public – in line with responsible disclosure guidelines – and Apple didn’t respond.</p>
<blockquote class="wp-block-quote">
<p>Ten days ago I asked for an explanation and warned then that I would make my research public if I don’t receive an explanation. My request was ignored so I’m doing what I said I would. My actions are in accordance with responsible disclosure guidelines (Google Project Zero discloses vulnerabilities in 90 days after reporting them to vendor, ZDI – in 120). I have waited much longer, up to half a year in one case.</p>
</blockquote>
<p>illusionofchaos shared details on the three other zero-day vulnerabilities that they found which include the “<a href="https://github.com/illusionofchaos/ios-gamed-0day">Gamed 0-day,</a>” “<a href="https://github.com/illusionofchaos/ios-nehelper-enum-apps-0day">Nehelper Enumerate Installed Apps 0-day</a>,” and “<a href="https://github.com/illusionofchaos/ios-nehelper-wifi-info-0day">Nehelper Wifi Info 0-day</a>” including proof of concept source code.</p>
<p>Here’s an overview of each one:</p>
<h3 id="h-gamed-0-day">Gamed 0-day</h3>
<p>Any app installed from the App Store may access the following data without any prompt from the user:</p>
<ul>
<li>Apple ID email and full name associated with it</li>
<li>Apple ID authentication token which allows to access at least one of the endpoints on *.apple.com on behalf of the user</li>
<li>Complete file system read access to the Core Duet database (contains a list of contacts from Mail, SMS, iMessage, 3rd-party messaging apps and metadata about all user’s interaction with these contacts (including timestamps and statistics), also some attachments (like URLs and texts)</li>
<li>Complete file system read access to the Speed Dial database and the Address Book database including contact pictures and other metadata like creation and modification dates (I’ve just checked on iOS 15 and this one inaccessible, so that one must have been quietly fixed recently)</li>
</ul>
<h3>Nehelper Enumerate Installed Apps 0-day</h3>
<p>The vulnerably allows any user-installed app to determine whether any app is installed on the device given its bundle ID.</p>
<h3>Nehelper Wifi Info 0-day</h3>
<p>XPC endpoint <code>com.apple.nehelper</code> accepts user-supplied parameter <code>sdk-version</code>, and if its value is less than or equal to 524288, <code>com.apple.developer.networking.wifi-info</code>entiltlement check is skipped. Ths makes it possible for any qualifying app (e.g. posessing location access authorization) to gain access to Wifi information without the required entitlement. This happens in <code>-[NEHelperWiFiInfoManager checkIfEntitled:]</code> in <code>/usr/libexec/nehelper</code>.</p>
<h2>Two perspectives</h2>
<p>Stepping back to look at the big picture, Apple has said its bug bounty program is a “runaway success” while the infosec community has shared a variety of specific criticisms and concerns about the program. These include claims that Apple has not responded or not responded promptly and also that Apple has not paid for flaws discovered that meet the bounty programs guidelines.</p>
<p>Notably, earlier this month we learned that Apple hired a new leader for its security bounty program with the goal of “reforming it.”</p>
<ul>
<li><a href="https://9to5mac.com/2021/09/09/apple-bug-bounty-program-complaints-reform/">Report: Apple hires new leader to reform its bug bounty program amid complaints from researchers</a></li>
</ul>
<div class="ad-disclaimer-container"><p class="disclaimer-affiliate"><em>FTC: We use income earning auto affiliate links.</em> <a href="https://9to5mac.com/about/#affiliate">More.</a></p><a href="https://bit.ly/3lEfJ7P"><img class="aligncenter wp-image-755154 size-full" src="https://9to5mac.com/wp-content/uploads/sites/6/2021/09/en_us-WD_MyPassportSSD_WEB-BNR-Sustain-750x150V2.jpg?quality=82&strip=all" alt width="750" height="150" referrerpolicy="no-referrer"></a></div><div id="after_disclaimer_placement"></div>
<!-- youtube embed -->
  
</div>
            