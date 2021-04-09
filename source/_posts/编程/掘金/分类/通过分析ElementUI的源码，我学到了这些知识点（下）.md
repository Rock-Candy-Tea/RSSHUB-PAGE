
---
title: '通过分析ElementUI的源码，我学到了这些知识点（下）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9901256fda14945b612a96974c5e65e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 08 Apr 2021 07:56:46 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9901256fda14945b612a96974c5e65e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文接着<a href="https://juejin.cn/post/6948405540703698974" target="_blank">上文</a>讲</p>
<h1 data-id="heading-0">4、createElement 与 为什么要在Vue中使用jsx</h1>
<p>createElement可能对于习惯于编写template的同学可能还比较陌生，这个方法用于编写render函数的场景，其中输入参数h便是createElement，请看下面的例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//已经省略无关代码</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'ElCollapseTransition'</span>,
  <span class="hljs-attr">functional</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params">h, &#123; children &#125;</span>)</span> &#123;
    <span class="hljs-keyword">const</span> data = &#123;
      <span class="hljs-attr">on</span>: <span class="hljs-keyword">new</span> Transition()
    &#125;;

    <span class="hljs-keyword">return</span> h(<span class="hljs-string">'transition'</span>, data, children);
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这段代码位于element-ui/src/transitions/collapse-transition.js中。
在Vue的官方文档中有这样<a href="https://cn.vuejs.org/v2/guide/render-function.html#%E6%B7%B1%E5%85%A5%E6%95%B0%E6%8D%AE%E5%AF%B9%E8%B1%A1" target="_blank" rel="nofollow noopener noreferrer">一节</a>详细阐述了createElement的用法。
为什么我们要用createElement呢？有些时候我们需要动态的插入一个VNode，并且想要这个VNode跟我们正常写的模板一样具备事件响应的能力，比如说表格、表单等，每个表格列里面要涵盖不同的渲染内容的需求，我们是没办法事先就想好这个表格里面要展示的内容的，最容易想到的方式就是在运行的时候插入一段VNode。所以我们就可以对外提供一个函数，要求这个函数的入参是createElement,并且返回一个VNode。
<br>ElementUI Tree自定义树节点的示例代码：</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-function"><span class="hljs-title">renderContent</span>(<span class="hljs-params">h, &#123; node, data, store &#125;</span>)</span> &#123;
        <span class="hljs-keyword">return</span> (
          <span class="xml"><span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"custom-tree-node"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;node.label&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span>></span>
              <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">size</span>=<span class="hljs-string">"mini"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">on-click</span>=<span class="hljs-string">&#123;</span> () =></span> this.append(data) &#125;>Append<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
              <span class="hljs-tag"><<span class="hljs-name">el-button</span> <span class="hljs-attr">size</span>=<span class="hljs-string">"mini"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">on-click</span>=<span class="hljs-string">&#123;</span> () =></span> this.remove(node, data) &#125;>Delete<span class="hljs-tag"></<span class="hljs-name">el-button</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">span</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">span</span>></span></span>);
      &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是createElement有一个天生的不足，就是代码实在是太太太太太太冗余了。于是，为了改进直接编写createElement造成的代码冗余，便出现了jsx，所以jsx并不是React专属的啦。
上述ElementUI Tree自定义树节点的示例代码就是基于JSX编写的。我们把这段代码编写成原生的createElement函数的形式让大家来感受一下JSX的好处。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">renderContent</span>(<span class="hljs-params">h, &#123; node, data, store &#125;</span>) </span>&#123;
  <span class="hljs-keyword">return</span> h(
    <span class="hljs-string">"span"</span>,
    &#123;
      <span class="hljs-attr">class</span>: <span class="hljs-string">"ustom-tree-node"</span>,
    &#125;,
    h(<span class="hljs-string">"span"</span>, &#123;&#125;, node.label),
    h(<span class="hljs-string">"span"</span>, &#123;&#125;, [
      h(
        <span class="hljs-string">"el-button"</span>,
        &#123;
          <span class="hljs-attr">props</span>: &#123;
            <span class="hljs-attr">size</span>: <span class="hljs-string">"mini"</span>,
            <span class="hljs-attr">type</span>: <span class="hljs-string">"text"</span>,
          &#125;,
          <span class="hljs-attr">on</span>: &#123;
            <span class="hljs-attr">click</span>: <span class="hljs-function">() =></span> &#123;
              <span class="hljs-built_in">this</span>.append(data);
            &#125;,
          &#125;,
        &#125;,
        <span class="hljs-string">"Append"</span>
      ),
      h(
        <span class="hljs-string">"el-button"</span>,
        &#123;
          <span class="hljs-attr">props</span>: &#123;
            <span class="hljs-attr">size</span>: <span class="hljs-string">"mini"</span>,
            <span class="hljs-attr">type</span>: <span class="hljs-string">"text"</span>,
          &#125;,
          <span class="hljs-attr">on</span>: &#123;
            <span class="hljs-attr">click</span>: <span class="hljs-function">() =></span> &#123;
              <span class="hljs-built_in">this</span>.remove(node, data);
            &#125;,
          &#125;,
        &#125;,
        <span class="hljs-string">"Delete"</span>
      ),
    ])
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>关于jsx的语法本文不做介绍。<br>
最后再聊另外一个话题，来看一段代码，我们分别用template的语法和jsx的语法来编写。
使用template编写的源码：</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div class="hello" :class="&#123; world: a &#125;">
    <input type="text" v-model="val" />
  </div>
</template>

<script>
export default &#123;
  data() &#123;
    return &#123;
      a: "",
      val: ""
    &#125;;
  &#125;,
  mounted() &#123;
    this.a = 1;
  &#125;
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译结果：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//以省略无关代码</span>
 <span class="hljs-keyword">var</span> o = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">var</span> e = <span class="hljs-built_in">this</span>,
        t = e.$createElement,
        o = e._self._c || t;
      <span class="hljs-keyword">return</span> o(<span class="hljs-string">"div"</span>, &#123; <span class="hljs-attr">staticClass</span>: <span class="hljs-string">"hello"</span>, <span class="hljs-attr">class</span>: &#123; <span class="hljs-attr">world</span>: e.a &#125; &#125;, [
        o(<span class="hljs-string">"input"</span>, &#123;
          <span class="hljs-attr">directives</span>: [
            &#123;
              <span class="hljs-attr">name</span>: <span class="hljs-string">"model"</span>,
              <span class="hljs-attr">rawName</span>: <span class="hljs-string">"v-model"</span>,
              <span class="hljs-attr">value</span>: e.val,
              <span class="hljs-attr">expression</span>: <span class="hljs-string">"val"</span>
            &#125;
          ],
          <span class="hljs-attr">attrs</span>: &#123; <span class="hljs-attr">type</span>: <span class="hljs-string">"text"</span> &#125;,
          <span class="hljs-attr">domProps</span>: &#123; <span class="hljs-attr">value</span>: e.val &#125;,
          <span class="hljs-attr">on</span>: &#123;
            <span class="hljs-attr">input</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">t</span>) </span>&#123;
              t.target.composing || (e.val = t.target.value);
            &#125;
          &#125;
        &#125;)
      ]);
    &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>惊不惊喜，意不意外，template最终经过webpack编译之后，还是成了createElement函数的形式，哈哈哈。
然后我们再将其改写成jsx的形式：
源码如下：</p>
<pre><code class="hljs language-vue copyable" lang="vue"><script>
export default &#123;
  data() &#123;
    return &#123;
      a: "",
      val: ""
    &#125;;
  &#125;,
  mounted() &#123;
    this.a = 1;
  &#125;,
  render(h) &#123;
    return (
      <div class=&#123;&#123; hello: true, word: a &#125;&#125;>
        <input v-model=&#123;this.val&#125; type="text" />
      </div>
    );
  &#125;
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译结果如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//以省略无关代码</span>
&#123;
            <span class="hljs-attr">data</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
              <span class="hljs-keyword">return</span> &#123; <span class="hljs-attr">a</span>: <span class="hljs-string">""</span>, <span class="hljs-attr">val</span>: <span class="hljs-string">""</span> &#125;;
            &#125;,
            <span class="hljs-attr">mounted</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
              <span class="hljs-built_in">this</span>.a = <span class="hljs-number">1</span>;
            &#125;,
            <span class="hljs-attr">render</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">e</span>) </span>&#123;
              <span class="hljs-keyword">var</span> r = <span class="hljs-built_in">this</span>;
              <span class="hljs-keyword">return</span> e(<span class="hljs-string">"div"</span>, &#123; <span class="hljs-attr">class</span>: &#123; <span class="hljs-attr">hello</span>: !<span class="hljs-number">0</span>, <span class="hljs-attr">word</span>: a &#125; &#125;, [
                e(
                  <span class="hljs-string">"input"</span>,
                  t()([
                    &#123;
                      <span class="hljs-attr">on</span>: &#123;
                        <span class="hljs-attr">input</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">e</span>) </span>&#123;
                          e.target.composing || (r.val = e.target.value);
                        &#125;
                      &#125;,
                      <span class="hljs-attr">attrs</span>: &#123; <span class="hljs-attr">type</span>: <span class="hljs-string">"text"</span> &#125;,
                      <span class="hljs-attr">domProps</span>: &#123; <span class="hljs-attr">value</span>: r.val &#125;
                    &#125;,
                    &#123;
                      <span class="hljs-attr">directives</span>: [
                        &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"model"</span>, <span class="hljs-attr">value</span>: r.val, <span class="hljs-attr">modifiers</span>: &#123;&#125; &#125;
                      ]
                    &#125;
                  ])
                )
              ]);
            &#125;
          &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以现在大家应该明白为什么如果我们既没有写template并且也没有写render函数的时候，Vue会抛出一个提示说render函数和template必须要有一个呢。<br>
<strong>需要注意一点的是JSX需要预编译，如果程序在运行的时候需要动态插入VNode的场景，仍然只能用createElement函数的形式</strong>。<br>
但实际项目中仍然优先考虑template的形式编写代码，一方面render函数入门门槛高，对于新手及其不友好，另一方面使用template编写的代码会经过webpack编译优化，在某些场景下性能会好一些。再者render函数里面不能使用指令（唯一一个v-model指令都是社区支持的，😁），编程体验不太好。但是render函数具有一定的可编程性，因此，需要根据开发场景适当的切换(我在实际项目几乎不会用到<component />组件，哈哈哈)。<br>还有一些笔者觉得在使用体验上不是特别友好的地方，Vue2中props和attrs是分开的，比如ElementUI里面写的组件接收的属性:</p>
<p><img alt="属性示例.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9901256fda14945b612a96974c5e65e~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">当我们切换到他的源码的时候你会发现,卧槽，你这个操作简直把我整神！！！</p>
<p><img alt="属性的小坑.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca1a4fe2368f4f4b860c67589f2f1c1f~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">因此你需要明确的将placeholder写到attrs属性上去，这个placeholder才会生效。<strong>道听途说没有得到求证的消息，Vue3里面统一了attrs和props</strong>
另外一个区别就是，使用render函数使用插槽不是特别方便，因为Vue把作用域插槽跟普通插槽分别进行了处理。关于这个插槽，接下来我们会讲到。<br>
Vue还提供了$createElement这个属性，这个属性其实就是我们的render函数的h，这个函数我只有在render函数的形式下才成功使用过。因为这个h入参的关系，假设业务特别复杂的情况下，我想要拆分render函数，但是拆分出来的函数老是第一个参数必须是h，实在是让人难以接受，于是，在拆分的函数中直接使用$createElement代替，避免了h参数的传递。</p>
<h1 data-id="heading-1">5、$slots 和$scopedSlots</h1>
<p>首先，如果对插槽不太熟悉的同学请查阅Vue的<a href="https://cn.vuejs.org/v2/guide/components-slots.html" target="_blank" rel="nofollow noopener noreferrer">官方文档</a>。<br>
在上一节中我们聊到了Vue中createElement函数的使用场景，并且说到了Vue中的插槽问题。<br>
什么时候使用插槽?什么时候使用createElement呢?<br>我的开发经验告诉我，如果你的API想要设计的反人类的话，就使用createElement函数吧，如果要设计的友好的话，就设计成插槽，哈哈哈。为什么这样说呢，上文说到了，当我们要在运行的时候动态的插入一段VNode的时候，我们可以借助Vue.component中组件的template的字段，然后再将其使用插槽插入，实际上我们把这个解析template得到VNode的过程交给Vue去处理了，否则我们将会面临写一大段的createElement生成VNode的问题。使用插槽的好处就是直观，可以方便的使用Vue的template的那些语法特性（最大的好处就是指令没有之一），代码简洁。
<br>
有些时候我们真的需要用一个JSON来表述表格的定义，从ElementUI-Table的使用体验上来说，感觉不是特别友好,
这儿我参考了AntDesign-Vue、iView、和ElementUI几个UI框架的在表格部分的设计，想要适应任何自定义表格列的组件。iview使用的是createElement形式实现自定义表格列的。ElementUI直接使用的是子组件（el-table-column）的形式配置表格列。AntDesign使用的是动态插槽（Vue3已经支持动态插槽）。回到ElementUI上来，我们先看看ElementUI-Table的slot-scope="xxx"(虽然这个写法已经废弃)这个语法特性是怎么实现的。
element-ui/packages/table/table-column.js第170行左右：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 已经省略无关代码</span>
    column.renderCell = <span class="hljs-function">(<span class="hljs-params">h, data</span>) =></span> &#123;
      <span class="hljs-keyword">let</span> children = <span class="hljs-literal">null</span>;
      <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.$scopedSlots.default) &#123;
        children = <span class="hljs-built_in">this</span>.$scopedSlots.default(data);
      &#125; <span class="hljs-keyword">else</span> &#123;
        children = originRenderCell(h, data);
      &#125;
      <span class="hljs-keyword">const</span> prefix = treeCellPrefix(h, data);
      <span class="hljs-keyword">const</span> props = &#123;
        <span class="hljs-attr">class</span>: <span class="hljs-string">'cell'</span>,
        <span class="hljs-attr">style</span>: &#123;&#125;
      &#125;;
      <span class="hljs-keyword">if</span> (column.showOverflowTooltip) &#123;
        props.class += <span class="hljs-string">' el-tooltip'</span>;
        props.style = &#123;<span class="hljs-attr">width</span>: (data.column.realWidth || data.column.width) - <span class="hljs-number">1</span> + <span class="hljs-string">'px'</span>&#125;;
      &#125;
      <span class="hljs-keyword">return</span> (<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> &#123; <span class="hljs-attr">...props</span> &#125;></span>
        &#123; prefix &#125;
        &#123; children &#125;
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>);
    &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>大家可以看到，<strong>其实$scopedSlots就是一个返回VNode的函数($slots是一个VNode)</strong>。
