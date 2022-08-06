
---
title: 'Parcel 2.7 发布，零配置构建工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9940'
author: 开源中国
comments: false
date: Sat, 06 Aug 2022 07:45:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9940'
---

<div>   
<div class="content">
                                                                                            <p>Parcel 是用于 Web 的零配置构建工具。它将出色的开箱即用开发体验与可扩展的体系结构相结合，可将你的项目从零发展为大规模生产应用程序。</p> 
<p>Parcel 2.7 发布，更新内容如下：</p> 
<h3>新增</h3> 
<ul> 
 <li>Core 
  <ul> 
   <li>为带有 <code>--log-level verbose</code> 的已解析目标添加了调试日志记录</li> 
   <li>允许插件配置以 .cjs 为扩展名编写</li> 
  </ul> </li> 
 <li>JavaScript 
  <ul> 
   <li>为 <code>@emotion/react</code> 添加 react 刷新支持</li> 
   <li>当 html 中只有普通脚本时，为 hmr 注入脚本</li> 
  </ul> </li> 
 <li>Elm 
  <ul> 
   <li>通过 <code>with</code> 查询参数增加对一次编译多个模块的支持</li> 
  </ul> </li> 
 <li>CSS 
  <ul> 
   <li>在 <code>@parcel/transformer-css</code> 中增加对 <code>errorRecovery</code> 选项的支持</li> 
  </ul> </li> 
 <li>实验性捆绑器 
  <ul> 
   <li>实现对多个目标的捆绑</li> 
   <li>内部化异步依赖关系</li> 
   <li>合并相同类型的捆绑程序</li> 
   <li>修复缺失的模块</li> 
  </ul> </li> 
</ul> 
<h3>修复</h3> 
<ul> 
 <li>JavaScript 
  <ul> 
   <li>导入 CommonJS 模块时缺失默认互操作</li> 
   <li>为跳过的资产中的外部依赖添加缺失的导入</li> 
   <li>升级 SWC 以修复未定义的变量</li> 
   <li>从 JS 加载的脚本中移除字符集，以避免在 Firefox 中重复获取</li> 
   <li>替换未使用的符号时使用占位符表达式</li> 
  </ul> </li> 
 <li>Core 
  <ul> 
   <li>解决了在没有文件内容变化的情况下捆绑哈希值的非确定性问题</li> 
   <li>修复 <code>@parcel/package-manager</code> 的 TypeScript 类型</li> 
  </ul> </li> 
 <li>依赖关系 
  <ul> 
   <li>将 terser 升级到 5.14.2</li> 
   <li>将 node-forge 升级到 1.3.0</li> 
  </ul> </li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fparcel-bundler%2Fparcel%2Freleases%2Ftag%2Fv2.7.0" target="_blank">https://github.com/parcel-bundler/parcel/releases/tag/v2.7.0</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            