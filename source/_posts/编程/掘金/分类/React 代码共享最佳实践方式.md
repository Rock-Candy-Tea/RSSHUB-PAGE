
---
title: 'React 代码共享最佳实践方式'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2126'
author: 掘金
comments: false
date: Tue, 11 May 2021 03:56:41 GMT
thumbnail: 'https://picsum.photos/400/300?random=2126'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>任何一个项目发展到一定复杂性的时候，必然会面临逻辑复用的问题。在<code>React</code>中实现逻辑复用通常有以下几种方式：<code>Mixin</code>、<code>高阶组件(HOC)</code>、<code>修饰器(decorator)</code>、<code>Render Props</code>、<code>Hook</code>。本文主要就以上几种方式的优缺点作分析，帮助开发者针对业务场景作出更适合的方式。</p>
<h2 data-id="heading-0">Mixin</h2>
<p>这或许是刚从<code>Vue</code>转向<code>React</code>的开发者第一个能够想到的方法。<code>Mixin</code>一直被广泛用于各种面向对象的语言中，<strong>其作用是为单继承语言创造一种类似多重继承的效果</strong>。虽然现在<code>React</code>已将其放弃中，但<code>Mixin</code>的确曾是<code>React</code>实现代码共享的一种设计模式。</p>
<p>广义的 mixin 方法，就是用赋值的方式将 mixin 对象中的方法都挂载到原对象上，来实现对象的混入，类似 ES6 中的 Object.assign()的作用。原理如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> mixin = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">obj, mixins</span>) </span>&#123;
  <span class="hljs-keyword">const</span> newObj = obj
  newObj.prototype = <span class="hljs-built_in">Object</span>.create(obj.prototype)

  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> prop <span class="hljs-keyword">in</span> mixins) &#123;
    <span class="hljs-comment">// 遍历mixins的属性</span>
    <span class="hljs-keyword">if</span> (mixins.hasOwnPrototype(prop)) &#123;
      <span class="hljs-comment">// 判断是否为mixin的自身属性</span>
      newObj.prototype[prop] = mixins[prop]; <span class="hljs-comment">// 赋值</span>
    &#125;
  &#125;
  <span class="hljs-keyword">return</span> newObj
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">在 React 中使用 Mixin</h3>
<p>假设在我们的项目中，多个组件都需要设置默认的<code>name</code>属性，使用<code>mixin</code>可以使我们不必在不同的组件里写多个同样的<code>getDefaultProps</code>方法，我们可以定义一个<code>mixin</code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> DefaultNameMixin = &#123;
  <span class="hljs-attr">getDefaultProps</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">name</span>: <span class="hljs-string">"Joy"</span>
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为了使用<code>mixin</code>，需要在组件中加入<code>mixins</code>属性，然后把我们写好的<code>mixin</code>包裹成一个数组，将它作为<code>mixins</code>的属性值：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> ComponentOne = React.createClass(&#123;
  <span class="hljs-attr">mixins</span>: [DefaultNameMixin]
  <span class="hljs-attr">render</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h2</span>></span>Hello &#123;this.props.name&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span></span>
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>写好的<code>mixin</code>可以在其他组件里重复使用。</strong></p>
<p>由于<code>mixins</code>属性值是一个数组，意味着我们<strong>可以同一个组件里调用多个<code>mixin</code></strong>。在上述例子中稍作更改得到：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> DefaultFriendMixin = &#123;
  <span class="hljs-attr">getDefaultProps</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">friend</span>: <span class="hljs-string">"Yummy"</span>
    &#125;
  &#125;
&#125;

<span class="hljs-keyword">const</span> ComponentOne = React.createClass(&#123;
  <span class="hljs-attr">mixins</span>: [DefaultNameMixin, DefaultFriendMixin]
  <span class="hljs-attr">render</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>Hello &#123;this.props.name&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>This is my friend &#123;this.props.friend&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>我们甚至可以在一个<code>mixin</code>里包含其他的<code>mixin</code></strong>。</p>
<p>比如写一个新的<code>mixin``DefaultProps</code>包含以上的<code>DefaultNameMixin</code>和<code>DefaultFriendMixin </code>：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> DefaultPropsMixin = &#123;
  <span class="hljs-attr">mixins</span>: [DefaultNameMixin, DefaultFriendMixin]
&#125;

<span class="hljs-keyword">const</span> ComponentOne = React.createClass(&#123;
  <span class="hljs-attr">mixins</span>: [DefaultPropsMixin]
  <span class="hljs-attr">render</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>Hello &#123;this.props.name&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>This is my friend &#123;this.props.friend&#125;<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>至此，我们可以总结出<code>mixin</code>至少拥有以下优势:</p>
<ul>
<li><strong>可以在多个组件里使用相同的<code>mixin</code></strong>；</li>
<li><strong>可以在同一个组件里使用多个<code>mixin</code></strong>；</li>
<li><strong>可以在同一个<code>mixin</code>里嵌套多个<code>mixin</code></strong>；</li>
</ul>
<p>但是在不同场景下，优势也可能变成劣势：</p>
<ul>
<li><strong>破坏原有组件的封装，可能需要去维护新的<code>state</code>和<code>props</code>等状态</strong>；</li>
<li><strong>不同<code>mixin</code>里的命名不可知，非常容易发生冲突</strong>；</li>
<li><strong>可能产生递归调用问题，增加了项目复杂性和维护难度</strong>；</li>
</ul>
<p>除此之外，<code>mixin</code>在状态冲突、方法冲突、多个生命周期方法的调用顺序等问题拥有自己的处理逻辑。感兴趣的同学可以参考一下以下文章：</p>
<ul>
<li><a href="https://segmentfault.com/a/1190000003016446" target="_blank" rel="nofollow noopener noreferrer">React Mixin 的使用</a></li>
<li><a href="https://reactjs.org/blog/2016/07/13/mixins-considered-harmful.html" target="_blank" rel="nofollow noopener noreferrer">Mixins Considered Harmful</a></li>
</ul>
<h2 data-id="heading-2">高阶组件</h2>
<p>由于<code>mixin</code>存在上述缺陷，故<code>React</code>剥离了<code>mixin</code>，改用<code>高阶组件</code>来取代它。</p>
<p><strong><code>高阶组件</code>本质上是一个函数，它接受一个组件作为参数，返回一个新的组件</strong>。</p>
<p><code>React</code>官方在实现一些公共组件时，也用到了<code>高阶组件</code>，比如<code>react-router</code>中的<code>withRouter</code>，以及<code>Redux</code>中的<code>connect</code>。在这以<code>withRouter</code>为例。</p>
<p>默认情况下，必须是经过<code>Route</code>路由匹配渲染的组件才存在<code>this.props</code>、才拥有<code>路由参数</code>、才能使用<code>函数式导航</code>的写法执行<code>this.props.history.push('/next')</code>跳转到对应路由的页面。<code>高阶组件</code>中的<code>withRouter</code>作用是将一个没有被<code>Route</code>路由包裹的组件，包裹到<code>Route</code>里面，从而将<code>react-router</code>的三个对象<code>history</code>、<code>location</code>、<code>match</code>放入到该组件的<code>props</code>属性里，因此能实现<code>函数式导航跳转</code>。</p>
<p><code>withRouter</code>的实现原理：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> withRouter = <span class="hljs-function">(<span class="hljs-params">Component</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> displayName = <span class="hljs-string">`withRouter(<span class="hljs-subst">$&#123;Component.displayName || Component.name&#125;</span>)`</span>
  <span class="hljs-keyword">const</span> C = <span class="hljs-function"><span class="hljs-params">props</span> =></span> &#123;
    <span class="hljs-keyword">const</span> &#123; wrappedComponentRef, ...remainingProps &#125; = props
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">RouterContext.Consumer</span>></span>
        &#123;context => &#123;
          invariant(
            context,
            `You should not use <$&#123;displayName&#125; /></span> outside a <Router><span class="hljs-string">`
          );
          return (
            <Component
              &#123;...remainingProps&#125;
              &#123;...context&#125;
              ref=&#123;wrappedComponentRef&#125;
            />
          )
        &#125;&#125;
      </RouterContext.Consumer>
    )
&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>使用代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; Component &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>
<span class="hljs-keyword">import</span> &#123; withRouter &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react-router"</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TopHeader</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        导航栏
        &#123;/* 点击跳转login */&#125;
        <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.exit&#125;</span>></span>退出<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
  &#125;

  exit = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// 经过withRouter高阶函数包裹，就可以使用this.props进行跳转操作</span>
    <span class="hljs-built_in">this</span>.props.history.push(<span class="hljs-string">"/login"</span>)
  &#125;
&#125;
<span class="hljs-comment">// 使用withRouter包裹组件，返回history,location等</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> withRouter(TopHeader)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于<code>高阶组件</code>的本质是<code>获取组件并且返回新组件的方法</code>，所以理论上它也可以像<code>mixin</code>一样实现多重嵌套。</p>
<p>例如：</p>
<p>写一个赋能唱歌的高阶函数</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; Component &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>

<span class="hljs-keyword">const</span> widthSinging = <span class="hljs-function"><span class="hljs-params">WrappedComponent</span> =></span> &#123;
<span class="hljs-keyword">return</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">HOC</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
<span class="hljs-title">constructor</span> (<span class="hljs-params"></span>) &#123;
<span class="hljs-built_in">super</span>(...arguments)
<span class="hljs-built_in">this</span>.singing = <span class="hljs-built_in">this</span>.singing.bind(<span class="hljs-built_in">this</span>)
&#125;

singing = <span class="hljs-function">() =></span> &#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'i am singing!'</span>)
&#125;

<span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
<span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">WrappedComponent</span> /></span></span>
&#125;
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>写一个赋能跳舞的高阶函数</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; Component &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>

<span class="hljs-keyword">const</span> widthDancing = <span class="hljs-function"><span class="hljs-params">WrappedComponent</span> =></span> &#123;
<span class="hljs-keyword">return</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">HOC</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
<span class="hljs-title">constructor</span> (<span class="hljs-params"></span>) &#123;
<span class="hljs-built_in">super</span>(...arguments)
<span class="hljs-built_in">this</span>.dancing = <span class="hljs-built_in">this</span>.dancing.bind(<span class="hljs-built_in">this</span>)
&#125;

dancing = <span class="hljs-function">() =></span> &#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'i am dancing!'</span>)
&#125;

<span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
<span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">WrappedComponent</span> /></span></span>
&#125;
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用以上高阶组件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; Component &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>
<span class="hljs-keyword">import</span> &#123; widthSing, widthDancing &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"hocs"</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Joy</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>Joy<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  &#125;
&#125;

<span class="hljs-comment">// 给Joy赋能唱歌和跳舞的特长</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> widthSinging(withDancing(Joy))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由上可见，只需使用高阶函数进行简单的包裹，就可以把原本单纯的 Joy 变成一个既能唱歌又能跳舞的夜店小王子了！</p>
<h3 data-id="heading-3">使用 HOC 的约定</h3>
<p>在使用<code>HOC</code>的时候，有一些墨守成规的约定：</p>
<ul>
<li>将不相关的 Props 传递给包装组件（传递与其具体内容无关的 props）；</li>
<li>分步组合（避免不同形式的 HOC 串联调用）；</li>
<li>包含显示的 displayName 方便调试（每个 HOC 都应该符合规则的显示名称）；</li>
<li>不要在<code>render</code>函数中使用高阶组件（每次 render，高阶都返回新组件，影响 diff 性能）；</li>
<li>静态方法必须被拷贝（经过高阶返回的新组件，并不会包含原始组件的静态方法）；</li>
<li>避免使用 ref（ref 不会被传递）;</li>
</ul>
<h3 data-id="heading-4">HOC 的优缺点</h3>
<p>至此我们可以总结一下<code>高阶组件(HOC)</code>的优点：</p>
<ul>
<li><code>HOC</code>是一个纯函数，便于使用和维护；</li>
<li>同样由于<code>HOC</code>是一个纯函数，支持传入多个参数，增强其适用范围；</li>
<li><code>HOC</code>返回的是一个组件，可组合嵌套，灵活性强；</li>
</ul>
<p>当然<code>HOC</code>也会存在一些问题：</p>
<ul>
<li>当多个<code>HOC</code>嵌套使用时，无法直接判断子组件的<code>props</code>是从哪个<code>HOC</code>负责传递的；</li>
<li>当父子组件有同名<code>props</code>，会导致父组件覆盖子组件同名<code>props</code>的问题，且<code>react</code>不会报错，开发者感知性低；</li>
<li>每一个<code>HOC</code>都返回一个新组件，从而产生了很多无用组件，同时加深了组件层级，不便于排查问题；</li>
</ul>
<p><code>修饰器</code>和<code>高阶组件</code>属于同一模式，在此不展开讨论。</p>
<h2 data-id="heading-5">Render Props</h2>
<p><strong><code>Render Props</code>是一种非常灵活复用性非常高的模式，它可以把特定行为或功能封装成一个组件，提供给其他组件使用让其他组件拥有这样的能力</strong>。</p>
<blockquote>
<p>The term “render prop” refers to a technique for sharing code between React components using a prop whose value is a function.</p>
</blockquote>
<p>这是<code>React</code>官方对于<code>Render Props</code>的定义，翻译成大白话即：“<code>Render Props</code>是实现<code>React Components</code>之间代码共享的一种技术，组件的<code>props</code>里边包含有一个<code>function</code>类型的属性，组件可以调用该<code>props</code>属性来实现组件内部渲染逻辑”。</p>
<p>官方示例：</p>
<pre><code class="hljs language-js copyable" lang="js"><DataProvider render=&#123;<span class="hljs-function">(<span class="hljs-params">data</span>) =></span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Hello &#123;data.target&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>&#125; />
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上，<code>DataProvider</code>组件拥有一个叫做<code>render</code>（也可以叫做其他名字）的<code>props</code>属性，该属性是一个函数，并且这个函数返回了一个<code>React Element</code>，在组件内部通过调用该函数来完成渲染，那么这个组件就用到了<code>render props</code>技术。</p>
<p>读者或许会疑惑，“我们为什么需要调用<code>props</code>属性来实现组件内部渲染，而不直接在组件内完成渲染”？借用<code>React</code>官方的答复，<code>render props</code>并非每个<code>React</code>开发者需要去掌握的技能，甚至你或许永远都不会用到这个方法，但它的存在的确为开发者在思考组件代码共享的问题时，提供了多一种选择。</p>
<h3 data-id="heading-6"><code>Render Props</code>使用场景</h3>
<p>我们在项目开发中可能需要频繁的用到弹窗，弹窗 UI 可以千变万化，但是功能却是类似的，即<code>打开</code>和<code>关闭</code>。以<code>antd</code>为例：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; Modal, Button &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"antd"</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">App</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  state = &#123; <span class="hljs-attr">visible</span>: <span class="hljs-literal">false</span> &#125;

  <span class="hljs-comment">// 控制弹窗显示隐藏</span>
  toggleModal = <span class="hljs-function">(<span class="hljs-params">visible</span>) =></span> &#123;
    <span class="hljs-built_in">this</span>.setState(&#123; visible &#125;)
  &#125;;

  handleOk = <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
    <span class="hljs-comment">// 做点什么</span>
    <span class="hljs-built_in">this</span>.setState(&#123; <span class="hljs-attr">visible</span>: <span class="hljs-literal">false</span> &#125;)
  &#125;

  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> &#123; visible &#125; = <span class="hljs-built_in">this</span>.state
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">Button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.toggleModal.bind(this,</span> <span class="hljs-attr">true</span>)&#125;></span>Open<span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">Modal</span>
          <span class="hljs-attr">title</span>=<span class="hljs-string">"Basic Modal"</span>
          <span class="hljs-attr">visible</span>=<span class="hljs-string">&#123;visible&#125;</span>
          <span class="hljs-attr">onOk</span>=<span class="hljs-string">&#123;this.handleOk&#125;</span>
          <span class="hljs-attr">onCancel</span>=<span class="hljs-string">&#123;this.toggleModal.bind(this,</span> <span class="hljs-attr">false</span>)&#125;
        ></span>
          <span class="hljs-tag"><<span class="hljs-name">p</span>></span>Some contents...<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">Modal</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上是最简单的<code>Model</code>使用实例，即便是简单的使用，我们仍需要关注它的显示状态，实现它的切换方法。但是开发者其实只想关注与业务逻辑相关的<code>onOk</code>，理想的使用方式应该是这样的：</p>
<pre><code class="hljs language-js copyable" lang="js"><MyModal>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Button</span>></span>Open<span class="hljs-tag"></<span class="hljs-name">Button</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Modal</span> <span class="hljs-attr">title</span>=<span class="hljs-string">"Basic Modal"</span> <span class="hljs-attr">onOk</span>=<span class="hljs-string">&#123;this.handleOk&#125;</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>Some contents...<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">Modal</span>></span></span>
</MyModal>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以通过<code>render props</code>实现以上使用方式：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; Modal, Button &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"antd"</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyModal</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  state = &#123; <span class="hljs-attr">on</span>: <span class="hljs-literal">false</span> &#125;

  toggle = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">this</span>.setState(&#123;
      <span class="hljs-attr">on</span>: !<span class="hljs-built_in">this</span>.state.on
    &#125;)
  &#125;

  renderButton = <span class="hljs-function">(<span class="hljs-params">props</span>) =></span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Button</span> &#123;<span class="hljs-attr">...props</span>&#125; <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.toggle&#125;</span> /></span></span>

  renderModal = <span class="hljs-function">(<span class="hljs-params">&#123; onOK, ...rest &#125;</span>) =></span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Modal</span>
      &#123;<span class="hljs-attr">...rest</span>&#125;
      <span class="hljs-attr">visible</span>=<span class="hljs-string">&#123;this.state.on&#125;</span>
      <span class="hljs-attr">onOk</span>=<span class="hljs-string">&#123;()</span> =></span> &#123;
        onOK && onOK()
        this.toggle()
      &#125;&#125;
      onCancel=&#123;this.toggle&#125;
    /></span>
  )

  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.props.children(&#123;
      <span class="hljs-attr">Button</span>: <span class="hljs-built_in">this</span>.renderButton,
      <span class="hljs-attr">Modal</span>: <span class="hljs-built_in">this</span>.renderModal
    &#125;)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样我们就完成了一个具备状态和基础功能的<code>Modal</code>，我们在其他页面使用该<code>Modal</code>时，只需要关注特定的业务逻辑即可。</p>
<p>以上可以看出，<code>render props</code>是一个真正的<code>React</code>组件，而不是像<code>HOC</code>一样只是一个<strong>可以返回组件的函数</strong>，这也意味着使用<code>render props</code>不会像<code>HOC</code>一样产生组件层级嵌套的问题，也不用担心<code>props</code>命名冲突产生的覆盖问题。</p>
<h3 data-id="heading-7"><code>render props</code>使用限制</h3>
<p>在<code>render props</code>中应该避免使用<code>箭头函数</code>，因为这会造成性能影响。</p>
<p>比如：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 不好的示例</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MouseTracker</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Mouse</span> <span class="hljs-attr">render</span>=<span class="hljs-string">&#123;mouse</span> =></span> (
        <span class="hljs-tag"><<span class="hljs-name">Cat</span> <span class="hljs-attr">mouse</span>=<span class="hljs-string">&#123;mouse&#125;</span> /></span>
      )&#125;/></span>
    )
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样写是不好的，因为<code>render</code>方法是有可能多次渲染的，使用<code>箭头函数</code>，会导致每次渲染的时候，传入<code>render</code>的值都会不一样，而实际上并没有差别，这样会导致性能问题。</p>
<p>所以更好的写法应该是将传入<code>render</code>里的函数定义为实例方法，这样即便我们多次渲染，但是绑定的始终是同一个函数。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 好的示例</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MouseTracker</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">renderCat</span>(<span class="hljs-params">mouse</span>)</span> &#123;
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Cat</span> <span class="hljs-attr">mouse</span>=<span class="hljs-string">&#123;mouse&#125;</span> /></span></span>
  &#125;

  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> (
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Mouse</span> <span class="hljs-attr">render</span>=<span class="hljs-string">&#123;this.renderTheCat&#125;</span> /></span></span>
    )
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8"><code>render props</code>的优缺点</h3>
<ul>
<li>
<p>优点</p>
<ul>
<li>props 命名可修改，不存在相互覆盖；</li>
<li>清楚 props 来源；</li>
<li>不会出现组件多层嵌套；</li>
</ul>
</li>
<li>
<p>缺点</p>
<ul>
<li>
<p>写法繁琐；</p>
</li>
<li>
<p>无法在<code>return</code>语句外访问数据；</p>
</li>
<li>
<p>容易产生函数回调嵌套；</p>
<p>如下代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> MyComponent = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Mouse</span>></span>
      &#123;(&#123; x, y &#125;) => (
        <span class="hljs-tag"><<span class="hljs-name">Page</span>></span>
          &#123;(&#123; x: pageX, y: pageY &#125;) => (
            <span class="hljs-tag"><<span class="hljs-name">Connection</span>></span>
              &#123;(&#123; api &#125;) => &#123;
                // yikes
              &#125;&#125;
            <span class="hljs-tag"></<span class="hljs-name">Connection</span>></span>
          )&#125;
        <span class="hljs-tag"></<span class="hljs-name">Page</span>></span>
      )&#125;
    <span class="hljs-tag"></<span class="hljs-name">Mouse</span>></span></span>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
</li>
</ul>
<h2 data-id="heading-9">Hook</h2>
<p><code>React</code>的核心是组件，因此，<code>React</code>一直致力于优化和完善声明组件的方式。从最早的<code>类组件</code>，再到<code>函数组件</code>，各有优缺点。<code>类组件</code>可以给我们提供一个完整的生命周期和状态（state）,但是在写法上却十分笨重，而<code>函数组件</code>虽然写法非常简洁轻便，但其限制是<strong>必须是纯函数，不能包含状态，也不支持生命周期</strong>，因此<code>类组件</code>并不能取代<code>函数组件</code>。</p>
<p>而<code>React</code>团队觉得<strong>组件的最佳写法应该是函数，而不是类</strong>，由此产生了<code>React Hooks</code>。</p>
<p><strong>React Hooks 的设计目的，就是加强版函数组件，完全不使用"类"，就能写出一个全功能的组件</strong>。</p>
<p>为什么说<code>类组件</code>“笨重”，借用<code>React</code>官方的例子说明：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; Component &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Button</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">super</span>()
    <span class="hljs-built_in">this</span>.state = &#123; <span class="hljs-attr">buttonText</span>: <span class="hljs-string">"Click me, please"</span> &#125;
    <span class="hljs-built_in">this</span>.handleClick = <span class="hljs-built_in">this</span>.handleClick.bind(<span class="hljs-built_in">this</span>)
  &#125;
  <span class="hljs-function"><span class="hljs-title">handleClick</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.setState(<span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">return</span> &#123; <span class="hljs-attr">buttonText</span>: <span class="hljs-string">"Thanks, been clicked!"</span> &#125;
    &#125;)
  &#125;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> &#123; buttonText &#125; = <span class="hljs-built_in">this</span>.state
    <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.handleClick&#125;</span>></span>&#123;buttonText&#125;<span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上是一个简单的按钮组件，包含最基础的状态和点击方法，点击按钮后状态发生改变。</p>
<p>本是很简单的功能组件，但是却需要大量的代码去实现。由于<code>函数组件</code>不包含状态，所以我们并不能用<code>函数组件</code>来声明一个具备如上功能的组件。但是我们可以用<code>Hook</code>来实现：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React, &#123; useState &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Button</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> [buttonText, setButtonText] = useState(<span class="hljs-string">"Click me,   please"</span>)

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleClick</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">return</span> setButtonText(<span class="hljs-string">"Thanks, been clicked!"</span>)
  &#125;

  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;handleClick&#125;</span>></span>&#123;buttonText&#125;<span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相较而言，<code>Hook</code>显得更轻量，在贴近<code>函数组件</code>的同时，保留了自己的状态。</p>
<p>在上述例子中引入了第一个钩子<code>useState()</code>，除此之外，<code>React</code>官方还提供了<code>useEffect()</code>、<code>useContext()</code>、<code>useReducer()</code>等钩子。具体钩子及其用法详情请见<a href="https://zh-hans.reactjs.org/docs/hooks-reference.html" target="_blank" rel="nofollow noopener noreferrer">官方</a>。</p>
<p><code>Hook</code>的灵活之处还在于，除了官方提供的基础钩子之外，我们还可以利用这些基础钩子来封装和自定义钩子，从而实现更容易的代码复用。</p>
<h3 data-id="heading-10">Hook 优缺点</h3>
<ul>
<li>优点
<ul>
<li>更容易复用代码；</li>
<li>清爽的代码风格；</li>
<li>代码量更少；</li>
</ul>
</li>
<li>缺点
<ul>
<li>状态不同步（函数独立运行，每个函数都有一份独立的作用域）</li>
<li>需要更合理的使用<code>useEffect</code></li>
<li>颗粒度小，对于复杂逻辑需要抽象出很多<code>hook</code></li>
</ul>
</li>
</ul>
<h2 data-id="heading-11">总结</h2>
<p>除了<code>Mixin</code>因为自身的明显缺陷而稍显落后之外，对于<code>高阶组件</code>、<code>render props</code>、<code>react hook</code>而言，并没有哪种方式可称为<code>最佳方案</code>，它们都是优势与劣势并存的。哪怕是最为最热门的<code>react hook</code>，虽然每一个<code>hook</code>看起来都是那么的简短和清爽，但是在实际业务中，通常都是一个业务功能对应多个<code>hook</code>，这就意味着当业务改变时，需要去维护多个<code>hook</code>的变更，相对于维护一个<code>class</code>而言，心智负担或许要增加许多。只有切合自身业务的方式，才是<code>最佳方案</code>。</p>
<hr>
<p>参考文档：</p>
<ul>
<li><a href="https://segmentfault.com/a/1190000003016446" target="_blank" rel="nofollow noopener noreferrer">React Mixin 的使用</a></li>
<li><a href="https://reactjs.org/blog/2016/07/13/mixins-considered-harmful.html" target="_blank" rel="nofollow noopener noreferrer">Mixins Considered Harmful</a></li>
<li><a href="https://reactjs.org/docs/higher-order-components.html" target="_blank" rel="nofollow noopener noreferrer">Higher-Order Components</a></li>
<li><a href="https://reactjs.org/docs/render-props.html" target="_blank" rel="nofollow noopener noreferrer">Render Props</a></li>
<li><a href="https://www.imooc.com/article/39388" target="_blank" rel="nofollow noopener noreferrer">React 拾遗：Render Props 及其使用场景</a></li>
<li><a href="https://zh-hans.reactjs.org/docs/hooks-state.html" target="_blank" rel="nofollow noopener noreferrer">Hook 简介</a></li>
</ul></div>  
</div>
            