
---
title: '浏览器渲染过程和CRP优化二：CRP优化'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bca298b4048547388e861bd4ecd82154~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 18 Jun 2021 03:30:53 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bca298b4048547388e861bd4ecd82154~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>上一篇文章解释了浏览器的渲染过程，简单说了一下什么是<a href="https://juejin.cn/post/6975028927223824391#heading-7" target="_blank">CRP</a>，这篇文章来记录一下如何进行CRP优化</p>
<p>浏览器渲染（解析）页面的过程如下：</p>
<ol>
<li><strong>导航</strong>：输入URL、DNS解析、建立连接</li>
<li><strong>响应</strong>：发送请求、接收第一次响应的HTML文本</li>
<li><strong>解析</strong>：构建DOM、构建CSSOM、编译javascript</li>
<li><strong>渲染</strong>：样式（Style，构建Render树）、布局计算（Layout，回流/重排）、绘制（Paint，重绘）。</li>
</ol>
<p>其中解析和渲染步骤比较重要</p>
<p>我们将解析和渲染的步骤中关键的五步提取出来，作为浏览器的<strong>关键渲染路径</strong>，优化关键渲染路径可<strong>提高渲染性能</strong></p>
<p>这五步分别是</p>
<ol>
<li>第一步是处理HTML标记，构建DOM树</li>
<li>第二步是处理CSS，构建CSSOM树。</li>
<li>第三步是将DOM和CSSOM组合成一个Render树。</li>
<li>第四步是在依据渲染树计算每个节点的大小和位置。</li>
<li>最后一步是根据渲染树和回流得到的几何信息，得到节点的绝对像素，将各个节点绘制到屏幕上。</li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bca298b4048547388e861bd4ecd82154~tplv-k3u1fbpfcp-watermark.image" alt="image。png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>即：构建DOM->构建CSSOM->构建Render树->回流->重绘。</p>
<p>详细参考上一篇文章 <a href="https://juejin.cn/post/6975028927223824391" target="_blank">浏览器渲染过程</a></p>
<h2 data-id="heading-0">CRP优化之-解析阶段优化</h2>
<h3 data-id="heading-1">构建DOM树时遇到样式</h3>
<p>构建DOM树时遇到样式，有以下几种情况
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aac2b3f521994720a19fdd484ad1cf3f~tplv-k3u1fbpfcp-watermark.image" alt="image。png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>
<p>遇到style内嵌样式，GUI直接渲染</p>
<ul>
<li>所以项目中如果CSS代码量比较少，直接内嵌即可，拉去HTML的时候，同时CSS也回来了，渲染的时候直接就渲染了</li>
<li>但是如果CSS代码比较多，如果还用内嵌，一方面会影响HTML的拉取速度，也不利于代码的维护，此时还是用外链的方式比较好</li>
</ul>
</li>
<li>
<p>遇到link标签（异步），浏览器开辟一个HTTP线程去请求资源文件信息，同时GUI继续向下渲染</p>
<p>tips：浏览器同时能够发送的HTTP请求是有数量限制的（谷歌：5~7个），超过最大并发限制的HTTP请求需要排队等待，所以HTTP请求一定是越少越好。</p>
</li>
<li>
<p>遇到@import（同步），浏览器也是开辟HTTP线程去请求资源，但是此时GUI也暂定了（导入式样式会阻碍GUI的渲染），当资源请求回来之后，GUI才能继续渲染</p>
<p>所以真实项目中应该避免使用@import</p>
</li>
</ol>
<h3 data-id="heading-2">构建DOM树时遇到js</h3>
<p>遇到 <code> <script src='xxx/xxx.js'></code> ，有三种解析的方式，分别是 默认，async，defer，默认情况下会阻碍GUI的渲染</p>
<p>如图所示三种方式的渲染规则：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/533b8033f8d742319ad77fc437900511~tplv-k3u1fbpfcp-watermark.image" alt="image。png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>（图片中， <code>'net'</code>  表示请求js文件 ， <code>'execution'</code>  表示执行（解析或者叫渲染）js）</p>
<p>如果不想阻碍GUI渲染，该怎么办？在标签里加属性 <code>async</code>   <code>defer</code></p>
<ul>
<li>defer：和link是类似的机制了，不会阻碍GUI渲染，当GUI渲染完，才会把请求回来的JS去渲染。</li>
<li>async：请求JS资源是异步的（单独开辟HTTP去请求），此时GUI继续渲染；但是一但当JS请求回来，会立即暂停GUI的处理，接下来去渲染JS</li>
</ul>
<p>假如我们有多个JS的请求，如果不设置任何属性，肯定是按照顺序请求和执行JS的（依赖关系是有效的）；但是如果设置async，谁先请求回来就先渲染谁，依赖关系是无效的；如果使用defer是可以建立依赖关系的。浏览器内部在GUI渲染完成后，等待所有设置defer的资源都请求回来，再按照编写的依赖顺序去加载渲染js。只有写在浏览器的开头或者中间才需要这样写，写在浏览器结尾和默认方式一样</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb0eff8f875f4da89fb38916d517889d~tplv-k3u1fbpfcp-watermark.image" alt="image。png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0d91845cabaf4678825d64901effc8b9~tplv-k3u1fbpfcp-watermark.image" alt="image。png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>tips：遇到img，音视频，也是和link的机制一样，异步加载，继续渲染GUI。</p>
<h3 data-id="heading-3">总结</h3>
<p>所以真实项目中开发是：</p>
<ol>
<li>link标签放在头部：一般把link放在页面的头部（是为了在没有渲染DOM的时候，就通知HTTP去请求CSS了，这样DOM渲染玩，CSS也差不多回来了，更有效的利用时间，提高页面的渲染速度）</li>
<li>script标签放在底部：我们一般把JS放在页面的底部，防止其阻碍GUI的渲染，如果不放在底部，我们最好设置上async/defer；</li>
</ol>
<h3 data-id="heading-4">解析阶段优化方案</h3>
<p>根据以上原理的具体优化方案：</p>
<ol>
<li>
<p>标签语义化和避免深层次嵌套。加快构建DOM树的过程。</p>
</li>
<li>
<p>css选择器不要过长。CSS选择器渲染是从右到左的，加快构建CSSOM的过程。</p>
</li>
<li>
<p>尽早尽快地把CSS下载到客户端（充分利用HTTP多请求并发机制），将style、link、@import放到顶部</p>
</li>
<li>
<p>避免阻塞的JS加载使用async、defer属性，或者将script标签放到底部</p>
</li>
</ol>
<h2 data-id="heading-5">CRP优化之-渲染阶段优化</h2>
<p>渲染阶段主要优化回流和重绘</p>
<p>虽然现在项目都用vue和react来写，DOM操作已经被极大的简化，很少考虑DOM操作的性能问题，但是当我们自己封装不依赖框架的功能性组件插件的时候，性能仍然是不可忽视的问题</p>
<h3 data-id="heading-6">DOM的重绘和回流Repaint & Reflow</h3>
<p>回流：元素的大小或者位置发生了变化（当页面布局和几何信息发生变化的时候） ， 触发了重新布局，导致渲染树重新计算布局。
如</p>
<ol>
<li>添加或删除可见的DOM元素；</li>
<li>元素的位置或尺寸发生变化；</li>
<li>内容发生变化（比如文本变化或图片被另一个不同尺寸的图片所替代）；</li>
<li>页面一开始渲染的时候（这个无法避免）；</li>
<li>因为回流是根据视口的大小来计算元素的位置和大小的，所以浏览器的窗口尺寸变化也会引发回流</li>
</ol>
<p>重绘：元素样式的改变（但宽高、大小、位置等不变）。如  <code>outline</code> ，  <code>visibility</code> ，  <code>color</code> ，  <code>background-color</code> 等</p>
<p>注意：回流-定会触发重绘。而重绘不一定会回流</p>
<h3 data-id="heading-7">避免DOM的回流重绘</h3>
<ol>
<li>
<p>放弃传统操作dom的时代，基于vue/react使用数据影响视图模式。</p>
<p>mwm/ mvc / virtual dom/ dom diff</p>
</li>
<li>
<p>css集中改变</p>
<p>举例：</p>
<pre><code class="hljs language-html copyable" lang="html"> <span class="hljs-tag"><<span class="hljs-name">head</span>></span>
     <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
     <span class="hljs-selector-id">#box</span> &#123;
             ackground: lightcoral;
             <span class="hljs-attribute">width</span>: <span class="hljs-number">500px</span>;
             <span class="hljs-attribute">height</span>: <span class="hljs-number">50px</span>;
         &#125;
     </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
 <span class="hljs-tag"></<span class="hljs-name">head</span>></span>
 <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
     <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"box"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
     <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"test.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
 <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>test.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> box = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#box'</span>);
