
---
title: 'Webpack v5.74.0 已发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5686'
author: 开源中国
comments: false
date: Tue, 26 Jul 2022 07:03:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5686'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#000000">Webpack 是一个模块打包器，主要目的是在浏览器上打包 JavaScript 文件。Webpack v5.74.0 现已发布，具体更新内容如下：</span></p> 
<p style="margin-left:0px"><span style="color:#24292f"><strong>Features</strong></span></p> 
<ul> 
 <li>添加<code>resolve.extensionAlias</code>选项，允许别名扩展名 
  <ul> 
   <li>当你被迫为导入文件添加 .js 扩展名时，这很有用，因为文件真正的扩展名是 .ts（typecript + "type": "module"）。</li> 
  </ul> </li> 
 <li>添加对 ES2022 features 的支持，例如静态块</li> 
 <li>为<code>ProvidePlugin</code>添加 Tree Shaking 支持</li> 
</ul> 
<p style="margin-left:0px"><span style="color:#24292f"><strong>Bug 修复</strong></span></p> 
<ul> 
 <li>当某些构建依赖项位于不同的 Windows 驱动器上时，修复持久缓存</li> 
 <li>在 concatenated 和 non-concatenated 模块之间确定无副作用模块的评估顺序</li> 
 <li>删除 TLA/async 模块运行时代码中的调试遗留问题</li> 
 <li>当文件实际上未被触及时，移除 watching 过程中不需要的额外的 1s 时间戳偏移 
  <ul> 
   <li>这有时会导致额外的第二次构建，而这并不是真正需要的</li> 
  </ul> </li> 
 <li>修复<code>ModuleFederationPlugin</code>的<code>shareScope</code>选项</li> 
 <li>也为同源脚本设置 <span style="color:#24292f"> `"use-credentials"``</span></li> 
</ul> 
<p style="margin-left:0px"><span style="color:#24292f"><strong>Performance</strong></span></p> 
<ul> 
 <li>改善内存的使用和聚合所需文件/目录的性能，以便观察 
  <ul> 
   <li>这会影响 rebuild 的性能</li> 
  </ul> </li> 
</ul> 
<p style="margin-left:0px"><span style="color:#24292f"><strong>Extensibility</strong></span></p> 
<ul> 
 <li>导出<code>HarmonyImportDependency</code>for plugins</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fwebpack%2Fwebpack%2Freleases%2Ftag%2Fv5.74.0" target="_blank">https://github.com/webpack/webpack/releases/tag/v5.74.0</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            