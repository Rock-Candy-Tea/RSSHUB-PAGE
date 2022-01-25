
---
title: 'iCloud syncing issues are plaguing third-party apps as Apple stays silent'
categories: 
 - 新媒体
 - 9To5
 - 9To5 分站
headimg: 'https://i0.wp.com/9to5mac.com/wp-content/uploads/sites/6/2022/01/apple-icloud-cloudkit.jpg?resize=1200%2C628&quality=82&strip=all&ssl=1'
author: 9To5
comments: false
date: Mon, 24 Jan 2022 18:16:37 GMT
thumbnail: 'https://i0.wp.com/9to5mac.com/wp-content/uploads/sites/6/2022/01/apple-icloud-cloudkit.jpg?resize=1200%2C628&quality=82&strip=all&ssl=1'
---

<div>   
<img src="https://i0.wp.com/9to5mac.com/wp-content/uploads/sites/6/2022/01/apple-icloud-cloudkit.jpg?resize=1200%2C628&quality=82&strip=all&ssl=1" referrerpolicy="no-referrer">
<p>Over the last several months, an issue with iCloud has emerged that is impacting many popular third-party applications that rely on Apple’s cloud infrastructure for syncing and other tasks. Apple has not yet publicly acknowledged the problem, but some developers have reportedly been privately contacted by the company to confirm that it’s an iCloud server problem impacting their apps rather than an issue with the app itself. </p>
<p><span id="more-783039"></span>
</p>
<p>A <a href="https://developer.apple.com/forums/thread/695278">thread</a> on Apple’s Developer Forums has garnered attention and responses from hundreds of developers. The issue seems to center on Apple’s CloudKit technology, which is used by developers to sync user content across devices, encrypt data stored within an application, and much more. </p>
<p>For those unfamiliar, here’s how Apple describes CloudKit: </p>
<blockquote class="wp-block-quote">
<p>CloudKit is designed for manageability, flexibility, and power. By organizing apps in containers, CloudKit ensures each app is siloed so its data won’t get entangled with other apps. Specialized databases and zones also let you easily separate app information by access type or function. And together with efficient syncing and sharing capabilities, CloudKit provides a comprehensive feature set that lets you easily develop powerful cloud apps.</p>
</blockquote>
<p>The popular note taking application GoodNotes has published a <a href="https://support.goodnotes.com/hc/en-us/articles/4410195261327-iCloud-sync-stops-working-due-to-Request-failed-with-HTTP-Status-Code-503-error-">dedicated support article</a> addressing these issues. The company says that some GoodNotes users are seeing an error message reading “Service unavailable” citing that the “Request failed with HTTP Status Code 503.” In the case of GoodNotes, this issues appears to impact syncing across devices.</p>
<p>GoodNotes says that this issue is not unique to its application, and that it is working with Apple Technical Support: </p>
<blockquote class="wp-block-quote">
<p>HTTP 503 is a temporary error code (“Service unavailable”) indicating iCloud servers aren’t responding correctly to requests from your devices. The error typically gets resolved as GoodNotes <em>automatically</em> retries, but we’re getting many reports of the error lingering on, causing sync failures.</p>
<p>This issue is not apparent to us and we’ve escalated the case to Apple Technical Support team for investigation. It seems it’s happening to other apps as well.</p>
</blockquote>
<p>Meanwhile, Tapbots, the company behind the popular Tweetbot client for Twitter, has even gone as far as to add a dedicated “Sync Status” dashboard in the latest version of the app. Tapbots developer Paul Haddad <a href="https://twitter.com/tapbot_paul/status/1482738974154178562?s=21">explained</a> on Twitter that Tweetbot added this option to “give users some insight as to what might be broken” because “iCloud has been so consistently unreliable.” </p>
<p>Tapbots is <a href="https://twitter.com/jazzychad/status/1484331016831389696?s=21">not the only developer team</a> to do this, signaling that it’s becoming an increasingly widespread problem. Quentin Zervaas, the developer of the popular Streaks app among others, also <a href="https://twitter.com/qzervaas/status/1484745003855650818?s=21">spoke about this issue</a> on Twitter. </p>
<p>Citing reliability issues, <a href="https://twitter.com/jamesthomson">James Thomson</a>, developer of the popular calculator app PCalc, even went as far as to <a href="https://apps.apple.com/us/app/pcalc/id284666222">disable iCloud syncing</a> by default in the latest update: </p>
<blockquote class="wp-block-quote">
<p>Due to ongoing iCloud problems, iCloud syncing of user data and layouts has been switched off by default. You can still manually export and import to sync. We will switch this back on when Apple fixes things.</p>
</blockquote>
<p>On their blog <em><a href="https://reverttosaved.com/2022/01/24/icloud-sync-is-randomly-breaking/">Revert to Saved,</a> </em>Craig Grannell detailed iCloud Sync issues plaguing a number of applications including Soulver, Transloader, and more. </p>
<h2 id="h-9to5mac-s-take">9to5Mac’s Take</h2>
<p>Again, Apple has not publicly acknowledged this issue, but some developers say that they have heard privately from the company that it is aware of the ongoing problems and working to fix them. In the meantime, the support burden falls primarily on the third-party developers themselves. </p>
<p>The issue has apparently been lingering for nearly a year, but has gotten much worse over the last several months. The escalation of the issue is what’s led to many developers taking matters into their own hands with in-app status pages and setting changes. </p>
<p>Apple needs to address this issue — publicly — sooner rather than later. The longer these iCloud syncing issues (and even data loss is some instances) continue, the less confident developers and users will be when deciding whether to use iCloud in the future. </p>
<div class="ad-disclaimer-container"><p class="disclaimer-affiliate"><em>FTC: We use income earning auto affiliate links.</em> <a href="https://9to5mac.com/about/#affiliate">More.</a></p><!-- post ad --></div><div id="after_disclaimer_placement"></div>
<!-- youtube embed -->
  
</div>
            