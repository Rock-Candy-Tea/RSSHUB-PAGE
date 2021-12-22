
---
title: 'Ember 4.0 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1297'
author: 开源中国
comments: false
date: Wed, 22 Dec 2021 07:56:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1297'
---

<div>   
<div class="content">
                                                                                            <p>Ember 项目发布了 Ember.js、Ember Data 和 Ember CLI 的 4.0 版本。Ember 4.0 版本删除了长期弃用的 API 和对传统平台的支持。</p> 
<p>自 Ember 3.15 以来，Ember "Octane" API 一直是新应用程序的默认配置，根据语义版本的承诺（即 3.xx 版本保持 API 兼容性），该框架此前一直支持 "Classic" 框架特性。再升级 Ember 4.0 之后，新版本放弃了已经过时的 Classic API，但是基础的 <code>EmberComponent</code> 和 <code>EmberObject</code> / <code>computed</code> API 在这个版本中没有被删除。</p> 
<p>Ember 3.28 将成为 Ember 最新的长期支持（LTS）版本。Ember LTS 提供了约 36 周的错误修复支持，以及约 54 周的安全补丁支持。4.0 系列的第一个 LTS 候选版本将会是 Ember 4.4。</p> 
<h3>Ember 的主要版本</h3> 
<p>从 Ember 2.0 开始，Ember 的主要版本都聚焦于移除废弃的 API，而不是引入新的功能或开发样式。Ember 4.0 遵循这一传统，将不包含新的功能。</p> 
<h3>值得注意的变化</h3> 
<p><strong>Ember 4 中的浏览器支持</strong></p> 
<p>Ember 4.0 支持两类浏览器。「Evergreen」（那些以数周为周期，自动升级的浏览器）和「非 Evergreen」。这个分类系统允许我们为前者创建一个滚动更新的最低版本，而对后者使用更传统的、固定的最低版本。</p> 
<p>具体而言，Ember 4.x 的发布政策包括对 Google Chrome、Mozilla Firefox、微软 Edge 和苹果 Safari 在桌面和移动端的支持。它不包括对任何版本的 Internet Explorer 的支持。</p> 
<p>支持的浏览器：</p> 
<ul> 
 <li>Chrome >= 92</li> 
 <li>Edge >= 93</li> 
 <li>Firefox >= 91</li> 
 <li>iOS >= 12</li> 
 <li>Safari >= 12</li> 
 <li>Chrome Android >= 96</li> 
 <li>Firefox Android >= 94</li> 
</ul> 
<h3>Ember.js 4.0 的变化</h3> 
<p>Ember.js 是 Ember 框架的核心。它提供路由、渲染和依赖注入功能。</p> 
<p>Ember.js 4.0 没有引入新的公共 API，主要聚焦于 bug 修复和删除以前 3.x 版本中废弃的公共 API。</p> 
<p>Ember 4.0 并没有删除 <code>EmberComponent</code> API 或 <code>EmberObject</code> 系统的核心部分。这些 API 被广泛使用，甚至在 Octane 发布后，被现有的应用程序和附加组件代码使用。</p> 
<h3>Ember.js 4.0 中删除的 API</h3> 
<ul> 
 <li>移除<code>Ember.Logger</code> ，转而使用本地 <code>console</code> API</li> 
 <li>移除 <code>Copyable</code> mixin，改用 <code>ember-copy</code>插件</li> 
 <li>移除 <code>sendAction</code></li> 
 <li>移除 <code>willTransition</code> 和 <code>didTransition</code></li> 
 <li>计算属性 <code>volatile()</code> 的调用被删除</li> 
 <li><code>this.$()</code> 和其他 jQuery APIs 已经被删除</li> 
 <li>……</li> 
</ul> 
<p>这些被删除的 API 很多都可以追溯到 Ember 1.x。</p> 
<h3>Ember Data 4.0 的变化</h3> 
<p>Ember Data 是 Ember.js 应用程序的官方数据持久化库。这个版本删除了在 3.x 周期中被弃用的 API：</p> 
<ul> 
 <li>移除 <code>store.defaultAdapter</code> API</li> 
 <li>对适配器类型依赖回退行为的支持被移除</li> 
 <li><code>adapter.defaultSerializer</code> 和对序列化器类型的依赖回退行为的支持也被移除</li> 
 <li>移除 Evented API</li> 
 <li>……</li> 
</ul> 
<h3>Ember CLI 4.0 的变化</h3> 
<p>Ember CLI 是用于管理和打包 Ember.js 应用程序的命令行界面。Ember CLI 4.0 中一些值得注意的变化包括：</p> 
<ul> 
 <li>当生成一个新的 Ember 应用程序（ <code>ember new appname</code> ）或插件（ <code>emmber addon addonname</code> ）时，选项 <code>-ci-provider</code> 现在可用。这可以通过 <code>travis</code> 或 <code>github</code> 来生成适当的 CI 配置文件</li> 
 <li>此外，新生成的应用程序和插件的默认 CI 提供程序现在是 GitHub Actions（取代 TravisCI ）</li> 
 <li>Ember CLI 的 <code>EmberApp</code> 接受一个选项 <code>addons</code> 来手动控制哪些已安装的插件将在构建期间运行。该选项中的属性 <code>exclude</code> 和 <code>include</code> 已经被引入，以取代属性 <code>blacklist</code> 和 <code>whiteelist</code>。被替换的属性将继续发挥作用，直到它们在下一个主要发布周期被移除</li> 
 <li>……</li> 
</ul> 
<p>有关 Ember 4.0 的更多变化，可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.emberjs.com%2Fember-4-0-released%2F" target="_blank">https://blog.emberjs.com/ember-4-0-released/</a></p>
                                        </div>
                                      
</div>
            