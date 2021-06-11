
---
title: 'Angular表单'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2727'
author: 掘金
comments: false
date: Fri, 11 Jun 2021 00:24:40 GMT
thumbnail: 'https://picsum.photos/400/300?random=2727'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">Angular 表单简介</h2>
<p>用表单处理用户输入是许多常见应用的基础功能。 应用通过表单来让用户登录、修改个人档案、输入敏感信息以及执行各种数据输入任务。</p>
<p>Angular 提供了两种不同的方法来通过表单处理用户输入：<strong>响应式表单</strong>和<strong>模板驱动表单</strong>。 两者都从视图中捕获用户输入事件、验证用户输入、创建表单模型、修改数据模型，并提供跟踪这些更改的途径。</p>
<p>本文提供的信息可以帮你确定哪种方式最适合你的情况。它介绍了这两种方法所用的公共构造块，还总结了两种方式之间的关键区别，并在建立、数据流和测试等不同的情境下展示了这些差异。</p>
<h2 data-id="heading-1">选择一种方法</h2>
<p>响应式表单和模板驱动表单以不同的方式处理和管理表单数据。每种方法都有各自的优点。</p>
<ul>
<li>
<p><strong>响应式表单</strong>提供对底层表单对象模型直接、显式的访问。它们与模板驱动表单相比，更加健壮：它们的可扩展性、可复用性和可测试性都更高。如果表单是你的应用程序的关键部分，或者你已经在使用响应式表单来构建应用，那就使用响应式表单。</p>
</li>
<li>
<p><strong>模板驱动表单</strong>依赖<strong>模板中</strong>的指令来创建和操作底层的对象模型。它们对于向应用添加一个简单的表单非常有用，比如电子邮件列表注册表单。它们很容易添加到应用中，但在扩展性方面不如响应式表单。如果你有可以只在模板中管理的非常基本的表单需求和逻辑，那么模板驱动表单就很合适。</p>
</li>
</ul>
<h3 data-id="heading-2">关键差异</h3>
<p>下表总结了响应式表单和模板驱动表单之间的一些关键差异。</p>






























<table><thead><tr><th></th><th>响应式</th><th>模板驱动</th></tr></thead><tbody><tr><td>建立表单模型</td><td>显式的，在组件类中创建</td><td>隐式的，由指令创建</td></tr><tr><td>数据模型</td><td>结构化和不可变的</td><td>非结构化和可变的</td></tr><tr><td>建立表单模型</td><td>同步</td><td>异步</td></tr><tr><td>建立表单模型</td><td>函数</td><td>指令</td></tr></tbody></table>
<h3 data-id="heading-3">可伸缩性</h3>
<p>如果表单是应用程序的核心部分，那么可伸缩性就非常重要。能够跨组件复用表单模型是至关重要的。</p>
<p>响应式表单比模板驱动表单更有可伸缩性。它们提供对底层表单 API 的直接访问，并且在视图和数据模型之间使用同步数据流，从而可以更轻松地创建大型表单。响应式表单需要较少的测试设置，测试时不需要深入理解变更检测，就能正确测试表单更新和验证。</p>
<p>模板驱动表单专注于简单的场景，可复用性没那么高。它们抽象出了底层表单 API，并且在视图和数据模型之间使用异步数据流。对模板驱动表单的这种抽象也会影响测试。测试程序非常依赖于手动触发变更检测才能正常运行，并且需要进行更多设置工作。</p>
<h2 data-id="heading-4">建立表单模型</h2>
<p>响应式表单和模板驱动型表单都会跟踪用户与之交互的表单输入元素和组件模型中的表单数据之间的值变更。这两种方法共享同一套底层构建块，只在如何创建和管理常用表单控件实例方面有所不同。</p>
<h3 data-id="heading-5">常用表单基础类</h3>
<p>响应式表单和模板驱动表单都建立在下列基础类之上。</p>
<ul>
<li>
<p>FormControl 实例用于追踪单个表单控件的值和验证状态。</p>
</li>
<li>
<p>FormGroup 用于追踪一个表单控件组的值和状态。</p>
</li>
<li>
<p>FormArray 用于追踪表单控件数组的值和状态。</p>
</li>
<li>
<p>ControlValueAccessor 用于在 Angular 的 FormControl 实例和原生 DOM 元素之间创建一个桥梁。</p>
</li>
</ul>
<h3 data-id="heading-6">建立响应式表单</h3>
<p>对于响应式表单，你可以直接在组件类中定义表单模型。[formControl] 指令会通过内部值访问器来把显式创建的 FormControl 实例与视图中的特定表单元素联系起来。</p>
<p>下面的组件使用响应式表单为单个控件实现了一个输入字段。在这个例子中，表单模型是 FormControl 实例。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; Component &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@angular/core'</span>;
<span class="hljs-keyword">import</span> &#123; FormControl &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@angular/forms'</span>;

<span class="hljs-meta">@Component</span>(&#123;
  <span class="hljs-attr">selector</span>: <span class="hljs-string">'app-reactive-favorite-color'</span>,
  <span class="hljs-attr">template</span>: <span class="hljs-string">`
    Favorite Color: <input type="text" [formControl]="favoriteColorControl">
  `</span>
&#125;)
<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">FavoriteColorComponent</span> </span>&#123;
  favoriteColorControl = <span class="hljs-keyword">new</span> FormControl(<span class="hljs-string">''</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">建立模板驱动表单</h3>
<p>在模板驱动表单中，表单模型是隐式的，而不是显式的。指令 NgModel 为指定的表单元素创建并管理一个 FormControl 实例。</p>
<p>下面的组件使用模板驱动表单为单个控件实现了同样的输入字段。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; Component &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@angular/core'</span>;

<span class="hljs-meta">@Component</span>(&#123;
  <span class="hljs-attr">selector</span>: <span class="hljs-string">'app-template-favorite-color'</span>,
  <span class="hljs-attr">template</span>: <span class="hljs-string">`
    Favorite Color: <input type="text" [(ngModel)]="favoriteColor">
  `</span>
&#125;)
<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">FavoriteColorComponent</span> </span>&#123;
  favoriteColor = <span class="hljs-string">''</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            