box.style.width = <span class="hljs-string">'100px'</span>;
box.style.height = <span class="hljs-string">'100px'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果直接这样写，不会出现样式改变的过程，因为在DOM解析的时候，最后会执行js，执行完js再构建DOM树，这时候box的样式已经变为100px，仅仅会执行一次回流和重绘，就是最开始的那一次。
所以我们这样写：</p>
<p>test.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
    <span class="hljs-keyword">let</span> box = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#box'</span>);
    box.style.width = <span class="hljs-string">'100px'</span>;
    box.style.height = <span class="hljs-string">'100px'</span>;
&#125;,<span class="hljs-number">1000</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上操作在老版本的浏览器中会改变两次回流重绘，因为改变了两次样式</p>
<p>这样写将央视集中改变可以减少次数</p>
<pre><code class="hljs language-js copyable" lang="js">box.style.cssText = <span class="hljs-string">"width:100px;height:100px;"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而新版浏览器不会重绘两次，新版浏览器有一个渲染队列机制。接下来再详细说明</p>
</li>
<li>
<p>分离css读写操作（ 现代的浏览器都有渲染队列的机制）</p>
<p>连续改变两次样式，在新版浏览器不会重绘两次。新版浏览器有一个<strong>渲染队列机制</strong>，会把所有要改变的样式依次放在渲染队列里面，然后把渲染队列中的样式渲染一次。</p>
<p>当修改样式的代码已经没有了或者遇到了获取元素样式的代码，都会刷新渲染队列：即把现有队列中的样式去统一修改和渲染一次，引发一次回流和重绘
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/76f19f82b1a840d99f8c9a795b396907~tplv-k3u1fbpfcp-watermark.image" alt="image。png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>获取样式的方式：</p>
<ul>
<li><code>style.xxx</code></li>
<li><code>getComputedStyle</code></li>
<li><code>getBoundingClientRect</code></li>
<li><code>offsetTop</code> 、 <code>offsetLeft</code> 、  <code>offsetWidth</code> 、  <code>offsetHeight</code> 、 <code>clientTop</code> 、  <code>clientLeft</code> 、  <code>clientWidth</code> 、 <code>clientHeight</code> 、 <code>scrollTop</code> 、 <code>scrollLeft</code> 、 <code>scrollWidth</code> 、 <code>scrollHeight</code> 、 <code>getComputedStyle</code> 、  <code>currentStyle</code> ...</li>
</ul>
<p>以下会引起两次回流和重绘
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c97c48a2e3c54470975815dcb2f4f8f9~tplv-k3u1fbpfcp-watermark.image" alt="image。png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果有一个需求，让其在原始宽度的基础上加100</p>
<pre><code class="hljs language-js copyable" lang="js">box.style.width = <span class="hljs-built_in">parseFloat</span>(<span class="hljs-built_in">window</span>.getComputedStyle(box)[<span class="hljs-string">'width'</span>]) + <span class="hljs-number">100</span> + <span class="hljs-string">'px'</span>;
box.style.height =  <span class="hljs-built_in">parseFloat</span>(<span class="hljs-built_in">window</span>.getComputedStyle(box)[<span class="hljs-string">'height'</span>]) + <span class="hljs-number">100</span> + <span class="hljs-string">'px'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>改为：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> prevW = <span class="hljs-built_in">parseFloat</span>(<span class="hljs-built_in">window</span>.getComputedStyle(box)[<span class="hljs-string">'width'</span>]),
    prevH = <span class="hljs-built_in">parseFloat</span>(<span class="hljs-built_in">window</span>.getComputedStyle(box)[<span class="hljs-string">'height'</span>]);<span class="hljs-number">0</span>
