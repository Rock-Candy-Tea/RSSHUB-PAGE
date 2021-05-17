
---
title: '使用react的7个避坑案例'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1935'
author: 掘金
comments: false
date: Sun, 16 May 2021 15:35:31 GMT
thumbnail: 'https://picsum.photos/400/300?random=1935'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><code>React</code>是个很受欢迎的前端框架。今天我们探索下<code>React</code>开发者应该注意的七个点。</p>
<h3 data-id="heading-0">1. 组件臃肿</h3>
<p><code>React</code>开发者没有创建必要的足够多的组件化，其实这个问题不局限于<code>React</code>开发者，很多<code>Vue</code>开发者也是。</p>
<blockquote>
<p>当然，我们现在讨论的是React</p>
</blockquote>
<p>在<code>React</code>中，我们可以创建一个很多内容的组件，来执行我们的各种任务，但是<strong>最好是保证组件精简</strong> -- 一个组件关联一个函数。这样不仅<strong>节约你的时间，而且能帮你很好地定位问题</strong>。</p>
<p>比如下面的<code>TodoList</code>组件：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ./components/TodoList.js</span>

<span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;

<span class="hljs-keyword">import</span> &#123; useTodoList &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../hooks/useTodoList'</span>;
<span class="hljs-keyword">import</span> &#123; useQuery &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../hooks/useQuery'</span>;
<span class="hljs-keyword">import</span> TodoItem <span class="hljs-keyword">from</span> <span class="hljs-string">'./TodoItem'</span>;
<span class="hljs-keyword">import</span> NewTodo <span class="hljs-keyword">from</span> <span class="hljs-string">'./NewTodo'</span>;

<span class="hljs-keyword">const</span> TodoList = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> &#123; getQuery, setQuery &#125; = useQuery();
  <span class="hljs-keyword">const</span> todos = useTodoList();
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
        &#123;todos.map((&#123; id, title, completed &#125;) => (
          <span class="hljs-tag"><<span class="hljs-name">TodoItem</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;id&#125;</span> <span class="hljs-attr">id</span>=<span class="hljs-string">&#123;id&#125;</span> <span class="hljs-attr">title</span>=<span class="hljs-string">&#123;title&#125;</span> <span class="hljs-attr">completed</span>=<span class="hljs-string">&#123;completed&#125;</span> /></span>
        ))&#125;
        <span class="hljs-tag"><<span class="hljs-name">NewTodo</span> /></span>
      <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        Highlight Query for incomplete items:
        <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;getQuery()&#125;</span> <span class="hljs-attr">onChange</span>=<span class="hljs-string">&#123;e</span> =></span> setQuery(e.target.value)&#125; />
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  );
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> TodoList;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">2. 直接更改state</h3>
<p>在<code>React</code>中，<strong>状态应该是不变的</strong>。如果你直接修改<code>state</code>，会导致难以修改的性能问题。</p>
<p>比如下面例子：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> modifyPetsList = <span class="hljs-function">(<span class="hljs-params">element, id</span>) =></span> &#123;
  petsList[id].checked = element.target.checked;
  setPetsList(petList)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面例子中，你想更改数组对象中<code>checked</code>键。但是你遇到一个问题：<strong>因为使用相同的引用更改了对象，React无法观察并触发重新渲染</strong>。</p>
