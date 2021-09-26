
---
title: 'webpack 5.54.0 发布，模块打包器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=444'
author: 开源中国
comments: false
date: Sun, 26 Sep 2021 07:31:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=444'
---

<div>   
<div class="content">
                                                                                            <p>webpack 5.54.0 现已发布。webpack 是一个模块打包器，主要目的是在浏览器上打包 JavaScript 文件。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">具体更新内容如下：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>Features</strong></p> 
<ul> 
 <li>改进常量折叠以允许跳过更多 && || 和 ?? 分支</li> 
 <li>允许在 webpack 中使用所有的 hashing，用<code>output.hashFunction</code>进行配置</li> 
 <li>在模块中使用<code>eval</code>时，不再完全从内部图分析中跳出</li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Bug 修复</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>force bump enhanced - 解决错误的方法</li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong>Performance</strong></p> 
<ul> 
 <li>减少创建 snapshots 时的分配次数</li> 
 <li>添加<code>output.hashFunction: "xxhash64"</code>一个基于 wasm 的超快速哈希函数</li> 
 <li>改进短字符串序列化时的 utf-8 转换</li> 
 <li>提高依赖项的 hashing 性能</li> 
 <li>添加<code>experiments.cacheUnaffected</code>，用户缓存未更改模块的计算并仅引用未更改模块</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fwebpack%2Fwebpack%2Freleases%2Ftag%2Fv5.54.0" target="_blank">https://github.com/webpack/webpack/releases/tag/v5.54.0</a> </p>
                                        </div>
                                      
</div>
            