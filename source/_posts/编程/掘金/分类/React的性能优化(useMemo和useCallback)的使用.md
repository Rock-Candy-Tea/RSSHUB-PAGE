
---
title: 'React的性能优化(useMemo和useCallback)的使用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=745'
author: 掘金
comments: false
date: Sat, 22 May 2021 18:12:28 GMT
thumbnail: 'https://picsum.photos/400/300?random=745'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一、业务场景</h2>
<blockquote>
<p><code>React</code>是一个用于构建用户界面的<code>javascript</code>的库，主要负责将数据转换为视图，保证数据和视图的统一，<code>react</code>在每次数据更新的时候都会重新<code>render</code>来保证数据和视图的统一，但是当父组件<strong>内部数据</strong>的变化，在父组件下挂载的所有子组件也会重新渲染，因为<code>react</code>默认会全部渲染所有的组件，包括子组件的子组件，这就造成不必要的浪费。</p>
</blockquote>
<ul>
<li>
<p>1、使用类定义一个父组件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Parent</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  state = &#123;
    <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>,
  &#125;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span>(
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        我是父组件
        <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> this.setState(&#123;count: this.state.count++&#125;)&#125;>点击按钮<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">Child</span> /></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>2、定义一个子组件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Child</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'我是子组件'</span>);
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        我是子组件
        <span class="hljs-tag"><<span class="hljs-name">Grandson</span> /></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>3、定义一个孙子组件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Grandson</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'孙子组件'</span>)
    <span class="hljs-keyword">return</span>(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>孙子组件<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>4、上面几个组件是比较标准的<code>react</code>的类组件,函数组件也是类似的，当你在父组件中点击按钮，其实你仅仅是想改变父组件内的<code>count</code>的值，但是你会发现每次点击的时候子组件和孙组件也会重新渲染，因为<code>react</code>并不知道是不是要渲染子组件，需要我们自己去判断。</p>
</li>
</ul>
<h2 data-id="heading-1">一、类组件中使用<code>shouldComponentUpdate</code>生命周期钩子函数</h2>
<ul>
<li>
<p>1、在子组件中使用<code>shouldComponentUpdate</code>来判断是否要更新，</p>
<blockquote>
<p>其实就是根据<code>this.props</code>和函数参数中的<code>nextProps</code>中的参数来对比，如果返回<code>false</code>就不更新，如果返回<code>ture</code>就表示需要更新当前组件</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Child</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  shouldComponentUpdate (nextProps, nextState) &#123;
    <span class="hljs-built_in">console</span>.log(nextProps, <span class="hljs-built_in">this</span>.props);
    <span class="hljs-keyword">if</span> (nextProps.count === <span class="hljs-built_in">this</span>.props.count) &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
    &#125;
  &#125;
  ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>**注意点:**这里的<code>count</code>是要父组件给当前组件传递的参数(就是你要监听变化的的来更新当前组件),如果你写一个<code>nextProps.name === this.props.name</code>其实，父组件并没有给当前组件传递<code>name</code>那么下面都是返回<code>false</code>组件不更新</p>
</li>
<li>
<p>2、当子组件没更新，那么孙组件同样的不更新数据</p>
</li>
</ul>
<h2 data-id="heading-2">二、使用<code>PureComponet</code>语法糖</h2>
<blockquote>
<p>其实<code>PureComponet</code>就是一个语法糖，只是官方在底层帮你实现了<code>shouldComponentUpdate</code>方法而已，使用的时候只需要子类继承这个类就可以</p>
</blockquote>
<ul>
<li>
<p>1、子组件中继承</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Child</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">PureComponent</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'我是子组件'</span>);
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        我是子组件
        <span class="hljs-tag"><<span class="hljs-name">Grandson</span> /></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>2、在父组件中使用</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// 下面这种情况不会重新渲染子组件</span>
<Child/>
<span class="hljs-comment">// 下面这种情况下会重新渲染子组件</span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">Child</span> <span class="hljs-attr">count</span>=<span class="hljs-string">&#123;this.state.count&#125;/</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h2 data-id="heading-3">三、<code>memo</code>的使用</h2>
<blockquote>
<p>当你子组件是类组件的时候可以使用<code>shouldComponentUpdate</code>钩子函数或类组件继承<code>PureComponent</code>来实现不渲染子组件，但是对于函数组件来说是不能用这两个方法的，因此<code>react</code>官方给函数组件提供了<code>memo</code>来对函数组件包装下，实现不必要的渲染。</p>
</blockquote>
<ul>
<li>
<p>1、组件定义(这里也可以使用类组件)</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'我是子组件'</span>);
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      子组件
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  )
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Parent</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> [count, setCount] = useState(<span class="hljs-number">0</span>);
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      我是父组件-&#123;count&#125;
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span>=></span>setCount(count + 1)&#125;>点击按钮<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Child</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>2、这里我们父组件内部改变<code>count</code>并没有传递给子组件，但是子组件一样的重新渲染了，这并不是我们希望看到的，因为需要对子组件包装下</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'我是子组件'</span>);
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      子组件
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  )
&#125;

