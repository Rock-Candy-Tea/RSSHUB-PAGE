
---
title: 'Webpack 5.69.0 发布，模块打包器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=687'
author: 开源中国
comments: false
date: Fri, 18 Feb 2022 07:05:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=687'
---

<div>   
<div class="content">
                                                                                            <p>webpack 5.69.0 现已发布。webpack 是一个模块打包器，主要目的是在浏览器上打包 JavaScript 文件。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">具体更新内容如下：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><strong>Features</strong></p> 
<ul> 
 <li>启用 ESM 输出模式时自动切换到 ESM 兼容环境</li> 
 <li>在创建上下文模块时处理多个替代目录（e. g. due to resolve.alias or resolve.modules）</li> 
 <li>添加<code>util/types</code>到 node.js 内置模块</li> 
 <li>添加<code>__webpack_exports_info__.<name>.canMangle</code>api</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><strong>Bug 修复</strong></p> 
<ul> 
 <li>修复 chunk graph generation 中的错误，该错误导致模块被包含在 chunk 中，尽管它们已经被包含在 parent chunks 中</li> 
 <li>避免在缓存序列化期间一次写入超过 2GB 的数据（作为 MacOS 上 node.js/libuv 错误的解决方法）</li> 
 <li>修复使用 Module Federation 时对 semver 范围内的空格的处理</li> 
 <li>避免生成仅包含数字的哈希值，因为它们可能与模块 ID 冲突</li> 
 <li>为数据 uri 修复基于资源名称的占位符</li> 
 <li>修复上下文元素的缓存序列化</li> 
 <li>修复在为 ProfilingPlugin 的插件提供工具时传递阶段选项的问题</li> 
 <li>修复跟踪串联模块中的声明，以避免冲突</li> 
 <li>修复不稳定的出口混乱</li> 
 <li>修复 loaders 路径中<code>#</code>的处理问题</li> 
 <li>在使用<code>experiments.buildHttp</code>时避免不必要的缓存更新</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start">更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fwebpack%2Fwebpack%2Freleases%2Ftag%2Fv5.69.0" target="_blank">https://github.com/webpack/webpack/releases/tag/v5.69.0</a></p>
                                        </div>
                                      
</div>
            