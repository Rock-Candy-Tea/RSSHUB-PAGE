
---
title: 'Webpack 5.67.0 发布，模块打包器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2068'
author: 开源中国
comments: false
date: Wed, 26 Jan 2022 07:07:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2068'
---

<div>   
<div class="content">
                                                                                            <p>webpack 5.67.0 现已发布。webpack 是一个模块打包器，主要目的是在浏览器上打包 JavaScript 文件。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">具体更新内容如下：</p> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong>Features</strong></p> 
<ul> 
 <li>为资源资产模块添加“outputPath”配置选项</li> 
 <li>在 eval source maps 中支持 Trusted Types</li> 
 <li><code>experiments.css</code> 
  <ul> 
   <li>允许只为节点中的 css 生成导出</li> 
   <li>添加<code>SyncModuleIdsPlugin</code>，在服务器和客户端编译中同步模块 ID</li> 
   <li>为<code>DeterministicModuleIdsPlugin</code>添加更多选项，以允许生成相同的 id</li> 
  </ul> </li> 
</ul> 
<p style="margin-left:0px; margin-right:0px; text-align:start"><strong>Developer Experience</strong></p> 
<ul> 
 <li>在统计打印机中限制数据 url 模块名称</li> 
 <li>允许 CLI 选项的特定描述</li> 
 <li>改进统计打印中的空间限制算法以显示部分列表</li> 
 <li>在回调中为添加<code>null</code></li> 
 <li>修复 addChunkInGroup 的调用签名类型</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#24292f"><strong>Bug 修复</strong></span></p> 
<ul> 
 <li>避免将不存在的 package.jsons 报告为依赖项</li> 
 <li><code>experiments.css</code> 
  <ul> 
   <li>修复仅使用初始 css 时缺少 css 运行时的问题</li> 
   <li>修复 css hmr 支持</li> 
   <li>对 CSS 模块的错误修复</li> 
  </ul> </li> 
 <li>修复 CreateScriptUrlDependency 的缓存序列化问题</li> 
 <li>修复加载器处理时的 data url 内容</li> 
 <li>修复标识符中包括<code>|</code>的 regexp</li> 
 <li>修复监控场景下的 ProfilingPlugin 问题</li> 
 <li>将 layer 添加到模块名称和标识符 
  <ul> 
   <li>这样可以避免在将其他模块添加到另一层时随机更改模块 ID</li> 
  </ul> </li> 
 <li>向 DependencyTemplates 提供 hashFunction 参数以允许在那里对其进行自定义</li> 
 <li>在启用 Experiments.lazyCompilation 时修复 HMR</li> 
 <li>将 url 存储为 Buffer 以避免序列化警告</li> 
 <li><code>webpack-hot-middleware/client</code>从惰性编译中排除</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fwebpack%2Fwebpack%2Freleases%2Ftag%2Fv5.67.0" target="_blank">https://github.com/webpack/webpack/releases/tag/v5.67.0</a></p>
                                        </div>
                                      
</div>
            