box.style.width = prevW + <span class="hljs-number">100</span> + <span class="hljs-string">'px'</span>;
box.style.height = prevH + <span class="hljs-number">100</span> + <span class="hljs-string">'px'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>元素批量修改</p>
<p>使用文档碎片减少回流： createDocumentFragment</p>
<p>以下会触发十次回流与重绘</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> box = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#box'</span>),
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">10</span>; i++) &#123;
        <span class="hljs-keyword">let</span> span = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'span'</span>);
        span.innerHTML = i + <span class="hljs-number">1</span>;
        box.appendChild(span);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>改为</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> box = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#box'</span>),
        frag = <span class="hljs-built_in">document</span>.createDocumentFragment();<span class="hljs-comment">//文档碎片</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">10</span>; i++) &#123;
        <span class="hljs-keyword">let</span> span = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'span'</span>);
        span.innerHTML = i + <span class="hljs-number">1</span>;
        frag.appendChild(span);
    &#125;
    box.appendChild(frag)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者用模板字符串拼接方式：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> box = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#box'</span>),
    str =  <span class="hljs-string">`  `</span> ;
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">10</span>; i++) &#123;
    str +=  <span class="hljs-string">` <span><span class="hljs-subst">$&#123;i+<span class="hljs-number">1</span>&#125;</span></span> `</span> ;
