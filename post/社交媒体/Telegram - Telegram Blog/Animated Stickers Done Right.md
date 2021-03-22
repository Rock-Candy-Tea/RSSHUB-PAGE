
---
title: Animated Stickers Done Right
categories: 
    - 社交媒体
    - Telegram - Telegram Blog
author: Telegram - Telegram Blog
comments: false
date: Sat, 06 Jul 2019 16:20:32 GMT
thumbnail: 'https://telegram.org/file/464001521/1/6li3qwayWto.24904/1d3d0efd640a61e4fe'
---

<div>   
<div class="dev_page_bread_crumbs"></div>
  <h1 id="dev_page_title" dir="auto">Animated Stickers Done Right</h1>
  
  <div id="dev_page_content" dir="auto"><div class="blog_side_image_wrap">
    <img src="https://telegram.org/file/464001521/1/6li3qwayWto.24904/1d3d0efd640a61e4fe" class="blog_side_image" referrerpolicy="no-referrer">
</div>

<div class="blog_wide_image">
    <a href="https://telegram.org/file/464001776/1/OT3p5F-BpWc.201999/cf29b6606b9abd380a" target="_blank"><img src="https://telegram.org/file/464001154/1/7GPPe2Yjums.71766/5a39af4670f27356ad" srcset="/file/464001776/1/OT3p5F-BpWc.201999/cf29b6606b9abd380a, 1200w" title="Archaeologists say that Telegram has supported stickers since the dawn of time but for the first time in history, you can watch them move. BTW, the gizmo in this picture is called a 'Praxinoscope'." alt="Cover Image" referrerpolicy="no-referrer"></a>
</div>

