
---
title: 'Angular v13.0.1 发布，修复若干 bug'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5497'
author: 开源中国
comments: false
date: Fri, 12 Nov 2021 06:42:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5497'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Angular 是一个基于 TypeScript 的开源前端框架，由 Google 的 Angular 团队以及社区共同领导，从 AngularJS 完全重写而成的。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Angular v13.0.1 已发布，此版本修复了 13.0.0 版本带来的若干 bug，主要内容如下：</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>compiler</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>确保部分编译的查询可以处理前向引用。（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fpull%2F44113" target="_blank">#44113</a>）</li> 
 <li>为安全的方法调用生成正确的代码。 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fpull%2F44088" target="_blank">#44088</a><span> </span>)</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>compiler-cli</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>禁用<strong><span> </span></strong><code>strictNullInputTypes</code><span> </span>类型时，确保文字类型被保留。(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fpull%2F38305" target="_blank">#38305</a>)</li> 
 <li>检查版本时正确处理预发布版本。(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fpull%2F44109" target="_blank">#44109</a>)</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>core</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>不在开发模式下使用函数构造器，以免违反 CSP 。(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fpull%2F43587" target="_blank">#43587</a>)</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>platform-browser</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>在 Animation<span> </span><code>removecchild</code><span> </span>回调中使用正确的父节点。(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fpull%2F44033" target="_blank">#44033</a>)</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#2e3033">更新公告：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Freleases%2Ftag%2F13.0.1" target="_blank">https://github.com/angular/angular/releases/tag/13.0.1</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            