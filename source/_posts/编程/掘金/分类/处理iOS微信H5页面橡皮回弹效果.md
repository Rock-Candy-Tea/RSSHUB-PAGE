
---
title: '处理iOS微信H5页面橡皮回弹效果'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8113'
author: 掘金
comments: false
date: Tue, 13 Jul 2021 19:16:11 GMT
thumbnail: 'https://picsum.photos/400/300?random=8113'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><h3 data-id="heading-0">🐱业务需求</h3>
<p>近期开发的项目有一部分是与微信公众号相关的H5页面，在Android端微信上页面效果展示无异常，但是在 <strong>iOS端</strong> 微信多多少少会出现一些意想不到的bug。此次主要针对移动端H5页面在iOS端产生的 <strong>橡皮回弹</strong>（<strong>橡皮筋效果</strong>）问题做一下相关记录，希望对遇到类似问题的同学有所帮助。</p>
<h3 data-id="heading-1">🐕方案一：使用 inobounce.js</h3>
<ul>
<li><strong>inobounce.js</strong>  <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Flazd%2FiNoBounce" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/lazd/iNoBounce" ref="nofollow noopener noreferrer">github地址</a></li>
</ul>
<p>在 <strong>html主页面 <strong>的 <strong>header</strong> 标签中引入</strong> inbounce.js</strong>，即 <strong></strong> 。当引入此文件之后，iOS端整个页面都无法滑动或滚动，若想滚动的元素能够实现滚动效果，则需要对滚动区域设置固定的高度，即 <strong>height</strong>、<strong>max-height</strong>，同时也要设置 <strong>overflow: auto</strong>，实现页面滑动。为防止iOS端页面滚动发生卡顿现象，需要对滚动区域设置 <strong>-webkit-overflow-scrolling: touch</strong> 属性。   </p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span> /></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span> /></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>inobounce<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"inobounce.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
<span class="hljs-selector-tag">ul</span> &#123;
<span class="hljs-attribute">height</span>: <span class="hljs-number">115px</span>;
<span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid gray;
<span class="hljs-attribute">overflow</span>: auto;
-webkit-<span class="hljs-attribute">overflow</span>-scrolling: touch;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
<span class="hljs-tag"><<span class="hljs-name">li</span>></span>List Item 1<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"><<span class="hljs-name">li</span>></span>List Item 2<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"><<span class="hljs-name">li</span>></span>List Item 3<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"><<span class="hljs-name">li</span>></span>List Item 4<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"><<span class="hljs-name">li</span>></span>List Item 5<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"><<span class="hljs-name">li</span>></span>List Item 6<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"><<span class="hljs-name">li</span>></span>List Item 7<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"><<span class="hljs-name">li</span>></span>List Item 8<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"><<span class="hljs-name">li</span>></span>List Item 9<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"><<span class="hljs-name">li</span>></span>List Item 10<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">🐒 方案二：CSS样式处理（推荐）</h3>
<p>偶然间在iOS端打开一些公众号的H5活动页，没有产生所谓的橡皮回弹效果，于是就想着是否可以采用此效果来解决iOS端网页产生的橡皮回弹效果。最终尝试此方法可以实现iOS端页面固定，不产生橡皮回弹效果。在系统版本iOS13+上的设备上已解决橡皮筋效果，系统版本iOS12+的设备上没有尝试，后续准备找iOS12+的苹果手机进行进一步的测试，其次再将测试结果进行补充。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span> /></span>
<span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span> /></span>
<span class="hljs-tag"><<span class="hljs-name">title</span>></span>iOS橡皮回弹<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
<span class="hljs-comment"><!-- 内容区 --></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>主要CSS代码：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-comment">/* 初始化 */</span>
* &#123;
<span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
<span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span>;
&#125;
<span class="hljs-comment">/* 基本样式 */</span>
<span class="hljs-selector-tag">html</span>,
<span class="hljs-selector-tag">body</span> &#123;
<span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
<span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
<span class="hljs-attribute">overflow</span>: hidden;
&#125;
<span class="hljs-selector-tag">body</span> &#123;
<span class="hljs-attribute">box-sizing</span>: border-box;
<span class="hljs-attribute">position</span>: relative;
&#125;
<span class="hljs-comment">/* 超出滚动 */</span>
<span class="hljs-selector-id">#app</span> &#123;
<span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
<span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
<span class="hljs-attribute">overflow-y</span>: auto;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">🐬<strong>总结：</strong></h3>
<p>总的来说，两种方案我在实际开发中都进行了尝试。方案一在微信中浏览H5网页时可以完美解决橡皮回弹效果；当H5页面在iOS端微信授权跳转时，底部会有一个导航条，此时导航条也有可能被遮盖，点击导航条两端的按钮没有反应。在Safari浏览器打开H5页面时，网页的顶端地址栏和底部菜单栏会有一定的遮挡，体验效果不是很理想，最终此方案被pass掉了。方案二是我实际工作中使用的，回弹效果得到了一定的改善。体验效果较方案一有了很大的提升。
如果页面有微信授权，以及页面路径的跳转，此时iOS端微信打开的网页底部会多出一个导航条，同样Android端微信不会出现类似导航条。若没有微信授权以及页面跳转，则两方案均可选；若有微信授权，推荐使用方案二。</p></div>  
</div>
            