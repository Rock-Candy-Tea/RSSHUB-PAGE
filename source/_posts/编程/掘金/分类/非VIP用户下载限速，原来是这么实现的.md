
---
title: '非VIP用户下载限速，原来是这么实现的'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83e7dc33bca54ba585ac8b3201a64fe2~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 30 Aug 2021 23:12:02 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83e7dc33bca54ba585ac8b3201a64fe2~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在日常工作之余，二狗子其实还是个隐藏的大触，一手素描画得出神入化，不少看过的小伙伴嗷嗷叫着求分享。为了让更多小粉丝能看到自己的作品，二狗子开发了一个提供有版权的素描稿件的下载网站。</p>
<p>二狗子的小网站，只要是注册用户就可以无限速下载素描稿。这原本是一件好事，但随着访问量的增多，带宽成本成为了二狗子不可承受之重。于是就有小伙伴建议做一个 VIP 服务，让 VIP 全速下载，免费用户稍微限速一点。二狗子觉得这是个很好的办法，于是打开百度找了找具体操作方式。</p>
<p>百度说传统的一些设置，都是在本地设置限制下载速度，如果是需要限制别人从你网站中下载的速度，则要用到 Rewrite 规则。</p>
<h2 data-id="heading-0">什么是 Rewrite 规则?</h2>
<p>Rewrite 是一种服务器的重写技术，主要的功能就是实现 URL 的跳转，它的正则表达式是基于 Perl 语言。可基于服务器级的(httpd.conf)和目录级的(.htaccess)两种方式。</p>
<p>如果要想用到 Rewrite 模块，必须先安装或加载 Rewrite 模块。方法有两种：一种是编译 apache 的时候就直接安装 Rewrite 模块；另一种是编译 apache 时以 DSO 模式安装 apache，然后再利用源码和 apxs 来安装 Rewrite 模块。</p>
<p>上面两种实现方法，二狗子看得一头雾水，感觉分开来每个字都看得懂，连起来又仿佛天书。无奈的二狗子尝试求助万能的又拍云客服——薇薇小姐姐。</p>
<p>“接入又拍云 CDN 就可以直接使用 Rewrite 功能哦，而且可以直接在控制台进行操作，非常方便。”薇薇小姐姐淡定回答。</p>
<p>好家伙！不愧是二狗子最爱的又拍云，赶快来看看具体使用方法吧。</p>
<h2 data-id="heading-1">又拍云 Rewrite 功能概述</h2>
<p>又拍云 Rewrite 功能主要是为了帮助用户简化内容分发业务逻辑，提升终端用户访问体验。特色是可以快速部署且配置简单，可极大降低业务实现成本。同时功能强大，涵盖了大部分互联网需求场景，包括：</p>
<ul>
<li>
<p>通过 URL 改写，可美化网站 URL，提升网站 SEO</p>
</li>
<li>
<p>为了节省更多访问带宽，限制网站请求下载速度</p>
</li>
<li>
<p>控制请求 URL 的结构、HTTP 头域等</p>
</li>
<li>
<p>自定义源站错误页面，提升终端用户体验</p>
</li>
<li>
<p>限制特定客户端的访问行为，合理进行访问控制</p>
</li>
</ul>
<p>在使用时，又拍云也根据不同用户需求划分了两种不同的使用方式：</p>
<ul>
<li>
<p>通用模式：适用于没有开发基础，且对语法规则不熟悉的用户，该模式使用方便快捷。</p>
</li>
<li>
<p>编程模式：适用于开发者，对相对通用模式来说，编程模式会更灵活，功能会更强大一些，适合对语法规则有深入了解的用户使用。</p>
</li>
</ul>
<p>为了让通用模式满足更多用户的需求。根据使用场景的不同，又拍云为【通用模式】配备了 7 大功能：</p>
<ul>
<li>
<p>添加 HTTP 头部（包括请求头和响应头）</p>
</li>
<li>
<p>删除 HTTP 头部（包括请求头和响应头）</p>
</li>
<li>
<p>边缘重定向</p>
</li>
<li>
<p>URL 改写</p>
</li>
<li>
<p>请求限速</p>
</li>
<li>
<p>访问控制</p>
</li>
<li>
<p>自定义错误页面</p>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83e7dc33bca54ba585ac8b3201a64fe2~tplv-k3u1fbpfcp-watermark.image" alt="1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">Rewrite 使用案例</h2>
<p>看完了又拍云 Rewrite 功能的介绍，二狗子配置下载限速，具体要怎么做呢。薇薇小姐姐告诉二狗子，通用和编程两种模式下都可以实现，并且一步步亲手示范怎么操作。</p>
<p>通用模式：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0e3436c43424042881b3be601f034ba~tplv-k3u1fbpfcp-watermark.image" alt="2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>编程模式：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/085d328bfeaf48898ae5f08476806462~tplv-k3u1fbpfcp-watermark.image" alt="3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个规则表示，当访问的 URL 匹配到这个域名的时候就在文件加载 1k 后开始限速，限速值为：60k。</p>
<p>设置完成后二狗子马上测试了一下，设置就生效，立刻完成了限速。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5fdcbd5771cb4f2196ab9f344e35cc04~tplv-k3u1fbpfcp-watermark.image" alt="4.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>薇薇还告诉二狗子，除了进行域名限速，也可以对指定类型的文件进行下载限速，比如：指定 zip 文件下载限速。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f243ea0694ae4451944d4771f072177f~tplv-k3u1fbpfcp-watermark.image" alt="5.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>完成这个设置后，当访问的 URL 匹配到这个域名，并且符合这个后缀的文件，就开始限速。</p>
<p>符合限制文件的效果：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca1794420e2a40e18a729d9aca62777c~tplv-k3u1fbpfcp-watermark.image" alt="6.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>其他文件的效果:</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a29740007a542f6b939b0a2f0d5e3fa~tplv-k3u1fbpfcp-watermark.image" alt="7.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当然了也可以进行 URL 改写，例如：当访问一个 URL 需要改写成在后面加上 !lalala 参数。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/882aa21e752c4da5b2fde3701fc21480~tplv-k3u1fbpfcp-watermark.image" alt="8.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-3">推荐阅读</h4>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.upyun.com%2Ftech%2Farticle%2F662%2F%25E8%25BF%2599%25E4%25B8%25A4%25E7%25A7%258D%25E5%25AE%258C%25E5%2585%25A8%25E4%25B8%258D%25E5%2590%258C%25E7%259A%2584JPEG%25E5%258A%25A0%25E8%25BD%25BD%25E6%2596%25B9%25E5%25BC%258F%25EF%25BC%258C%25E4%25BD%25A0%25E8%2582%25AF%25E5%25AE%259A%25E8%25A7%2581%25E8%25BF%2587%25EF%25BC%2581.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.upyun.com/tech/article/662/%E8%BF%99%E4%B8%A4%E7%A7%8D%E5%AE%8C%E5%85%A8%E4%B8%8D%E5%90%8C%E7%9A%84JPEG%E5%8A%A0%E8%BD%BD%E6%96%B9%E5%BC%8F%EF%BC%8C%E4%BD%A0%E8%82%AF%E5%AE%9A%E8%A7%81%E8%BF%87%EF%BC%81.html" ref="nofollow noopener noreferrer">这两种完全不同的JPEG加载方式，你肯定见过！</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.upyun.com%2Ftech%2Farticle%2F661%2F%25E7%259F%25AD%25E8%25A7%2586%25E9%25A2%2591%25E6%2597%25B6%25E4%25BB%25A3%25E4%25B8%258D%25E5%258F%25AF%25E5%25BF%25BD%25E8%25A7%2586%25E7%259A%2584%25E5%25B9%2595%25E5%2590%258E%25E5%258A%259F%25E8%2587%25A3%25E7%25AB%259F%25E7%2584%25B6%25E6%2598%25AF%25E5%25AE%2583%25EF%25BC%2581.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.upyun.com/tech/article/661/%E7%9F%AD%E8%A7%86%E9%A2%91%E6%97%B6%E4%BB%A3%E4%B8%8D%E5%8F%AF%E5%BF%BD%E8%A7%86%E7%9A%84%E5%B9%95%E5%90%8E%E5%8A%9F%E8%87%A3%E7%AB%9F%E7%84%B6%E6%98%AF%E5%AE%83%EF%BC%81.html" ref="nofollow noopener noreferrer">短视频时代不可忽视的幕后功臣竟然是它！</a></p></div>  
</div>
            