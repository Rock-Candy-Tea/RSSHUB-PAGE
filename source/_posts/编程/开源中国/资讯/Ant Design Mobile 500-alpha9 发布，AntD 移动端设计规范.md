
---
title: 'Ant Design Mobile 5.0.0-alpha.9 发布，AntD 移动端设计规范'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6640'
author: 开源中国
comments: false
date: Thu, 12 Aug 2021 07:25:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6640'
---

<div>   
<div class="content">
                                                                                            <p>Ant Design Mobile 5.0.0-alpha.9 发布了。Ant Design Mobile 即 Ant Design 移动端设计规范，<code>antd-mobile</code> 是 Ant Design 的移动规范的 React 实现，服务于蚂蚁及口碑无线业务。</p> 
<p>更新内容如下：</p> 
<ul> 
 <li>优化 
  <ul> 
   <li>默认字号调整为 13px</li> 
   <li>DesensText 命名调整为 DesenseText，相关的属性也从 desens 调整为 desense</li> 
  </ul> </li> 
 <li>修复 
  <ul> 
   <li>修复了 DesenseText 在部分情况下图标变化有延迟的 bug</li> 
   <li>修复了由于 convertPx 计算有误导致的部分组件样式异常的 bug</li> 
   <li>修复了样式文件引入时，由于根目录下 assets 缺失导致的报错 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fissues%2F3884" target="_blank">#3884</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Fissues%2F3885" target="_blank">#3885</a></li> 
  </ul> </li> 
</ul> 
<p>迁移建议</p> 
<ul> 
 <li>检查是否使用了 DesensText 组件，如有的话需要同步调整一下命名</li> 
 <li>由于默认字号发生了变化，需要留意一下项目中的页面样式和布局是否有异常</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Freleases%2Ftag%2Fv5.0.0-alpha.9" target="_blank">https://github.com/ant-design/ant-design-mobile/releases/tag/v5.0.0-alpha.9</a> </p>
                                        </div>
                                      
</div>
            