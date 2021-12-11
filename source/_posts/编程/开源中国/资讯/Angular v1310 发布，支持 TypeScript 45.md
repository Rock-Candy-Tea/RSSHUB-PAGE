
---
title: 'Angular v13.1.0 发布，支持 TypeScript 4.5'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5061'
author: 开源中国
comments: false
date: Sat, 11 Dec 2021 07:08:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5061'
---

<div>   
<div class="content">
                                                                                            <div style="margin-left:0; margin-right:0"> 
 <div style="margin-left:0; margin-right:0"> 
  <div style="margin-left:0; margin-right:0"> 
   <p style="margin-left:0; margin-right:0">Angular 是一个基于 TypeScript 的开源前端框架，由 Google 的 Angular 团队以及社区共同领导，从 AngularJS 完全重写而成。</p> 
   <p style="margin-left:0; margin-right:0">Angular v13.1.0 已发布，此版本主要更新内容如下：</p> 
   <ul style="margin-left:0; margin-right:0"> 
    <li>弃用基于 NgModule<span> </span><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292f">factories</span><span> </span>的<span> </span><code>downgradeModule</code><span> </span>函数签名（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fpull%2F44090" target="_blank">#44090</a>）</li> 
    <li>支持 NgModule 类作为<span> </span><code>downgradeModule</code><span> </span>函数的参数(<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fpull%2F43973" target="_blank">#43973</a><span> </span>)</li> 
   </ul> 
   <p style="margin-left:0; margin-right:0">已弃用基于<span> </span><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292f">NgModule factories 的<span> </span></span><code>downgradeModule</code><span> </span>函数调用，改用基于 NgModule 类的<span> </span><code>downgradeModule</code><span> </span>调用。</p> 
   <ul style="margin-left:0; margin-right:0"> 
    <li><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292f"><code>TestRequest</code><span> </span>的 XHR errors 错误类型不正确 (</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fpull%2F36082" target="_blank">#36082</a><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292f">)</span></li> 
   </ul> 
   <p style="margin-left:0; margin-right:0">来自<span> </span><code>@angular/common/http/testing</code><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292f"><span> </span>的</span><span data-darkreader-inline-color style="--darkreader-inline-color:#c9c5be; color:#2e3033">测试请求（</span><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292f"><code>TestRequest</code>）在</span><span data-darkreader-inline-color style="--darkreader-inline-color:#c9c5be; color:#2e3033">模拟 XHR 错误时不再接受<span> </span></span><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292f"><code>ErrorEvent</code></span>，取而代之的是传递<span> </span><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292f"><code>ProgressEvent</code><span> </span>实例，以</span><span data-darkreader-inline-color style="--darkreader-inline-color:#c9c5be; color:#2e3033">匹配本地浏览器的行为。</span></p> 
   <ul style="margin-left:0; margin-right:0"> 
    <li><span data-darkreader-inline-color style="--darkreader-inline-color:#c9c5be; color:#2e3033">减少 ngFor 指令的代码大小<span> </span></span><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292f">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fpull%2F44315" target="_blank">#44315</a><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292f">)</span></li> 
    <li>从占位符中引用 ICU 消息 ID (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fpull%2F43534" target="_blank">#43534</a><span> </span>)</li> 
    <li>添加迁移以移除<span data-darkreader-inline-color style="--darkreader-inline-color:#c9c5be; color:#2e3033">输入组件（</span><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292f">entryComponents） </span><span> </span><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292f">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fpull%2F44308" target="_blank">#44308</a><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292f">) (</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fpull%2F44322" target="_blank">#44322</a><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292f">)</span></li> 
    <li><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292f"><strong>支持 TypeScript 4.5</strong><span> </span>(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fpull%2F44164" target="_blank">#44164</a><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292f">)</span></li> 
    <li>向<span> </span><code>HttpContext</code><span> </span>类添加<span> </span><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292f"><code>has()</code></span><span> </span>方法（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fpull%2F43887" target="_blank">#43887</a>）</li> 
    <li>支持占位符的“关联消息 ID”（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fpull%2F43534" target="_blank">#43534</a>）</li> 
    <li>正确解决 UMD 依赖项 (<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fpull%2F44381" target="_blank">#44381</a><span> </span>)</li> 
   </ul> 
   <p style="margin-left:0; margin-right:0">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Freleases%2Ftag%2F13.1.0" target="_blank">https://github.com/angular/angular/releases/tag/13.1.0</a></p> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            