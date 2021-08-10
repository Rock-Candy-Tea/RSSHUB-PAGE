
---
title: 'Reality Capture 初探'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/33746474569e4dc48c4cb112bd228da8~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 07 Aug 2021 06:12:34 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/33746474569e4dc48c4cb112bd228da8~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p><strong>这是我参与8月更文挑战的第7天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h1 data-id="heading-0">Reality Capture</h1>
<h2 data-id="heading-1">起因</h2>
<p><code>Reality Capture</code>是一款3D模型制作软件，可以帮助用户对3D模型进行制作和编辑，多用于游戏开发以及一些模型设计领域，制作的3D模型非常的精细</p>
<p>至于我是如何了解到这款软件的，是因为当时在在微信的公众号上看到了一篇文章，觉得很有趣，所以自己也去下载安装了一个准备开始进行一下尝试。</p>
<p>踏坑引路文章（<del>万恶起源</del>）：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FNgvjv93S-RF0304WCNmAVg" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s/Ngvjv93S-RF0304WCNmAVg" ref="nofollow noopener noreferrer">心酸！鸿星尔克官网年久失修，给他写了个720°全景看鞋展厅 </a></p>
<p>其实在这篇文章当中，不仅仅有<code>Reality Capture</code>，还有<code>Three，js</code>的应用。</p>
<p>不过我之前已经学过一些<code>Three，js</code>，这个发现还是挺高兴的。</p>
<p>这是我three.js的专栏，有兴趣的朋友可以去了解一下（后续会在掘金把threeJS文章整理一下的）：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fqq_36171287%2Fcategory_10641247.html" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/qq_36171287/category_10641247.html" ref="nofollow noopener noreferrer">《threeJS专栏》 </a></p>
<br>
<hr>
<br>
<h2 data-id="heading-2">软件安装</h2>
<p>说到一款软件，那肯定避免不了软件的安装和下载了。</p>
<p>可以从<code>Reality Capture</code>的官网上直接进行下载，不过该软件是收费的，并且价格并不便宜（对于个人来说）</p>
<p><code>Reality Capture</code>的官网 ：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.capturingreality.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.capturingreality.com/" ref="nofollow noopener noreferrer">www.capturingreality.com/</a></p>
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/33746474569e4dc48c4cb112bd228da8~tplv-k3u1fbpfcp-watermark.image" width="600" loading="lazy" referrerpolicy="no-referrer">
<p>在进入官网后，可以在price中查看软件的收费标准</p>
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fab7c67046af48cb948f9da454c92457~tplv-k3u1fbpfcp-watermark.image" width="600" loading="lazy" referrerpolicy="no-referrer">
<p>不过大家当然是老司机了，懂的都懂，八仙过海各显奇招，在网上也有着各种过时的<strong>免费</strong>版本，虽然不是最新的，但是对于个人来说，也已经足够入门使用了。</p>
<h2 data-id="heading-3">软件安装</h2>
<p>在获得软件的下载文件后，就可以点击进行安装了</p>
<ol>
<li>进入安装界面，点击next到下一步</li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/71bdb435b3a344a985254b89d7d215ef~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>勾选接受协议，然后next下一步</li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/81331eb465724858879633d304647073~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="3">
<li>可以修改文件安装位置，然后下一步</li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/054d53f348414c80ae0f3de23a933c2b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="4">
<li>点击install进行安装</li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd2ebfb997b04cd3a29f98050d5538e3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="5">
<li>安装结束之后，现在桌面上已经有Reality Capture的图标了</li>
</ol>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9db62c6935294f3a8a237da2578a553f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="6">
<li>点击图标打开后的界面</li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae542b1d44534a8fbbbe0e4f2992155e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="7">
<li>在最顶部是工作布局栏，可以调控不同的工作布局</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3400cb9bba2459782dbaa37697a692d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>应用程序布局：了解应用程序布局</strong></p>
<p>Reality Capture提供几种布局是优化执行不同任务。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/474236f892ca488eb5411071a72f6d15~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>改变布局</strong></p>
<p>改变布局，在应用中选择带工作流程选项卡，选择所需的布局选项面板下的应用布局中的子菜单。你也可以通过单击应用程序窗口的快捷栏一个相应的布局图标改变布局。</p>
<p><strong>调整大小</strong></p>
<p>要调整布局的单元格大小，只需在两个单元格之间拖动一个边并移动它即可。拖动并移动连接点以改变所有相邻单元格的大小。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ca758d3ff7c4856af5d992196b05ed3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>保存并重置布局</strong></p>
<p>应用程序退出时自动保存应用程序布局。若要将布局重置为默认大小，请选择“工作流程”选项卡，单击“应用程序面板”下的“设置”按钮，打开应用程序设置。然后单击“重置布局”按钮。</p>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8cf6dc77233d41eb9603feb49e2563f7~tplv-k3u1fbpfcp-watermark.image" height="400" loading="lazy" referrerpolicy="no-referrer">
<h2 data-id="heading-4">告辞</h2>
<p>我对<code>Reality Capture</code>这款软件的初探就这样结束了，接下来需要我尝试功能的使用了</p>
<p>希望一路顺利，不要处处踩坑！</p>
<br>
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/264c6c01df074c97bbd003d29d0b9106~tplv-k3u1fbpfcp-watermark.image" height="400" loading="lazy" referrerpolicy="no-referrer"></div>  
</div>
            