
---
title: '【Angular教程】-内容投影_@ContentChild_@ViewChild'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/680467778e1a4694b57e85a503707721~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image'
author: 掘金
comments: false
date: Wed, 04 Aug 2021 08:16:27 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/680467778e1a4694b57e85a503707721~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto;border:3px solid rgba(62,175,124,.2)&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-weight:700;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-radius:6px;border:2px solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c&#125;.markdown-body a:active,.markdown-body a:hover&#123;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a:before&#123;content:"⇲"&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(62,175,124,.2)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:.5rem solid;border-color:#42b983;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none&#125;.markdown-body ul li:before&#123;content:"•";margin-right:4px;color:#3eaf7c&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第4天，活动详情查看：</strong><a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></p>
<h3 data-id="heading-0">前言</h3>
<p>这一篇我们带来的是关于组件基础使用的最后一块,内容投影和Vue中的插槽很类似,在组件封装的时候非常有用,我们一起来体验一下。</p>
<h3 data-id="heading-1">正文</h3>
<h4 data-id="heading-2">1. 投影一块内容</h4>
<ol>
<li><strong>容器组件这样写</strong></li>
</ol>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
  编号1
  <span class="hljs-tag"><<span class="hljs-name">ng-content</span>></span><span class="hljs-tag"></<span class="hljs-name">ng-content</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li><strong>业务组件这样用</strong></li>
</ol>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">app-page-container</span>></span>
未指定投影位置的内容会被投影到无select属性的区域
<span class="hljs-tag"></<span class="hljs-name">app-page-container</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">2. 投影多块内容/组件</h4>
<ol>
<li><strong>容器组件这样写</strong>
<ol>
<li>使用标签锁定投影位置</li>
<li>使用class锁定投影位置</li>
<li>用自定义组件名称锁定投影位置</li>
<li>使用自定义属性锁定投影位置</li>
</ol>
</li>
</ol>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
  编号2
  <span class="hljs-tag"><<span class="hljs-name">ng-content</span> <span class="hljs-attr">select</span>=<span class="hljs-string">"h3"</span>></span><span class="hljs-tag"></<span class="hljs-name">ng-content</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">ng-content</span> <span class="hljs-attr">select</span>=<span class="hljs-string">".my-class"</span>></span><span class="hljs-tag"></<span class="hljs-name">ng-content</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">ng-content</span> <span class="hljs-attr">select</span>=<span class="hljs-string">"app-my-hello"</span>></span><span class="hljs-tag"></<span class="hljs-name">ng-content</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">ng-content</span> <span class="hljs-attr">select</span>=<span class="hljs-string">"[content]"</span>></span><span class="hljs-tag"></<span class="hljs-name">ng-content</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li><strong>业务组件这样用</strong></li>
</ol>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">app-page-container</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">h3</span>></span>使用标签锁定投影位置<span class="hljs-tag"></<span class="hljs-name">h3</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"my-class"</span>></span>使用class锁定投影位置<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">app-my-hello</span>></span>使用自定义组件名称锁定投影位置<span class="hljs-tag"></<span class="hljs-name">app-my-hello</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">content</span>></span>使用自定义属性锁定投影位置<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">app-page-container</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li><strong>演示</strong></li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/680467778e1a4694b57e85a503707721~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-4">3. 投影子元素</h4>
<blockquote>
<p>使用<code>ng-container</code>来包裹子元素,减少不必要的dom层,类似vue中的template</p>
</blockquote>
<ol>
<li><strong>容器组件这样写</strong></li>
</ol>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
  编号4
  <span class="hljs-tag"><<span class="hljs-name">ng-content</span> <span class="hljs-attr">select</span>=<span class="hljs-string">"question"</span>></span><span class="hljs-tag"></<span class="hljs-name">ng-content</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li><strong>业务组件这样写</strong></li>
</ol>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">app-page-container</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">ng-container</span> <span class="hljs-attr">ngProjectAs</span>=<span class="hljs-string">"question"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>内容投影酷吗?<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>内容投影酷吗?<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>内容投影酷吗?<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>内容投影酷吗?<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">ng-container</span>></span>
<span class="hljs-tag"></<span class="hljs-name">app-page-container</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">4. 有条件的内容投影</h4>
<blockquote>
<p>中文网的描述:</p>
<ol>
<li>如果你的组件需要_<strong>有条件地</strong>_渲染内容或多次渲染内容，则应配置该组件以接受一个 ng-template 元素，其中包含要有条件渲染的内容。</li>
<li>在这种情况下，不建议使用 ng-content 元素，因为只要组件的使用者提供了内容，即使该组件从未定义 ng-content 元素或该 ng-content 元素位于 <a href="https://link.juejin.cn/?target=http%3A%2F%2Fangular.cn%2Fapi%2Fcommon%2FNgIf" target="_blank" rel="nofollow noopener noreferrer" title="http://angular.cn/api/common/NgIf" ref="nofollow noopener noreferrer">ngIf</a> 语句的内部，该内容也总会被初始化。</li>
<li>使用 ng-template 元素，你可以让组件根据你想要的任何条件显式渲染内容，并可以进行多次渲染。在显式渲染 ng-template 元素之前，Angular 不会初始化该元素的内容。</li>
</ol>
</blockquote>
<ol>
<li><strong>使用<code>ng-container</code>定义我们的投影区块</strong>
<ol>
<li>使用<code>ngTemplateOutlet</code>指令来渲染<code>ng-template</code>元素。</li>
<li>通过内置的动态指令<code>*ngIf</code>来控制是否渲染投影。</li>
</ol>
</li>
</ol>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
  编号3
  <span class="hljs-tag"><<span class="hljs-name">ng-content</span> <span class="hljs-attr">select</span>=<span class="hljs-string">"[button]"</span>></span><span class="hljs-tag"></<span class="hljs-name">ng-content</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">p</span> *<span class="hljs-attr">ngIf</span>=<span class="hljs-string">"expanded"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">ng-container</span> [<span class="hljs-attr">ngTemplateOutlet</span>]=<span class="hljs-string">"content.templateRef"</span>></span> <span class="hljs-tag"></<span class="hljs-name">ng-container</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li><strong>在业务组件中我们使用<code>ng-template</code>来包裹我们的实际元素。</strong></li>