<span class="hljs-keyword">const</span> ChildMemo = React.memo(Child);
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Parent</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> [count, setCount] = useState(<span class="hljs-number">0</span>);
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      我是父组件-&#123;count&#125;
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span>=></span>setCount(count + 1)&#125;>点击按钮<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      &#123;/* 这种情况下不会渲染子组件 */&#125;
      <span class="hljs-tag"><<span class="hljs-name">ChildMemo</span> /></span>
      &#123;/* 这种情况下会渲染子组件 */&#125;
      <span class="hljs-tag"><<span class="hljs-name">ChildMemo</span> <span class="hljs-attr">count</span>=<span class="hljs-string">&#123;count&#125;/</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h2 data-id="heading-4">四、<code>useMemo</code>和<code>useCallback</code>的认识</h2>
<ul>
<li>
<p>1、<code>useMemo</code>和<code>useCallback</code>都是具有缓存作用的，只是他们缓存对象不一样，一个是属性，一个是缓存函数，特点都是，当缓存依赖的没变，去获取还是获取曾经的缓存</p>
</li>
<li>
<p>2、<code>useMemo</code>是对函数组件中的属性包装，返回一个具有缓存效果的新的属性，当依赖的属性没变化的时候，这个返回新属性就会从缓存中获取之前的。</p>
</li>
<li>
<p>3、<code>useCallback</code>是对函数组件中的方法缓存，返回一个被缓存的方法</p>
</li>
</ul>
<h2 data-id="heading-5">五、<code>useMemo</code>的使用(我们依赖借用子组件更新的来做)</h2>
<ul>
<li>
<p>1、根据上面的方式我们在父组件更新数据，观察子组件变化</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> Child = <span class="hljs-function">(<span class="hljs-params">props</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'重新渲染子组件'</span>, props);
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>子组件<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  )
&#125;
<span class="hljs-keyword">const</span> ChildMemo = React.memo(Child);

<span class="hljs-keyword">const</span> Parent = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> [count, setCount] = useState(<span class="hljs-number">0</span>);
  <span class="hljs-keyword">const</span> [number, setNumber]=useState(<span class="hljs-number">0</span>)
  <span class="hljs-keyword">const</span> userInfo = &#123;
    <span class="hljs-attr">age</span>: count,
    <span class="hljs-attr">name</span>: <span class="hljs-string">'hello'</span>,
  &#125;

  <span class="hljs-keyword">const</span> btnHandler = <span class="hljs-function">() =></span> &#123;
    setNumber(number+<span class="hljs-number">1</span>);
  &#125;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      &#123;number&#125;-&#123;count&#125;
      <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;btnHandler&#125;</span>></span>按钮<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">ChildMemo</span> <span class="hljs-attr">userInfo</span>=<span class="hljs-string">&#123;userInfo&#125;/</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面发现我们仅仅是更新了<code>number</code>的值，传递给子组件的对象值并没有变化，但是每次子组件都重新更新了，虽然我们在子组件上用了<code>React.memo</code>包装还是不行，这是因为在父组件中每次重新渲染，对于对象来说会是重新一个新的对象了。因此子组件要重新更新，</p>
