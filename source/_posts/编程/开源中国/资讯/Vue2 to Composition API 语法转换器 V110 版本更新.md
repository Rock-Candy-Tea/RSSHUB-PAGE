
---
title: 'Vue2 to Composition API 语法转换器 V1.1.0 版本更新'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-bac19f23c0bf0c58421497631789c28319e.png'
author: 开源中国
comments: false
date: Fri, 22 Jul 2022 10:04:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-bac19f23c0bf0c58421497631789c28319e.png'
---

<div>   
<div class="content">
                                                                                            <h1>Vue2 Opitons api to Vue 3 Composition api</h1> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-bac19f23c0bf0c58421497631789c28319e.png" referrerpolicy="no-referrer"></p> 
<h2>在线使用</h2> 
<p><strong>网站</strong></p> 
<p><a href="http://wd3322.gitee.io/to-vue3/">Gitee: vue2-to-composition-api</a></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwd3322.github.io%2Fto-vue3%2F" target="_blank">Github: vue2-to-composition-api</a></p> 
<p><code>vue2-to-composition-api</code> 是一款可以将Options API转换成Composition API的在线应用工具，转换后直接导出 <code>Script setup</code> 内容，帮助Vue2项目减少Options API语法迁移成本</p> 
<p><strong>更新内容</strong></p> 
<ul> 
 <li>修订 Watch 中的 key 值替换精确度</li> 
 <li>修订 Function 中的 key 值替换精确度</li> 
 <li>修订 $refs、$emit 的替换精确度</li> 
 <li>修订 数据类型、数据长度校验</li> 
</ul> 
<p><strong>注意事项</strong></p> 
<ul> 
 <li><code>Template</code> 中的内容不在转换器解析范畴内，需要手工替换 <code>Data</code> 数据源</li> 
 <li><code>Mixin</code>、<code>Component</code> 等外部内容无法被解析，转换前需将其剔除</li> 
 <li>转换后仍然留下 <code>this.</code> 指向的都是未知来源的数据</li> 
 <li>如果你使用了被Vue3废弃的指令，如 <code>$on</code>、<code>$once</code>、<code>$off</code> 等，都需要手工进行移除，转换器仍然会指向vm实例下</li> 
 <li>转化工具在设计思路上，对Vue2.7版本会更加友好，其他问题详见网站文档或本文下方</li> 
</ul>
                                        </div>
                                      
</div>
            