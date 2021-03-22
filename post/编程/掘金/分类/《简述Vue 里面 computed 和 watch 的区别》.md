
---
title: '《简述Vue 里面 computed 和 watch 的区别》'
categories: 
    - 编程
    - 掘金
    - 分类

author: 掘金
comments: false
date: Sun, 21 Mar 2021 23:37:41 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a2e535c6bc7e4543ada3591c57d10f55~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">computed 计算属性</h2>
<p>computed 是指计算属性; 它会根据所依赖的数据动态显示新的计算结果, 该计算结果会被缓存起来。computed 的值在 getter 执行后是会被缓存的。如果所依赖的数据发生改变时候, 就会重新调用 getter 来计算最新的结果。</p>
<h3 data-id="heading-1">computed 是用来计算出一个值的，</h3>
<ul>
<li>第一，这个值在调用的时候不用加（），</li>
<li>第二，如果依赖不变，会自动缓存，computed 的值就不会重新计算</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
  <span class="hljs-attr">data</span>: &#123;
    <span class="hljs-attr">message</span>: <span class="hljs-string">'hello'</span>
  &#125;,
  <span class="hljs-attr">template</span>: <span class="hljs-string">`
    <div>
      <p>原始字符串：&#123;&#123;message&#125;&#125;</p>
      <p>反转后的字符串：&#123;&#123;reversedMessage&#125;&#125;</p>
    </div>
  `</span>,
  <span class="hljs-attr">computed</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">reversedMessage</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.message.split(<span class="hljs-string">''</span>).reverse().join(<span class="hljs-string">''</span>)
    &#125;
  &#125;
&#125;).$mount(<span class="hljs-string">"#app"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">watch 监听数据的变化</h2>
<p>watch 它是一个对 data 的数据监听回调, 当依赖的 data 的数据变化时, 会执行一个回调函数。在回调中会传入newVal和oldVal两个参数。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">new</span> Vue(&#123;
  <span class="hljs-attr">data</span>: &#123;
    <span class="hljs-attr">message</span>: <span class="hljs-string">""</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">"ry"</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>
  &#125;,
  <span class="hljs-attr">template</span>: <span class="hljs-string">`
    <div>
      <p>个人信息: &#123;&#123;message&#125;&#125;</p>
      <p>年龄: <input type="text" v-model="age" /></p>
    </div>
  `</span>,
  <span class="hljs-attr">watch</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">age</span>(<span class="hljs-params">newValue, oldValue</span>)</span>&#123;
      <span class="hljs-built_in">this</span>.message = <span class="hljs-built_in">this</span>.name + <span class="hljs-string">" 今年 "</span> + newValue + <span class="hljs-string">" 岁"</span>;
    &#125;
  &#125;
&#125;).$mount(<span class="hljs-string">"#app"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第一次页面初始化效果如下：
<img alt="WX20210322-150613@2x.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a2e535c6bc7e4543ada3591c57d10f55~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>如上 watch 有一个特点是：</p>
<ul>
<li>第一次初始化页面的时候，是不会去执行 age 这个属性监听的，</li>
<li>只有当 age 值发生改变的时候才会执行监听计算。因此我们上面第一次初始化页面的时候，message 属性值默认为空字符串。</li>
<li>那么我们现在想要第一次初始化页面的时候也希望它能够执行 age 进行监听，因此我们需要修改下我们的 watch 的方法，需要引入 <code>handler</code> 方法和 <code>immediate</code> 属性</li>
</ul>
<h3 data-id="heading-3">handler 方法及 immediate 属性</h3>
<p>代码如下所示:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">new</span> Vue(&#123;
  <span class="hljs-attr">data</span>: &#123;
    <span class="hljs-attr">message</span>: <span class="hljs-string">""</span>,
    <span class="hljs-attr">name</span>: <span class="hljs-string">"ry"</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>
  &#125;,
  <span class="hljs-attr">template</span>: <span class="hljs-string">`
    <div>
      <p>个人信息: &#123;&#123;message&#125;&#125;</p>
      <p>年龄: <input type="text" v-model="age" /></p>
    </div>
  `</span>,
  <span class="hljs-attr">watch</span>: &#123;
    <span class="hljs-attr">age</span>: &#123;
      <span class="hljs-function"><span class="hljs-title">handler</span>(<span class="hljs-params">newValue, oldValue</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.message = <span class="hljs-built_in">this</span>.name + <span class="hljs-string">" 今年 "</span> + newValue + <span class="hljs-string">" 岁"</span>;
      &#125;,
      <span class="hljs-attr">immediate</span>: <span class="hljs-literal">true</span>
    &#125;
  &#125;
&#125;).$mount(<span class="hljs-string">"#app"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上代码， age 属性绑定了一个 handler 方法。其实我们之前的 watch 当中的方法默认就是这个 handler 方法。但是在这里我们使用了<code>immediate: true</code>，含义是: 如果在 watch 里面声明了 age 的话，就会立即执行里面的 handler 方法。如果 immediate 值为  false 的话，果就和之前的一样, 就不会立即执行 handler 这个方法的。因此设置了 <code>mediate:true</code>的话，一次页面加载的时候也会执行该 handler 函数的。即第一次 message 有值。</p>
<p>因此第一次页面初始化效果如下：</p>
<p><img alt="WX20210322-150520@2x.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0d3a5812afe4847a79dd39daedea21c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">deep属性</h3>
<p>watch 面有一个属性为 <code>deep</code>，含义是：是否深度监听某个对象的值，值默认为 <code>false</code>。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">new</span> Vue(&#123;
  <span class="hljs-attr">data</span>: &#123;
    <span class="hljs-attr">obj</span>: &#123;
      <span class="hljs-attr">message</span>: <span class="hljs-string">""</span>,
      <span class="hljs-attr">name</span>: <span class="hljs-string">"ry"</span>,
      <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>
    &#125;
  &#125;,
  <span class="hljs-attr">template</span>: <span class="hljs-string">`
    <div>
      <p>个人信息: &#123;&#123;message&#125;&#125;</p>
      <p>年龄: <input type="text" v-model="obj.age" /></p>
    </div>
  `</span>,
  <span class="hljs-attr">watch</span>: &#123;
    <span class="hljs-string">'obj'</span>: &#123;
      <span class="hljs-function"><span class="hljs-title">handler</span>(<span class="hljs-params">newValue, oldValue</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.message = <span class="hljs-built_in">this</span>.obj.name + <span class="hljs-string">" 今年 "</span> + newValue.age + <span class="hljs-string">" 岁"</span>;
      &#125;,
      <span class="hljs-attr">immediate</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">deep</span>: <span class="hljs-literal">true</span>
    &#125;
  &#125;
&#125;).$mount(<span class="hljs-string">"#app"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上代码， 如果不添加 <code>deep: true</code> 的话，当我们在输入框中输入值的时候，改变<code>obj.age</code> 值后，obj 对象中的 handler 函数是不会被执行到的。 Vue 不能检测到对象属性的添加或删除的。它只能监听到 obj 这个对象的变化。</p>
<h2 data-id="heading-5">watch 和 computed 的区别是：</h2>
<p><strong>相同点</strong>：他们两者都是观察页面数据变化的。</p>
<p><strong>不同点</strong>：</p>
<ul>
<li>computed 只有当依赖的数据变化时才会计算, 当数据没有变化时, 它会读取缓存数据。</li>
<li>watch 每次都需要执行函数。watch 更适用于数据变化时的异步操作。</li>
</ul></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            