</li>
<li>
<p>2、使用<code>useMemo</code>对属性的包装</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> userInfo = useMemo(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">age</span>: count,
    <span class="hljs-attr">name</span>: <span class="hljs-string">'hello'</span>,
  &#125;;
&#125;, [count]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用<code>useMemo</code>包装后的对象，重新返回一个具有缓存效果的新对象，第二个参数表示依赖性，或者叫观察对象，当被观察的没变化，返回的就是缓存对象，如果被观察的变化了，那么就会返回新的，现在不管你怎么更新<code>number</code>的值，子组件都不会重新更新了</p>
</li>
<li>
<p>3、注意点:<code>useMemo</code>要配合<code>React.memo</code>来使用，不然传递到子组件也是不生效的</p>
</li>
</ul>
<h2 data-id="heading-6">六、<code>useCallback</code>的使用</h2>
<p>前面介绍了，<code>useCallback</code>是对一个方法的包装，返回一个具有缓存的方法，常见的使用场景是，父组件要传递一个方法给子组件</p>
<ul>
<li>
<p>1、在不使用<code>useCallback</code>的时候</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> Child = <span class="hljs-function">(<span class="hljs-params">props</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'渲染了子组件'</span>);
  <span class="hljs-keyword">const</span> &#123; onClick &#125; = props;
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;onClick&#125;</span>></span>点击按钮获取值<span class="hljs-tag"></<span class="hljs-name">button</span>></span></span>
  )
&#125;

<span class="hljs-keyword">const</span> ChildMemo = React.memo(Child);

<span class="hljs-keyword">const</span> Parent = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> [text, updateText] = useState(<span class="hljs-string">''</span>);
  <span class="hljs-keyword">const</span> textRef = useRef(text);
  <span class="hljs-keyword">const</span> handleSubmit = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'当前的值'</span>, text);
  &#125;
  <span class="hljs-keyword">return</span>(
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      我是父组件
      <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;text&#125;</span> <span class="hljs-attr">onChange</span>=<span class="hljs-string">&#123;(e)</span> =></span> updateText(e.target.value)&#125;/>
      <span class="hljs-tag"><<span class="hljs-name">ChildMemo</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;handleSubmit&#125;/</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果是每次输入框输入值的时候，子组件就会重新渲染一次，其实子组件中仅仅是一个按钮，要获取最终输入的值，每次父组件输入值的时候，子组件就更新，很耗性能的</p>
</li>
<li>
<p>2、使用<code>useCallback</code>来包装一个方法</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> Parent = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> [text, updateText] = useState(<span class="hljs-string">''</span>);
  <span class="hljs-keyword">const</span> textRef = useRef();

  <span class="hljs-comment">// useCallback又依赖了textRef的变化，因此可以获取到最新的数据</span>
  <span class="hljs-keyword">const</span> handleSubmit = useCallback(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'当前输入框的值:'</span>, textRef.current);
  &#125;, [textRef])

  <span class="hljs-comment">// 当text的值变化的时候就会给textRef的current重新赋值</span>
  useEffect(<span class="hljs-function">() =></span> &#123;
    textRef.current = text;
  &#125;, [text]);
  
  <span class="hljs-keyword">return</span>(
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      我是父组件
      <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;text&#125;</span> <span class="hljs-attr">onChange</span>=<span class="hljs-string">&#123;(e)</span> =></span> updateText(e.target.value)&#125;/>
      <span class="hljs-tag"><<span class="hljs-name">ChildMemo</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;handleSubmit&#125;/</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul></div>  
</div>
            