<p>解决这个问题，我们应该使用<code>setState()</code>方法或者<code>useState()</code>钩子。</p>
<p>我们使用<code>useState()</code>方法来重写之前的例子。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> modifyPetsList = <span class="hljs-function">(<span class="hljs-params">element, id</span>) =></span> &#123;
  <span class="hljs-keyword">const</span> &#123; checked &#125; = element.target;
  setpetsList(<span class="hljs-function">(<span class="hljs-params">pets</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> pets.map(<span class="hljs-function">(<span class="hljs-params">pet, index</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (id === index) &#123;
        pet = &#123; ...pet, checked &#125;;
      &#125;
      <span class="hljs-keyword">return</span> pet;
    &#125;);
  &#125;);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">3. props该传数字类型的值却传了字符串，反之亦然</h3>
<p>这是个很小的错误，不应该出现。</p>
<p>比如下面的例子：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Arrival</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>
        Hi! You arrived &#123;this.props.position === 1 ? "first!" : "last!"&#125; .
      <span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里<code>===</code>对字符串<code>'1'</code>是无效的。而解决这个问题，需要我们在传递<code>props</code>值的时候用<code>&#123;&#125;</code>包裹。</p>
<p>修正如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// ❌</span>
<span class="hljs-keyword">const</span> element = <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Arrival</span> <span class="hljs-attr">position</span>=<span class="hljs-string">'1'</span> /></span></span>;

<span class="hljs-comment">// ✅</span>
<span class="hljs-keyword">const</span> element = <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Arrival</span> <span class="hljs-attr">position</span>=<span class="hljs-string">&#123;1&#125;</span> /></span></span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">4. list组件中没使用<code>key</code></h3>
<p>假设我们需要渲染下面的列表项：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> lists = [<span class="hljs-string">'cat'</span>, <span class="hljs-string">'dog'</span>, <span class="hljs-string">'fish’];

render() &#123;
  return (
    <ul>
      &#123;lists.map(listNo =>
        <li>&#123;listNo&#125;</li>)&#125;
    </ul>
  );
&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>当然，上面的代码可以运行。当列表比较庞杂并需要进行更改等操作的时候，就会带来渲染的问题。</p>
<p><strong>React跟踪文档对象模型（DOM）上的所有列表元素</strong>。没有记录可以告知<code>React</code>，列表发生了什么改动。</p>
<p>解决这个问题，<strong>你需要添加keys在你的列表元素中</strong>。<code>keys</code>赋予每个元素唯一标识，这有助于<code>React</code>确定已添加，删除，修改了哪些项目。</p>
<p>如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><ul>
  &#123;lists.map(<span class="hljs-function"><span class="hljs-params">listNo</span> =></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;listNo&#125;</span>></span>&#123;listNo&#125;<span class="hljs-tag"></<span class="hljs-name">li</span>></span></span>)&#125;
</ul>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">5. setState是异步操作</h3>
<p>很容易忘记<strong>React中的state是异步操作的</strong>。如果你在设置一个值之后就去访问它，那么你可能不能立马获取到该值。</p>
<p>我们看看下面的例子：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">handlePetsUpdate = <span class="hljs-function">(<span class="hljs-params">petCount</span>) =></span> &#123;
  <span class="hljs-built_in">this</span>.setState(&#123; petCount &#125;);
  <span class="hljs-built_in">this</span>.props.callback(<span class="hljs-built_in">this</span>.state.petCount); <span class="hljs-comment">// Old value</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你可以使用<code>setState()</code>的第二个参数，回调函数来处理。比如：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">handlePetsUpdate = <span class="hljs-function">(<span class="hljs-params">petCount</span>) =></span> &#123;
  <span class="hljs-built_in">this</span>.setState(&#123; petCount &#125;, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">this</span>.props.callback(<span class="hljs-built_in">this</span>.state.petCount); <span class="hljs-comment">// Updated value</span>
  &#125;);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">6. 频繁使用Redux</h3>
<p>在大型的<code>React app</code>中，很多开发者使用<code>Redux</code>来管理全局状态。</p>
<p><strong>虽然Redux很有用，但是没必要使用它来管理每个状态</strong>。</p>
<p>如果我们的应用程序没有需要交换信息的并行级组件的时候，那么就不需要在项目中添加额外的库。比如我们想更改组件中的表单按钮状态的时候，我们更多的是优先考虑<code>state</code>方法或者<code>useState</code>钩子。</p>
<h3 data-id="heading-6">7. 组件没以大写字母开头命名</h3>
<p><strong>在JSX中，以小写开头的组件会向下编译为HTML元素</strong>。</p>
<p>所以我们应该避免下面的写法：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">demoComponentName</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这将导致一个错误：如果你想渲染React组件，则需要以大写字母开头。</p>
<p>那么得采取下面这种写法：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">DemoComponentName</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">后话</h3>
<p>上面的内容提取自<a href="https://dev.to/educative/top-10-mistakes-to-avoid-when-using-react-27hn" target="_blank" rel="nofollow noopener noreferrer">Top 10 mistakes to avoid when using React</a>，采用了意译的方式，提取了7条比较实用的内容。</p></div>  
</div>
            