
---
title: 'React函数组件Hooks-useMemo详解'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b74d742faf3b4dfab314286aab5e5689~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 02 Jul 2021 04:46:28 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b74d742faf3b4dfab314286aab5e5689~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b74d742faf3b4dfab314286aab5e5689~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-0">Memo</h1>
<p><a href="https://codesandbox.io/s/dawn-sun-00023" target="_blank" rel="nofollow noopener noreferrer">使用场景</a>：一个App组件里有m和n数据。还有一个Child子组件，它接受一个m作为它的外部数据。当点击把n+1的按钮时，我们知道，App会再次执行，那么Child子组件也会再次执行吗？</p>
<pre><code class="copyable">function App() &#123;
  const [n, setN] = React.useState(0);
  const [m, setM] = React.useState(0);
  const onClick = () => &#123;
    setN(n + 1);
  &#125;;

  return (
    <div className="App">
      <div>
        <button onClick=&#123;onClick&#125;>update n &#123;n&#125;</button>
      </div>
      <Child data=&#123;m&#125;/>
    </div>
  );
&#125;

function Child(props) &#123;
  console.log("child 执行了");
  console.log('假设这里有大量代码')
  return <div>child: &#123;props.data&#125;</div>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过在Child函数组件里打log，我们发现，改变n，Child也会执行一次。可是明明Child这个组件只依赖m，n变化它为什么要跟着执行呢？怎么解决这个问题？</p>
<p>就可以使用 <code>React.memo</code> 封装Child</p>
<pre><code class="copyable">const Child2 = React.memo(Child);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>把Child放在 <code>React.memo</code> 里，得到一个Child2，Child2是Child优化之后的函数。在App里渲染这个Child2</p>
<p>结果：改变n，Child不执行了，只有改变它依赖的外部数据m时，才会执行。</p>
<p>使代码更简洁：直接把匿名函数组件放在memo里作为参数，得到Child组件。</p>
<pre><code class="copyable">const Child = React.memo((props)=>&#123;
  console.log("child 执行了");
  console.log('假设这里有大量代码')
  return <div>child: &#123;props.data&#125;</div>;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">结论</h2>
<p>React默认会有多余的render，当改变组件里的数据时，由于组件本身会再次执行，就导致这个组件的子组件也会再次执行。</p>
<p><code>React.memo</code> 使得一个组件<strong>只有在它依赖的props变化时，才会执行</strong>。</p>
<h2 data-id="heading-2"><a href="https://codesandbox.io/s/blissful-wilbur-5tw75" target="_blank" rel="nofollow noopener noreferrer">memo有一个bug</a></h2>
<p>如果子组件接受了一个函数props，这个函数在父组件里定义，给子组件传进去。当我改变父组件里的n时，App()肯定会再次执行。就会<strong>导致定义在里边的这个函数也执行</strong>了。</p>
<pre><code class="copyable">function App() &#123;
  const [n, setN] = React.useState(0);
  const [m, setM] = React.useState(0);
  const onClick = () => &#123;
    setN(n + 1);
  &#125;;
  const onClickChild=()=>&#123;&#125;     // 再次执行时，虽然函数内容一样，但是地址不同了
  return (
    <div className="App">
      <div>
        <button onClick=&#123;onClick&#125;>update n &#123;n&#125;</button>
      </div>
      <Child data=&#123;m&#125; onClickChild=&#123;onClickChild&#125;/>
    </div>
  );
&#125;

const Child = React.memo((props)=>&#123;
  console.log("child 执行了");
  return <div onClick=&#123;props.onClickChild&#125;>child: &#123;props.data&#125;</div>;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果：点击按钮，改变n。Child明明不依赖n，但是Child也执行了。</p>
<p>就是因为App再次执行时，<code>onClickChild</code> 这个函数也被重新定义了，虽然内容不会变，但是地址不同了，React就认为这个函数变了。Child接受的这个props变了，自然就会再次执行。</p>
<p>怎么办呢？能不能让这个函数在某种情况下，不要重新生成，继续使用上一次的缓存结果</p>
<h1 data-id="heading-3">用useMemo，实现函数重用</h1>
<pre><code class="copyable">const onClickChild = useMemo(() => &#123;
    return () => &#123;&#125;;
  &#125;, [m]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>把这个函数经过 <code>useMemo</code> 优化。<code>useMemo</code> 接受两个参数，第一个参数是一个返回函数的函数，返回的就是该函数本来的逻辑。第二个参数是依赖，表示只有当m变化时，才重新生成函数。如果依赖的m没变，就复用上一次的缓存，不生成新的函数。</p>
<p>点击n+1的按钮后，发现Child组件没有执行了。因为我们使用 <code>useMemo</code> 规定了，只有当m变化时，才重新生成props函数。m没变，即使App再次执行，这个函数也不会生成一个新的。</p>
<p><code>useMemo</code> 经常用来缓存一些在两次新旧组件迭代的时候，希望使用上一次的值。</p>
<p>有时要缓存的，也就是return 的不一定是函数，也可以是对象</p>
<p>useMemo的第一个参数：<code>()=> value</code>，没有形参，返回一个value。第二个参数：依赖 <code>[m,n]</code>。只有当依赖变化时，才会计算新的value。依赖没变，就重用之前的value</p>
<h2 data-id="heading-4">useMemo的特点：</h2>
<ul>
<li>第一个参数是()=>value</li>
<li>第二个参数是依赖<code>[m,n]</code></li>
<li>只有当依赖变化时，才会重新计算出新的value</li>
<li>如果依赖不变，那么就重用之前的value</li>
<li>类似Vue2的computed</li>
</ul>
<p>注意：如果你的value是一个函数，那么就要写成</p>
<pre><code class="copyable">useMemo（()=>(x)=>console.log(x)）
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是一个返回函数的函数</p>
<p>是不是觉得很难用，那么 <code>useCallback</code> 来了</p>
<h2 data-id="heading-5">useCallback的用法（useMemo的语法糖）</h2>
<pre><code class="copyable">useCallback（x=>console.log(x)，[m]）
<span class="copy-code-btn">复制代码</span></code></pre>
<p>等价于</p>
<pre><code class="copyable">useMemo（()=>(x)=>console.log(x)，[m]）
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            