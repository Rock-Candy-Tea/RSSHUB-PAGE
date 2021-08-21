
---
title: '摸鱼不如来了解一下--DOM文档对象模型（节点操作）｜8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19c5e83433344403b6c70c93b06f0deb~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 20 Aug 2021 16:35:29 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19c5e83433344403b6c70c93b06f0deb~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><p>这是我参与8月更文挑战的第20天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a>”</p>
<h1 data-id="heading-0"><strong>节点操作</strong></h1>
<h2 data-id="heading-1">节点的三个基本属性</h2>
<h3 data-id="heading-2">节点类型nodeType</h3>
<blockquote>
<p>●   元素节点nodeType为1</p>
<p>●   属性节点nodeType为2</p>
<p>●   文本节点nodeType为3。(文本节点包括文字、空格、换行等)</p>
</blockquote>
<h3 data-id="heading-3">节点名称nodeName</h3>
<h3 data-id="heading-4">节点值nodeValue</h3>
<h2 data-id="heading-5">节点层级</h2>
<h3 data-id="heading-6">父级节点node.parentNode，获得的是最近的一级的父节点；若找不到则返回空null（要先获取子元素）</h3>
<p>●   <strong>子节点parentNode.childNodes，返回包含指定节点的 子节点 的集合，注意是包含了元素节点，文本节点等（要先获取父元素）。若只想得到元素节点，则需要专门处理，所以一般不提倡使用childNodes</strong></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19c5e83433344403b6c70c93b06f0deb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>●   <strong>子节点parentNode.children，这是一个只读属性，返回所有的子元素节点(伪数组的形式)。他只返回子元素节点，其余类型的节点不返回</strong></p>
<blockquote>
<p>●   获取元素的第一个子节点parentNode.firstChild，找不到则返回null,注意是返回所有的子节点，包含元素节点，文本节点</p>
<p>●   <strong>获取第一个子元素节点parentNode.firstElementChild (有兼容性问题，IE9以上才支持)</strong></p>
<p>●   获取元素的最后一个子节点parentNode.lastChild，找不到返回null</p>
<p>●   <strong>获取最后一个子元素节点parentNode.lastElementChild (有兼容性问题)</strong></p>
</blockquote>
<h3 data-id="heading-7">获取兄弟节点</h3>
<h4 data-id="heading-8">node.nextSibling</h4>
<p>●   返回当前元素的下一个兄弟节点，找不到就返回null。<strong>返回的节点包含所有类型的节点</strong></p>
<h4 data-id="heading-9">node.previousSibling</h4>
<p>●   返回当前元素的上一个兄弟节点</p>
<h4 data-id="heading-10">node.nextElementSibling</h4>
<p>●   <strong>返回当前元素的下一个兄弟元素节点(兼容性问题，IE9以上才支持)</strong></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/09d4672480f34963bf05d8f3d13b41a7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>●   node.previousElementSibling</p>
<p>●   返回当前元素的上一个兄弟元素节点</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66d0323efb7d441e8f8703496080440a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>●   parentNode.firstElementChild和parentNode.lastElementChild有兼容性问题，ie9以上才支持</p>
<h2 data-id="heading-11"><strong>动态创建元素节点</strong></h2>
<p>●   <strong>document.createElement('tagName')</strong> <strong>，只创建是不能够看见的，还需要添加节点</strong></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cee6d8302bf940149e491a7cce3b0cd4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-12"><strong>添加节点</strong></h2>
<p>●   <strong>node.appendChild(child)</strong> <strong>将一个节点添加到指定父节点的子节点集合的末尾(类似于css的after伪元素)</strong></p>
<p>●   <strong>node.insertBefore(child,</strong> <strong>指定元素) 将一个节点添加到父节点的指定子节点的前面(类似于css的before伪元素)</strong></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e3082256550b48e2a146f1eb1f4c4c65~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-13">删除节点</h2>
<p>●   node.removeChild(child)，删除父节点node中的某个子节点，返回删除的节点</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/25ac74b93f9f4427b630ec29f1df0562~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-14">复制节点</h3>
<h4 data-id="heading-15">node.cloneNode()返回调用该方法的节点的一个副本</h4>
<blockquote>
<p>●   <strong>括号内无参数或者参数为false，则为浅拷贝，只克隆节点本身，不会克隆里面的子节点(只复制标签不复制内容)</strong></p>
<p>●   <strong>node.cloneNode(true)</strong> <strong>为深拷贝，复制节点本身及里面所有子节点(既复制标签也复制内容)</strong></p>
</blockquote>
<h4 data-id="heading-16"><strong>创建和添加节点-->element.insertAdjacentHTML(position, text)</strong></h4>
<p>●   <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FAPI%2FElement%2FinsertAdjacentHTML" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/API/Element/insertAdjacentHTML" ref="nofollow noopener noreferrer">element.insertAdjacentHTML - Web API 接口参考 | MDN (mozilla.org)</a></p>
<p>●   position插入位置</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9986bebef0b84b45a3f9073ed9a22c55~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>●   text插入的内容(要以字符串的形式)</p>
<pre><code class="copyable">d1.insertAdjacentHTML('afterend', '<div id="two">two</div>');
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            