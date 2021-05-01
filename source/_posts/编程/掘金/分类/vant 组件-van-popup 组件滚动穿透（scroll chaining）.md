
---
title: 'vant 组件-van-popup 组件滚动穿透（scroll chaining）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/259a8762933e48f386f61f7ab9809774~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 01 May 2021 02:56:34 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/259a8762933e48f386f61f7ab9809774~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/259a8762933e48f386f61f7ab9809774~tplv-k3u1fbpfcp-zoom-1.image" alt="WX20210501-185136@2x" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-0">问题描述</h3>
<p>当页面出现浮层（例如 popup 弹窗类型组件），在滑动浮层内的内容时候，浮层下的页面内容也随之发生滚动，从而出现了滚动穿透。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30fa2b76f1674223938d37712e4b62f8~tplv-k3u1fbpfcp-zoom-1.image" alt="图像" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">官方解决方案</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/89740523ce5c4ef9a49f641f1dfffc9b~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210501184818764" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>弊端：</strong></p>
<p>如果在van-popup 层 使用 catch:touchStart ="stopSlide" 事件，则pop里面的内容都不可以响应bind：tap 事件，即不可以实现pop页面的自定义的键盘； 参考文档（van-popup）<a href="https://vant-contrib.gitee.io/vant-weapp/#/popup" target="_blank" rel="nofollow noopener noreferrer">vant-contrib.gitee.io/vant-weapp/…</a></p>
<h3 data-id="heading-2">个人解决方案</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">catch</span>:touchmove = <span class="hljs-string">'stop_scroll_chaining'</span> 不要禁止 touchstart，禁止touchmove即可，保证浮窗内的元素可以被点击，同时保证不会滑动穿透；
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            