
---
title: 'Apple details the ways its CSAM detection system is designed to prevent misuse'
categories: 
 - 新媒体
 - 9To5
 - 9To5 分站
headimg: 'https://i1.wp.com/9to5mac.com/wp-content/uploads/sites/6/2021/08/Screen-Shot-2021-08-13-at-2.01.20-PM.jpeg?resize=1200%2C628&quality=82&strip=all&ssl=1'
author: 9To5
comments: false
date: Fri, 13 Aug 2021 19:02:41 GMT
thumbnail: 'https://i1.wp.com/9to5mac.com/wp-content/uploads/sites/6/2021/08/Screen-Shot-2021-08-13-at-2.01.20-PM.jpeg?resize=1200%2C628&quality=82&strip=all&ssl=1'
---

<div>   
<img src="https://i1.wp.com/9to5mac.com/wp-content/uploads/sites/6/2021/08/Screen-Shot-2021-08-13-at-2.01.20-PM.jpeg?resize=1200%2C628&quality=82&strip=all&ssl=1" referrerpolicy="no-referrer">
<p>Apple has <a href="https://9to5mac.com/2021/08/05/apple-announces-new-protections-for-child-safety-imessage-safety-icloud-photo-scanning-more/">published</a> a new document today that offers additional detail on its <a href="https://9to5mac.com/2021/08/05/apple-announces-new-protections-for-child-safety-imessage-safety-icloud-photo-scanning-more/">recently announced child safety features</a>. The company is addressing concerns about the potential for the new CSAM detection capability to turn into a backdoor, with specifics on the threshold it’s using and more. </p>
<p><span id="more-744667"></span>
</p>
<p>One of the more notable announcements by Apple today is that the system will be able to be audited by third parties. Apple explains that it will publish a Knowledge Base article with the root hash of the encrypted CSAM hash database. Apple will also allow users to inspect the root hash database on their device and compare against the database in the Knowledge Base article: </p>
<blockquote class="wp-block-quote">
<p>Apple will publish a Knowledge Base article containing a root hash of the encrypted CSAM hash database included with each version of every Apple operating system that supports the feature. Additionally, users will be able to inspect the root hash of the encrypted database present on their device, and compare it to the expected root hash in the Knowledge Base article. That the calculation of the root hash shown to the user in Settings is accurate is subject to code inspection by security researchers like all other iOS device-side security claims.</p>
<p>This approach enables third-party technical audits: an auditor can confirm that for any given root hash of the encrypted CSAM database in the Knowledge Base article or on a device, the database was generated only from an intersection of hashes from participating child safety organizations, with no additions, removals, or changes. Facilitating the audit does not require the child safety organization to provide any sensitive information like raw hashes or the source images used to generate the hashes – they must provide only a non-sensitive attestation of the full database that they sent to Apple. Then, in a secure on-campus environment, Apple can provide technical proof to the auditor that the intersection and blinding were performed correctly. A participating child safety organization can decide to perform the audit as well.</p>
</blockquote>
<p>Apple also addressed the possibility that an organization could include something other than known CSAM content in the database. Apple says that it will work with at least two child safety organizations to generate the database included in iOS that are not under control of the same government: </p>
<blockquote class="wp-block-quote">
<p>Apple generates the on-device perceptual CSAM hash database through an intersection of hashes provided by at least two child safety organizations operating in separate sovereign jurisdictions – that is, not under the control of the same government. Any perceptual hashes appearing in only one participating child safety organization’s database, or only in databases from multiple agencies in a single sovereign jurisdiction, are discarded by this process, and not included in the encrypted CSAM database that Apple includes in the operating system. This mechanism meets our source image correctness requirement.</p>
</blockquote>
<p>Apple also offers new details on the manual review process that is performed once the threshold is reached: </p>
<blockquote class="wp-block-quote">
<p>Since Apple does not possess the CSAM images whose perceptual hashes comprise the on-device database, it is important to understand that the reviewers are not merely reviewing whether a given flagged image corresponds to an entry in Apple’s encrypted CSAM image database – that is, an entry in the intersection of hashes from at least two child safety organizations operating in separate sovereign jurisdictions. Instead, the reviewers are confirming one thing only: that for an account that exceeded the match threshold, the positively-matching images have visual derivatives that are CSAM. This means that if non-CSAM images were ever inserted into the on-device perceptual CSAM hash database – inadvertently, or through coercion – there would be no effect unless Apple’s human reviewers were also informed what specific non-CSAM images they should flag (for accounts that exceed the match threshold), and were then coerced to do so.</p>
</blockquote>
<p>You can find the full document published by Apple today, <a href="https://www.apple.com/child-safety/pdf/Security_Threat_Model_Review_of_Apple_Child_Safety_Features.pdf">titled “Security Threat Model Review of Apple’s Child Safety Features,” right here</a>. </p>
<div class="ad-disclaimer-container"><p class="disclaimer-affiliate"><em>FTC: We use income earning auto affiliate links.</em> <a href="https://9to5mac.com/about/#affiliate">More.</a></p><!-- post ad --></div><div id="after_disclaimer_placement"></div>
  
</div>
            