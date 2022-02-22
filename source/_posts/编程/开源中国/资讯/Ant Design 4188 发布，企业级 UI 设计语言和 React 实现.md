
---
title: 'Ant Design 4.18.8 发布，企业级 UI 设计语言和 React 实现'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9973'
author: 开源中国
comments: false
date: Tue, 22 Feb 2022 07:04:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9973'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#000000">Ant Design 4.18.8 现已发布，主要变化如下：</span></p> 
<ul> 
 <li>修复 <code>message.config</code> 多次配置 <code>getContainer</code> 时无法生效的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34123" target="_blank">#34123</a> </li> 
 <li>修复 Menu 组件中无效的缓存逻辑。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34121" target="_blank">#34121</a> </li> 
 <li>修复 ConfigProvider 在服务端配置主题会崩溃的问题，同时现在会提示动态主题于 SSR 上无效。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34118" target="_blank">#34118</a></li> 
 <li>Table 
  <ul> 
   <li>修复 Table 在首次加载时会渲染两次的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34106" target="_blank">#34106</a></li> 
   <li>优化 Table 渲染性能，现在不使用废弃 <code>column.render: () => &#123; children, props &#125;</code> 方法时默认会跳过无用渲染。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34075" target="_blank">#34075</a></li> 
  </ul> </li> 
 <li>修复 Typography 启用 <code>copyable</code> 时 <code>children</code> 内容变化后复制内容没变的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34034" target="_blank">#34034</a> </li> 
 <li>优化 Avatar、List、Pagination、Steps 以防止初始化时非必要的额外渲染。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34122" target="_blank">34122</a></li> 
 <li>修复 Form 下 Select 内容太长导致布局换行的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34117" target="_blank">#34117</a></li> 
 <li>完善 <code>sk-SK</code> 中 Table、Form、Modal 的文案。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34061" target="_blank">#34061</a> </li> 
 <li>TypeScript 
  <ul> 
   <li>导出 Layout 组件的 <code>SiderProps</code> 类型。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Fpull%2F34137" target="_blank">#34137</a> </li> 
  </ul> </li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design%2Freleases%2Ftag%2F4.18.8" target="_blank">https://github.com/ant-design/ant-design/releases/tag/4.18.8</a></p>
                                        </div>
                                      
</div>
            