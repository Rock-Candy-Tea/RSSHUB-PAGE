
---
title: '浏览器系列 -- CDN缓存'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/74b71c3681db4164af7989345e20b2c8~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 17 Apr 2021 00:11:00 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/74b71c3681db4164af7989345e20b2c8~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>大型Web应用对速度的追求并没有止步于仅仅利用浏览器缓存，因为浏览器缓存始终只是为了提升二次访问的速度，对于首次访问的加速，我们需要从网络层面进行优化，最常见的手段就是<code>CDN加速</code>。<strong>通过将静态资源(例如javascript，css，图片等等）缓存到离用户很近的相同网络运营商的CDN节点上，即<code>CDN缓存</code></strong></p>
<p>不同于浏览器缓存，<code>CDN缓存</code>是一种<strong>服务端缓存</strong></p>
<h2 data-id="heading-0">CDN 加速的原理</h2>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/74b71c3681db4164af7989345e20b2c8~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ol>
<li>内容源（可以理解为服务器所在地）在国内<code>某个省份</code>内，但用户来自<code>全国各地</code></li>
<li>CDN服务商在<code>全国各个省份</code><strong>部署CDN节点</strong></li>
<li>在一个地区内<strong>只要有一个</strong>用户先加载资源</li>
<li>CDN通过将静态资源（例如javascript，css，图片等等）<strong>缓存到离用户很近</strong>的相同网络运营商的CDN节点上，即<code>CDN缓存</code></li>
<li>该地区内的其他所有用户访问资源时，就会<code>访问到离自己最近</code>的相同网络线路上的CDN节点</li>
<li>当请求达到CDN节点后，节点会判断<strong>自己的内容缓存是否有效</strong></li>
<li>如果有效，则立即响应缓存内容给用户，从而加快响应速度</li>
<li>如果CDN节点的缓存失效，它会根据服务配置去我们的<strong>内容源服务器</strong><code>获取最新的资源响应给用户</code>，并将内容<code>再次缓存下来</code>以便响应给后续访问的用户</li>
</ol>
<h2 data-id="heading-1">CDN访问资源流程图</h2>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c59b373fc6048e980d59b1c71380a8e~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">如何配置</h2>
<p>整体来说，和<strong>浏览器缓存</strong>配置<code>保持同步</code>即可
<img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b55cf4357b454a62a6e10019c1bf11f6~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
值得注意的是：</p>
<ul>
<li><strong>浏览器缓存</strong>是按照<code>TCP头部规则</code>进行自己的缓存处理</li>
<li><strong>CDN缓存</strong>是由<code>CDN服务商</code>来负责缓存控制的，<strong>二者不会互相冲突</strong></li>
</ul>
<h2 data-id="heading-3">问题出现</h2>
<p>问题场景：如果我们浏览器缓存设置<code>cache-control: max-age=600</code>，即缓存<code>10分钟</code>，但CDN缓存配置中设置文件缓存时间为<code>1小时</code>，此时如果服务器资源更新了，那如果资源在被访问后第12分钟修改并上传到<code>服务器</code>，用户重新访问资源，响应码会是304，<code>拿不到最新资源</code>，<code>一个小时后再次访问</code>才能更新为最新资源</p>
<h2 data-id="heading-4">用户访问资源全过程</h2>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/111a7eca45df490e8a50404cf1ec7591~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ol>
<li>当用户访问我们的业务服务器时，首先进行的就是http缓存处理</li>
<li>如果http缓存通过校验，则直接响应给用户</li>
<li>如果未通过校验，则继续进行cdn缓存的处理，cdn缓存处理完成后返回给客户端，由客户端进行http缓存规则存储并响应给用户。</li>
<li>CDN节点每隔一段时间就会去服务器请求最新资源，这段时间是由CDN服务商决定的</li>
</ol>
<h2 data-id="heading-5">解决问题</h2>
<ol>
<li>我们可以和CDN服务商商讨一下把CDN缓存<code>有效时间缩短</code>到跟浏览器缓存一致</li>
<li>或者在浏览器缓存失效时使用CDN服务商提供的<code>强制更新功能</code>，使得CDN缓存得到更新</li>
</ol></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            