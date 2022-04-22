
---
title: 'Ember 4.3 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4352'
author: 开源中国
comments: false
date: Fri, 22 Apr 2022 07:15:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4352'
---

<div>   
<div class="content">
                                                                                            <p>Ember 项目近日发布了 Ember.js、Ember Data 和 Ember CLI 的 4.3 版本，各个项目的更新内容如下：</p> 
<h3>Ember.js 4.3 的变化</h3> 
<p>漏洞修复</p> 
<ul> 
 <li>修复了 Router Service 类的内存泄漏，它影响了测试和 FastBoot 应用程序；</li> 
 <li>使用 <code>RouterService#transitionTo</code> 不再在 URL 中添加未指定的默认查询参数；</li> 
 <li><code>FactoryManager</code> 正确地将 <code>props</code> 与 factory 和 owner 相关联</li> 
</ul> 
<h3>Ember Data 4.3 的变化</h3> 
<p>错误修复</p> 
<ul> 
 <li>推送重复标识符的记录不会导致重复记录</li> 
 <li>修复了序列化查询参数时编码空格字符的问题</li> 
 <li>修正了一个回归，当 <code>createRecord</code> 中涉及到设置属性的 setter 时， <code>createRecord</code> 会崩溃</li> 
 <li>修正了一个回归，支持 <code>await</code> 加载关系</li> 
</ul> 
<p>特性</p> 
<ul> 
 <li>当你的应用程序处于 <code>DEBUG</code> 模式时，现在更容易挖掘到 <code>Store</code>、 <code>Symbol</code> 和 <code>RecordReference</code>。</li> 
 <li>增加对 RFC 637 中描述的 Customizeable 测试设置的支持</li> 
 <li>Reference API 现在与 autotracking 兼容</li> 
 <li><code>attributesDefinitionFor</code> 和 <code>relationshipsDefinitionFor</code> 有更简单的 API</li> 
</ul> 
<h3>Ember CLI 4.3 的变化</h3> 
<p>错误修复</p> 
<ul> 
 <li>broccoli debug 文件夹被添加到 <code>gitignore</code> 文件中</li> 
</ul> 
<p>特性</p> 
<ul> 
 <li>可定制的 setupTest 函数</li> 
 <li>增加了对 <code>ember generate</code> 命令指定路径的支持</li> 
</ul> 
<p>弃用</p> 
<ul> 
 <li>弃用了 Bower 支持</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.emberjs.com%2Fember-released-4-3%2F" target="_blank">https://blog.emberjs.com/ember-released-4-3/</a></p>
                                        </div>
                                      
</div>
            