
---
title: 'Webpack v 5.70.0 已发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1139'
author: 开源中国
comments: false
date: Sat, 05 Mar 2022 07:56:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1139'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">Webpack v<span> </span></span><span style="color:#000000">5.70.0<span> </span></span><span style="color:#333333">发布了！Webpack 是一个常见的静态模块打包工具，主要用途是在浏览器上打包 JavaScript 文件。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">版本主要改动如下：</span></p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><span style="color:#333333">新特性</span></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>更新 ESM 支持的 node.js 版本约束</li> 
 <li>添加<code>baseUri</code>到<code>entry</code>选项，以配置静态基础 uri（基于<span> </span><code>new URL()</code>）</li> 
 <li>尽可能按字母顺序对命名空间对象中的导出进行排序</li> 
 <li>添加<span> </span><code>__webpack_exports_info__.name.canMangle</code></li> 
 <li>添加代理支持到<span> </span><code>experiments.buildHttp</code></li> 
 <li><code>import.meta.webpackContext</code><span> </span>作为 ESM 的替代品添加到<span> </span><code>require.context</code></li> 
 <li>在创建上下文模块时处理多个替代目录</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">修复</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修复<code>global</code>分配给变量时出现的问题</li> 
 <li>修复使用多块<code>experiments.outputModule</code><span> </span>和<span> </span><code>loaderContext.importModule</code><span> </span>时的崩溃</li> 
 <li>避免在编译开始之前生成进度输出（ProgressPlugin）</li> 
 <li>在同一模块中使用 TLA 和 HMR 修复非静态 ESM 依赖项的处理</li> 
 <li>在散列中包含资产模块文件名</li> 
 <li><code>output.clean</code>将保留 HMR 资源至少 10 秒，以允许 HMR 访问它们</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>表现</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修复使用 BannerPlugin 时的资产缓存</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fwebpack%2Fwebpack%2Freleases%2Ftag%2Fv5.70.0" target="_blank">https://github.com/webpack/webpack/releases/tag/v5.70.0</a></p>
                                        </div>
                                      
</div>
            