&#125;
box.innerHTML = str;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>动画效果应用到position属性为absolute或fixed的元素上(脱离文档流)
因为在重回的时候,是分层冲毁的,每一个文档流单独进行重绘,所以将动画效果单独放到一个文档流上面,可以减少性能开销</p>
</li>
<li>
<p>CSS3硬件加速( GPU加速)
比起考虑如何减少回流重绘,我们更期望的是,根本不要回流重绘;
<code>transfom</code>  \  <code>opacity</code>  \  <code>filters</code> 这些属性会触发硬件加速，不会引发回流和重绘
可能会引发的坑：过多使用会占用大量内存，性能消耗严重、有时候会导致字体模糊等</p>
</li>
<li>
<p>回牺牲平滑度换取速度
每次1像素移动一一个动画，但是如果此动画使用了100%的CPU，动画就会看上去是跳动的，因为浏览器正在与更新回流做斗争。每次移动3像素可能看起来平滑度低了，但它不会导致CPU在较慢的机器中抖动</p>
</li>
<li>
<p>避免table布局和使用css的javascript表达式</p>
</li>
</ol>
<h4 data-id="heading-8">利用渲染队列机制做一个轮播图</h4>
<p>写一个轮播图，原理是将第一张图复制一个放在最后，然后再运动到最后的时候，无过渡跳转到第一张图，再继续运行轮播图。代码如下：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
    * &#123;
        <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span>;
    &#125;

    <span class="hljs-selector-class">.container</span> &#123;
        <span class="hljs-attribute">position</span>: relative;
        <span class="hljs-attribute">margin</span>: <span class="hljs-number">20px</span> auto;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">800px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">300px</span>;
        <span class="hljs-attribute">overflow</span>: hidden;
    &#125;

    <span class="hljs-selector-class">.container</span> <span class="hljs-selector-class">.wrapper</span> &#123;
        <span class="hljs-attribute">position</span>: absolute;
        <span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">z-index</span>: <span class="hljs-number">10</span>;
        <span class="hljs-attribute">display</span>: flex;
        <span class="hljs-attribute">justify-content</span>: flex-start;
        <span class="hljs-attribute">align-items</span>: center;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">4000px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;

        <span class="hljs-comment">/* 动画 */</span>
        <span class="hljs-attribute">transition</span>: left .<span class="hljs-number">3s</span> linear <span class="hljs-number">0s</span>;
    &#125;

    <span class="hljs-selector-class">.container</span> <span class="hljs-selector-class">.wrapper</span> <span class="hljs-selector-class">.slide</span> &#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">800px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
    &#125;

    <span class="hljs-selector-class">.container</span> <span class="hljs-selector-class">.wrapper</span> <span class="hljs-selector-class">.slide</span> <span class="hljs-selector-tag">img</span> &#123;
        <span class="hljs-attribute">display</span>: block;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
    &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"container"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"wrapper"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"slide"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"images/1.jpg"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">""</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"slide"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"images/2.jpg"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">""</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"slide"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"images/3.jpg"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">""</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"slide"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"images/4.jpg"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">""</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-comment"><!-- 克隆 --></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"slide"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"images/1.jpg"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">""</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> container = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'.container'</span>),
    wrapper = container.querySelector(<span class="hljs-string">'.wrapper'</span>),
    step = <span class="hljs-number">0</span>,
    timer;

