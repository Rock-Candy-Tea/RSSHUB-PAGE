
---
title: 'babel7 的配置，整合 react 和 ts'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/043189bc706245ab87443f8fb914251c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 24 Jul 2021 01:18:21 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/043189bc706245ab87443f8fb914251c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>babel7 开始核心带了@，话不多说，走一波，试试看</p>
<h4 data-id="heading-0">1.起步</h4>
<blockquote>
<p>npm install @babel/core @babel/cli @babel/preset-env -D</p>
</blockquote>
<blockquote>
<p>npm install --save @babel/polyfill -S (已经作废)</p>
</blockquote>
<h4 data-id="heading-1">2.babel.config.js</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/043189bc706245ab87443f8fb914251c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>@babel/core   babel核心包</li>
<li>@babel/cli    babel工具包</li>
<li>@babel/preset-env 包含了 es 转换的所有 plugin。预设就是一个plugin集合。*</li>
<li>@babel/polyfill 就是 es 方法的垫片，比如 es6 里面的数组有 map() 方法，但是不支持 es 的浏览器就不支持这个方法，那就用 polyfill 垫片铺平这个差异，当前，polyfill已经作废了。因为 他会将所有的东西一次性全部导入。当前有很多浏览器的新版本都开始支持 es6 里面的新特性了，如果你依旧全量导入垫片，就显得很啰嗦。此时就出来了 runtime。</li>
<li>在配置里面 "useBuiltIns": "usage", "corejs": 3，就表示引入了 @babel/polyfill</li>
</ul>
<blockquote>
<p>npm i @babel/plugin-transform-runtime -D</p>
</blockquote>
<blockquote>
<p>npm install @babel/runtime -S</p>
</blockquote>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b68f0aec06244e7d9f8d7cd31995e261~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上面这个才是最终解法。</p>
<h4 data-id="heading-2">@babel/plugin-transform-runtime比@babel/polyfill的优势如下：</h4>
<ul>
<li>可以结合配置 corejs: 3 来实现按需加载，来减少打包数量。</li>
<li>不会污染全局变量。</li>
<li>实现了对辅助函数的服用，来解决转义语法出现的代码冗余。</li>
</ul></div>  
</div>
            