</ol>
<blockquote>
<p>my-hello组件只在ngOnInit()做日志输出来观察打印情况。</p>
</blockquote>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">app-page-container</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">appToggle</span>></span>切换<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">ng-template</span> <span class="hljs-attr">appContent</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">app-my-hello</span>></span>有条件的内容投影~<span class="hljs-tag"></<span class="hljs-name">app-my-hello</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">ng-template</span>></span>
<span class="hljs-tag"></<span class="hljs-name">app-page-container</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li><strong>现在你会发现页面并没有像前面那么顺利的正常渲染,因为我们的逻辑还没有串通,我们继续。创建一个指令,并在NgModule中注册,一定要注册才能用哦~</strong></li>
</ol>
<blockquote>
<p>指令需要注册哦~</p>
</blockquote>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">import</span> &#123; Directive, TemplateRef &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@angular/core'</span>;

<span class="hljs-meta">@Directive</span>(&#123;
  <span class="hljs-attr">selector</span>: <span class="hljs-string">'[appContent]'</span>,
&#125;)
<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ContentDirective</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"><span class="hljs-keyword">public</span> templateRef: TemplateRef<unknown></span>)</span> &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li><strong>我们再定义一个指令来控制组件中显示/隐藏的标识</strong></li>
</ol>
<blockquote>
<p>指令需要注册哦~</p>
</blockquote>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-meta">@Directive</span>(&#123;
  <span class="hljs-attr">selector</span>: <span class="hljs-string">'[appToggle]'</span>,
&#125;)
<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ToggleDirective</span> </span>&#123;
  <span class="hljs-meta">@HostListener</span>(<span class="hljs-string">'click'</span>) <span class="hljs-function"><span class="hljs-title">toggle</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.app.expanded = !<span class="hljs-built_in">this</span>.app.expanded;
  &#125;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"><span class="hljs-keyword">public</span> app: PageContainerComponent</span>)</span> &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li><strong>在我们的容器组件中申明刚才定义的内容指令,页面目前不报错咯~</strong></li>
</ol>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">PageContainerComponent</span> <span class="hljs-title">implements</span> <span class="hljs-title">OnInit</span> </span>&#123;

  <span class="hljs-attr">expanded</span>: <span class="hljs-built_in">boolean</span> = <span class="hljs-literal">false</span>;

  <span class="hljs-meta">@ContentChild</span>(ContentDirective)
  content!: ContentDirective;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="6">
<li><strong>通过日志可以看到我们在切换容器组件的<code>expanded</code>标识时,只有开启状态<code>my-hello</code>组件才会初始化,下面的这个<code>ngIf</code>虽然在页面看不到渲染的内容,但组件实实在在被初始化过了。</strong></li>
</ol>
<pre><code class="hljs language-typescript copyable" lang="typescript"><div *ngIf=<span class="hljs-string">"false"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">ng-content</span> *<span class="hljs-attr">ngIf</span>=<span class="hljs-string">"false"</span> <span class="hljs-attr">select</span>=<span class="hljs-string">"app-my-hello"</span>></span><span class="hljs-tag"></<span class="hljs-name">ng-content</span>></span></span>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>​</p>
<h4 data-id="heading-6">5. @ContentChild & @ContentChildren</h4>
<blockquote>
<p>使用这两个装饰器来对被投影的组件进行操作</p>
</blockquote>
<ol>
<li><strong>使用注解在业务组件中定义被投影的组件</strong></li>
</ol>
<pre><code class="hljs language-html copyable" lang="html">@ContentChild(HelloWorldComp)
helloComp: HelloWorldComp;

@ContentChildren(HelloWorldComp)
helloComps: QueryList<span class="hljs-tag"><<span class="hljs-name">HelloWorldComp</span>></span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li><strong>在<code>ngAfterContentInit()</code>钩子执行后对被投影组件进行操作</strong></li>
</ol>
<h4 data-id="heading-7">6. @ViewChild & @ViewChildren</h4>
<blockquote>
<p>使用这两个装饰器来对指接子组件进行操作</p>
</blockquote>
<ol>
<li><strong>使用注解在业务组件中定义子组件</strong></li>
</ol>
<pre><code class="hljs language-html copyable" lang="html">@ViewChild(HelloWorldComp)
helloComp: HelloWorldComp;
  
@ViewChildren(HelloWorldComp)
helloComps QueryList<span class="hljs-tag"><<span class="hljs-name">HelloWorldComp</span>></span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li><strong>在<code>ngAfterViewInit()</code>钩子执行后对直接子组件进行操作</strong></li>
</ol>
<h3 data-id="heading-8">结语</h3>
<p>关于组件的使用我们就先写到这里了,文笔功底有限,加油了~,下一篇打算写写自定义指令的使用。</p></div>  
</div>
            