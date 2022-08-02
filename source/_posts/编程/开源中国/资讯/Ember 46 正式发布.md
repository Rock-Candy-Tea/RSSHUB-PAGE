
---
title: 'Ember 4.6 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3518'
author: 开源中国
comments: false
date: Tue, 02 Aug 2022 07:12:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3518'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Ember 项目近日发布了 Ember.js、Ember Data 和 Ember CLI 的 4.6 版本。</p> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start">Ember.js 的变化</h2> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Ember.js 4.6 是一个增量的、向后兼容的 Ember 版本，并进行了 bug 修复。</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">漏洞修复</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Ember.js 4.6 引入了 2 个 bug 修复：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>用<span> </span><code>substring()</code><span> </span>方法替换已弃用的<span> </span><code>substr()</code><span> </span>方法</li> 
 <li>调整<span> </span><code>uniqueId()</code><span> </span>实现，只生成有效的选择器。<span> </span><code>querySelector</code><span> </span>在第一个字符是数字的情况下不工作，所以现在我们确保第一个字符是字母。</li> 
</ul> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start">Ember Data 的变化</h2> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">Node 支持</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Ember Data 4.6 放弃了对 Node 12 的支持，Node 12 在 2022 年 4 月达到生命周期结束。</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">错误修复</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Ember Data 4.6 引入了 9 个错误修复:</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>将空数组项目序列化为空字符串</li> 
 <li><code>waiter</code><span> </span>应始终处于开启状态</li> 
 <li>清理<span> </span><code>RecordState</code></li> 
 <li>调度<span> </span><code>watchTypeIfUnseen</code><span> </span>以防止循环</li> 
 <li>修复 addons 中测试设置函数的生成导入路径</li> 
 <li>修复保存的<span> </span><code>PromiseProxy</code><span> </span>弃用问题</li> 
 <li>测试<span> </span><code>async hasMany</code><span> </span>时不触发关系获取</li> 
 <li>归一化时向<span> </span><code>keyFor<Attribute|Relationship></code><span> </span>传递正确的 args</li> 
 <li>修复了 async hasMany 加载时计算链不更新的问题</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">特性</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Ember Data 4.6 引入了对构建大小的改进。</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">弃用</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">新的弃用情况如下，对弃用 API 的支持将在 Ember 的下一个主要版本中删除。</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>弃用 RSVP.Promise 的一些内部用法</li> 
 <li>弃用快照上的<span> </span><code>type</code><span> </span>属性</li> 
 <li>弃用<span> </span><code>store.find</code></li> 
 <li>弃用<span> </span><code>store.hasRecordForId</code>，因为<span> </span><code>peekRecord</code><span> </span>通常更有用，提供相同的信息（甚至更多）。</li> 
 <li>弃用<span> </span><code>store.recordWasInvalid</code>，这是一个未使用的内部 api</li> 
 <li>弃用<span> </span><code>attributesDefinitionFor</code><span> </span>和<span> </span><code>relationshipDefinitionFor</code></li> 
 <li>弃用<span> </span><code>json-api</code></li> 
</ul> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start">Ember CLI 的变化</h2> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">Node 支持</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Ember CLI 放弃了对 Node 12 的支持，增加了对 Node 18 的支持。Node 12 在 2022 年 4 月达到生命周期结束。</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">弃用</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Ember CLI 4.6 引入了 1 个弃用：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><code>vendor-shim</code><span> </span>蓝图已被弃用，请使用<span> </span><code>ember-auto-import</code><span> </span>代替</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.emberjs.com%2Fember-4-6-released%2F" target="_blank">https://blog.emberjs.com/ember-4-6-released/</a></p>
                                        </div>
                                      
</div>
            