
---
title: 'uniapp和小程序如何分包，详细步骤'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d3f85441e844a0387abd0e5480541ce~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 01 Sep 2021 17:14:23 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d3f85441e844a0387abd0e5480541ce~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">一、小程序分包</h1>
<p>每个使用分包小程序必定含有一个主包。所谓的主包，即放置默认启动页面/TabBar 页面，以及一些所有分包都需用到公共资源/JS 脚本；而分包则是根据开发者的配置进行划分。</p>
<p>在小程序启动时，默认会下载主包并启动主包内页面，当用户进入分包内某个页面时，客户端会把对应分包下载下来，下载完成后再进行展示</p>
<p>目前小程序分包大小有以下限制：</p>
<p>整个小程序所有分包大小不超过 20M
单个分包/主包大小不能超过 2M
对小程序进行分包，可以优化小程序首次启动的下载时间，以及在多团队共同开发时可以更好的解耦协作。</p>
<p>这里直接点击去看官方的分包教程容易理解:</p>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevelopers.weixin.qq.com%2Fminiprogram%2Fdev%2Fframework%2Fsubpackages%2Fbasic.html" target="_blank" rel="nofollow noopener noreferrer" title="https://developers.weixin.qq.com/miniprogram/dev/framework/subpackages/basic.html" ref="nofollow noopener noreferrer">developers.weixin.qq.com/miniprogram…</a></p>
</blockquote>
<h1 data-id="heading-1">二、uniapp分包小程序</h1>
<p>App默认为整包。兼容小程序的分包配置。其目的不用于下载提速，而用于首页是vue时的启动提速。</p>
<ul>
<li>components:公共组件（供主包引用）</li>
<li>page_后跟拼音的都是分包</li>
<li>分包里的components是单个分包自己的组件目录，分包vue页面的引用只能是在自己page_xxxx分包目录下才可以引用</li>
<li>pages是主包，里面都是启动页面/TabBar 页面</li>
<li>static里放的是公共静态资源，图片类</li>
</ul>
<h2 data-id="heading-2">分包步骤：</h2>
<h3 data-id="heading-3">1.配置manifest.json</h3>
<p>"mp-weixin": &#123;</p>
<p>"optimization":&#123;"subPackages":true&#125;</p>
<p>&#125;</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d3f85441e844a0387abd0e5480541ce~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>优化分包：</p>
<p>在对应平台的配置(manifest.json)下添加"optimization":&#123;"subPackages":true&#125;开启分包优化</p>
<p>目前只支持mp-weixin、mp-qq、mp-baidu的分包优化</p>
<ul>
<li>静态文件：分包下支持 static 等静态资源拷贝，即分包目录内放置的静态资源不会被打包到主包中，也不可在主包中使用</li>
<li>js文件：当某个 js 仅被一个分包引用时，该 js 会被打包到该分包内，否则仍打到主包（即被主包引用，或被超过 1 个分包引用）</li>
<li>自定义组件：若某个自定义组件仅被一个分包引用时，且未放入到分包内，编译时会输出提示信息</li>
</ul>
<h3 data-id="heading-4">2.配置pages.json</h3>
<p>在pages.json中新建数组"subPackages"，数组中包含两个参数：1.root：为子包的根目录，2.pages：子包由哪些页面组成，参数同pages；</p>
<p>注意：主包和分包是不能再同一目录下，在构建uniapp项目时，可以考虑一下目录结构，以便后期进行分包；</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f6c7353925fa4a479de1f9f7b77bf94a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">3.分包预载配置（preloadRule）</h3>
<p>做这一步主要为了优化速度，不想优化速度的可以跳过这个配置</p>
<p>配置preloadRule后，在进入小程序某个页面时，由框架自动预下载可能需要的分包，提升进入后续分包页面时的启动速度</p>
<p>preloadRule 中，key 是页面路径，value 是进入此页面的预下载配置，每个配置有以下几项：</p>


























<table><thead><tr><th>字段</th><th>类型</th><th>必填</th><th>默认值</th><th>说明</th></tr></thead><tbody><tr><td>packages</td><td>StringArray</td><td>是</td><td>无</td><td>进入页面后预下载分包的 <code>root</code> 或 <code>name</code>。<code>__APP__</code> 表示主包。</td></tr><tr><td>network</td><td>String</td><td>否</td><td>wifi</td><td>在指定网络下预下载，可选值为：all（不限网络）、wifi（仅wifi下预下载）</td></tr></tbody></table>
<p>app的分包，同样支持preloadRule，但网络规则无效。</p>
<p>可查看官方配置项:</p>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Funiapp.dcloud.io%2Fcollocation%2Fpages%3Fid%3Dsubpackages" target="_blank" rel="nofollow noopener noreferrer" title="https://uniapp.dcloud.io/collocation/pages?id=subpackages" ref="nofollow noopener noreferrer">uniapp.dcloud.io/collocation…</a></p>
</blockquote></div>  
</div>
            