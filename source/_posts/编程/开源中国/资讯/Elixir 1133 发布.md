
---
title: 'Elixir 1.13.3 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6675'
author: 开源中国
comments: false
date: Fri, 25 Feb 2022 07:11:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6675'
---

<div>   
<div class="content">
                                                                                            <p>Elixir 是一种动态的函数式语言，旨在构建可扩展和可维护的应用程序。Elixir 1.13.3 正式发布，更新内容如下：</p> 
<h2>增强</h2> 
<h3>Mix</h3> 
<ul> 
 <li>[mix format] 为格式化插件提供文件和行</li> 
 <li>[mix format] 支持在格式化插件中嵌入Elixir表达式。</li> 
</ul> 
<h2>错误修复</h2> 
<h3>Elixir</h3> 
<ul> 
 <li>[Code] 修复重复的绑定在评估过程中导致的错误</li> 
 <li>[Kernel] 确保存储在 Documentation 块中的签名不包含新行</li> 
 <li>[Kernel] 修正在编译具有递归映射访问的守护时的无限循环</li> 
 <li>[Macro] 修正在给定普通别名 <code>Elixir</code> 时 <code>Macro.to_string/1</code> 的错误</li> 
 <li>[String] 修正 <code>String.split_at/2</code> 中某些代码点组合的错误。</li> 
</ul> 
<h3>Mix</h3> 
<ul> 
 <li>[mix compile] 从依赖项导出时重新编译项目文件</li> 
 <li>[mix test] 修复总覆盖率即使高于阈值也始终显示为红色的问题</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felixir-lang%2Felixir%2Freleases%2F" target="_blank">https://github.com/elixir-lang/elixir/releases/</a></p>
                                        </div>
                                      
</div>
            