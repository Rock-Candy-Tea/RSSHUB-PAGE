
---
title: 'Ant Design Mobile 5.0.0-alpha.19 发布，AntD 移动端设计规范'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5683'
author: 开源中国
comments: false
date: Tue, 24 Aug 2021 07:29:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5683'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Ant Design Mobile 5.0.0-alpha.19 发布了。Ant Design Mobile 即 Ant Design 移动端设计规范，<code>antd-mobile</code> 是 Ant Design 的移动规范的 React 实现，服务于蚂蚁及口碑无线业务。</p> 
<p>更新内容如下：</p> 
<ul> 
 <li><strong>优化</strong> 
  <ul> 
   <li>NoticeBar <code>type</code> 属性改为 <code>color</code>，<code>default</code> 调整为灰色，增加 <code>alert</code> 配色 </li> 
   <li>Toast 的 <code>success</code> <code>fail</code> <code>loading</code> 方法合并到 <code>show</code> 方法中 </li> 
   <li>Toast 移除了 <code>updateConfig</code> 返回函数 </li> 
   <li><code>Toast.show</code> 支持了直接传入 <code>string</code> 作为参数</li> 
   <li>调整了多个组件的受控和非受控模式的判断逻辑</li> 
   <li>Form 和 List 的部分间距微调</li> 
  </ul> </li> 
</ul> 
<p><strong>迁移建议</strong></p> 
<ul> 
 <li>NoticeBar 之前的 <code>default</code> 配色现在改为了 <code>alert</code>，需要显式地进行设置，所以需要把之前的 <code><NoticeBar /></code> 改为 <code><NoticeBar color='alert' /></code></li> 
 <li>Toast 不再返回 <code>updateConfig</code> 函数，所以需要去掉对应的依赖（如果遇到用法上的问题可以创建一条 Discussion）</li> 
 <li>Toast 之前有 <code>show</code> <code>success</code> <code>fail</code> <code>loading</code> 四个方法，现在都合并到 <code>show</code> 一个方法中了，具体的用法可以参考最新版的文档</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fant-design%2Fant-design-mobile%2Freleases%2Ftag%2Fv5.0.0-alpha.19" target="_blank">https://github.com/ant-design/ant-design-mobile/releases/tag/v5.0.0-alpha.19</a></p>
                                        </div>
                                      
</div>
            