
---
title: 'Ember 4.4 发布，包含 Ember.js、Ember CLI 和 Ember Data'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5470'
author: 开源中国
comments: false
date: Tue, 31 May 2022 07:29:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5470'
---

<div>   
<div class="content">
                                                                                            <p>近日 Ember 项目发布了 Ember.js、Ember Data 和 Ember CLI 的 4.4 版本，各个项目的更新内容如下：</p> 
<h2>Ember.js 4.4 的变化</h2> 
<p>Ember.js 4.4 是一个增量的、向后兼容的 Ember 版本。</p> 
<h3>特性</h3> 
<p>Ember.js 4.4 引入了 4 个特性：</p> 
<ul> 
 <li>在新的 Ember 应用程序中， <code>&#123;&#123;unique-id&#125;&#125;</code> 帮助器将被默认包含。开发者可以使用这个助手来生成一个唯一的 ID 字符串，适合作为 DOM 中的 ID 属性使用</li> 
 <li>当一个废止设置了 until 字段时，它现在将与其他信息一起被记录下来</li> 
 <li>现在可以定制 <code>setupTest*</code> 函数了</li> 
 <li><code>hasListeners</code> 函数现在是公开的，所以你可以在调用 <code>removeListeners</code> 之前调用它</li> 
</ul> 
<h2>Ember Data 4.4 的变化</h2> 
<h3>弃用</h3> 
<p>Ember Data 4.4 引入了 1 个弃用：</p> 
<ul> 
 <li><code>Model.save()</code> 将返回一个本地的 <code>Promise</code> 而不是 <code>PromiseProxyMixin</code>。要返回一个 <code>Promise</code>，你可以设置你的 <code>compatWith</code> 为 4.4。</li> 
</ul> 
<p>对 Ember Data 记录的 <code>toJSON</code> 方法的支持已被删除，它此前已在 3.x 中被弃用。</p> 
<h2>Ember CLI 4.4 的变化</h2> 
<h3>错误修复</h3> 
<p>Ember CLI 4.4 引入了 3 个错误修复：</p> 
<ul> 
 <li>更新 <code>since.available</code> 和 <code>since.enabled</code> 版本，以适应 Bower 的废弃</li> 
 <li>修复附加组件 <code>.gitignore</code> 文件的内容</li> 
 <li>附加组件的 README 现在将使用更标准的 Markdown 作为 headers</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.emberjs.com%2Fember-released-4-4%2F" target="_blank">https://blog.emberjs.com/ember-released-4-4/</a></p>
                                        </div>
                                      
</div>
            