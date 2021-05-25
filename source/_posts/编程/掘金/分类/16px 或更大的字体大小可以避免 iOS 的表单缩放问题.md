
---
title: '16px 或更大的字体大小可以避免 iOS 的表单缩放问题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/02c0571c07b549299ee4446bdecbfc35~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 24 May 2021 03:21:56 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/02c0571c07b549299ee4446bdecbfc35~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<ul>
<li>原文地址：<a href="https://css-tricks.com/16px-or-larger-text-prevents-ios-form-zoom/" target="_blank" rel="nofollow noopener noreferrer">16px or Larger Text Prevents iOS Form Zoom</a></li>
<li>原文作者：<a href="https://css-tricks.com/author/chriscoyier/" target="_blank" rel="nofollow noopener noreferrer">Chris Coyier </a></li>
<li>译文出自：<a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a></li>
<li>本文永久链接：<a href="https://github.com/xitu/gold-miner/blob/master/article/2021/.md" target="_blank" rel="nofollow noopener noreferrer">github.com/xitu/gold-m…</a></li>
<li>译者：<a href="https://github.com/PassionPenguin" target="_blank" rel="nofollow noopener noreferrer">霜羽 Hoarfroster</a></li>
<li>校对者：<a href="https://github.com/KimYangOfCat" target="_blank" rel="nofollow noopener noreferrer">Kim Yang</a>、<a href="https://github.com/Chorer" target="_blank" rel="nofollow noopener noreferrer">Chorer</a></li>
</ul>
</blockquote>
<p><a href="https://twitter.com/joshwcomeau/status/1379782931116351490?s=12" target="_blank" rel="nofollow noopener noreferrer">“今天我已经学到的” —— 我从乔什·科莫（Josh W. Comeau）的推特中学习到</a> 的东西真的是太棒了！！！如果 <code><input></code> 的 <code>font-size</code> 被设定为 <code>16px</code> 或更大，那么 iOS 上的 Safari 将正常聚焦到输入表单中。但是，一旦 <code>font-size</code> 等于或小于 <code>15px</code>，视图窗口就会放大并聚焦到该 <code><input></code>（或许是因为苹果认为字体太小，因此它会放大以帮助你更清楚地看到自己在做什么）。这个设计是用来增强可访问性的，如果你不想要，请确保 <code><input></code> 的字体足够大。</p>
<p>如果你想自己试试，请打开<a href="https://codepen.io/joshwcomeau/pen/VwPMPZo" target="_blank" rel="nofollow noopener noreferrer">乔什的 <code>codepen</code></a>。</p>
<p>总的来说，我还挺喜欢这个功能。它可以帮助人们了解自己在做什么，并且也表了态 —— 苹果不建议开发者在 UI 中使用过小的字体。让人略感遗憾的是（我在这里并没责怪任何人），在不同字体大小的可读性上，并非所有字体都是一样的。比如说，下图是字体大小为 16px 的 <em>San Francisco</em> 与 <em>Caveat</em> 的对比：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/02c0571c07b549299ee4446bdecbfc35~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><small>左边是 <em>San Francisco</em>，右边是 <em>Caveat</em>。即使 <code>font-size</code> 相同，<em>Caveat</em> 在外观上看起来也要小得多。</small></p>
<p>你可以在 Safari 浏览器中打开<a href="https://cdpn.io/chriscoyier/debug/MWJxXWz" target="_blank" rel="nofollow noopener noreferrer">调试模式</a> ，查看<a href="https://codepen.io/chriscoyier/pen/MWJxXWz" target="_blank" rel="nofollow noopener noreferrer">该示例</a>，并更改字体大小以查看会自动放大聚焦与不会放大聚焦的具体表现。</p>
<hr>
<blockquote>
<p>🔥 将表单输入设置为 1rem（16px）或更大的字体，以防止在点击时 iOS Safari 浏览器自动放大并聚焦到 <code>input</code> 元素上。</p>
<p>从用户体验的角度来看有很大的不同！</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5a1dfcac00a4c43bf3e14254be9d889~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>—— Josh W. Comeau @JoshWComeau 9:07, Apr 7, 2021</p>
<hr>
<p>当 Safari 放大时，它似乎希望让该 input 控件的实际字体大小为 16px。在下面两张图中，用户在输入文本时看到的字体大小其实都是 16px。因此更改后，输入文本的阅读体验实际上并没有变得更差！！</p>
<p>另外，人们始终可以根据需要手动放大。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd1d2868bce542f49521114613285a1f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d8fb3fc45a044a6da0e357dab1446ad5~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>—— Josh W. Comeau @JoshWComeau 9:07, Apr 7, 2021</p>
</blockquote>
<blockquote>
<p>如果发现译文存在错误或其他需要改进的地方，欢迎到 <a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a> 对译文进行修改并 PR，也可获得相应奖励积分。文章开头的 <strong>本文永久链接</strong> 即为本文在 GitHub 上的 MarkDown 链接。</p>
</blockquote>
<hr>
<blockquote>
<p><a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a> 是一个翻译优质互联网技术文章的社区，文章来源为 <a href="https://juejin.im/" target="_blank" rel="nofollow noopener noreferrer">掘金</a> 上的英文分享文章。内容覆盖 <a href="https://github.com/xitu/gold-miner#android" target="_blank" rel="nofollow noopener noreferrer">Android</a>、<a href="https://github.com/xitu/gold-miner#ios" target="_blank" rel="nofollow noopener noreferrer">iOS</a>、<a href="https://github.com/xitu/gold-miner#%E5%89%8D%E7%AB%AF" target="_blank" rel="nofollow noopener noreferrer">前端</a>、<a href="https://github.com/xitu/gold-miner#%E5%90%8E%E7%AB%AF" target="_blank" rel="nofollow noopener noreferrer">后端</a>、<a href="https://github.com/xitu/gold-miner#%E5%8C%BA%E5%9D%97%E9%93%BE" target="_blank" rel="nofollow noopener noreferrer">区块链</a>、<a href="https://github.com/xitu/gold-miner#%E4%BA%A7%E5%93%81" target="_blank" rel="nofollow noopener noreferrer">产品</a>、<a href="https://github.com/xitu/gold-miner#%E8%AE%BE%E8%AE%A1" target="_blank" rel="nofollow noopener noreferrer">设计</a>、<a href="https://github.com/xitu/gold-miner#%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD" target="_blank" rel="nofollow noopener noreferrer">人工智能</a>等领域，想要查看更多优质译文请持续关注 <a href="https://github.com/xitu/gold-miner" target="_blank" rel="nofollow noopener noreferrer">掘金翻译计划</a>、<a href="http://weibo.com/juejinfanyi" target="_blank" rel="nofollow noopener noreferrer">官方微博</a>、<a href="https://zhuanlan.zhihu.com/juejinfanyi" target="_blank" rel="nofollow noopener noreferrer">知乎专栏</a>。</p>
</blockquote></div>  
</div>
            