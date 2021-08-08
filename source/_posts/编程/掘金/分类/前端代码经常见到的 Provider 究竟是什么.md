
---
title: '前端代码经常见到的 Provider 究竟是什么'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cb6a20bdfb534ae0975a0c4c18f060bb~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 07 Aug 2021 15:43:41 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cb6a20bdfb534ae0975a0c4c18f060bb~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>不知道你有没有在某处见过 xxProvider，Provider 并不是 23 种经典设计模式之一，但是却应用特别多，可以算是一种比较新的模式。</p>
<ul>
<li>Angular2 中提供了创建对象的时候基于 Provider</li>
<li>VSCode 插件中有各种 registerXxxProvider 的 api</li>
<li>React 提供了 Provider 组件用于 context 数据的传递</li>
</ul>
<p>还有很多别的地方也经常会见到 Provider 的概念，那么 Provider 究竟是什么呢？</p>
<p>本文就来回答下这几个问题：</p>
<ul>
<li>provider 是什么</li>
<li>provider 创建对象和 factory 有什么区别</li>
<li>provider 的具体应用</li>
</ul>
<h2 data-id="heading-0">provider 是什么</h2>
<p>provider 是提供者，从名字上和设计模式中创建对象的那些模式很像，比如工厂方法模式，但其实两者是有区别的。</p>
<p>工厂方法模式是用于创建不同的产品，通过继承的方式。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cb6a20bdfb534ae0975a0c4c18f060bb~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>但有的时候创建的对象可能有别的来源，比如从别的地方获取的一个值，或者已经创建好的对象。这时候来源就不只有工厂了。</p>
<p>也就是说这时候要创建的对象有多种策略，工厂只是其中一种，策略 + 工厂/其他方式就是 Provider。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6eefad54e77f436ea61fd40ab7385730~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>provider 被微软引入到了 .net 2.0，而且微软其他的一些技术产品也随处可以见 provider，比如 VSCode 的 xxxProvider、angular2 的 providers。</p>
<p>我们来看一些具体的应用。</p>
<h2 data-id="heading-1">provider 的具体应用</h2>
<h3 data-id="heading-2">VSCode 插件的 provider 系列 api</h3>
<p>VSCode 插件中最常见的 api 就是 registerXxxProvider，通过该 api 注册的 Provider 就是实现了 provideXxx 的对象。</p>
<p>比如智能补全就是注册一个 CompletionProvider，然后根据 document 的内容，返回具体的 CompletionItem 的对象。</p>
<p>因为 VSCode 并不关心 CompletionItem 是怎么创建出来的，只知道通过这个 provider 可以拿到需要的 completion 数据，所以设计了 provider 的 api。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">const</span> provider = vscode.languages.registerCompletionItemProvider(
        <span class="hljs-string">'plaintext'</span>,
        &#123;
                <span class="hljs-function"><span class="hljs-title">provideCompletionItems</span>(<span class="hljs-params"><span class="hljs-built_in">document</span>: vscode.TextDocument, position: vscode.Position</span>)</span> &#123;
                        <span class="hljs-keyword">return</span> [
                                <span class="hljs-keyword">new</span> vscode.CompletionItem(<span class="hljs-string">'log'</span>, vscode.CompletionItemKind.Method),
                                <span class="hljs-keyword">new</span> vscode.CompletionItem(<span class="hljs-string">'warn'</span>, vscode.CompletionItemKind.Method),
                                <span class="hljs-keyword">new</span> vscode.CompletionItem(<span class="hljs-string">'error'</span>, vscode.CompletionItemKind.Method),
                        ];
                &#125;
        &#125;,
        <span class="hljs-string">'.'</span>
);