有了这个基础之后，我们就大有可为了，我们可以判断当前$scopedSlots是否具有某个变量，如果有，则执行。在这儿，我贴一段我自己封装ElementUI表格时候对动态插槽的实现：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//这是我编写的表格列的组件中的一段代码</span>
 <span class="hljs-function"><span class="hljs-title">setupSlots</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">var</span> slotFunc = <span class="hljs-built_in">this</span>.$scopedSlots[<span class="hljs-built_in">this</span>.prop]
      <span class="hljs-comment">//如果当前表格列对应的prop存在这个具名作用于插槽的话，则使用插槽的内容进行渲染，否则使用table-column-wrapper组件进行渲染。</span>
      <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">default</span>: <span class="hljs-function">(<span class="hljs-params">&#123; row, $index &#125;</span>) =></span> &#123;
          <span class="hljs-keyword">return</span> <span class="hljs-keyword">typeof</span> slotFunc === <span class="hljs-string">'function'</span> ? (
            slotFunc(&#123; row, $index &#125;)
          ) : (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">table-column-wrapper</span>
              <span class="hljs-attr">prop</span>=<span class="hljs-string">&#123;this.prop&#125;</span>
              <span class="hljs-attr">row</span>=<span class="hljs-string">&#123;row&#125;</span>
              <span class="hljs-attr">index</span>=<span class="hljs-string">&#123;$index&#125;</span>
              <span class="hljs-attr">config</span>=<span class="hljs-string">&#123;this.config&#125;</span>
            /></span></span>
          )
        &#125;,
      &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们花了很大的篇幅介绍$scopedSlots,接下来该介绍$slots了，我最开始使用JSX编写基础组件的时候，因为深入数据对象那一节，想当然的以为使用JSX只有一个$scopeSlots，当我某一天用JSX写ElementUI的el-input的时候发现代码并没有生效。
我编写的代码如下：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-comment">//已省略非关键代码</span>
<span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params">h</span>)</span> &#123;
    <span class="hljs-keyword">const</span> spanNode = h(<span class="hljs-string">"span"</span>, <span class="hljs-string">"HelloWorld"</span>);
    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">el-input</span>
          <span class="hljs-attr">v-model</span>=<span class="hljs-string">&#123;this.val&#125;</span>
          <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span>
          &#123;<span class="hljs-attr">...</span>&#123;
            <span class="hljs-attr">scopedSlots:</span> &#123;
              <span class="hljs-attr">prepend:</span> <span class="hljs-attr">spanNode</span>
            &#125;
          &#125;&#125;
        /></span></span>
    );
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>后来我回想到，我们正常写template的时候，写插槽，都是将需要插入的组件放到当前组件的内部，然后添加slot属性。于是对这段代码进行改正：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"> <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params">h</span>)</span> &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">el-input</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">&#123;this.val&#125;</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">"append"</span>></span>HelloWorld<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">el-input</span>></span></span>
    );
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样就会生效了，但是这样又有了新问题，我们硬编码了slot，如何实现动态的slot呢，我是这样解决的：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"> methods: &#123;
    <span class="hljs-function"><span class="hljs-title">genSlots</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">Object</span>.entries(<span class="hljs-built_in">this</span>.$slots).map(<span class="hljs-function">(<span class="hljs-params">[prop, vnode]</span>) =></span> &#123;
        <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">slot</span>=<span class="hljs-string">&#123;prop&#125;</span>></span>&#123;vnode&#125;<span class="hljs-tag"></<span class="hljs-name">template</span>></span></span>;
      &#125;);
    &#125;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params">h</span>)</span> &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">el-input</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">&#123;this.val&#125;</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span>></span>
        &#123;/* 不管你生成多少个slot，只能是我当前这个组件支持的slot，我才会给你展示 */&#125;
        &#123;this.genSlots()&#125;
      <span class="hljs-tag"></<span class="hljs-name">el-input</span>></span></span>
    );
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>目前我对动态插槽的实现思路，还没有经过对程序的运行性能影响的检验，忘读者酌情参考，如有纰漏，敬请指正。</strong>
基于以上思路就可以完全在Vue2中实现动态插槽。</p>
<h1 data-id="heading-2">6 $attrs 和 $listeners</h1>
<p>在element-ui/packages/image/src/main.vue中，我们可以看到如下代码：</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div class="el-image">
    <img
      v-else
      class="el-image__inner"
      v-bind="$attrs"
      v-on="$listeners"
      @click="clickHandler"
      :src="src"
      :style="imageStyle"
      :class="&#123; 'el-image__inner--center': alignCenter, 'el-image__preview': preview &#125;">
  </div>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这两个属性对于封装基于第三方组件的组件的时候，是十分好用的，由于笔者在之前的文章有对这个知识点的讲解，感兴趣的朋友可以参考<a href="https://juejin.cn/post/6908368803877355533" target="_blank">这里</a>，此处将不再赘述。</p>
