
---
title: 'PureScript v0.14.4 发布，小巧而强大的静态类型语言'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2071'
author: 开源中国
comments: false
date: Fri, 27 Aug 2021 07:06:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2071'
---

<div>   
<div class="content">
                                                                                            <p>PureScript  v0.14.4 发布了。PureScript 是个小巧而强大的静态类型语言，可以编译成 JavaScript。PureScript 主要是由 Haskell 和 PureScript 编写的。</p> 
<p><strong>Bug 修复：</strong></p> 
<ul> 
 <li> <p>解决当 all 和 right 已经关闭 rows 时，Prim.Row.Union left right all 对 left 的约束（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpurescript%2Fpurescript%2Fpull%2F3720" target="_blank">#3720</a>）。反映现有的函数依赖 all right -> left</p> </li> 
 <li> <p>从文档中排除无趣的 kind sigs 时考虑多余的后缀（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpurescript%2Fpurescript%2Fpull%2F4137" target="_blank">#4137</a>）</p> </li> 
 <li> <p>在外部数据类型声明中添加错误提示（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpurescript%2Fpurescript%2Fpull%2F4161" target="_blank">#4161</a>）</p> </li> 
 <li> <p>捆绑时不要删除函数声明中引用的绑定（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpurescript%2Fpurescript%2Fpull%2F4044" target="_blank">#4044</a>）</p> </li> 
 <li> <p>改进 row type error messages（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpurescript%2Fpurescript%2Fpull%2F4159" target="_blank">＃4159</a>）</p> 
  <ul> 
   <li>删除重复错误类型的冗余提示</li> 
   <li>正确区分包含重复项的 rows</li> 
   <li>从错误行中擦除 kind applications（默认情况下）</li> 
  </ul> </li> 
 <li> <p>修复超类和类型同义词之间的不良交互（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpurescript%2Fpurescript%2Fpull%2F4164" target="_blank">#4164</a>）参见 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpurescript%2Fpurescript%2Fissues%2F4101" target="_blank">#4101</a>。</p> </li> 
 <li> <p>修复 row unification 中的回归（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpurescript%2Fpurescript%2Fpull%2F4168" target="_blank">#4168</a>）</p> </li> 
 <li> <p>修复 backtick operator rule（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpurescript%2Fpurescript%2Fpull%2F4172" target="_blank">＃4172</a>）</p> </li> 
</ul> 
<p><strong>其他改进：</strong></p> 
<ul> 
 <li>在 readme 中添加开发者指南（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpurescript%2Fpurescript%2Fpull%2F3900" target="_blank">＃3900</a>）</li> 
</ul> 
<p><strong>Internal：</strong></p> 
<ul> 
 <li> <p>将未发布的更新日志条目 CHANGELOG.d（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpurescript%2Fpurescript%2Fpull%2F4132" target="_blank">＃4132</a>）</p> </li> 
 <li> <p>在 RELEASE_GUIDE 中明确说明，当发布的版本被破坏时该如何处理（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpurescript%2Fpurescript%2Fpull%2F4147" target="_blank">#4147</a>）</p> </li> 
 <li> <p>发布指南的其他更新/说明（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpurescript%2Fpurescript%2Fpull%2F4131" target="_blank">#4131</a>）</p> </li> 
 <li> <p>在 CI 中运行 Weeder 并 make it happy（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpurescript%2Fpurescript%2Fpull%2F4148" target="_blank">#4148</a>）</p> </li> 
 <li> <p>在类型类声明、种类声明和外部数据类型声明中添加 self cycles 的 golden tests（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpurescript%2Fpurescript%2Fpull%2F4162" target="_blank">#4162</a>）</p> </li> 
 <li> <p>将 class dictionaries 表示为 newtypes（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpurescript%2Fpurescript%2Fpull%2F4125" target="_blank">＃4125</a>）</p> </li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpurescript%2Fpurescript%2Freleases%2Ftag%2Fv0.14.4" target="_blank">https://github.com/purescript/purescript/releases/tag/v0.14.4</a></p>
                                        </div>
                                      
</div>
            