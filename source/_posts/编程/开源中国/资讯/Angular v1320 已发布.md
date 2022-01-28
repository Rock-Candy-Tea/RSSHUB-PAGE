
---
title: 'Angular v13.2.0 已发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7704'
author: 开源中国
comments: false
date: Fri, 28 Jan 2022 07:24:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7704'
---

<div>   
<div class="content">
                                                                                            <p>Angular 是一个基于 TypeScript 的开源前端框架，由 Google 的 Angular 团队以及社区共同领导，从 AngularJS 完全重写而成。</p> 
<p>目前 Angular v13.2.0 已发布，带来如下变更：</p> 
<h3>弃用</h3> 
<ul> 
 <li>弃用 <code>CachedResourceLoader</code> 和 <code>RESOURCE_CACHE_PROVIDER</code> 符号（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fpull%2F44749" target="_blank">#44749</a>）</li> 
 <li>弃用<code>ComponentFactory</code>和<code>ComponentFactoryResolver</code>符号（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fpull%2F44749" target="_blank">#44749</a>）</li> 
 <li>弃用<code>CompilerOptions</code>界面中未使用的配置选项 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fpull%2F44749" target="_blank">#44749</a> )</li> 
</ul> 
<h3><strong>编译器</strong></h3> 
<ul> 
 <li>在模板中添加对安全调用的支持 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fpull%2F44580" target="_blank">#44580</a> )</li> 
 <li>使用注释解析绑定时，显示正确的 span 标签 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fpull%2F44785" target="_blank">#44785</a>)</li> 
 <li>启用覆盖报告时正确编译 DI factories ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fpull%2F44732" target="_blank">#44732</a> )</li> 
</ul> 
<h3><strong>编译器-cli</strong></h3> 
<ul> 
 <li>默认启用扩展诊断 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fpull%2F44712" target="_blank">#44712</a> )</li> 
 <li>为<code>DirectiveMeta</code> 提供动画(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fpull%2F44630" target="_blank">#44630</a>)</li> 
 <li>在索引器中处理<code>ng-template</code>结构指令 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fpull%2F44788" target="_blank">#44788</a> )</li> 
 <li>在模板上正确索引元素（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fpull%2F44785" target="_blank">#44785</a>）</li> 
 <li>删除剩余的<code>_extendedTemplateDiagnostics</code> 要求 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fpull%2F44777" target="_blank">#44777</a> )</li> 
 <li>如果存在配置错误，请跳过 <code>ExtendedTemplateCheckerImpl</code> 构建 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fpull%2F44778" target="_blank">#44778</a> )</li> 
</ul> 
<h3>Core</h3> 
<ul> 
 <li>始终使用命名空间短名称（namespace short name），而不是 URI ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fpull%2F44766" target="_blank">#44766</a> )</li> 
 <li>如果使用 noop 区域调用 NgZone.isInAngularZone ，则会出错 ( <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fpull%2F44800" target="_blank">#44800</a> )</li> 
</ul> 
<h3>表单</h3> 
<ul> 
 <li>允许 FormControl 使用初始值作为默认值。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fpull%2F44434" target="_blank">#44434</a>）</li> 
 <li>进行一些小的修正，以实现类型化表单的前向兼容性。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fpull%2F44540" target="_blank">#44540</a>）</li> 
</ul> 
<h3><strong>语言服务</strong></h3> 
<ul> 
 <li>支持动画自动补全（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fpull%2F44630" target="_blank">#44630</a>）</li> 
</ul> 
<h3><strong>router</strong></h3> 
<ul> 
 <li>允许<code>Route</code><span style="color:#c9d1d9"> </span><code>data</code>和<code>resolve</code>属性的符号键（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fpull%2F44519" target="_blank">#44519</a>）</li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Freleases%2Ftag%2F13.2.0" target="_blank">https://github.com/angular/angular/releases/tag/13.2.0</a></p>
                                        </div>
                                      
</div>
            