
---
title: '关于google插件(扩展程序)如何发布及开发环境使用问题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d81ab4c2500d4f6c978a9ee40d28f4fe~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 25 Aug 2021 18:20:32 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d81ab4c2500d4f6c978a9ee40d28f4fe~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>最近接手Google插件开发的需求，在此将自己的经验做个总结，防止忘记，也供其他小伙伴做参考</p>
<p>发现一篇比较好的关于google如何开发的文档，附上作者的文档出处，# <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cnblogs.com%2Fliuxianan%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cnblogs.com/liuxianan/" ref="nofollow noopener noreferrer">小茗同学的博客园</a>   <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cnblogs.com%2Fliuxianan%2Fp%2Fchrome-plugin-develop.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cnblogs.com/liuxianan/p/chrome-plugin-develop.html" ref="nofollow noopener noreferrer">【干货】Chrome插件(扩展)开发全攻略</a></p>
<h2 data-id="heading-0">一.如何发布</h2>
<h3 data-id="heading-1">1.创建并登录google账号</h3>
<h3 data-id="heading-2">2.来到 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fchrome.google.com%2Fwebstore%2Fdevconsole%2F84db9341-0822-4df1-bd6c-8ce61078445e%3Fhl%3Dzh-CN" target="_blank" rel="nofollow noopener noreferrer" title="https://chrome.google.com/webstore/devconsole/84db9341-0822-4df1-bd6c-8ce61078445e?hl=zh-CN" ref="nofollow noopener noreferrer">开发者信息中心</a> 点击上传新内容,这里要先付费哦</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d81ab4c2500d4f6c978a9ee40d28f4fe~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e3cd2c059d74d1388fd02c4c47a55bf~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">3.点击上传新内容，弹出下图的弹框（图1），拖入zip包的时候，会让二次信息验证（图2）</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e04f22f82ba94d2eac3dc9c43564efa2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f06b6586ada54ce5bf7cb396231da3d9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">4.根据提示，在浏览器输入2次验证的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.google.com%2Flanding%2F2step" target="_blank" rel="nofollow noopener noreferrer" title="https://www.google.com/landing/2step" ref="nofollow noopener noreferrer">地址</a></h3>
<h3 data-id="heading-5">5.这里的发布跟微信小程序不一样哦，审核通过会自动发布的，不需要手动发布，所以小伙伴们在提交审核的时候需要注意一下哈，而且审核的时间有点久，至少7天。</h3>
<h3 data-id="heading-6">发布注意事项</h3>
<p>a.提交审核需要修改manifest.json文件 version 的版本号</p>
<p>b.注意key.pem 文件需要存在，并且ID要跟google应用商店的ID保持一致</p>
<p>c.手动压缩成zip包拖入即可</p>
<h2 data-id="heading-7">二. 想拿到应用商店的代码</h2>
<p>在浏览器搜索 chrome 插件下载  会有很多网上出现，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcrxdl.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://crxdl.com/" ref="nofollow noopener noreferrer">本人常用的是</a> ，供大家参考</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.gugeapps.net%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.gugeapps.net/" ref="nofollow noopener noreferrer">google网上应用店 地址</a></p>
<h2 data-id="heading-8">三. 开发环境使用扩展程序</h2>
<p>这个模块相信开发的小伙伴都有在使用，这里做个记录</p>
<h3 data-id="heading-9">1.google浏览器右上角竖着的三个点，点击弹框选择设置，进入下图的页面，选择扩展程序。</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d7a626ef1d8445bbbaaab1d1ec0b88a8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">2.扩展程序页面</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/40cff2454670414da142cfe368ea2753~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-11">3.</h3>
<p>a.【打包扩展程序】，打包生成crx, 开发环境用的后缀可改成zip(此zip为crx改的，非压缩生成的)，直接安装</p>
<p>b.zip解压后的数据，可通过【加载已解压的扩展程序】 加入到浏览器的扩展程序中</p>
<p>c.<strong>打包开发环境的，使用chrome打包，需要把key拿出来，单独选目录和key，key不能丢，开发环境打包先挪走，发布在挪回来打包</strong></p>
<h3 data-id="heading-12">开发模式经常会遇到安装的error问题，用【加载已解压的扩展程序】 产生问题的可能性最小</h3>
<p>crx > zip > 已解压</p></div>  
</div>
            