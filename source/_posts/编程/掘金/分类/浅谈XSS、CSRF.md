
---
title: '浅谈XSS、CSRF'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/21e8146c6c2e4e4badcde047b4a3253c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 27 Jul 2021 02:06:12 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/21e8146c6c2e4e4badcde047b4a3253c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">XSS：跨站脚本攻击 js注入</h1>
<pre><code class="copyable">分为三类：存储型（持久型）
         反射型（非持久型）
         DOM型
         
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/21e8146c6c2e4e4badcde047b4a3253c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
（图片来自于<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1DW411U7XE%2F%3Fspm_id_from%3D333.788.recommend_more_video.-1" target="_blank" rel="nofollow noopener noreferrer" title="https://www.bilibili.com/video/BV1DW411U7XE/?spm_id_from=333.788.recommend_more_video.-1" ref="nofollow noopener noreferrer">XSS 原理和攻防 - Web 安全常识_哔哩哔哩_bilibili</a> 02：59  侵删</p>
<p>反射型：一般出现在url链接中。通常通过邮件或者聊天地址给你一个点击地址。发出请求的时候，xss的代码出现在我们的访问链接中，作为一部分的输入提交到服务器。服务器解析之后做出响应。这段代码就会随着响应返回到浏览器中进行渲染。/</p>
<pre><code class="copyable">    也就是说xss代码会被web服务器反射回客户端进行执行。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>存储型：最典型的情况在留言中。和反射型的区别在于提交的代码回存储在web服务器中（持久型）下一次请求的时候不需要再次请求。</p>
<p>XSS存在的原因：对url中的参数或者用户提交输入的地方没有提交过滤，造成的不合法的参数能够被提交到web服务器。但是我们没有办法对它进行完全充分百分百的过滤。
xss的防范：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/22b5ca6f7b974f0e94091a0f391fcd6d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
图片来源于<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1DW411U7XE%2F%3Fspm_id_from%3D333.788.recommend_more_video.-1" target="_blank" rel="nofollow noopener noreferrer" title="https://www.bilibili.com/video/BV1DW411U7XE/?spm_id_from=333.788.recommend_more_video.-1" ref="nofollow noopener noreferrer">XSS 原理和攻防 - Web 安全常识_哔哩哔哩_bilibili</a> 08：24 侵删</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44c5c90fa59d4bf3844c2dd1facb1473~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">同上，侵删
ps.session和cookie的区别</p>
<p>在node.js中如何做防范呢，使用js-xss库</p>
<h1 data-id="heading-1">CSRF：跨站点请求伪造</h1>
<p>你可以这样去理解：攻击者盗用了你的身份，以你的名义去发送恶意请求</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f75ba0f31c7c4b558f0c8b9dd06c7535~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
图源：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1iW411171s%2F%3Fspm_id_from%3D333.788.recommend_more_video.0" target="_blank" rel="nofollow noopener noreferrer" title="https://www.bilibili.com/video/BV1iW411171s/?spm_id_from=333.788.recommend_more_video.0" ref="nofollow noopener noreferrer">CSRF 攻击和防御 - Web 安全常识_哔哩哔哩_bilibili</a> 01：12 侵删
本质原因：上图右下角紫色的服务器验证不够
解决方法：在服务器服务端去做验证处理</p>
<h5 data-id="heading-2">1.尽可能使用post请求</h5>
<h5 data-id="heading-3">2.加入验证码/滑块等等</h5>
<h3 data-id="heading-4">3.验证Referer（http头上的字段）（当前请求的来源地址）（简单-方便的方案）但是也有网站可以篡改referer</h3>
<h2 data-id="heading-5">4.anti CSRF token(最常用的）：</h2>
<pre><code class="copyable">1)在form表单或者头信息中传递一个随机产生的token
2)token存储在服务端（不在cookie，一般用户信息存储在cookie就极容易被CSRF攻击）
3)服务端通过拦截器验证token
4)校验失败就拒绝请求，token验证通过后要立刻销毁
(刚查看了感觉掘金不是使用的token,如有发现的请留言指正)
5)自定义header（本质上其实和4)一样的）
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            