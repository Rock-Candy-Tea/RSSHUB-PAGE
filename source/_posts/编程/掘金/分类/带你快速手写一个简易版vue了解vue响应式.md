
---
title: '带你快速手写一个简易版vue了解vue响应式'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f3e24468cf0493fa17028b7b2a37360~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 30 Jul 2021 22:32:47 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f3e24468cf0493fa17028b7b2a37360~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h1 data-id="heading-0"></h1>
<h2 data-id="heading-1">起始</h2>
<p>在使用vue的时候,数据双向绑定,插值语法...等等,一系列让人眼花缭乱的操作.作为一个使用者搞懂轮子是怎么造,并不是为了自己造一个轮子,而是为了更好的使用轮子.</p>
<p>虽然现在vue3已经开始使用,但是很多公司现在使用的应该还是vue2.X.</p>
<h2 data-id="heading-2">使用</h2>
<p>在我们使用的时候,一般都是在main文件进行初始化,一般都是这样</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">new</span> Vue(&#123;
  router,
  store,
  .......
  <span class="hljs-attr">render</span>: <span class="hljs-function"><span class="hljs-params">h</span> =></span> h(App)
&#125;).$mount(<span class="hljs-string">'#app'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这里对于我一个初入前端的切图仔肯定不会实现我们在项目中那么复杂,对于vue我们还有另一种用法,在html文件中引入vue.js,譬如这样</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
    <span class="hljs-attr">data</span>: &#123;
      <span class="hljs-attr">number</span>: <span class="hljs-number">1</span>,
    &#125;,
    <span class="hljs-attr">methods</span>: &#123;
      <span class="hljs-function"><span class="hljs-title">add</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.number++
      &#125;,
      <span class="hljs-function"><span class="hljs-title">changeInput</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'changeInput'</span>);
      &#125;
    &#125;
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>就像这样,今天实现的就是以这样使用的,在vue的真正使用中会有三种render,template和el,优先级也是如此排列.</p>
<h2 data-id="heading-3">分析</h2>
<p>首先需要分析我们实现的是怎样的一个类</p>
<ul>
<li>首先它会接受一个对象,有el,data,methods.....</li>
<li>data中的数据需要响应式处理</li>
<li>解析模板处理,也就是我们在div中写入的&#123;&#123;number&#125;&#125;之类</li>
<li>响应式更新,这也是最重要的,在改变数据的时候通知视图进行更新</li>
<li>处理事件和指令,比如v-model,@click之类</li>
</ul>
<h2 data-id="heading-4">开始操刀实现</h2>
<p>首先创建vue这个类</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Vue</span></span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">options</span>)</span> &#123;
    <span class="hljs-comment">// 将传入的保存</span>
    <span class="hljs-built_in">this</span>.$options = options;
    <span class="hljs-comment">// 将传入data,保存在$data中</span>
    <span class="hljs-built_in">this</span>.$data = options.data
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是在我们的使用data的值时我们从来没有使用过$data,我们都是this.xxx就可以拿到这个值,由此可见我们首先需要将this.$data中的数据全部代理到这个类上让我们可以使用this.XXX可以使用这个也很简单,使用defineProperty就可以实现,下边来实现这个方法.</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">proxy</span>(<span class="hljs-params">vm</span>) </span>&#123;
  <span class="hljs-comment">//这里的vm需要我们拿到vue本身的实例</span>
  <span class="hljs-built_in">Object</span>.keys(vm.$data).forEach(<span class="hljs-function"><span class="hljs-params">key</span> =></span> &#123;
    <span class="hljs-built_in">Object</span>.defineProperty(vm, key, &#123;
      <span class="hljs-attr">get</span>: <span class="hljs-function">() =></span> vm.$data[key],
      <span class="hljs-attr">set</span>: <span class="hljs-function">(<span class="hljs-params">v</span>) =></span> vm.$data[key] = v
    &#125;)
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个方法很简单,不用做过多赘述,下边在vue类中使用让我们可以通过实例可以拿到data中的值</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Vue</span></span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">options</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.$options = options;
    <span class="hljs-built_in">this</span>.$data = options.data
+   proxy(<span class="hljs-built_in">this</span>)
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样我们就可以使用this.xx拿到,因为我们还没有实现method所以我们通过new Vue拿到的实例来实验</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
    <span class="hljs-attr">data</span>: &#123;
      <span class="hljs-attr">counter</span>: <span class="hljs-number">1</span>,
    &#125;,
  &#125;)
  <span class="hljs-built_in">console</span>.log(app.number);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们在控制台可以看到成功输出了numbe的值</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f3e24468cf0493fa17028b7b2a37360~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
那么对于data的代理就成功了.</p>
<h2 data-id="heading-5">模板解析</h2>
<p>对于模板解析,需要处理写入的插值表达式(写入的自定义指令和事件,后边会解决)</p>
<h3 data-id="heading-6">首先先将模板中的插值解析时页面打开不会满屏的大括号.</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Compile</span> </span>&#123;
  <span class="hljs-comment">//我们需要将el和vue本身传入来进行模板解析,el需要用来拿到元素,vue本身则需要其中的data,methds...</span>
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">el, vm</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.$vm = vm
    <span class="hljs-comment">//拿到我们解析的元素</span>
    <span class="hljs-built_in">this</span>.$el = <span class="hljs-built_in">document</span>.querySelector(el)

    <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.$el) &#123;
      <span class="hljs-comment">// 编写一个函数来解析模板</span>
      <span class="hljs-built_in">this</span>.compile(<span class="hljs-built_in">this</span>.$el)
    &#125;
  &#125;
  <span class="hljs-function"><span class="hljs-title">compile</span>(<span class="hljs-params">el</span>)</span> &#123;
    <span class="hljs-comment">// 遍历el的子节点 判断他们的类型做相应的处理</span>
    <span class="hljs-keyword">const</span> childNodes = el.childNodes
    <span class="hljs-keyword">if</span>(!childNodes) <span class="hljs-keyword">return</span>;
    childNodes.forEach(<span class="hljs-function"><span class="hljs-params">node</span> =></span> &#123;
      <span class="hljs-keyword">if</span>(node.nodeType === <span class="hljs-number">1</span>) &#123;
        <span class="hljs-comment">// 元素 处理指令和事件(后续来处理)</span>
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.isInter(node)) &#123;
        <span class="hljs-comment">// 文本</span>
        <span class="hljs-built_in">this</span>.compileText(node)
      &#125;
      <span class="hljs-comment">// 在有子元素的情况下需要递归</span>
      <span class="hljs-keyword">if</span>(node.childNodes) &#123;
        <span class="hljs-built_in">this</span>.compile(node)
      &#125;
    &#125;)
  &#125;
  
  <span class="hljs-comment">// 编译文本</span>
  <span class="hljs-function"><span class="hljs-title">compileText</span>(<span class="hljs-params">node</span>)</span> &#123;
      node.textContent = <span class="hljs-built_in">this</span>.$vm[<span class="hljs-built_in">RegExp</span>.$1]
  &#125;

  <span class="hljs-comment">// 是否插值表达式</span>
  <span class="hljs-function"><span class="hljs-title">isInter</span>(<span class="hljs-params">node</span>)</span> &#123;
    <span class="hljs-keyword">return</span> node.nodeType === <span class="hljs-number">3</span> && <span class="hljs-regexp">/\&#123;\&#123;(.*)\&#125;\&#125;/</span>.test(node.textContent)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在vue中使用它.</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Vue</span></span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">options</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.$options = options;
    <span class="hljs-built_in">this</span>.$data = options.data
    proxy(<span class="hljs-built_in">this</span>)
+   <span class="hljs-keyword">new</span> Compile(options.el, <span class="hljs-built_in">this</span>)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样页面中的插值就可以被替换为data中的数据了,但是我们在外边通过vue实例修改的时候数据是没有变化的.</p>
<h2 data-id="heading-7">实现数据响应式</h2>
<p>在实现数据响应式这里,借用源码的思想,使用Observer来做响应式,watcher和dep来通知更新,在vue中一个组件只有一个watcher,而我们的粒度就没办法相提并论了,毕竟是一个只实现部分的简单版vue.
首先编写Observer</p>
<h3 data-id="heading-8">Observer编写</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 遍历obj做响应式</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">observer</span>(<span class="hljs-params">obj</span>) </span>&#123;
  <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> obj !== <span class="hljs-string">'object'</span> || obj === <span class="hljs-literal">null</span>) &#123;
    <span class="hljs-keyword">return</span>
  &#125;
  <span class="hljs-comment">// 遍历obj的所有key做响应式</span>
  <span class="hljs-keyword">new</span> Observer(obj);