<h1 data-id="heading-3">7、aria-*</h1>
<p>关于aria-*标签，我最开始使用ElementUI的时候，也比较好奇，为什么好端端的代码要多写一些“无意义”的标签呢，后来我通过查阅资料得知，这让网站的对无障碍访问支持有重要的意义。
下面这段话是我搬运的MDN的官方释义（我不光生产代码，还是代码的搬运工，哈哈哈哈）：</p>
<blockquote>
<p>Accessible Rich Internet Applications (ARIA) 是能够让残障人士更加便利的访问 Web 内容和使用 Web 应用（特别是那些由JavaScript 开发的）的一套机制。<br><br>ARIA 是一组特殊的易用性属性，可以添加到任意标签上，尤其适用于 HTML。role 属性定义了对象的通用类型（例如文章、警告，或幻灯片）。额外的 ARIA 属性提供了其他有用的特性，例如表单的描述或进度条的当前值。</p>
</blockquote>
<p>因此，在后面的开发中，为了是我们的网站具备更好的无障碍访问特性，还得在合适的时机使用这些语法呢，害，知识又增加了呢。</p>
<h1 data-id="heading-4">8、i18n</h1>
<p>ElementUI是支持多语言的一个UI库，但是通过研读它的代码发现，其实多语言的实现也并不复杂。
其核心代码位于element-ui/src/locale/index.js中。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//如果有应用了Vue其它对i18n支持的插件，则使用其它的多语言插件</span>
<span class="hljs-keyword">let</span> i18nHandler = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  
  <span class="hljs-keyword">const</span> vuei18n = <span class="hljs-built_in">Object</span>.getPrototypeOf(<span class="hljs-built_in">this</span> || Vue).$t;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> vuei18n === <span class="hljs-string">'function'</span> && !!Vue.locale) &#123;
    <span class="hljs-keyword">if</span> (!merged) &#123;
      merged = <span class="hljs-literal">true</span>;
      Vue.locale(
        Vue.config.lang,
        deepmerge(lang, Vue.locale(Vue.config.lang) || &#123;&#125;, &#123; <span class="hljs-attr">clone</span>: <span class="hljs-literal">true</span> &#125;)
      );
    &#125;
    <span class="hljs-keyword">return</span> vuei18n.apply(<span class="hljs-built_in">this</span>, <span class="hljs-built_in">arguments</span>);
  &#125;
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> t = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">path, options</span>) </span>&#123;
  <span class="hljs-keyword">let</span> value = i18nHandler.apply(<span class="hljs-built_in">this</span>, <span class="hljs-built_in">arguments</span>);
  <span class="hljs-comment">//如果返回的值满足条件，说明用户使用了其它的i18n插件</span>
  <span class="hljs-keyword">if</span> (value !== <span class="hljs-literal">null</span> && value !== <span class="hljs-literal">undefined</span>) <span class="hljs-keyword">return</span> value;

  <span class="hljs-keyword">const</span> array = path.split(<span class="hljs-string">'.'</span>);
  <span class="hljs-keyword">let</span> current = lang;
  <span class="hljs-comment">//否则使用ElementUI自己内置的语言替换模式  </span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>, j = array.length; i < j; i++) &#123;
    <span class="hljs-keyword">const</span> property = array[i];
    value = current[property];
    <span class="hljs-keyword">if</span> (i === j - <span class="hljs-number">1</span>) <span class="hljs-keyword">return</span> format(value, options);
    <span class="hljs-keyword">if</span> (!value) <span class="hljs-keyword">return</span> <span class="hljs-string">''</span>;
    current = value;
  &#125;
  <span class="hljs-keyword">return</span> <span class="hljs-string">''</span>;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后local保留解析方法(代码位于element-ui/src/mixins/locale.js)
代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; t &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'element-ui/src/locale'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">t</span>(<span class="hljs-params">...args</span>)</span> &#123;
      <span class="hljs-keyword">return</span> t.apply(<span class="hljs-built_in">this</span>, args);
    &#125;
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在任何需要的地方（我以DatePicker为例）引入locale混入，
代码示例如下:</p>
<pre><code class="hljs language-vue copyable" lang="vue"><!--已省略非关键代码-->
<template>
  <table
    :class="&#123; 'is-week-mode': selectionMode === 'week' &#125;">
    <tbody>
    <tr>
      <th v-if="showWeekNumber">&#123;&#123; t('el.datepicker.week') &#125;&#125;</th>
      <th v-for="(week, key) in WEEKS" :key="key">&#123;&#123; t('el.datepicker.weeks.' + week) &#125;&#125;</th>
    </tr>
    </tbody>
  </table>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其既支持Vue主流的多语言插件，又提供了内置支持，这个手段对于我们在编写插件的时候还是有一定的借鉴意义的，毕竟其还是有可能面向外国用户使用的，如果预先不考虑这个问题，到时候又修改一堆的代码（忽然想到了邓爷爷的一句话，教育要面向现代化，面向世界，面向未来，哈哈哈😁）。</p>
<h1 data-id="heading-5">总结</h1>
<p>这两篇文章通过ElementUI的源码分析，阐述了SCSS的一些高级用法以及CSS BEM和一些Vue高级API用法，很多内容都是来自于我在实际开发中的理解与心得体会，我可能阐述了的ElementUI所蕴含的编程技法的冰山一角都还算不上（有兴趣的读者可以查阅一下ElementUI下utils模块中的内容，也有一定的价值，可能会帮助你更好的使用ElementUI。），希望广大读者与我分享一些好的开发心得体会，毕竟只有交流才能碰撞出思维的火花，彼此都能进步，哈哈哈。<br>最后，在此感谢ElementUI团队为我们贡献出了如此优秀的开源项目，点赞三连。<br>由于笔者水平有限，写作过程中难免出现错误，若有纰漏，请各位读者指正，你们的意见将会帮助我更好的进步。本文乃笔者原创，若转载，请联系作者本人，邮箱<a href="mailto:404189928@qq.com">404189928@qq.com</a>🥰</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            