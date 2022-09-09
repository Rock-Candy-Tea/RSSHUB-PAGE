
---
title: '个人博客搭建遇坑流程のVuePress2 📕'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/baefc60ec9294422be97a2c96c3f8c5e~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
author: 掘金
comments: false
date: Thu, 08 Sep 2022 01:13:22 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/baefc60ec9294422be97a2c96c3f8c5e~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p>“我报名参加金石计划1期挑战——瓜分10万奖池，这是我的第1篇文章，<a href="https://s.juejin.cn/ds/jooSN7t" title="https://s.juejin.cn/ds/jooSN7t" target="_blank">点击查看活动详情</a>”</p>
<h1 data-id="heading-0">序</h1>
<p>最近突然想重新做一下个人博客的网页，自己以前曾经使用过<strong>hexo</strong>编写过，现在准备使用<code>vuepress</code>了。</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fqq_36171287%2Farticle%2Fdetails%2F105961636" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/qq_36171287/article/details/105961636" ref="nofollow noopener noreferrer">《快速搭建个人博客网站——Hexo》</a></li>
</ul>
<p><code>vuepress</code>的配置使用跟着官网的快速上手走基本就可以了，一些重要内容的配置主要是编写在<code>config.js</code>文件中的。</p>
<p><code>vuepress</code>官网：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fv2.vuepress.vuejs.org%2Fzh%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://v2.vuepress.vuejs.org/zh/" ref="nofollow noopener noreferrer">vuepress中文网</a></p>
<blockquote>
<p>我的博客</p>
<ul>
<li>我的项目地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fkongchengji%2Fkongchengji-blog" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/kongchengji/kongchengji-blog" ref="nofollow noopener noreferrer">github.com/kongchengji…</a></li>
<li>我的博客地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fkongchengji.github.io%2Fblog-project%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://kongchengji.github.io/blog-project/" ref="nofollow noopener noreferrer">kongchengji.github.io/blog-projec…</a></li>
</ul>
</blockquote>
<p>不过因为我不太喜欢<code>vuepress</code>提供的默认模板样式，所以我去找了<code>vuepress-theme-reco</code>主题。这是一款简洁而优雅的 vuepress 博客 & 文档 主题。</p>
<p>此主题有0.x、1.x、2.x三个版本，其中2.x主要是alpha测试版。不过我直接不怕死的选择了2.x，虽然看官网上，好像问题贼多。</p>
<p>让我开始体验一下<code>vuepress-theme-reco2.x</code>的使用吧</p>
<hr>
<h1 data-id="heading-1">vuepress-theme-reco2.x使用</h1>
<blockquote>
<p>官网：<a href="https://link.juejin.cn/?target=http%3A%2F%2Fv2.vuepress-reco.recoluan.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://v2.vuepress-reco.recoluan.com/" ref="nofollow noopener noreferrer">v2.vuepress-reco.recoluan.com/</a></p>
</blockquote>
<p>虽然不知道为什么，但是官网上并没有<code>favicon.ico</code>的标识，希望到时候我能设置吧💦</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/baefc60ec9294422be97a2c96c3f8c5e~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="p1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>首先先全局安装:  <code>yarn global add @vuepress-reco/theme-cli@1.0.7</code></li>
</ol>
<p>然后创建项目：<code>theme-cli init</code></p>
<p>这里会出现项目的选项页面，有点像<code>vue cli</code>创建项目时的样子。在最后一项选择时，选择<code>2.x</code>就好。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c0b4c186380141faa655786e739aa5be~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="p2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li><code>cd</code>进入项目当中，然后使用<code>yarn</code>安装一下需要的依赖包</li>
</ol>
<p>当前项目的<code>package.json</code>是如下的：可以对其中一些描述信息进行修改</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb29a0a8402c4ff8a997c5fdb6ffc31c~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="p3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="3">
<li>然后在控制台中使用<code>yarn dev</code>运行项目，可以在<a href="https://link.juejin.cn/?target=http%3A%2F%2Flocalhost%3A8080%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://localhost:8080/" ref="nofollow noopener noreferrer">http://localhost:8080/</a> 打开项目网页，查看效果。
此时reco项目的模板样式已经出现，接下来的就是对其进行修改了</li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3ed9ae32c7e44830a4f8c4739c82ab39~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="p4.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="4">
<li>在项目目录层级中有一个<code>.vuepress</code>文件夹，此文件夹是用来存放配置和css\js\img等资源的。内部有<strong>config.ts</strong>配置文件
<strong>config.ts</strong>可以对名称端口等信息进行配置，在<code>export default defineUserConfig</code>中添加：</li>
</ol>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-title function_">defineUserConfig</span>(&#123;
  <span class="hljs-attr">title</span>: <span class="hljs-string">'空城机の博文'</span>,  <span class="hljs-comment">// 名称</span>
  <span class="hljs-attr">description</span>: <span class="hljs-string">'这是使用vuepress-reco进行的第一次配置'</span>,  <span class="hljs-comment">// 描述</span>
  <span class="hljs-attr">dest</span>: <span class="hljs-string">'./dist'</span>,  <span class="hljs-comment">// 打包文件的位置</span>
  <span class="hljs-attr">port</span>: <span class="hljs-number">9074</span>,  <span class="hljs-comment">// 运行端口号</span>
  <span class="hljs-comment">// 添加到html的head顶部的东西</span>
  <span class="hljs-attr">head</span>: [
    [<span class="hljs-string">'link'</span>, &#123; <span class="hljs-attr">rel</span>: <span class="hljs-string">'icon'</span>, <span class="hljs-attr">href</span>: <span class="hljs-string">'./img/icon.svg'</span> &#125;],
    [<span class="hljs-string">'meta'</span>, &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'keywords'</span>, <span class="hljs-attr">content</span>: <span class="hljs-string">'空城机的个人博客网页'</span> &#125;],  
    [<span class="hljs-string">'meta'</span>, &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'description'</span>, <span class="hljs-attr">content</span>: <span class="hljs-string">'空城机的个人博客网页'</span> &#125;],  
    [<span class="hljs-string">'meta'</span>, &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'author'</span>, <span class="hljs-attr">content</span>: <span class="hljs-string">'空城机'</span> &#125;],  
    [<span class="hljs-string">'meta'</span>, &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'robots'</span>, <span class="hljs-attr">content</span>: <span class="hljs-string">'all'</span> &#125;],  
  ],
  <span class="hljs-attr">theme</span>: ...  <span class="hljs-comment">// 主题</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样一来，顶部的<code>title</code>和<code>icon</code>标签页还有运行时端口号和<code>meta</code>这些信息都会修改了</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e1ba4273583e4f4dbd34facaf70f1499~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="p5.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在<code>theme</code>主题的设置文档：<a href="https://link.juejin.cn/?target=http%3A%2F%2Fv2.vuepress-reco.recoluan.com%2Fdocs%2Ftheme%2Fhome.html" target="_blank" rel="nofollow noopener noreferrer" title="http://v2.vuepress-reco.recoluan.com/docs/theme/home.html" ref="nofollow noopener noreferrer">v2.vuepress-reco.recoluan.com/docs/theme/…</a></p>
<h2 data-id="heading-2">模板修改</h2>
<ol>
<li>在之前程序运行的时候，控制台中会出现一个警告，index.css是空的</li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75bb216c89e04536b52ca75574a55ea6~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="p6.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个<code>.temp</code>文件夹是运行之后的配置文件夹，内部的<code>index.css</code>其实是自定义样式的文件，如果想要去除掉此警告，可以在<code>.vuepress/public/styles</code>下创建一个<code>index.css</code>文件，这样重新运行后，就不会出现警告了。
因为之后在<code>.temp/styles</code>文件夹下的<code>index.css</code>文件夹中就会使用<code>@import</code>引入自定义样式文件</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/adce791c04064300ba835c6fcb5e8ab2~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="p7.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>对首页markdown文件进行修改
首页的md文件其实就是项目的<code>README.md</code>文件</li>
</ol>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ba563a2ed1b240e3855c89e44df5b81a~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="p8.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>此文件中有一个被<code>---</code>括起来的模块，这就是配置的地方</p>
<ul>
<li><code>home: true</code>就是在说明这是首页</li>
<li><code>modules</code>：说明页面中有几个模块，分别是顶部的<code>BannerBrand</code>、内容<code>MdContent</code>、底部<code>Footer</code></li>
</ul>
<p>至于之后的配置修改，可以参考：<a href="https://link.juejin.cn/?target=http%3A%2F%2Fv2.vuepress-reco.recoluan.com%2Fdocs%2Ftheme%2Fhome.html" target="_blank" rel="nofollow noopener noreferrer" title="http://v2.vuepress-reco.recoluan.com/docs/theme/home.html" ref="nofollow noopener noreferrer">v2.vuepress-reco.recoluan.com/docs/theme/…</a></p>
<ol start="3">
<li>在首页中，可以配置blog模块。在<code>config.ts</code>文件中可以设置用户名<code>author</code>和用户头像<code>authorAvatar</code>；在<code>README.md</code>文件中，可以设置社交地址<code>socialLinks</code>。</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/839f7caeec334245a896002a4ebb8192~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="p9.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>不过我在设置社交地址时，本来想使用<code>csdn</code>和<code>掘金</code>的地址，但是发现没有图标。一开始我已经从<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.iconfont.cn%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.iconfont.cn/" ref="nofollow noopener noreferrer">阿里巴巴图标矢量库</a> 中找到了这两个图标，并且下载svg了，通过设置<code>icon</code>相对地址的方式，结果发现没有成功。</p>
<p>然后回过头再去看官方文档，发现需要使用的是<strong>Xions</strong>，然后，这个图标库里并没有<code>csdn</code>和<code>掘金</code>的图标。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cab3d65a99514978866cc86e2455923b~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="p10.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样的话，只能我自己手动进行添加了（好麻烦）</p>
<p>其实是对于<code>GitHub</code>图标的仿制，在<strong>Xions</strong>中有一个<code>BrandGithub</code>的图标，那么在<code>node_modules</code>中找到<code>@vicons/tabler</code>文件夹，搜索里面的<code>BrandGithub</code>图标，然后进行仿制。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/491f1a56bb7b481c9719705880de1517~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="p11.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>比如在<code>index.d.ts</code>下的导出示例就可以这样子写：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b452f8f5705493bb439194c243f9b37~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="p12.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>并且可以根据阿里巴巴矢量图标库的图标svg内容，改写出<code>csdn</code>和<code>掘金</code>的图标</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0fc7ac43cc247d9b9a33423c481c150~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="p13.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p><strong>注意</strong>： 这里有一点很重要，我当时写完之后重新运行，发现界面依旧找不到我刚刚添加进去的图标（找了很久原因），浏览器也把缓存给重新清理了，最后发现在项目的<code>.vuepress</code>文件夹中，存在一个<code>.cache</code>缓存文件夹，将其删除后，重新<code>yarn dev</code>运行项目，这样就能够实现效果了。</p>
</blockquote>
<p>至于如果是<code>dark</code>黑暗模式下，在<code>style/index.css</code>中自定义自己想要的颜色，使用<code>fill</code>填充即可</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dec20fce32f5494ba53772bbba404a77~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="p14.png" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<h2 data-id="heading-3">博客添加</h2>
<p>我之前在<code>csdn</code>、<code>掘金</code>这些写作平台写过博客，这次准备先把这些博客文章导下来变成markdown。</p>
<p>这里我使用了<code>csdnsynchexo</code>，支持 csdn/博客园/掘金/segmentfault/腾讯云加社区/github 等平台一键迁移 hexo。</p>
<p>不过虽然说的是支持一键迁移hexo， 但实际上用在<code>vuepress</code>也是一样可行的。(不过对于<code>tags</code>和<code>categories</code>格式需要修改一些，使用列表格式)</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5445bb463c9f45f0a5cafacf0c02bfe7~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="p16.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>npm说明：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fcsdnsynchexo" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/csdnsynchexo" ref="nofollow noopener noreferrer">www.npmjs.com/package/csd…</a></p>
</blockquote>
<p>可以创建一个项目，然后<code>yarn add csdnsynchexo</code>安装</p>
<p>通过创建一个<code>config.json</code>配置文件，因为我爬取的是自己的掘金博客，所以配置如下：</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-punctuation">&#123;</span>
    <span class="hljs-attr">"userId"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"你的掘金id"</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">"type"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"juejin"</span><span class="hljs-punctuation">,</span>
    <span class="hljs-attr">"output"</span><span class="hljs-punctuation">:</span> <span class="hljs-string">"./example"</span>
<span class="hljs-punctuation">&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在控制台中使用命令运行：<code>npx csdnsynchexo@latest --config ./config.json</code></p>
<p>这样即可将博客爬取到<code>example</code>文件夹当中</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0f02b09bd1f74bddb78d1f2880956de9~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="p15.png" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<h2 data-id="heading-4">打包</h2>
<p>如果觉得自己的博客差不多了，那就使用<code>yarn build</code>命令进行打包吧</p>
<h3 data-id="heading-5">TypeError: Invalid value used as weak map key</h3>
<p>然后，我就遇到了一个报错：<code>TypeError: Invalid value used as weak map key</code></p>
<p>上网搜了一下，发现这是由于使用了非标准的html标签，因为<code>vuepress2.x</code>是基于<code>Vue3</code>，校验更加严格，在编译阶段没什么问题，但是打包后就有问题了。比如说<code><font></code>，这样我就全局将<code><font></code>替换成了<code><div></code></p>
<p>然后继续打包，发现还是报此错误，但是因为添加的markdown太多了，就不想管了。直接在对应的报错js位置，添加<code>try catch</code>。让其不阻断打包，可以将打包顺利的完成。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ffa2b3ecca3482b81be20ec5ae4ea98~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="p17.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">Must use import to load ES Module: @vuepress\plugin-back-to-top</h3>
<p>在项目最初的更新包阶段，我也曾遇到过一个问题，使用<code>yarn</code>下载完<code>node_module</code>包之后，使用<code>yarn dev</code>运行，发现报错<code>Must use import to load ES Module: @vuepress\plugin-back-to-top</code></p>
<p>这个问题我本来以为是<code>config.ts</code>配置问题，然后找了好久。后来又以为是<code>markdown</code>格式问题，然后反复去校验。</p>
<p>我的<code>package.json</code>中版本如下：</p>
<ul>
<li>vuepress: 2.0.0-beta.48，</li>
<li>vuepress-theme-reco: 2.0.0-beta.33</li>
</ul>
<p>然后去下载了作者的案例博客： <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Frecoluan%2Frecoluan.github.io" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/recoluan/recoluan.github.io" ref="nofollow noopener noreferrer">github.com/recoluan/re…</a></p>
<p>发现里面<code>yarn</code>安装后是正常的，然后在<code>issues</code>中也发现了关于此问题的讨论，虽然没有结果就是了</p>
<blockquote>
<p>issues地址： <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvuepress-reco%2Fvuepress-theme-reco%2Fissues%2F127" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vuepress-reco/vuepress-theme-reco/issues/127" ref="nofollow noopener noreferrer">github.com/vuepress-re…</a></p>
</blockquote>
<p>不过根据案例中的<code>yarn.lock</code>和我的<code>yarn.lock</code>做对比，发现<code>@vuepress\plugin-back-to-top</code>会有不同</p>
<p>我对一份成功的和一份报此错误的项目<strong>yarn.lock</strong>进行了对比，发现<code>@vuepress/plugin-back-to-top@^2.0.0-beta.48</code>的版本不同，猜测可能是因为这个原因</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/918fd14fbfc84d9084e95ee0ba7919bb~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="p18.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d2357d13a08e4c82913da2de05006d28~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="p19.png" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<h2 data-id="heading-7">发布</h2>
<p>项目打包之后的<code>dist</code>已经出来了，不过查看了一下里面的<code>index.html</code></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/567d33995e5b4c4e80a05d97ca9e37f1~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="p20.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>里面引入的文件都是绝对路径，所以需要发布出去才能查看。这里我是准备发布到<code>github</code>或者<code>gitee</code>的pages中的。不过现在本地IIS中看看。</p>
<h3 data-id="heading-8">本地IIS</h3>
<p>打开IIS的方法：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fjingyan.baidu.com%2Farticle%2Fe9fb46e16aa05c3421f76695.html" target="_blank" rel="nofollow noopener noreferrer" title="https://jingyan.baidu.com/article/e9fb46e16aa05c3421f76695.html" ref="nofollow noopener noreferrer">win10打开IIS</a></p>
<ol>
<li>在网站处选择添加网站</li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ae4000fd3e24db58873f0024d3e66e3~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="p21.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>2.设置网站添加的信息，IP地址如果未分配，将会默认选择本地</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/40521ec370274a1abc350d2cbad4b2e8~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="p22.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="3">
<li>启动网站后，在浏览器中打开<code>http://localhost:8046/</code>，将会打开之前打包的博客项目</li>
</ol>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e5c9070508604619a658d83f4cdf7b13~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="p23.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">Github</h3>
<p>鉴于目前<code>Gitee</code>的pages服务需要开启实名认证，所以先使用<code>Github</code></p>
<p>参考：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fweixin_44240581%2Farticle%2Fdetails%2F121373803" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/weixin_44240581/article/details/121373803" ref="nofollow noopener noreferrer">《发布 VuePress 网站到 github》</a></p>
<p>可以创建一个GitHub的仓库，然后将项目提交到该仓库当中。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/149ee7695f49425a9439455d54848362~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="p24.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>不过当前只有项目的代码，想要将网页<code>dist</code>发布出来，还需要新开一个分支<code>gh-pages</code>，取其他名字也可以。</p>
<p>需要先将<code>dist</code>内容单独提到一个文件夹中，可以添加一个<code>README.md</code>说明</p>
<ol>
<li>
<p><code>git init</code>初始化一下<code>git</code>版本库</p>
</li>
<li>
<p>将要提交的远端仓库关联起来</p>
</li>
</ol>
<ul>
<li>关联命令：<code>git remote add blog-origin 远端仓库地址</code></li>
<li>查看当前的远端仓库：<code>git remote -v</code></li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/714314ed677b49fc85a252de7765553a~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="p31.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="3">
<li>此时可以使用<code>git status</code>命令查看本地仓库状态，会发现当前没有任何提交</li>
</ol>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d0f320cbc95948629dd395c985d00911~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="p25.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="4">
<li>此时使用<code>git add .</code>命令将这些文件添加进入项目的管理队列当中</li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3b9199a687c44125909dc0903c234542~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="p26.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="5">
<li>使用<code>git commit</code>命令将这些加入进来的文件做一次提交
会出现跳转到<code>vim</code>编辑器中，可以添加提交说明
使用<code>shift + ;</code>键，可以输入内容<code>set nu</code>，进入编辑，然后输入提交说明</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5105400fbb554d9b9c2116cad7e3fe67~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="p27.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>添加完说明后，使用<code>Esc</code>退出插入，然后继续使用<code>shift + ;</code>。</p>
<p>输入<code>wq</code>，退出<code>vim编辑器</code>。</p>
<p>这样再次输入<code>git status</code>查看状态，就会发现当前已经没有需要提交的内容了</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/39565e55cbe94dd6901c2f3952d37d99~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="p28.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="6">
<li>因为我要提交的是新分支，而不是默认的<code>master</code>分支，所以需要在本地先创建新分支</li>
</ol>
<ul>
<li>命令：<code>git checkout -b gh-pages</code></li>
<li>查看目前分支: <code>git branch</code></li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d6655e7692f645bdb0d21e5ddf5ffc82~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="p29.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8e18f17af4c741b48bec604c7956b206~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="p30.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="7">
<li>使用命令进行推送，格式是<code>git push --set-upstream 远端 分支名:分支名</code></li>
</ol>
<ul>
<li>命令：<code>git push --set-upstream blog-origin gh-pages:gh-pages</code></li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31f47b2c653d46a4972d4ca74a7609d2~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="p32.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>重新回到<code>github</code>仓库中，发现已经出现新的分支了</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6519f8775e32472287df606a6cee8fd9~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="p33.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p><strong>注意</strong>：推送的过程中可能产生一些失败，我就遇到了<code>Logon failed, use ctrl+c to cancel basic credential prompt.</code>。这其实需要<code>github</code>添加一个<code>token</code>。具体可参考：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Flm_is_dc%2Farticle%2Fdetails%2F120745701" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/lm_is_dc/article/details/120745701" ref="nofollow noopener noreferrer">blog.csdn.net/lm_is_dc/ar…</a></p>
</blockquote>
<ol start="8">
<li>可以去<code>Settings</code>中，选择<code>Pages</code>，然后根据自己的分支，将其保存使用，会自动生成一个网址，可以通过其进行访问了</li>
</ol>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d712564a39b486ba180218f01ca1d09~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="p34.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>目前博客项目就已经挂载到网站上面了，可以通过地址进行访问了</p>
<blockquote>
<p><strong>注意</strong>： 这里可能会遇到一个引入文件路径出错的问题，可以在项目的<code>config.ts</code>文件当中进行解决，通过配置<code>base</code>名为GitHub的仓库名称
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/35834fe8147348a19553c31113c69b09~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="p36.png" loading="lazy" referrerpolicy="no-referrer"></p>
</blockquote></div>  
</div>
            