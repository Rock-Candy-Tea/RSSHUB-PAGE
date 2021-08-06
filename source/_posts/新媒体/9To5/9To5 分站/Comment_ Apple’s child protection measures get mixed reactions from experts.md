
---
title: 'Comment_ Apple’s child protection measures get mixed reactions from experts'
categories: 
 - 新媒体
 - 9To5
 - 9To5 分站
headimg: 'https://i1.wp.com/9to5mac.com/wp-content/uploads/sites/6/2021/08/Apples-child-protection-measures-tricky.jpg?resize=1200%2C628&quality=82&strip=all&ssl=1'
author: 9To5
comments: false
date: Fri, 06 Aug 2021 13:12:32 GMT
thumbnail: 'https://i1.wp.com/9to5mac.com/wp-content/uploads/sites/6/2021/08/Apples-child-protection-measures-tricky.jpg?resize=1200%2C628&quality=82&strip=all&ssl=1'
---

<div>   
<img src="https://i1.wp.com/9to5mac.com/wp-content/uploads/sites/6/2021/08/Apples-child-protection-measures-tricky.jpg?resize=1200%2C628&quality=82&strip=all&ssl=1" referrerpolicy="no-referrer">
<p>The announcement yesterday of <a href="https://9to5mac.com/2021/08/05/apple-announces-new-protections-for-child-safety-imessage-safety-icloud-photo-scanning-more/" target="_blank" rel="noreferrer noopener">Apple’s child protection measures</a> confirmed <a href="https://9to5mac.com/2021/08/05/report-apple-photos-casm-content-scanning/" target="_blank" rel="noreferrer noopener">an earlier report</a> that the company would begin scanning for child abuse photos on iPhones. The news has seen mixed reactions from experts in both cybersecurity and child safety.</p>
<p><a href="https://9to5mac.com/2021/08/05/scanning-for-child-abuse-images/" target="_blank" rel="noreferrer noopener">Four concerns had already been raised</a> before the details were known, and Apple’s announcement addressed two of them … </p>
<p><span id="more-742655"></span>
</p>
<h2 id="h-csam-scanning-concerns">CSAM scanning concerns</h2>
<p>The original concerns included the fact that digital signatures for child sexual abuse materials (CSAM) are deliberately fuzzy, to allow for things like crops and other image adjustments. That creates a risk of false positives, either by chance (concern one) or malicious action (concern two).</p>
<p>Apple addressed these by announcing that action would not be triggered by a single matching image. Those who collect such material tend to have multiple images, so Apple said a certain threshold would be required before a report was generated. The company didn’t reveal what the threshold is, but did say that it reduced the chances of a false positive to less than one in a trillion. Personally, that completely satisfies me.</p>
<p>However, two further risks remain.</p>
<p></p>
<blockquote>
<h3 id="h-misuse-by-authoritarian-governments">Misuse by authoritarian governments</h3>
<p></p>
<p>A digital fingerprint can be created for <em>any</em> type of material, not just CSAM. What’s to stop an authoritarian government adding to the database images of political campaign posters or similar?</p>
<p></p>
<p>So a tool that is designed to target serious criminals could be trivially adapted to detect those who oppose a government or one or more of its policies.</p>
<p></p>
<h3 id="h-potential-expansion-into-messaging">Potential expansion into messaging</h3>
<p></p>
<p>If you use an end-to-end encrypted messaging service like iMessage, Apple has no way to see the content of those messages. If a government arrives with a court order, Apple can simply shrug and say it doesn’t know what was said. </p>
<p></p>
<p>But if a government adds fingerprints for types of text – let’s say the date, time, and location of a planned protest – then it could easily create a database of political opponents.</p>
</blockquote>
<p></p>
<p>The Electronic Frontier Foundation (EFF) <a href="https://www.eff.org/deeplinks/2021/08/apples-plan-think-different-about-encryption-opens-backdoor-your-private-life" target="_blank" rel="noreferrer noopener">highlighted the misuse risk</a>, pointing out that there is no way for either Apple or users to audit the digital fingerprints. A government can <em>tell</em> Apple that it only contains CSAM hashes, but there is no way for the company to verify that.</p>
<p>Right now, the process is that Apple will manually review flagged images, and only if the review confirms abusive material will the company pass the details to law enforcement. But again, there is no guarantee that the company will be allowed to continue following this process. </p>
<p>Cryptography academic Matthew Green <a href="https://twitter.com/matthew_d_green/status/1423102556209876994" target="_blank" rel="noreferrer noopener">reiterated this point</a> after his pre-announcement tweets.</p>
<blockquote class="wp-block-quote">
<p>Whoever controls this list can search for whatever content they want on your phone, and you don’t really have any way to know what’s on that list because it’s invisible to you (and just a bunch of opaque numbers, even if you hack into your phone to get the list.)</p>
</blockquote>
<p><a href="https://www.eff.org/deeplinks/2021/08/apples-plan-think-different-about-encryption-opens-backdoor-your-private-life" target="_blank" rel="noreferrer noopener">The EFF says</a> this is more than a theoretical risk:</p>
<blockquote class="wp-block-quote">
<p>We’ve already seen this mission creep in action. One of the technologies originally built to scan and hash child sexual abuse imagery has been repurposed to create a <a href="https://www.eff.org/deeplinks/2020/08/one-database-rule-them-all-invisible-content-cartel-undermines-freedom-1">database of “terrorist” content</a> that companies can contribute to and access for the purpose of banning such content. The database, managed by the <a href="https://gifct.org/">Global Internet Forum to Counter Terrorism</a> (GIFCT), is troublingly without external oversight, despite <a href="https://cdt.org/insights/human-rights-ngos-in-coalition-letter-to-gifct/">calls from civil society</a>. While it’s therefore impossible to know whether the database has overreached, we do know that platforms <a href="https://www.eff.org/wp/caught-net-impact-extremist-speech-regulations-human-rights-content">regularly flag critical content</a> as “terrorism,” including documentation of violence and repression, counterspeech, art, and satire. </p>
</blockquote>
<p>In Hong Kong, for example, <a href="https://www.bbc.co.uk/news/world-asia-china-52765838" target="_blank" rel="noreferrer noopener">criticism of the Chinese government</a> is classified on the same level as terrorism, and is punishable by life imprisonment.</p>
<h2 id="h-imessage-scanning-concerns">iMessage scanning concerns</h2>
<p>Concerns have also been raised about the AI-based scanning iPhones will conduct on photos in iMessage. This scanning doesn’t rely on digital signatures, but instead tries to identify nude photos based on machine-learning.</p>
<p>Again, Apple has protections built in. It’s only for suspected nude photos. It only affects child accounts as part of family groups. The child is warned that an incoming message might be inappropriate, and then chooses whether or not to view it. No external report is generated, only a parent notified if appropriate.</p>
<p>But again, the slippery slope argument is being raised. These are all controls that apply right now, but <a href="https://www.eff.org/deeplinks/2021/08/apples-plan-think-different-about-encryption-opens-backdoor-your-private-life" target="_blank" rel="noreferrer noopener">the EFF asks</a> what if a repressive government forces Apple to change the rules?</p>
<blockquote class="wp-block-quote">
<p>Governments that outlaw homosexuality might require the classifier to be trained to restrict apparent LGBTQ+ content, or an authoritarian regime might demand the classifier be able to spot popular satirical images or protest flyers.</p>
</blockquote>
<p>The organization also argues that false matches are a definite risk here.</p>
<blockquote class="wp-block-quote">
<p>We know from years of documentation and research that machine-learning technologies, used without human oversight, have a habit of wrongfully classifying content, including supposedly “sexually explicit” content. When blogging platform Tumblr instituted a filter for sexual content in 2018, it famously caught all sorts of other imagery in the net, including pictures of Pomeranian puppies, selfies of fully-clothed individuals, and more. Facebook’s attempts to police nudity have resulted in the removal of pictures of famous statues such as Copenhagen’s Little Mermaid.</p>
</blockquote>
<p>Again, that’s not an issue with Apple’s current implementation due to the safeguards included, but creating technology that can scan the contents of private messages has huge potential for future abuse.</p>
<p>The EFF also highlights an issue raised by some child-protection experts: that a parent or legal guardian isn’t always a safe person with whom to share a child’s private messages.</p>
<blockquote class="wp-block-quote">
<p>This system will give parents who do not have the best interests of their children in mind one more way to monitor and control them.</p>
</blockquote>
<p>Some of the discussion highlights that tricky tightrope Apple is trying to walk. For example, one protection is that parents are not automatically alerted: The child is warned first, and then given the choice of whether or not to view or send the image. If they choose not to, no alert is generated. <a href="https://twitter.com/elegant_wallaby/status/1423453567940063236" target="_blank" rel="noreferrer noopener">David Thiel</a> was one of many to point out the obvious flaw there:</p>
<figure class="wp-block-embed aligncenter is-type-rich is-provider-twitter wp-block-embed-twitter">
<div class="wp-block-embed__wrapper">
<blockquote class="twitter-tweet" data-dnt="true">
<p lang="en" dir="ltr">Finally, it seems obvious that when faced with a dialog that says "we're going to tell your parents", conversation will immediately shift to another platform, potentially Facetime where these mechanisms are all useless. 14/</p>
<p>— David Thiel (@elegant_wallaby) <a href="https://twitter.com/elegant_wallaby/status/1423453567940063236?ref_src=twsrc%5Etfw">August 6, 2021</a></p></blockquote>
<p>
</p></div>
</figure>
<h2 id="h-apple-s-child-protection-measures-can-t-please-everyone">Apple’s child protection measures can’t please everyone</h2>
<p>Everyone supports Apple’s intentions here, and personally I’m entirely satisfied by the threshold protection against false positives. Apple’s other safeguards are also thoughtful, and ought to be effective. The company is to be applauded for trying to address a serious issue in a careful manner.</p>
<p>At the same time, the slippery slope risks are very real. It is extremely common for a government – even a relatively benign one – to indulge in mission-creep. It first introduces a law that nobody could reasonably oppose, then later widens its scope, sometimes salami-style, one slice at a time. This is especially dangerous in authoritarian regimes. </p>
<p>Conversely, you could argue that by making this system public, Apple just tipped its hand. Now anyone with CSAM on their iPhone knows they should switch off iCloud, and abusers know if they want to send nudes to children, they shouldn’t use iMessage. So you could argue that Apple shouldn’t be doing this at all, or you could argue that it should have done it without telling anyone.</p>
<p>The reality is that there’s no perfect solution here, and every stance Apple could take has both benefits and risks.</p>
<p>Yesterday, before the full details were known, the vast majority of you <a href="https://9to5mac.com/2021/08/05/scanning-for-child-abuse-images/" target="_blank" rel="noreferrer noopener">opposed the move</a>. Where do you stand now that the details – and the safeguards – are known? Please again take our poll, and share your thoughts in the comments.</p>
<p><a name="pd_a_10894507" href="https://9to5mac.com/2021/08/06/comment-apples-child-protection-measures-get-mixed-reactions-from-experts/undefined"></a>
</p><div class="CSS_Poll PDS_Poll" id="PDI_container10894507" style="display:inline-block;"></div>
<div id="PD_superContainer"></div>

<noscript><a href="https://poll.fm/10894507">Take Our Poll</a></noscript><p></p>
<p><em>Photo: <a href="https://unsplash.com/@david_watkis?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">David Watkis</a>/<a href="https://unsplash.com/s/photos/traffic-lights?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a></em></p>
<div class="ad-disclaimer-container"><p class="disclaimer-affiliate"><em>FTC: We use income earning auto affiliate links.</em> <a href="https://9to5mac.com/about/#affiliate">More.</a></p><figure class="wp-block-image size-full is-resized"><a href="https://bit.ly/3C0YHbr"><img src="https://9to5mac.com/wp-content/uploads/sites/6/2021/08/9to5mac_promo-01.png" alt class="wp-image-742121" width="750" height="150" referrerpolicy="no-referrer"></a></figure></div><div id="after_disclaimer_placement"></div>
<!-- youtube embed -->
  
</div>
            