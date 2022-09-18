
---
title: '扒一扒elementUI el-image的源码，我学到了 ... _ 源码解析'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9d567d393d874d24ad672df7f7a4029b~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
author: 掘金
comments: false
date: Sat, 17 Sep 2022 22:40:23 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9d567d393d874d24ad672df7f7a4029b~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
---

<div>   
<div class="markdown-body cache"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:var(--cyanosis-base-color);transition:color .35s;--cyanosis-base-color:#353535;--cyanosis-title-color:#005bb7;--cyanosis-strong-color:#2196f3;--cyanosis-em-color:#4fc3f7;--cyanosis-del-color:#ccc;--cyanosis-link-color:#3da8f5;--cyanosis-linkh-color:#007fff;--cyanosis-border-color:#bedcff;--cyanosis-border-color-2:#ececec;--cyanosis-bg-color:#fff;--cyanosis-blockquote-color:#8c8c8c;--cyanosis-blockquote-bg-color:#f0fdff;--cyanosis-code-color:#c2185b;--cyanosis-code-bg-color:#fff4f4;--cyanosis-code-pre-color:#f8f8f8;--cyanosis-table-border-color:#c3e0fd;--cyanosis-table-th-color:#dff0ff;--cyanosis-table-tht-color:#005bb7;--cyanosis-table-tr-nc-color:#f7fbff;--cyanosis-table-trh-color:#e0edf7;--cyanosis-slct-title-color:#005bb7;--cyanosis-slct-titlebg-color:rgba(175,207,247,0.25);--cyanosis-slct-text-color:#c80000;--cyanosis-slct-bg-color:rgba(175,207,247,0.25);--cyanosis-slct-del-color:#999;--cyanosis-slct-elbg-color:#e8ebec;--cyanosis-slct-codebg-color:#ffeaeb;--cyanosis-slct-prebg-color:rgba(160,200,255,0.25)&#125;.markdown-body.__dark&#123;--cyanosis-base-color:#cacaca;--cyanosis-title-color:#ddd;--cyanosis-strong-color:#fe9900;--cyanosis-em-color:#ffd28e;--cyanosis-del-color:#ccc;--cyanosis-link-color:#ffb648;--cyanosis-linkh-color:#fe9900;--cyanosis-border-color:#ffe3ba;--cyanosis-border-color-2:#ffcb7b;--cyanosis-bg-color:#2f2f2f;--cyanosis-blockquote-color:#c7c7c7;--cyanosis-blockquote-bg-color:rgba(255,199,116,0.1);--cyanosis-code-color:#000;--cyanosis-code-bg-color:#ffcb7b;--cyanosis-code-pre-color:rgba(255,227,185,0.5);--cyanosis-table-border-color:#fe9900;--cyanosis-table-th-color:#ffb648;--cyanosis-table-tht-color:#000;--cyanosis-table-tr-nc-color:#6d5736;--cyanosis-table-trh-color:#947443;--cyanosis-slct-title-color:#000;--cyanosis-slct-titlebg-color:#fe9900;--cyanosis-slct-text-color:#00c888;--cyanosis-slct-bg-color:rgba(175,207,247,0.25);--cyanosis-slct-del-color:#999;--cyanosis-slct-elbg-color:#000;--cyanosis-slct-codebg-color:#ffcb7b;--cyanosis-slct-prebg-color:rgba(160,200,255,0.25)&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:var(--cyanosis-title-color);transition:color .35s&#125;.markdown-body h2&#123;position:relative;padding-left:10px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid var(--cyanosis-border-color-2)&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-14px&#125;.markdown-body h2:after&#123;content:"」";position:relative;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:var(--cyanosis-title-color);padding-left:6px;transition:color .35s&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:var(--cyanosis-strong-color)&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:var(--cyanosis-title-color);padding-left:6px;transition:color .35s&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:var(--cyanosis-title-color);padding-left:6px;transition:color .35s&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,var(--cyanosis-link-color),rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),var(--cyanosis-link-color));border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background-color:var(--cyanosis-bg-color);background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center;transition:background-color .5s&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:var(--cyanosis-code-color);word-break:break-word;overflow-x:auto;background-color:var(--cyanosis-code-bg-color);border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:var(--cyanosis-code-pre-color)&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:var(--cyanosis-border-color)&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:var(--cyanosis-strong-color);border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:var(--cyanosis-link-color);border-bottom:1px solid var(--cyanosis-border-color)&#125;.markdown-body a:hover&#123;border-bottom-color:var(--cyanosis-linkh-color)&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:var(--cyanosis-linkh-color)&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid var(--cyanosis-border-color);transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:var(--cyanosis-linkh-color)&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid var(--cyanosis-table-border-color);border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:var(--cyanosis-table-tr-nc-color)&#125;.markdown-body table tr:hover&#123;background-color:var(--cyanosis-table-trh-color)&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid var(--cyanosis-table-border-color)&#125;.markdown-body table th&#123;color:var(--cyanosis-table-tht-color);background-color:var(--cyanosis-table-th-color)&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:var(--cyanosis-blockquote-color);border-left:4px solid var(--cyanosis-strong-color);background-color:var(--cyanosis-blockquote-bg-color);padding:1px 20px;margin:22px 0;transition:color .35s&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:var(--cyanosis-strong-color)&#125;.markdown-body em,.markdown-body i&#123;color:var(--cyanosis-em-color)&#125;.markdown-body del&#123;color:var(--cyanosis-del-color)&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:var(--cyanosis-title-color);font-size:20px;font-weight:bolder;border-bottom:1px solid var(--cyanosis-border-color);cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:var(--cyanosis-blockquote-bg-color);border:2px dashed var(--cyanosis-strong-color)&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:var(--cyanosis-slct-title-color);background-color:var(--cyanosis-slct-titlebg-color)&#125;.markdown-body ol li::selection,.markdown-body p::selection,.markdown-body ul li::selection&#123;color:var(--cyanosis-slct-text-color);background-color:var(--cyanosis-slct-bg-color)&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:var(--cyanosis-slct-elbg-color)&#125;.markdown-body del::selection&#123;color:var(--cyanosis-slct-del-color);background-color:var(--cyanosis-slct-elbg-color)&#125;.markdown-body table thead th::selection&#123;background-color:transparent&#125;.markdown-body table tbody td::selection&#123;background-color:var(--cyanosis-slct-bg-color)&#125;.markdown-body code::selection&#123;background-color:var(--cyanosis-slct-codebg-color)&#125;.markdown-body pre>code::selection&#123;background-color:var(--cyanosis-slct-prebg-color)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>“我报名参加金石计划1期挑战——瓜分10万奖池，这是我的第2篇文章，<a href="https://s.juejin.cn/ds/jooSN7t" title="https://s.juejin.cn/ds/jooSN7t" target="_blank">点击查看活动详情</a>”</p>
<h1 data-id="heading-0">背景</h1>
<blockquote>
<p>最近公司遇到一个需求，就是实现一个 图片集的预览，功能包括 放大，缩小，鼠标拖动图片，旋转，恢复原位等<br>
由于<code>ElementUI</code>中的 <code>el-image</code>的预览不符合 业务需求，所以需要自己写<br>
自己看了下源码，并借鉴了过来，此处做个 <code>ElementUI</code>的<code>el-image</code>的源码解读，当做学习笔记</p>
</blockquote>
<h1 data-id="heading-1">稳重代码地址</h1>
<p>掘金的在线编辑有点问题，没有展示出来，但是我代码已经写在 <code>script</code>，点击<code>下面框的右上角马上掘金-查看详情</code>
<span href="https://code.juejin.cn/pen/7144598132792557599" target="_blank" class="code-editor-container"><iframe class="code-editor-frame" data-code="code-editor-element" data-code-id="7144598132792557599" data-src="https://code.juejin.cn/pen/7144598132792557599" style="display: none" loading="lazy"></iframe></span></p>
<h1 data-id="heading-2">先看效果</h1>
<p><strong>要实现的效果</strong></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9d567d393d874d24ad672df7f7a4029b~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="业务效果.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong><code>el-image</code>的效果</strong></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a7d41ea79e504827a1b238633c5755a7~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="ele效果.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-3">需求陈述</h1>
<p>业务希望图片查看可以固定在页面的左边，图片在左边的一个固定的框里面，图片被限制在这个框里面，图片可以实现 拖动，缩放，旋转等功能。</p>
<p>而右侧是表单操作，业务需要根据左侧看到的图片，并在右侧做相关操作</p>
<p>而<code>el-image</code>组件，这些功能都有，但是它是相当于弹框的形式，是个全局弹框的样子，无法满足业务的场景需求</p>
<p>所以我就看了下<code>el-image</code>的预览的源码，比较有感触</p>
<p>虽然在不看源码的情况下，也能自己实现，但是却没有源码实现的那么的 <strong>优雅，也不会有很多的细节处理</strong></p>
<p>不得不感叹，平时实现业务代码，能用就行，但是实现同样的功能，代码如何可以写的更好，看了<code>el-image</code>的预览源码，这就是以后需要努力的方向</p>
<h1 data-id="heading-4">知识点前置总结</h1>
<ul>
<li>鼠标的按下的事件监听方法 <code>mousedown</code></li>
<li>鼠标的移动的事件监听方法 <code>mouseover</code></li>
<li>鼠标的抬起的事件监听方法 <code>mouseup</code></li>
<li>缩放使用 <code>transform.scale</code></li>
<li>旋转使用  <code>transform.rotate</code></li>
<li>移动使用 <code>margin-left</code> 和 <code>margin-top</code></li>
</ul>
<h1 data-id="heading-5">代码逻辑解析</h1>
<h2 data-id="heading-6">点击鼠标拖动图片</h2>
<h3 data-id="heading-7">思路</h3>
<ul>
<li>先通过监听 图片的 <code>mousedown</code>的方法</li>
<li>获取起点：记录下鼠标点击图片的那一刻的鼠标的位置，作为移动的起点 <code>e.pageX</code> 和 <code>e.pageY</code></li>
<li>获取鼠标移动的路径，获取移动的位置，计算出移动的位置与起点的 偏移值，同时改变 图片的<code>margin-left</code> 和 <code>margin-top</code></li>
<li>获取终点：监听<code>mouseup</code>, <code>mouseup</code>事件出发后，就 停止监听 <code>mousemove</code> 方法，最后松开鼠标的点也就是 最后一次 <code>mousemove</code> 执行的值</li>
</ul>
<h3 data-id="heading-8">注意点</h3>
<ul>
<li>监听 <code>mouseup</code> 和 <code>mouseup</code> 事件，必须在 <code>mousedown</code>的回调函数里面。大白话就是：在鼠标点击在 图片的时候，才算拖动图片 <br> 这个时候 才开始监听 鼠标的移动和鼠标放开（因为存在一个情况：即使不按下鼠标，鼠标就在图片上面滑动，<code>mousemove</code>也是触发的,但那不是我们想要的，所以要避免这种情况）</li>
<li><code>mousedown</code>的事件回调必须 <code>e.preventDefault();</code>也就是阻止冒泡，这个很好理解，这个拖动事件不需要传递到外层</li>
</ul>
<h3 data-id="heading-9">代码如下</h3>
<pre><code class="hljs language-js copyable" lang="js"><img <span class="hljs-keyword">class</span>=<span class="hljs-string">"img-box__item"</span> @mousedown=<span class="hljs-string">"handleMouseDown"</span> :src=<span class="hljs-string">"url"</span> alt=<span class="hljs-string">""</span> :style=<span class="hljs-string">"imgStyle"</span>>
<span class="hljs-title function_">handleMouseDown</span>(<span class="hljs-params">e</span>)&#123;
    <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">'handleMouseDown ==='</span>,e)
    <span class="hljs-keyword">const</span> &#123; offsetX, offsetY &#125; = <span class="hljs-variable language_">this</span>.<span class="hljs-property">transform</span>;
    <span class="hljs-comment">// 起点</span>
    <span class="hljs-keyword">const</span> startX = e.<span class="hljs-property">pageX</span>;
    <span class="hljs-keyword">const</span> startY = e.<span class="hljs-property">pageY</span>;
    <span class="hljs-comment">// rafThrottle 防抖事件</span>
    <span class="hljs-variable language_">this</span>.<span class="hljs-property">_dragHandler</span> = <span class="hljs-title function_">rafThrottle</span>(<span class="hljs-function"><span class="hljs-params">ev</span> =></span> &#123;
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">transform</span>.<span class="hljs-property">offsetX</span> = offsetX + ev.<span class="hljs-property">pageX</span> - startX;
        <span class="hljs-variable language_">this</span>.<span class="hljs-property">transform</span>.<span class="hljs-property">offsetY</span> = offsetY + ev.<span class="hljs-property">pageY</span> - startY;
    &#125;);
    <span class="hljs-comment">// on 是封装的监听事件</span>
    <span class="hljs-title function_">on</span>(<span class="hljs-variable language_">document</span>, <span class="hljs-string">'mousemove'</span>, <span class="hljs-variable language_">this</span>.<span class="hljs-property">_dragHandler</span>);
    <span class="hljs-title function_">on</span>(<span class="hljs-variable language_">document</span>, <span class="hljs-string">'mouseup'</span>, <span class="hljs-function"><span class="hljs-params">ev</span> =></span> &#123;
        <span class="hljs-comment">// off 是封装的解除监听事件</span>
        <span class="hljs-title function_">off</span>(<span class="hljs-variable language_">document</span>, <span class="hljs-string">'mousemove'</span>, <span class="hljs-variable language_">this</span>.<span class="hljs-property">_dragHandler</span>);
    &#125;);
    e.<span class="hljs-title function_">preventDefault</span>();
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">缩放，旋转</h2>
<h3 data-id="heading-11">说明</h3>
<p>旋转，可以通过点击按钮事件触发</p>
<p>缩放， 需要通过按钮触发，并且也可以通过 鼠标的滚轮实现</p>
<h3 data-id="heading-12">思路</h3>
<ul>
<li>点击按钮（旋转），触发事件，直接改变 <code>image</code>的样式中的 <code>transform.rotate</code></li>
<li>点击按钮（缩放），触发事件，直接改变 <code>image</code>的样式中的 <code>transform.scale</code></li>
<li>(鼠标滚动实现缩放)：页面初始化的时候，监听 <code>mousewheel</code>,根据回调函数，判断 滚轮是 上滚还是下滚，然后给一个固定的缩放 ，改变<code>transform.scale</code></li>
</ul>
<h3 data-id="heading-13">代码如下</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-title function_">handleActions</span>(<span class="hljs-params">action, options = &#123;&#125;</span>) &#123;
    <span class="hljs-keyword">const</span> &#123; zoomRate, rotateDeg, enableTransition &#125; = &#123;
        <span class="hljs-attr">zoomRate</span>: <span class="hljs-number">0.2</span>,
        <span class="hljs-attr">rotateDeg</span>: <span class="hljs-number">90</span>,
        <span class="hljs-attr">enableTransition</span>: <span class="hljs-literal">true</span>,
        ...options
    &#125;;
    <span class="hljs-keyword">const</span> &#123; transform &#125; = <span class="hljs-variable language_">this</span>;
    <span class="hljs-keyword">switch</span> (action) &#123;
        <span class="hljs-comment">// 缩小</span>
        <span class="hljs-keyword">case</span> <span class="hljs-string">'zoomOut'</span>:
            <span class="hljs-keyword">if</span> (transform.<span class="hljs-property">scale</span> > <span class="hljs-number">0.2</span>) &#123;
                transform.<span class="hljs-property">scale</span> = <span class="hljs-built_in">parseFloat</span>((transform.<span class="hljs-property">scale</span> - zoomRate).<span class="hljs-title function_">toFixed</span>(<span class="hljs-number">3</span>));
            &#125;
            <span class="hljs-keyword">break</span>;
            <span class="hljs-comment">// 变大</span>
        <span class="hljs-keyword">case</span> <span class="hljs-string">'zoomIn'</span>:
            transform.<span class="hljs-property">scale</span> = <span class="hljs-built_in">parseFloat</span>((transform.<span class="hljs-property">scale</span> + zoomRate).<span class="hljs-title function_">toFixed</span>(<span class="hljs-number">3</span>));
            <span class="hljs-keyword">break</span>;
            <span class="hljs-comment">// 顺时针旋转</span>
        <span class="hljs-keyword">case</span> <span class="hljs-string">'clocelise'</span>:
            transform.<span class="hljs-property">deg</span> += rotateDeg;
            <span class="hljs-keyword">break</span>;
            <span class="hljs-comment">// 逆时针旋转</span>
        <span class="hljs-keyword">case</span> <span class="hljs-string">'anticlocelise'</span>:
            transform.<span class="hljs-property">deg</span> -= rotateDeg;
            <span class="hljs-keyword">break</span>;
    &#125;
    transform.<span class="hljs-property">enableTransition</span> = enableTransition;
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>滚轮缩放</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-variable language_">this</span>.<span class="hljs-property">_mouseWheelHandler</span> = <span class="hljs-title function_">rafThrottle</span>(<span class="hljs-function"><span class="hljs-params">e</span> =></span> &#123;
    <span class="hljs-keyword">const</span> delta = e.<span class="hljs-property">wheelDelta</span> ? e.<span class="hljs-property">wheelDelta</span> : -e.<span class="hljs-property">detail</span>;
    <span class="hljs-keyword">if</span> (delta > <span class="hljs-number">0</span>) &#123;
        <span class="hljs-variable language_">this</span>.<span class="hljs-title function_">handleActions</span>(<span class="hljs-string">'zoomIn'</span>, &#123;
            <span class="hljs-attr">zoomRate</span>: <span class="hljs-number">0.13</span>,
            <span class="hljs-attr">enableTransition</span>: <span class="hljs-literal">false</span>
        &#125;);
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-variable language_">this</span>.<span class="hljs-title function_">handleActions</span>(<span class="hljs-string">'zoomOut'</span>, &#123;
            <span class="hljs-attr">zoomRate</span>: <span class="hljs-number">0.13</span>,
            <span class="hljs-attr">enableTransition</span>: <span class="hljs-literal">false</span>
        &#125;);
    &#125;
&#125;);
<span class="hljs-comment">// on 是封装的监听事件</span>
<span class="hljs-title function_">on</span>(<span class="hljs-variable language_">document</span>, mousewheelEventName, <span class="hljs-variable language_">this</span>.<span class="hljs-property">_mouseWheelHandler</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">细节处理</h2>
<ul>
<li>
<p>监听<code>mousemove</code> 一定是在 <code>mousedown</code>的回调方法里面，也就是 <strong>必须鼠标按下图片之后才可以拖动</strong></p>
</li>
<li>
<p>监听 <code>mouseup</code> 也是一样也是在 <code>mousedown</code>的回调方法里面，道理同上</p>
</li>
<li>
<p>监听 鼠标滚轮的事件 做了 兼容 ,<code>firefox</code>中与其他浏览器有所不同<br>
<code>const mousewheelEventName = isFirefox() ? 'DOMMouseScroll' : 'mousewheel';</code></p>
</li>
<li>
<p><code>mousemove</code> 方法的回调，做了优化 ,在每次 浏览器页面 重绘的时候，处理 <code>mousemove</code>的回调函数，不仅仅起到了防抖的作用，而且在UI展现上面，不会有损失。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">function</span> <span class="hljs-title function_">rafThrottle</span>(<span class="hljs-params">fn</span>) &#123;
    <span class="hljs-keyword">let</span> locked = <span class="hljs-literal">false</span>;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">function</span>(<span class="hljs-params">...args</span>) &#123;
        <span class="hljs-keyword">if</span> (locked) <span class="hljs-keyword">return</span>;
        locked = <span class="hljs-literal">true</span>;
        <span class="hljs-variable language_">window</span>.<span class="hljs-title function_">requestAnimationFrame</span>(<span class="hljs-function"><span class="hljs-params">_</span> =></span> &#123;
            fn.<span class="hljs-title function_">apply</span>(<span class="hljs-variable language_">this</span>, args);
            locked = <span class="hljs-literal">false</span>;
        &#125;);
    &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>通过 <code>transform</code> 来控制缩放与旋转，通过<code>margin</code>来控制拖动，最后直接把 <code>style</code>直接挂到 <code>img</code>的组件上
说实话，我刚开始自己想的是，通过原生操作<code>DOM</code>来不断的用<code>js</code>设置 <code>style</code>，虽然也能实现，但是没有这个简练</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-title function_">imgStyle</span>(<span class="hljs-params"></span>) &#123;
    <span class="hljs-keyword">const</span> &#123; scale, deg, offsetX, offsetY, enableTransition &#125; = <span class="hljs-variable language_">this</span>.<span class="hljs-property">transform</span>;
    <span class="hljs-keyword">const</span> style = &#123;
        <span class="hljs-attr">transform</span>: <span class="hljs-string">`scale(<span class="hljs-subst">$&#123;scale&#125;</span>) rotate(<span class="hljs-subst">$&#123;deg&#125;</span>deg)`</span>,
        <span class="hljs-attr">transition</span>: enableTransition ? <span class="hljs-string">'transform .3s'</span> : <span class="hljs-string">''</span>,
        <span class="hljs-string">'margin-left'</span>: <span class="hljs-string">`<span class="hljs-subst">$&#123;offsetX&#125;</span>px`</span>,
        <span class="hljs-string">'margin-top'</span>: <span class="hljs-string">`<span class="hljs-subst">$&#123;offsetY&#125;</span>px`</span>
    &#125;;
    <span class="hljs-keyword">return</span> style;
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>其他方面<br>
源码里面还有一些边界的判断的问题，也做了很多的处理，包括工具的封装等，都是很值得学习的</p>
</li>
</ul>
<h1 data-id="heading-15">总结</h1>
<p>虽然只是一个简单的小功能，但是人家的源码写的<strong>如何简单，并且还做了很好的封装，也做了很好的兼容处理</strong></p>
<p>若是我们自己写，当然也能写出来，但是代码估计就没有这么的简洁，封装没有这么的好，很多兼容或者适配都没有做好</p>
<p>被社区证明的框架源码其实就是最值得我们学习的，说白了就是代码的最佳实践</p>
<p>这么好的学习资源要用起来</p>
<p>而不是整天埋怨没有机会提升，这源码不就摆在这里，而且你还天天在用，多么好的学习机会</p></div>  
</div>
            