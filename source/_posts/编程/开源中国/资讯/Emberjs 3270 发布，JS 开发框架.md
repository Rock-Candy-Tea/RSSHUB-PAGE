
---
title: 'Ember.js 3.27.0 发布，JS 开发框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9296'
author: 开源中国
comments: false
date: Wed, 05 May 2021 07:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9296'
---

<div>   
<div class="content">
                                                                                            <p>Ember.js 是一个 JavaScript 框架，可大大减少构建任何 Web 应用程序所需的时间、精力和资源。它致力于通过执行大多数 Web 开发项目中涉及的所有常见、重复但必不可少的任务，使开发者尽可能地高效。</p> 
<p>Ember 框架的一个有价值的属性是它使用语义版本控制来帮助项目跟上框架的变化。在删除任何功能或 API 之前，它首先会经过一个弃用期，在该期间内仍支持该功能，但是使用该功能会生成一条警告，并记录到浏览器控制台中。</p> 
<p>以下是 Ember.js 3.27.0 版本更新的内容：</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Femberjs%2Fember.js%2Fpull%2F19309" target="_blank">#19309</a> / <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Femberjs%2Fember.js%2Fpull%2F19487" target="_blank">#19487</a> / <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Femberjs%2Fember.js%2Fpull%2F19474" target="_blank">#19474</a> [FEATURE] 根据 RFC #432 启用 <code>(helper</code> 和 <code>(modifier</code> 帮助器；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Femberjs%2Fember.js%2Fpull%2F19382" target="_blank">#19382</a> / <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Femberjs%2Fember.js%2Fpull%2F19430" target="_blank">#19430</a> [FEATURE] 根据 RFC #671 进行剩余的实施工作；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Femberjs%2Fember.js%2Fpull%2F19457" target="_blank">#19457</a> / <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Femberjs%2Fember.js%2Fpull%2F19463" target="_blank">#19463</a> / <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Femberjs%2Fember.js%2Fpull%2F19464" target="_blank">#19464</a> / <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Femberjs%2Fember.js%2Fpull%2F19467" target="_blank">#19467</a> [DEPRECATION] 根据 RFC #706，为 Ember Global 添加弃用；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Femberjs%2Fember.js%2Fpull%2F19407" target="_blank">#19407</a> [DEPRECATION] 根据 RFC #491 添加 <code>Route#disconnectOutlet</code> 的弃用；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Femberjs%2Fember.js%2Fpull%2F19433" target="_blank">#19433</a> [DEPRECATION] 根据 RFC #418 添加 <code>Route#renderTemplate</code> 的弃用；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Femberjs%2Fember.js%2Fpull%2F19442" target="_blank">#19442</a> [DEPRECATION] 根据 RFC #418 添加 <code>Route#render</code> 方法的弃用；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Femberjs%2Fember.js%2Fpull%2F19429" target="_blank">#19429</a> [DEPRECATION] <code>registerPlugin</code> / <code>unregisterPlugin</code> 和基于传统类的 AST 插件（私有 API）；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Femberjs%2Fember.js%2Fpull%2F19499" target="_blank">#19499</a> [DEPRECATION] 根据 RFC #496 弃用 <code>@foo=&#123;&#123;helper&#125;&#125;</code></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Femberjs%2Fember.js%2Fpull%2F19499" target="_blank">#19499</a> [BUGFIX] 更新渲染引擎至 <code>@glimmer/*</code> 0.78.2 以修复包括： 
  <ul> 
   <li><code><:else></code> 和 <code><:inverse></code> 应该是别名；</li> 
   <li>修复了动态帮助器中对帮助器的嵌套调用；</li> 
  </ul> </li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Femberjs%2Fember.js%2Fpull%2F19477" target="_blank">#19477</a> [BUGFIX] 允许 <code><LinkToExternal /></code> 覆盖内部断言；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Femberjs%2Fember.js%2Fpull%2F19481" target="_blank">#19481</a> [BUGFIX] 从正确的路径导出 <code>on</code> ；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Femberjs%2Fember.js%2Fpull%2F19466" target="_blank">#19466</a> [BUGFIX] 重命名私有的 runloop 函数；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Femberjs%2Fember.js%2Fpull%2F19384" target="_blank">#19384</a> 在帮助器和组件测试蓝图中使用qunit-dom；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Femberjs%2Fember.js%2Fpull%2F19390" target="_blank">#19390</a> 重构内部 Ember 加载器，使用标准 Ember CLI 加载器；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Femberjs%2Fember.js%2Fpull%2F19441" target="_blank">#19441</a> 在 NPM 中增加自动发布每周 alpha 版本的功能；</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Femberjs%2Fember.js%2Fpull%2F19462" target="_blank">#19462</a> 在 <code>ember g helper</code> 蓝图中使用 <code>positional</code> 和 <code>named</code> 作为参数名称；</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Femberjs%2Fember.js%2Freleases%2Ftag%2Fv3.27.0" target="_blank">https://github.com/emberjs/ember.js/releases/tag/v3.27.0</a></p>
                                        </div>
                                      
</div>
            