<p>We launched <a href="https://telegram.org/blog/stickers">stickers</a> back in January <strong>2015</strong>. Since then, the Telegram sticker format has been adopted by other apps to reach a total of <strong>2 billion</strong> people. Today we're introducing a <strong>new format</strong> for <strong>animated stickers</strong>.</p>
<p>We asked ourselves: Can animated stickers have <strong>higher quality</strong> than static ones while taking <strong>less</strong> bandwidth? The answer turned out to be <em>YES</em> (but only after we told developers they'd get moving cat pictures).</p>
<div class="blog_video_player_wrap" style="max-width: 400px; margin: 20px auto 20px;">
 <video class="blog_video_player tl_blog_vid_autoplay" onclick="videoTogglePlay(this)" autoplay loop controls muted poster="/file/464001273/1/AQspRFqKbUw.37605/a10ec56c664f124170" style="max-width: 400px;" title="Each animated sticker takes ~20-30 Kilobytes. If you find a floppy disk in the attic, you might fit up to twelve dozen animated stickers on it (and since you're retro enough to own a floppy disk, you might as well call twelve dozens a 'gross')." alt="Animated Telegram stickers in a chat and in the sticker panel">
  <source src="/file/464001660/1/9pDnhhfdD4k.6301287.mp4/d533e8529b7fdccaa1" type="video/mp4">
 </video>
</div>

<!--<div class="blog_video_player_wrap" style="max-width: 400px; margin: 20px auto 20px;">
 <video class="blog_video_player tl_blog_vid_autoplay" onclick="videoTogglePlay(this)" autoplay loop controls muted poster="/file/464001444/1/jbKsH5zv9jY.37315/5b9bf1ccd45efe548b" style="max-width: 400px;" title="Each animated sticker takes ~20-30 Kilobytes. If you find a floppy disk in the attic, you might fit up to twelve dozen animated stickers on it (and since you're retro enough to own a floppy disk, you might as well call twelve dozens a 'gross')." alt="TITLE">
  <source src="/file/464001733/1/GKYJRff_YZ4.5384562.mp4/fef6ee3f08f9b6a1b5" type="video/mp4">
 </video>
</div>-->

<h4><a class="anchor" name="smooth-animations-tiny-size" href="https://telegram.org/blog/animated-stickers#smooth-animations-tiny-size"><i class="anchor-icon"></i></a>Smooth Animations, Tiny Size</h4>
<p>Telegram engineers experimented with vector graphics, packaging methods and forbidden magic to create the Lottie-based <strong>.TGS</strong> format, in which each sticker takes up about <strong>20-30 Kilobytes</strong> – <strong>six times</strong> smaller than the average photo.</p>
<p>Thanks to various optimizations, animated stickers consume <strong>less battery</strong> than GIFs and run at a smooth <strong>60 frames per second</strong>. If a picture is worth a thousand words, that's <strong>180,000</strong> words per sticker.</p>
<div class="blog_video_player_wrap" style="max-width: 400px; margin: 20px auto 20px;">
 <video class="blog_video_player tl_blog_vid_autoplay" onclick="videoTogglePlay(this)" autoplay loop controls muted poster="/file/464001390/1/Nu0FRcUOOuc.32923/91c686c4b5ecb1f302" style="max-width: 400px;" title="Due to their small size, animated stickers will load instantly on any connection, so you can watch this cat in a tie while you await your rescue from a desert island." alt="Cat showing off muscles">
  <source src="/file/464001497/1/2QKiFWOvlpQ.1246528.mp4/f2fac7a125f20dd801" type="video/mp4">
 </video>
</div>

<!--<div class="blog_video_player_wrap" style="max-width: 400px; margin: 20px auto 20px;">
 <video class="blog_video_player tl_blog_vid_autoplay" onclick="videoTogglePlay(this)" autoplay loop controls muted poster="/file/464001663/1/VAdeeeaGydw.25311/07c380850bbae4309e" style="max-width: 400px;" title="Due to their small size, animated stickers will load instantly on any connection, so you can watch this cuddly cavy while you await your rescue from a desert island." alt="Applauding guinnea pig">
  <source src="/file/464001666/1/h0xohkjiaJw.469399.mp4/4ff6651bd25543ec16" type="video/mp4">
 </video>
</div>-->

<h4><a class="anchor" name="open-platform" href="https://telegram.org/blog/animated-stickers#open-platform"><i class="anchor-icon"></i></a>Open Platform</h4>
<p>Naturally, animated stickers are a <strong>free platform</strong>. All artists are welcome to <strong>create</strong> new sets and <strong>share</strong> them with Telegram users.</p>
<p>Like its static predecessor, the Telegram animated sticker format is likely to become the new industry standard in messaging. Check out <a href="https://core.telegram.org/animated_stickers">this quick guide</a> to get started.</p>
<div class="blog_video_player_wrap" style="max-width: 400px; margin: 20px auto 20px;">
 <video class="blog_video_player tl_blog_vid_autoplay" onclick="videoTogglePlay(this)" autoplay loop controls muted poster="/file/464001549/1/q2NNoVCmotM.23854/f5ece7783dc87a99fa" style="max-width: 400px;" title="Keep a close eye on all your animated stickers while you're working on a set. Our artists are still hunting one of the cherries that managed to escape." alt="A winking panda">
  <source src="/file/464001595/1/eYxg2Qp-zVw.738457.mp4/c550733c78bf39b1a1" type="video/mp4">
 </video>
</div>

<h4><a class="anchor" name="starter-packs" href="https://telegram.org/blog/animated-stickers#starter-packs"><i class="anchor-icon"></i></a>Starter Packs</h4>
<div>

To get your conversations moving right away, our artists have created a <a href="https://t.me/addstickers/Bunnyta" target="_blank">few</a> <a href="https://t.me/addstickers/OfficeTurkey" target="_blank">sample</a> <a href="https://t.me/addstickers/ResistanceDog" target="_blank">sets</a> ranging from <a href="https://t.me/addstickers/MelieTheCavy" target="_blank">Rambunctious Rodents</a> to <a href="https://t.me/addstickers/TheFoods" target="_blank">Sentient Snacks</a>. You can find more animated sticker sets in the 'Trending' section of your sticker panel. <img class="emoji" src="https://telegram.org/img/emoji/40/F09F94A5.png" width="20" height="20" alt="🔥" referrerpolicy="no-referrer">

<br><br></div>

<p>As always, the fastest way to find a sticker that fits your mood is to type in a <strong>relevant emoji</strong> – Telegram will immediately suggest matching stickers.</p>
<div class="blog_video_player_wrap" style="max-width: 400px; margin: 20px auto 20px;">
 <video class="blog_video_player tl_blog_vid_autoplay" onclick="videoTogglePlay(this)" autoplay loop controls muted poster="/file/464001623/1/L4rZ1qTMJlU.29105/914f53e58c12155ea1" style="max-width: 400px;" title="We ran out of ideas for clandestine desktop-only jokes. Let's just hope you never find this alt-text." alt="Sticker selected and sent from emoji suggestions">
  <source src="/file/464001338/1/lqWbVCVvaQc.3938267.mp4/1970a4c6dfc896b462" type="video/mp4">
 </video>
</div>

<p>Keep an eye out for new animated stickers – and our next update.</p>
<div><br></div>

<p><em>July 6, 2019<br>The Telegram Team</em></p>
</div>
  
  
</div>
            