&#125;
<span class="hljs-comment">// 遍历obj的所有key做响应式</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Observer</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">value</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.value = value
    <span class="hljs-keyword">if</span>(<span class="hljs-built_in">Array</span>.isArray(<span class="hljs-built_in">this</span>.value)) &#123;
      <span class="hljs-comment">// TODO  对于数组的操作不做处理  无非是对于数组的七个方法进行重写覆盖</span>
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-built_in">this</span>.walk(value)
    &#125;
  &#125;
  <span class="hljs-comment">// 对象响应式</span>
  <span class="hljs-function"><span class="hljs-title">walk</span>(<span class="hljs-params">obj</span>)</span> &#123;
    <span class="hljs-built_in">Object</span>.keys(obj).forEach(<span class="hljs-function"><span class="hljs-params">key</span> =></span> &#123;
      <span class="hljs-comment">//这个东西看到很多人会觉得很眼熟,当然也只是名字眼熟</span>
      defineReactive(obj, key, obj[key])
    &#125;)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>defineReactive这里是用于数据进行响应式处理函数,在进行这个函数的编写之前,还需要先进行watcher的编写</p>
<h3 data-id="heading-9">watcher编写</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 监听器：负责依赖更新</span>
<span class="hljs-keyword">const</span> watchers = []; <span class="hljs-comment">//先不使用dep  先使用一个数组来收集watcher进行更新</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Watcher</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">vm, key, updateFn</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.vm = vm;
    <span class="hljs-built_in">this</span>.key = key;
    <span class="hljs-built_in">this</span>.updateFn = updateFn
    watchers.push(<span class="hljs-built_in">this</span>)
  &#125;

  <span class="hljs-comment">// 未来被Dep调用</span>
  <span class="hljs-function"><span class="hljs-title">update</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 执行实际的更新操作</span>
    <span class="hljs-comment">//因为我们需要在watcher更新时拿到最新的值,所以需要我们在这里作为参数传递给我们在收集到的函数</span>
    <span class="hljs-built_in">this</span>.updateFn.call(<span class="hljs-built_in">this</span>.vm, <span class="hljs-built_in">this</span>.vm[<span class="hljs-built_in">this</span>.key])
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有了watcher之后,需要修改我们之前写的Compile类来进行watcher的收集,于此同时,修改编译时的修改方法同时为v-model和v-test...做前置基础</p>
<h3 data-id="heading-10">Compile进化</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Compile</span> </span>&#123;
  <span class="hljs-comment">//我们需要将el和vue本身传入来进行模板解析,el需要用来拿到元素,vue本身则需要其中的data,methds...</span>
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">el, vm</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.$vm = vm
    <span class="hljs-comment">//拿到我们解析的元素</span>
    <span class="hljs-built_in">this</span>.$el = <span class="hljs-built_in">document</span>.querySelector(el)

    <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.$el) &#123;
      <span class="hljs-comment">// 编写一个函数来解析模板</span>
      <span class="hljs-built_in">this</span>.compile(<span class="hljs-built_in">this</span>.$el)
    &#125;
  &#125;
  <span class="hljs-function"><span class="hljs-title">compile</span>(<span class="hljs-params">el</span>)</span> &#123;
    <span class="hljs-comment">// 遍历el的子节点 判断他们的类型做相应的处理</span>
    <span class="hljs-keyword">const</span> childNodes = el.childNodes
    <span class="hljs-keyword">if</span>(!childNodes) <span class="hljs-keyword">return</span>;
    childNodes.forEach(<span class="hljs-function"><span class="hljs-params">node</span> =></span> &#123;
      <span class="hljs-keyword">if</span>(node.nodeType === <span class="hljs-number">1</span>) &#123;
        <span class="hljs-comment">// 元素 处理指令和事件(后续来处理)</span>
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.isInter(node)) &#123;
        <span class="hljs-comment">// 文本</span>
        <span class="hljs-built_in">this</span>.compileText(node)
      &#125;
      <span class="hljs-comment">// 在有子元素的情况下需要递归</span>
      <span class="hljs-keyword">if</span>(node.childNodes) &#123;
        <span class="hljs-built_in">this</span>.compile(node)
      &#125;
    &#125;)
  &#125;
  
  <span class="hljs-comment">//新添加函数</span>
  <span class="hljs-comment">//node 为修改的元素  exp为获取到大括号内的值的key dir为这边自定义的要执行的操作</span>
  <span class="hljs-function"><span class="hljs-title">update</span>(<span class="hljs-params">node, exp, dir</span>)</span> &#123;
    <span class="hljs-comment">// 初始化</span>
    <span class="hljs-keyword">const</span> fn = <span class="hljs-built_in">this</span>[dir + <span class="hljs-string">'Update'</span>]
    fn && fn(node, <span class="hljs-built_in">this</span>.$vm[exp])
    <span class="hljs-comment">// 更新  在这里创建watcher 并将更新的函数传进去  这里的val就是watcher触发更新函数时传入的最新值</span>
    <span class="hljs-keyword">new</span> Watcher(<span class="hljs-built_in">this</span>.$vm, exp, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">val</span>) </span>&#123;
      fn && fn(node, val)
    &#125;)
  &#125;
  <span class="hljs-comment">//新添加函数</span>
  <span class="hljs-function"><span class="hljs-title">textUpdate</span>(<span class="hljs-params">node, val</span>)</span> &#123;
     node.textContent = val
   &#125;
  <span class="hljs-comment">// 编译文本</span>
  <span class="hljs-function"><span class="hljs-title">compileText</span>(<span class="hljs-params">node</span>)</span> &#123;
  -   <span class="hljs-comment">//node.textContent = this.$vm[RegExp.$1]</span>
  +   <span class="hljs-built_in">this</span>.update(node, <span class="hljs-built_in">RegExp</span>.$1, <span class="hljs-string">'text'</span>)
  &#125;

  <span class="hljs-comment">// 是否插值表达式</span>
  <span class="hljs-function"><span class="hljs-title">isInter</span>(<span class="hljs-params">node</span>)</span> &#123;
    <span class="hljs-keyword">return</span> node.nodeType === <span class="hljs-number">3</span> && <span class="hljs-regexp">/\&#123;\&#123;(.*)\&#125;\&#125;/</span>.test(node.textContent)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">defineReactive编写</h3>
<p>下边来编写defineReactive来达到视图真正的更新</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 在key发生变化时可以感知做出操作
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>obj 对象
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>key 需要拦截的key
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>val 初始值
 */</span>
 <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">defineReactive</span>(<span class="hljs-params">obj, key, val</span>) </span>&#123;
  <span class="hljs-comment">//  递归</span>
  observer(val);
  <span class="hljs-built_in">Object</span>.defineProperty(obj, key, &#123;
    <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> val
    &#125;,
    <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">newVal</span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'set'</span>, newVal);
      <span class="hljs-keyword">if</span> (newVal != val) &#123;
        observer(newVal)
        val = newVal
        <span class="hljs-comment">//这里为粗糙实现  后续会加入dep会更加精致一点</span>
        watchers.forEach(<span class="hljs-function"><span class="hljs-params">w</span> =></span> w.update())
      &#125;
    &#125;
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在vue类中使用</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Vue</span></span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">options</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.$options = options;
    <span class="hljs-built_in">this</span>.$data = options.data
+   observer(<span class="hljs-built_in">this</span>.$data)
    proxy(<span class="hljs-built_in">this</span>)
    <span class="hljs-keyword">new</span> Compile(options.el, <span class="hljs-built_in">this</span>)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来在修改我们使用的页面</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
    <span class="hljs-attr">data</span>: &#123;
      <span class="hljs-attr">number</span>:<span class="hljs-number">10</span>,
    &#125;
  &#125;)
  <span class="hljs-built_in">console</span>.log(app.number);
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    app.counter = <span class="hljs-number">100</span>
  &#125;, <span class="hljs-number">1000</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>就可以在页面中看到在一秒钟之后视图朝着我们预想的结果发生变化,这样子就达到了我想要的结果,但是这样存在一个问题,就是当我们在data中定义了很多属性的时候,在页面中使用.
当我们改变其中一个的时候,我们所有的watcher都会执行一遍,页面所有用到data的地方都会发生更新,这样的问题我是肯定不想要的,这样就需要dep来管理,达到我们修改其中一个值,那只有修改的地方会发生变化,这样就会更好一点.
接下来先编写dep这个类,这个类的的功能很简单,一个dep管理data中的一条数据,收集和这条数据有关系的watcher,在发生变化时通知更新</p>
<h3 data-id="heading-12">Dep编写</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dep</span></span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.deps = []
  &#125;
  <span class="hljs-function"><span class="hljs-title">addDep</span>(<span class="hljs-params">dep</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.deps.push(dep)
  &#125;
  <span class="hljs-function"><span class="hljs-title">notify</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.deps.forEach(<span class="hljs-function"><span class="hljs-params">dep</span> =></span> dep.update())
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在dep为前提时需要修改watcher这个类,同时也不再需要watchers这个数组来管理.</p>
<h3 data-id="heading-13">Watcher进化</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 监听器：负责依赖更新</span>
- <span class="hljs-comment">//const watchers = []; //先不使用dep  先使用一个数组来收集watcher进行更新</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Watcher</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">vm, key, updateFn</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.vm = vm;
    <span class="hljs-built_in">this</span>.key = key;
    <span class="hljs-built_in">this</span>.updateFn = updateFn
-    watchers.push(<span class="hljs-built_in">this</span>)
    <span class="hljs-comment">// 触发依赖收集</span>
+   Dep.target = <span class="hljs-built_in">this</span>
    <span class="hljs-comment">//在这里纯属因为需要触发get来进行收集,下边重写defineReactive是会用到</span>
+   <span class="hljs-built_in">this</span>.vm[<span class="hljs-built_in">this</span>.key]
+   Dep.target = <span class="hljs-literal">null</span>
  &#125;

  <span class="hljs-comment">// 未来被Dep调用</span>
  <span class="hljs-function"><span class="hljs-title">update</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 执行实际的更新操作</span>
    <span class="hljs-comment">//因为我们需要在watcher更新时拿到最新的值,所以需要我们在这里作为参数传递给我们在收集到的函数</span>
    <span class="hljs-built_in">this</span>.updateFn.call(<span class="hljs-built_in">this</span>.vm, <span class="hljs-built_in">this</span>.vm[<span class="hljs-built_in">this</span>.key])
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编写好Watcher后来重新方法,来使用到dep来管理更新,而不是将所有watcher都进行触发更新</p>
<h3 data-id="heading-14">defineReactive进化</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 在key发生变化时可以感知做出操作
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>obj 对象
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>key 需要拦截的key
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>val 初始值
 */</span>
 <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">defineReactive</span>(<span class="hljs-params">obj, key, val</span>) </span>&#123;
  <span class="hljs-comment">//  递归</span>
  observer(val);
   <span class="hljs-comment">// 创建Dep实例</span>
  <span class="hljs-comment">// data中的数据每一项都会进入到此，创建一个Dep</span>
+  <span class="hljs-keyword">const</span> dep = <span class="hljs-keyword">new</span> Dep()
  <span class="hljs-built_in">Object</span>.defineProperty(obj, key, &#123;
    <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
       <span class="hljs-comment">// 依赖收集</span>
      <span class="hljs-comment">// 只有在调用时存在target才会被Dep收集更新（在初始化时设置静态属性target为watcher，被收集）</span>
      <span class="hljs-comment">//我们在watcher进入时获取过一次当前使用到的watcher的值这里就会进入get,并且当时wacher将自己设置为了Dep的target,在这里使用到进行收集方便更新,但是在触发之后将dep.target设置为了null,使我们在平时的读取时不做这个操作</span>
+     Dep.target && dep.addDep(Dep.target)
+     <span class="hljs-keyword">return</span> val
    &#125;,
    <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">newVal</span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'set'</span>, newVal);
      <span class="hljs-keyword">if</span> (newVal != val) &#123;
        observer(newVal)
        val = newVal
        <span class="hljs-comment">//这里为粗糙实现  后续会加入dep会更加精致一点</span>
-       watchers.forEach(<span class="hljs-function"><span class="hljs-params">w</span> =></span> w.update())
        <span class="hljs-comment">// 被修改时通知所有属于自己的watcher更新</span>
        <span class="hljs-comment">// 一个watcher对应一处依赖，一个Dep对应一个data中的数据  一个dep的更新可以指向多个watcher</span>
+       dep.notify()
      &#125;
    &#125;
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来修改使用的html文件来查看效果</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
    <span class="hljs-attr">data</span>: &#123;
      <span class="hljs-attr">counter</span>: <span class="hljs-number">1</span>,
      <span class="hljs-attr">number</span>:<span class="hljs-number">10</span>,
    &#125;,
  &#125;)
  <span class="hljs-built_in">console</span>.log(app.number);
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
    app.counter = <span class="hljs-number">100</span>
  &#125;, <span class="hljs-number">2000</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样子我们在没有使用到这个数据的地方就不会产生dom更新.在使用number的地方并没有产生变化</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59b96284c57b4f6da6ce6594f07a11fd~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
接下来编写指令和事件的梳理
主要修改Compile类在模板解析时处理,处理之前我们首先修改Vue类,将methods保存</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Vue</span></span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">options</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.$options = options;
    <span class="hljs-built_in">this</span>.$data = options.data
+   <span class="hljs-built_in">this</span>.$methods = options.methods
    observer(<span class="hljs-built_in">this</span>.$data)
    proxy(<span class="hljs-built_in">this</span>)
    <span class="hljs-keyword">new</span> Compile(options.el, <span class="hljs-built_in">this</span>)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">Compile最终成型</h3>
<p>接下来修改Compile类在模板解析时处理指令和事件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Compile</span> </span>&#123;
  <span class="hljs-comment">//我们需要将el和vue本身传入来进行模板解析,el需要用来拿到元素,vue本身则需要其中的data,methds...</span>
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">el, vm</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.$vm = vm
    <span class="hljs-comment">//拿到我们解析的元素</span>
    <span class="hljs-built_in">this</span>.$el = <span class="hljs-built_in">document</span>.querySelector(el)

    <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.$el) &#123;
      <span class="hljs-comment">// 编写一个函数来解析模板</span>
      <span class="hljs-built_in">this</span>.compile(<span class="hljs-built_in">this</span>.$el)
    &#125;
  &#125;
  <span class="hljs-function"><span class="hljs-title">compile</span>(<span class="hljs-params">el</span>)</span> &#123;
    <span class="hljs-comment">// 遍历el的子节点 判断他们的类型做相应的处理</span>
    <span class="hljs-keyword">const</span> childNodes = el.childNodes
    <span class="hljs-keyword">if</span>(!childNodes) <span class="hljs-keyword">return</span>;
    childNodes.forEach(<span class="hljs-function"><span class="hljs-params">node</span> =></span> &#123;
      <span class="hljs-keyword">if</span>(node.nodeType === <span class="hljs-number">1</span>) &#123;
        <span class="hljs-comment">// 元素 处理指令和事件</span>
+       <span class="hljs-keyword">const</span> attrs = node.attributes
+       <span class="hljs-built_in">Array</span>.from(attrs).forEach(<span class="hljs-function"><span class="hljs-params">attr</span> =></span> &#123;
+         <span class="hljs-comment">// v-xxx="abc"</span>
+         <span class="hljs-keyword">const</span> attrName = attr.name
+         <span class="hljs-keyword">const</span> exp = attr.value
+         <span class="hljs-comment">//当属性值以v-开头便认为这是一个指令 这里只处理v-text v-model v-html</span>
+         <span class="hljs-keyword">if</span>(attrName.startsWith(<span class="hljs-string">'v-'</span>)) &#123;
+           <span class="hljs-keyword">const</span> dir = attrName.substring(<span class="hljs-number">2</span>)
+           <span class="hljs-built_in">this</span>[dir] && <span class="hljs-built_in">this</span>[dir](node, exp)
+         <span class="hljs-comment">//事件的处理也非常简单</span>
+         &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(attrName.startsWith(<span class="hljs-string">'@'</span>)) &#123;
+           <span class="hljs-keyword">const</span> dir = attrName.substring(<span class="hljs-number">1</span>)
+           <span class="hljs-built_in">this</span>.eventFun(node, exp, dir)
+         &#125;
+       &#125;)
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.isInter(node)) &#123;
        <span class="hljs-comment">// 文本</span>
        <span class="hljs-built_in">this</span>.compileText(node)
      &#125;
      <span class="hljs-comment">// 在有子元素的情况下需要递归</span>
      <span class="hljs-keyword">if</span>(node.childNodes) &#123;
        <span class="hljs-built_in">this</span>.compile(node)
      &#125;
    &#125;)
  &#125;
+ <span class="hljs-comment">//新添加函数 处理事件</span>
  <span class="hljs-function"><span class="hljs-title">eventFun</span>(<span class="hljs-params">node, exp, dir</span>)</span> &#123;
    node.addEventListener(dir, <span class="hljs-built_in">this</span>.$vm.$methods[exp].bind(<span class="hljs-built_in">this</span>.$vm))
  &#125;
  <span class="hljs-comment">//node 为修改的元素  exp为获取到大括号内的值的key dir为这边自定义的要执行的操作</span>
  <span class="hljs-function"><span class="hljs-title">update</span>(<span class="hljs-params">node, exp, dir</span>)</span> &#123;
    <span class="hljs-comment">// 初始化</span>
    <span class="hljs-keyword">const</span> fn = <span class="hljs-built_in">this</span>[dir + <span class="hljs-string">'Update'</span>]
    fn && fn(node, <span class="hljs-built_in">this</span>.$vm[exp])
    <span class="hljs-comment">// 更新  在这里创建watcher 并将更新的函数传进去  这里的val就是watcher触发更新函数时传入的最新值</span>
    <span class="hljs-keyword">new</span> Watcher(<span class="hljs-built_in">this</span>.$vm, exp, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">val</span>) </span>&#123;
      fn && fn(node, val)
    &#125;)
  &#125;
  <span class="hljs-function"><span class="hljs-title">textUpdate</span>(<span class="hljs-params">node, val</span>)</span> &#123;
     node.textContent = val
   &#125;
+ <span class="hljs-comment">//新添加函数 处理v-text</span>
  <span class="hljs-function"><span class="hljs-title">text</span>(<span class="hljs-params">node, exp</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.update(node, exp, <span class="hljs-string">'text'</span>)
  &#125;
+ <span class="hljs-comment">//新添加函数 处理v-html</span>
  <span class="hljs-function"><span class="hljs-title">html</span>(<span class="hljs-params">node, exp</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.update(node, exp, <span class="hljs-string">'html'</span>)
  &#125;
+ <span class="hljs-comment">//新添加函数</span>
  <span class="hljs-function"><span class="hljs-title">htmlUpdate</span>(<span class="hljs-params">node, val</span>)</span> &#123;
    node.innerHTML = val
  &#125;
  <span class="hljs-comment">// 编译文本</span>
  <span class="hljs-function"><span class="hljs-title">compileText</span>(<span class="hljs-params">node</span>)</span> &#123;
  -   <span class="hljs-comment">//node.textContent = this.$vm[RegExp.$1]</span>
  +   <span class="hljs-built_in">this</span>.update(node, <span class="hljs-built_in">RegExp</span>.$1, <span class="hljs-string">'text'</span>)
  &#125;
+ <span class="hljs-comment">//新添加函数 处理v-model</span>
  <span class="hljs-function"><span class="hljs-title">model</span>(<span class="hljs-params">node, exp</span>)</span> &#123;
    <span class="hljs-comment">// console.log(node, exp);</span>
    <span class="hljs-built_in">this</span>.update(node, exp, <span class="hljs-string">'model'</span>)
    node.addEventListener(<span class="hljs-string">'input'</span>, <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
      <span class="hljs-comment">// console.log(e.target.value);</span>
      <span class="hljs-comment">// console.log(this);</span>
      <span class="hljs-built_in">this</span>.$vm[exp] = e.target.value
    &#125;)
  &#125;
  <span class="hljs-comment">// 是否插值表达式</span>
  <span class="hljs-function"><span class="hljs-title">isInter</span>(<span class="hljs-params">node</span>)</span> &#123;
    <span class="hljs-keyword">return</span> node.nodeType === <span class="hljs-number">3</span> && <span class="hljs-regexp">/\&#123;\&#123;(.*)\&#125;\&#125;/</span>.test(node.textContent)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来修改html文件查看效果</p>
<pre><code class="hljs language-js copyable" lang="js"><body>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"add"</span>></span>&#123;&#123;counter&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;&#123;counter&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;&#123;counter&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;&#123;number&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">v-text</span>=<span class="hljs-string">"counter"</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">v-html</span>=<span class="hljs-string">"desc"</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">c-model</span>=<span class="hljs-string">"desc"</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"changeInput"</span> @<span class="hljs-attr">input</span>=<span class="hljs-string">"changeInput"</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> Vue(&#123;
    <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
    <span class="hljs-attr">data</span>: &#123;
      <span class="hljs-attr">counter</span>: <span class="hljs-number">1</span>,
      <span class="hljs-attr">number</span>:<span class="hljs-number">10</span>,
      <span class="hljs-attr">desc</span>: <span class="hljs-string">`<h1 style="color:red">hello CVue</h1>`</span>
    &#125;,
    <span class="hljs-attr">methods</span>: &#123;
      <span class="hljs-function"><span class="hljs-title">add</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'add'</span>,<span class="hljs-built_in">this</span>);
        <span class="hljs-built_in">this</span>.counter++
      &#125;,
      <span class="hljs-function"><span class="hljs-title">changeInput</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'changeInput'</span>);
      &#125;
    &#125;
  &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>到这里就编写结束了,页面也达到了预期的效果.</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/325554798d5a4bb98504dd7b704a15ca~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>体验网址: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodesandbox.io%2Fs%2Fdazzling-williams-h9o0u%3Ffile%3D%2Fsrc%2Findex.js" target="_blank" rel="nofollow noopener noreferrer" title="https://codesandbox.io/s/dazzling-williams-h9o0u?file=/src/index.js" ref="nofollow noopener noreferrer">codesandbox.io/s/dazzling-…</a></p>
<p>作为自己学习的笔记,代码中也有很多疏忽,借鉴别人的代码来实现,不过学到了就是自己的.</p>
<h1 data-id="heading-16">最后</h1>
<p><strong>点个赞再走吧!</strong></p></div>  
</div>
            