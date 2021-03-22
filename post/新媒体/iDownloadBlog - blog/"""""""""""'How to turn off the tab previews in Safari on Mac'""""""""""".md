
---
title: """""""""""'How to turn off the tab previews in Safari on Mac'"""""""""""
categories: 
    - 新媒体
    - iDownloadBlog - blog
author: iDownloadBlog - blog
comments: false
date: Fri, 19 Mar 2021 17:51:46 GMT
thumbnail: 'https://cdn-0.idownloadblog.com/wp-content/uploads/2021/03/Safari-with-Tab-Previews-Mac.jpg'
---

<div>   
<p>With Safari 14 on Mac came a cool feature for tab previews. This allows you to see a tiny snapshot of a webpage you have open in another tab when hovering your mouse over this tab. The thing with this feature is, it’s simply not for everyone. Some find it distracting. If you fall into this group, we’re here to help. Here’s how to disable the <a href="https://www.idownloadblog.com/tag/safari/">Safari</a> tab previews on your Mac.<span id="more-858127"></span></p>
<p style="text-align: center;"><img loading="lazy" class="alignnone size-full wp-image-858188" src="https://cdn-0.idownloadblog.com/wp-content/uploads/2021/03/Safari-with-Tab-Previews-Mac.jpg" alt="Safari with Tab Previews on Mac" width="2344" height="1324" srcset="https://cdn-0.idownloadblog.com/wp-content/uploads/2021/03/Safari-with-Tab-Previews-Mac.jpg 2344w, https://cdn-0.idownloadblog.com/wp-content/uploads/2021/03/Safari-with-Tab-Previews-Mac-255x144.jpg 255w, https://cdn-0.idownloadblog.com/wp-content/uploads/2021/03/Safari-with-Tab-Previews-Mac-768x434.jpg 768w, https://cdn-0.idownloadblog.com/wp-content/uploads/2021/03/Safari-with-Tab-Previews-Mac-1536x868.jpg 1536w, https://cdn-0.idownloadblog.com/wp-content/uploads/2021/03/Safari-with-Tab-Previews-Mac-2048x1157.jpg 2048w, https://cdn-0.idownloadblog.com/wp-content/uploads/2021/03/Safari-with-Tab-Previews-Mac-745x421.jpg 745w" sizes="(max-width: 2344px) 100vw, 2344px" referrerpolicy="no-referrer"></p>
<h2>Allow full access to Terminal</h2>
<p>Currently, macOS doesn’t offer a simple switch to turn off Safari’s previews. But, you can use a Terminal command to make it happen.</p>
<p>Before you open Terminal and use the command we’ll provide, you’ll need to allow full disk access to Terminal. If you know you have already done this, then you’re set and can move onto the steps for the tab previews. If you have not, do the following.</p>

<p><strong>1)</strong> Open <strong>System Preferences</strong> and select <strong>Security & Privacy</strong>.</p>
<p><strong>2)</strong> Click the <strong>padlock</strong> on the bottom left and enter your password to unlock these settings and make the change.</p>
<p><strong>3)</strong> On the left, select <strong>Full Disk Access</strong>.</p>
<p><strong>4)</strong> On the right, check the box next to <strong>Terminal</strong>.</p>

<p><img loading="lazy" class="aligncenter wp-image-858189" src="https://cdn-0.idownloadblog.com/wp-content/uploads/2021/03/Allow-Full-Disk-Access-for-Terminal-Mac.jpg" alt="Allow Full Disk Access for Terminal Mac" width="650" height="571" srcset="https://cdn-0.idownloadblog.com/wp-content/uploads/2021/03/Allow-Full-Disk-Access-for-Terminal-Mac.jpg 1300w, https://cdn-0.idownloadblog.com/wp-content/uploads/2021/03/Allow-Full-Disk-Access-for-Terminal-Mac-245x215.jpg 245w, https://cdn-0.idownloadblog.com/wp-content/uploads/2021/03/Allow-Full-Disk-Access-for-Terminal-Mac-768x675.jpg 768w, https://cdn-0.idownloadblog.com/wp-content/uploads/2021/03/Allow-Full-Disk-Access-for-Terminal-Mac-569x500.jpg 569w" sizes="(max-width: 650px) 100vw, 650px" referrerpolicy="no-referrer"></p>
<p>You can then relock and close the preferences. And, you can remove Full Disk Access from Terminal after you take care of those Safari previews if you like. Just use the same steps above and uncheck Terminal.</p>
<h2>Disable tab previews in Safari</h2>
<p>If you’re ready to eliminate those tab previews in Safari on Mac, follow these steps.</p>
<p><strong>1)</strong> <strong>Quit Safari</strong>. You can use <strong>Safari</strong> > <strong>Quit Safari</strong> from the menu bar or right-click Safari’s Dock icon and choose <strong>Quit</strong>.</p>

<p><strong>2)</strong> Launch <strong>Terminal</strong> from the Utilities folder (or by using one of these other methods to open Terminal). Type in the following command and hit <strong>Return</strong>.</p>
<pre>defaults write com.apple.Safari DebugDisableTabHoverPreview 1</pre>
<p><strong>3)</strong> Reopen Safari and check it out. You should no longer see those tab previews you didn’t like.</p>
<p><img loading="lazy" class="aligncenter wp-image-858190" src="https://cdn-0.idownloadblog.com/wp-content/uploads/2021/03/Terminal-Command-to-Remove-Safari-Tab-Previews-Mac.jpg" alt="Terminal Command to Remove Safari Tab Previews on Mac" width="750" height="105" srcset="https://cdn-0.idownloadblog.com/wp-content/uploads/2021/03/Terminal-Command-to-Remove-Safari-Tab-Previews-Mac.jpg 1500w, https://cdn-0.idownloadblog.com/wp-content/uploads/2021/03/Terminal-Command-to-Remove-Safari-Tab-Previews-Mac-255x36.jpg 255w, https://cdn-0.idownloadblog.com/wp-content/uploads/2021/03/Terminal-Command-to-Remove-Safari-Tab-Previews-Mac-768x107.jpg 768w, https://cdn-0.idownloadblog.com/wp-content/uploads/2021/03/Terminal-Command-to-Remove-Safari-Tab-Previews-Mac-745x104.jpg 745w" sizes="(max-width: 750px) 100vw, 750px" referrerpolicy="no-referrer"></p>
<h2>Reenable tab previews in Safari</h2>
<p>Should you decide down the road that you want to give the tab previews in Safari another try, it’s just as easy to reenable them.</p>
<p>Open <strong>Terminal</strong>, enter the below command and hit <strong>Return</strong>.</p>
<pre>defaults write com.apple.Safari DebugDisableTabHoverPreview 0</pre>
<p>You’ll notice the only difference between this command and the first is you include a zero (0) at the end instead of a one (1).</p>

<h2>Wrapping it up</h2>
<p>It’s nice to know that even though Apple doesn’t give us a way to toggle off Safari tab previews, a simple Terminal command can take care of it. And we’d like to thank <a href="https://www.macrumors.com/how-to/disable-tab-previews-safari-mac/" target="_blank" rel="noopener noreferrer">MacRumors</a> for posting this tip!</p>
<p>Over to you! Are you going to get rid of the tab previews in Safari on your Mac or do you find them helpful? Let us know!</p>

<!-- AI CONTENT END 1 -->

  
</div>
            