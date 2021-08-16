
---
title: 'Misusing CSAM scanning in US prevented by Fourth Amendment, argues Corellium'
categories: 
 - 新媒体
 - 9To5
 - 9To5 分站
headimg: 'https://i1.wp.com/9to5mac.com/wp-content/uploads/sites/6/2021/08/4th-Amemdment-prohibits-misusing-CSAM-scanning.jpg?resize=1200%2C628&quality=82&strip=all&ssl=1'
author: 9To5
comments: false
date: Tue, 10 Aug 2021 14:08:50 GMT
thumbnail: 'https://i1.wp.com/9to5mac.com/wp-content/uploads/sites/6/2021/08/4th-Amemdment-prohibits-misusing-CSAM-scanning.jpg?resize=1200%2C628&quality=82&strip=all&ssl=1'
---

<div>   
<img src="https://i1.wp.com/9to5mac.com/wp-content/uploads/sites/6/2021/08/4th-Amemdment-prohibits-misusing-CSAM-scanning.jpg?resize=1200%2C628&quality=82&strip=all&ssl=1" referrerpolicy="no-referrer">
<p>While <a href="https://9to5mac.com/2021/08/06/comment-apples-child-protection-measures-get-mixed-reactions-from-experts/" target="_blank" rel="noreferrer noopener">most of the concerns</a> about governments misusing <a href="https://9to5mac.com/2021/08/05/apple-announces-new-protections-for-child-safety-imessage-safety-icloud-photo-scanning-more/" target="_blank" rel="noreferrer noopener">CSAM scanning</a> to detect things like political opposition have related to <em>foreign</em> governments, some have suggested that it could become an issue in the US, too.</p>
<p>Matt Tait, COO of security company <a href="https://9to5mac.com/guides/corellium/" target="_blank" rel="noreferrer noopener">Corellium</a>, and a former analyst at British NSA equivalent GCHQ, says the Fourth Amendment means that this could not happen in the US … </p>
<p><span id="more-743562"></span>
</p>
<p>Johns Hopkins cryptographer Matthew Green <a href="https://twitter.com/matthew_d_green/status/1424804380008660997" target="_blank" rel="noreferrer noopener">highlighted</a> the following scenario with regard to adding non-child sexual abuse materials to the database:</p>
<blockquote class="wp-block-quote">
<p>1. US DoJ approaches NCMEC, asks them to add non-CSAM photos to the hash database.</p>
<p>2. When these photos trigger against Apple users, DoJ sends a preservation order to Apple to obtain customer IDs.</p>
</blockquote>
<p><a href="https://twitter.com/pwnallthethings/status/1424873629003702273" target="_blank" rel="noreferrer noopener">Tait says in a Twitter thread</a> that the database is compiled by the National Center for Missing & Exploited Children (<a href="https://www.missingkids.org/" target="_blank" rel="noreferrer noopener">NCMEC</a>), which isn’t strictly speaking a government agency – it’s a quasi-autonomous body, though it is mostly funded by the DOJ. </p>
<blockquote class="wp-block-quote">
<p>That hands-off-ness serves means that DOJ can’t simply NCMEC to do things. It could perhaps try and compel them via court order or ask quietly for them to do things. But it can’t just make them to do things directly.</p>
<p>Let’s take those in turn. What if DOJ asks nicely? In this case, NCMEC has every incentive to say “no”. CSAM scanning by tech companies in the US happens voluntarily. There’s a legal obligation to report CSAM, but no legal obligation to <em>look</em> for it.</p>
<p>Let’s suppose DOJ asks NCMEC to add a hash for, idk, let’s say a photo of a classified document, and hypothetically NCMEC says “yes” and Apple adopts it into its clever CSAM-scanning algorithm. Let’s see what happens.</p>
<p>In this scenario, perhaps someone has this photo on their phone and uploaded it to iCloud so it got scanned, and triggered a hit. First, in iS Apple’s protocol, that single hit is not enough to identify that the person has the document, until the preconfigured threshold is reached.</p>
<p>But suppose the request was a bunch of photos, or the person with the photo also has CSAM or w/e and the threshold is reached. What then?</p>
<p>Well, in this case, Apple gets alerted, and Apple reviews the images in question. But wait! The images aren’t CSAM. That means two things. First: Apple is not obliged to report it to NCMEC. And second, Apple now knows that NCMEC is not operating honestly.</p>
<p>As soon as Apple knows NCMEC is not operating honestly, they will drop the NCMEC database. Remember: they’re legally obliged to <em>report</em> CSAM, but not legally obliged to <em>look for</em> it.</p>
<p>So thanks to DOJ asking and NCMEC saying “yes”, Apple has dropped CSAM scanning entirely, and neither NCMEC nor DOJ actually got a hit. Moreover, NCMEC is now ruined: nobody in tech will use their database. So the long story short is DOJ can’t ask NCMEC politely and get to a yes</p>
</blockquote>
<p>But, he says, let’s look at what happens if the government <em>compels</em> the NCMEC to add the fingerprint to the database. That, he says, would prevent a prosecution because it would conflict with the Fourth Amendment, which protects against illegal search and seizure.</p>
<blockquote class="wp-block-quote">
<p>When NCMEC gets a CSAM hit –what they call a “cyber tip” –they report it to relevant law-enforcement. Law-enforcement then typically gets a subpoena for records, and then work their way up to a full search warrant for evidence against the individual trading in CSAM.</p>
<p>To put that person in prison, they’ll need to eventually bring evidence, and that means they need the entire chain of evidence to be 4A-compliant. The ultimately evidence is derived from the warrant, its probable cause from the subpoena, and SO on, all the way back to the start.</p>
<p>But was the <em>original search</em> 4A-compliant? If no, the whole chain falls apart. This is a is a complicated area, and courts have wrestled with it for a long time. But broadly the consensus view is yes, it is 4A-compliant, because the original CSAM search was voluntary by the tech co.</p>
<p>But if NCMEC or Apple were * compelled* to do the search, then this search was not voluntary by the tech company, but a “deputized search”. And because it’s a deputized search, it is a 4A search and requires a particularized warrant (and particularization is not possible here).</p>
</blockquote>
<p>So although the US government could get evidence this way, it couldn’t use it to prosecute anyone.</p>
<p>Of course, that doesn’t mean the government couldn’t use the information in other ways, but then you’re into a whole other legal rabbit hole.</p>
<p>Stanford’s Alex Stamos has <a href="https://9to5mac.com/2021/08/10/apple-child-protection-controversy-alex-stamos/" target="_blank" rel="noreferrer noopener">called for more nuanced discussion</a> on the risks of misusing CSAM scanning, and this thread certainly qualifies.</p>
<div class="ad-disclaimer-container"><p class="disclaimer-affiliate"><em>FTC: We use income earning auto affiliate links.</em> <a href="https://9to5mac.com/about/#affiliate">More.</a></p><figure class="wp-block-image size-full is-resized"><a href="https://bit.ly/2VOl9DV"><img src="https://9to5mac.com/wp-content/uploads/sites/6/2021/08/9to5mac_promo_rev2-01-1.png" alt class="wp-image-744631" width="750" height="150" referrerpolicy="no-referrer"></a></figure></div><div id="after_disclaimer_placement"></div>
<!-- youtube embed -->
  
</div>
            