context.subscriptions.push(provider);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">React 中的 context 的 Provider</h3>
<p>react 组件树可以在父组件放一些数据到 context 中，然后子组件取出来用，也是通过 provider 的方式。</p>
<p>父组件的作为 Provider 需要实现 getChildContext 方法，返回具体的对象。就像上面的 provideXxx 一样，react 并不关心这个对象是怎么来的。</p>
<p>父组件里提供 getChildContext 提供数据</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Ancestor</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">getChildContext</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123; <span class="hljs-attr">value1</span>: <span class="hljs-string">"context1"</span>, <span class="hljs-attr">value2</span>: <span class="hljs-string">"context2"</span> &#125;;
  &#125;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Parent</span> /></span></span>;
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Parent</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Child</span> /></span></span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>子组件里拿出来</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Child</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.context.value1);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然，react 对上面的流程进行了封装，提供了 React.createContext 的 api 和 Provider、Consumer 组件。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">const</span> Context = React.createContext();

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Child</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Context.Consumer</span>></span>
        &#123;(&#123; value1 &#125;) => &#123;
          console.log(value1);
        &#125;&#125;
      <span class="hljs-tag"></<span class="hljs-name">Context.Consumer</span>></span></span>
    );
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Parent</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Child</span> /></span></span>
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Ancestor</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Context.Provider</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;&#123;</span>
        <span class="hljs-attr">value1:</span> "<span class="hljs-attr">context1</span>"
      &#125;&#125;></span>
        <span class="hljs-tag"><<span class="hljs-name">Parent</span> /></span>
      <span class="hljs-tag"></<span class="hljs-name">Context.Provider</span>></span></span>
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里也是 provider 的思想。</p>
<h3 data-id="heading-4">Angular2 的 providers</h3>
<p>angular 最大的特点就是实现了 ioc，也就是在容器内的对象，可以声明依赖对象，然后用到的时候会自动注入。这个对象的创建方式也是 provider 的形式。</p>
<p>我们知道，provider 并不关心具体对象是怎么创建的，可以动态切换多种创建策略，而 angular2 就提供了 4种策略： Class、Factory、Value、Exsiting</p>
<p>直接值：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-meta">@NgModule</span>(&#123;
  <span class="hljs-attr">providers</span>: [
       &#123; <span class="hljs-attr">provide</span>: <span class="hljs-string">'ggg'</span>, <span class="hljs-attr">useValue</span>: <span class="hljs-string">'guang'</span> &#125;
  ]
&#125;)
<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MainModule</span> </span>&#123; &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>已有的：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-meta">@NgModule</span>(&#123;
  <span class="hljs-attr">providers</span>: [
      &#123; <span class="hljs-attr">provide</span>: <span class="hljs-string">'ggg'</span>, <span class="hljs-attr">useExisting</span>: Guang &#125;
  ]
&#125;)
<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MainModule</span> </span>&#123; &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>类:</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-meta">@Injectable</span>()
<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Guang</span> </span>&#123;
   <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"><span class="hljs-keyword">public</span> name: <span class="hljs-built_in">string</span></span>)</span> &#123;
   &#125;
&#125;
<span class="hljs-meta">@NgModule</span>(&#123;
  <span class="hljs-attr">providers</span>: [
       &#123; <span class="hljs-attr">provide</span>: <span class="hljs-string">'ggg'</span>, <span class="hljs-attr">useClass</span>: Guang&#125;
  ]
&#125;)
<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MainModule</span> </span>&#123; &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>工厂：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">guangFactory</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'guang'</span> &#125;;
&#125;

<span class="hljs-meta">@NgModule</span>(&#123;
  <span class="hljs-attr">providers</span>: [
       &#123; <span class="hljs-attr">provide</span>: <span class="hljs-string">'ggg'</span>, <span class="hljs-attr">useFacotry</span>: guangFactory &#125;
  ]
&#125;)
<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MainModule</span> </span>&#123; &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，angular 提供的 provider 具体的创建策略有好多种，工厂只是其中一种方式，这是 provider 和工厂的区别。</p>
<h2 data-id="heading-5">总结</h2>
<p>provider 是一种创建对象的模式，但是和工厂不同，它是有不同的创建策略的，算是一种复合模式，工厂只是其中一种策略，这种模式在 Angular 的 ioc 创建对象的时候、VSCode 插件注册各种处理函数的时候都有大量应用，还有 React 也基于 Provider 做 context 的传递。</p>
<p>Provider 是各种框架中频繁出现的一个概念，掌握 provider 的思想，对于理解框架还有我们设计代码架构都会有帮助。希望本文能够帮大家理解 Provider。</p>
<p>大家还有没有在别的地方见过 Provider 呢？可以留言交流哦～</p></div>  
</div>
            