timer = <span class="hljs-built_in">setInterval</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    step++;
    <span class="hljs-keyword">if</span> (step >= <span class="hljs-number">5</span>) &#123;
        <span class="hljs-comment">// 立即回到第一张</span>
        wrapper.style.transition = <span class="hljs-string">'left 0s'</span>;
        wrapper.style.left =  <span class="hljs-string">`0px`</span> ;
        <span class="hljs-comment">// 运动到第二张</span>
        step = <span class="hljs-number">1</span>;
    &#125;
    wrapper.style.transition = <span class="hljs-string">'left .3s'</span>;
    wrapper.style.left =  <span class="hljs-string">`-<span class="hljs-subst">$&#123;step*<span class="hljs-number">800</span>&#125;</span>px`</span> ;
&#125;, <span class="hljs-number">2000</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是这样运行后会有问题，发现运行到最后的时候，突然跳到第二涨，并且还存在过渡。</p>
<p>原因是与渲染队列机制有关系，当运行step运行到5，浏览器会把四句样式修改放到渲染队列中，最后执行一次回流重绘，这样的话就只有最后两句css起作用了，就从最后一张直接拉到第二张了，而且还有过渡动画。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c65e0d7150ad4621b2daa78ab78574a0~tplv-k3u1fbpfcp-watermark.image" alt="image。png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>所以我需要让让其立即刷新一下渲染队列，先跳到第一章，再从第一张过渡到第二张。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> container = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'.container'</span>),
    wrapper = container.querySelector(<span class="hljs-string">'.wrapper'</span>),
    step = <span class="hljs-number">0</span>,
    timer;

timer = <span class="hljs-built_in">setInterval</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    step++;
    <span class="hljs-keyword">if</span> (step >= <span class="hljs-number">5</span>) &#123;
        <span class="hljs-comment">// 立即回到第一张</span>
        wrapper.style.transition = <span class="hljs-string">'left 0s'</span>;
        wrapper.style.left =   <span class="hljs-string">`0px`</span>  ;
        <span class="hljs-comment">// 运动到第二张</span>
        step = <span class="hljs-number">1</span>;
        <span class="hljs-comment">// 刷新渲染队列</span>
        wrapper.offsetLeft;
    &#125;
    wrapper.style.transition = <span class="hljs-string">'left .3s'</span>;
    wrapper.style.left =   <span class="hljs-string">`-<span class="hljs-subst">$&#123;step*<span class="hljs-number">800</span>&#125;</span>px`</span>;
&#125;, <span class="hljs-number">2000</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f9c02d5f62645fea44bd0bd6acfe890~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>手动刷新渲染队列</p>
<p>如果不利用这个机制，那么只能这样写</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b1bf3733ad747ffb2a0655366fd123c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            