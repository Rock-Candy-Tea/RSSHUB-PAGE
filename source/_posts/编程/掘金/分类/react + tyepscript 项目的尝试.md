
---
title: 'react + tyepscript 项目的尝试'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/029c00fea8834adca7251868ab336171~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 13 Jul 2021 19:20:19 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/029c00fea8834adca7251868ab336171~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">失败记录</h2>
<ul>
<li>关于 <code>react + typescript</code> 项目更新 <code>dependencies</code> 或更新 <code>yarn</code> 都会遇到无法解决的问题</li>
</ul>
<h2 data-id="heading-1">步骤</h2>
<ul>
<li>第一步, 创建项目 <code>npx create-react-app try01 --template typescript</code></li>
<li>第二步，释放 <code>webpack</code> 配置 <code>cd try01 && npm run eject</code></li>
<li>第三步，使用 <code>ncu</code> 升级所有dependencies <code>npx npm-check-udpates -u</code></li>
<li>第四步，将 <code>yarn</code> 升级到 2.x 版本 <code>yarn set version berry</code></li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/029c00fea8834adca7251868ab336171~tplv-k3u1fbpfcp-watermark.image" alt="WeChatWorkScreenshot_178b2213-9e02-4904-9475-8c588dd683ba.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>第五步，安装依赖 <code>yarn</code></li>
<li>第六步，启动项目 -- 已经开始报错了 <code>yarn start</code></li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f6883683a2bf4117a9cc2457732cf28b~tplv-k3u1fbpfcp-watermark.image" alt="WeChatWorkScreenshot_b6bae0eb-21db-45c8-9e96-eb466ee17256.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">End</h2>
<ul>
<li>结束了，暂无法解决，换下一个方案</li>
</ul>
<h2 data-id="heading-3">New Start</h2>
<ul>
<li>上面的第四步跳过，yarn的版本不升级
<ul>
<li><code>yarn v1.22</code> 版本使用ncu升级后依然会报错</li>
<li>解决方案: 进入 <code>webpack.config.js</code>, 找到 <code>new TerserPlugin</code> 删除行 <code>sourceMap: shouldUseSourceMap,</code> 即可</li>
</ul>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e7d84213c1884c6e8ba4cb4564483ef6~tplv-k3u1fbpfcp-watermark.image" alt="WeChatWorkScreenshot_ddcb52ea-fea8-4a09-8200-a0f83f4c2f12.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>持续解决问题中... 无限循环解决问题中...</p>
</li>
<li>
<p>卡在了无法解决的问题上 ...</p>
</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f3d7bac2b4c47d2aa3da636d5addcd2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            