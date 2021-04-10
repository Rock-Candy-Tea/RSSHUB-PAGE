
---
title: '理解React中key的作用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7444b9bc5afa487fa8a4dce1c1138bc2~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 09 Apr 2021 23:03:57 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7444b9bc5afa487fa8a4dce1c1138bc2~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>要了解React中key的作用，可以从key的取值入手，key的取值可以分为三种，不定值、索引值、确定且唯一值</p>
<p>在下面的代码中，key的取值是不定值（Math.random()）</p>
<p><strong>问题：</strong>
点击按钮的时候，span的颜色会变成红色吗？</p>
<pre><code class="hljs language-import copyable" lang="import">import React, &#123; useState &#125; from 'react';

function App() &#123;
  const [initMap, setInitMap] = useState([1,2,3,4]);
  const handleClick = () => &#123;
    setInitMap([1,2,3,4])
    var spanEle = document.getElementsByTagName('span');
    Array.from(spanEle).map(it => it.style.color = 'red')
  &#125;
  
  return (
    <div className="App" id="app">
      &#123;
        initMap.map((it,index) => <div key=&#123;Math.random()&#125;><span>color</span></div>)
      &#125;
      <button onClick=&#123;() => handleClick()&#125;></button>
    </div>
  );
&#125;

export default App;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>答案是：不会</p>
<p><strong>这个问题涉及react渲染机制和diff算法</strong></p>
<p>官网中对于diff有如下规则：</p>
<ul>
<li><strong>当元素类型变化时，会销毁重建</strong></li>
<li><strong>当元素类型不变时，对比属性</strong></li>
<li><strong>当组件元素类型不变时，通过props递归判断子节点</strong></li>
<li><strong>递归对比子节点，当子节点是列表时，通过key和props来判断。若key一致，则进行更新，若key不一致，就销毁重建</strong></li>
</ul>
<p><strong>分析上述问题：</strong></p>
<p>当点击按钮时，setInitMap([1,2,3,4])会造成渲染，渲染时会生成新的虚拟dom，但此时获取到的span元素是之前的元素（因为setInitMap是异步执行的），<strong>所以新旧dom会做对比</strong></p>
<pre><code class="copyable">在initMap.map((it,index) => <div key=&#123;Math.random()&#125;><span>color</span></div>)这段代码中
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里的div是列表，对比第四条diff规则，react会根据key来判断是否更新真实dom。<code>key=            &#123;Math.random()&#125;</code>，新旧dom的值不一致，就会重新生成div。而我们是给更新之前的元素加了红色的样式，所以重新创建的元素上不会有这个样式，效果如下</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7444b9bc5afa487fa8a4dce1c1138bc2~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5df3864b1fa44a13bf48bb943df75dc6~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><strong>第二种情况：key的取值为索引值</strong></p>
<p>上面我们分析的结果是，因为key的变化，导致div元素在render的时候会重新生成。那如果key在render前后保持不变呢？例如，将key改为index</p>
<p><strong>问题：</strong>
这段代码在button点击之后，span的颜色会变吗？</p>
<pre><code class="copyable">return (
    <div className="App" id="app">
      <Spin spinning=&#123;spin&#125;></Spin>
      &#123;
        initMap.map((it,index) => <div key=&#123;index&#125;><span>color</span></div>)
      &#125;
      <button onClick=&#123;() => handleClick()&#125;></button>
    </div>
  );
<span class="copy-code-btn">复制代码</span></code></pre>
<p>答案：会</p>
<p><strong>分析：</strong> 因为在render前后，index不变，所以div不会重新生成，接着对比span元素，span元素在render前后，属性变化，因此react只会为span元素应用新的属性，但是他们指向的还是之前的元素</p>
<p>点击前：
<img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/36dcc8a2cf2b4f64ad4dfc8a433483b3~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
点击后：<img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c5c914064ad540bb93c4b690a3d1d072~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><strong>第三种情况：key的取值确定且唯一</strong>：</p>
<p>在这个例子中，通过将key设置成index，span的颜色有了变化，但是在使用key时，React官网不推荐使用index</p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eff025d9097b426a87aae598e3add047~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>改造一下上面的代码</p>
<pre><code class="hljs language-function copyable" lang="function">  const [initMap, setInitMap] = useState([1,2,3,4]);
  const handleClick = () => &#123;
    setInitMap([3,2,1,4])
  &#125;
  return (
    <div className="App" id="app">
      &#123;
        initMap.map((it,index) => <div key=&#123;index&#125;><input type="radio" />&#123;it&#125;</div>)
      &#125;
      <button onClick=&#123;() => handleClick()&#125;>点击</button>
    </div>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>在初始化的时候选中值为3的按钮</li>
</ol>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b7bb7cc4bf284bcaa8c18ed5a978b1f3~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>点击按钮</li>
</ol>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c34b68dca55d446b8a93d96fcddea85c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><strong>我们预期的效果是，选中的依旧是值为3的按钮，但此时变成了值为1的按钮</strong></p>
<p><strong>分析：</strong></p>
<ol>
<li>setState之后会导致render</li>
<li>div的index不变，所以div不会重新生成，<strong>input不受state和props控制，因此元素的状态不变</strong></li>
<li><strong>所以变化的只有受state影响的it</strong></li>
</ol>
<p><strong>如果想要达到预期效果，我们要设置唯一且确定的key</strong></p>
<p>测试一：</p>
<pre><code class="copyable">&#123;
   initMap.map((it) => <div key=&#123;it&#125;><input type="radio" />&#123;it&#125;</div>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>初始化的时候选中第三个按钮</li>
</ol>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a1cf530cbc8041209b60917c086c9365~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>点击按钮</li>
</ol>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/98695438d40c4264ab94ee36ed8faf1b~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><strong>这才是符合预期的效果</strong></p>
<p>思考一下，将key设置为Math.random()，会有什么效果？按钮的状态会保留吗？</p>
<p>点击前：</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c8803a1dcdf44082a2f9565c18393970~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>点击后：</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/69298f1468a74431b64833f0fa1077e1~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><strong>radio的状态不会被保留</strong></p>
<p>通过上面的例子，我们大概可以理解React中key的作用了，下面的内容是对React知识点的一些扩展</p>
<p><strong>扩展内容：</strong>
文章开始的代码还涉及React两个其他知识点，一个是提到过的React渲染条件，一个是对真实dom的操作；</p>
<p><strong>扩展一：</strong> React渲染条件</p>
<pre><code class="copyable">import './App.css';
import React, &#123; useState &#125; from 'react';

function App() &#123;
  const [initMap, setInitMap] = useState([1,2,3,4]);
  const [spin, setSpin] = useState(false);
  const handleClick = () => &#123;
    setSpin(true); //变化部分
    var spanEle = document.getElementsByTagName('span');
    Array.from(spanEle).map(it => it.style.color = 'red')
    setSpin(false); //变化部分
  &#125;
  
  return (
    <div className="App" id="app">
      <Spin spinning=&#123;spin&#125;></Spin>
      &#123;
        initMap.map((it,index) => <div key=&#123;Math.random()&#125;><span>&#123;it&#125;</span></div>)
      &#125;
      <button onClick=&#123;() => handleClick()&#125;></button>
    </div>
  );
&#125;

export default App;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>测试结果如下
点击前：</p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0dac5b1d93ce4a9fb056a3bc53482b4c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>点击后：</p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b4f4b7006774698a7956e41d80486ae~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>在这段代码中，div的key仍然使用的是Math.random()，<strong>但initMap的state并没有改变</strong>，所以没有重新渲染，此时div不会销毁重建</p>
<p><strong>扩展二：是否可以对真实dom操作</strong></p>
<p>在React中，虚拟dom的出现是为了减少对真实dom的操作，因为真实的dom元素是一个较复杂的对象，操作的话计算量比较大。我们上面的代码中，都是直接操作dom节点，更改样式，这样并不可取。由于React是根据state和props的变化来渲染页面，因此通过state来控制页面渲染比较好</p>
<p>修改后的代码如下：</p>
<pre><code class="copyable">function App() &#123;
  const [initMap, setInitMap] = useState([1,2,3,4]);
  const [spin, setSpin] = useState(false);
  const [showColor, setShowColor] = useState(false);
  const handleClick = () => &#123;
    setInitMap([3,2,1,4]);
    setShowColor(true);
  &#125;
  
  return (
    <div className="App" id="app">
      <Spin spinning=&#123;spin&#125;>
      &#123;
        initMap.map((it,index) => <div key=&#123;Math.random()&#125;><span className=&#123;showColor && 'span-color'&#125;>color</span></div>)
      &#125;
      </Spin>
      <button onClick=&#123;() => handleClick()&#125;>点击</button>
    </div>
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时<strong>span是受控组件</strong>，可以通过showColor的状态控制元素的渲染</p>
<p>点击前：</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d8321a33d79943148140b312b5087394~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>点击后：</p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0f752f2a95c64305b8c6030fbc9ee3f0~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>使用state控制渲染后，代码量会变少，同时结果符合预期</p>
<p><strong>总结</strong></p>
<ol>
<li>在使用key时，要保证key的唯一和确定性，如果key的值为Math.random()，可能造成组件重新构建，使之前对元素的操作失效</li>
<li>在渲染页面时，尽量不要操作真实的dom，使用state来更新页面</li>
</ol></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            