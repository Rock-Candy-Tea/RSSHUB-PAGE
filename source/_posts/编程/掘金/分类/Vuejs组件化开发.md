
---
title: 'Vue.js组件化开发'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8091'
author: 掘金
comments: false
date: Mon, 16 Aug 2021 10:32:42 GMT
thumbnail: 'https://picsum.photos/400/300?random=8091'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">Vue.js组件</h1>
<p>组件是可复用的 Vue 实例。组件用于封装页面的部分功能，将功能的结构、样式、逻辑代码封装为整体。这提高了功能的复用性及可维护性，使我们更好的专注于业务逻辑。</p>
<p>组件使用时为自定义的HTML标签形式，通过组件名作为自定义标签名。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
  <span class="hljs-comment"><!-- 普通 p 标签 --></span>
  <span class="hljs-tag"><<span class="hljs-name">p</span>></span>这是p标签<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  <span class="hljs-comment"><!-- vue.js 组件 --></span>
  <span class="hljs-tag"><<span class="hljs-name">my-component</span>></span><span class="hljs-tag"></<span class="hljs-name">my-component</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vuejs.org%2Fv2%2Fguide%2Fcomponents.html" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vuejs.org/v2/guide/components.html" ref="nofollow noopener noreferrer">官方文档</a></p>
<h1 data-id="heading-1">组件注册</h1>
<p>即组件创建。</p>
<h2 data-id="heading-2">全局注册</h2>
<p>全局注册的组件可以用于任意的vue实例或组件中。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 全局组件注册，必须放在根实例创建之前</span>
Vue.component(<span class="hljs-string">'my-component'</span>, &#123; 
  <span class="hljs-attr">template</span>: <span class="hljs-string">'<div>这是我们全局注册的组件</div>'</span>
&#125;)

<span class="hljs-comment">// 根实例</span>
<span class="hljs-keyword">new</span> Vue(&#123;
  <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
  <span class="hljs-attr">data</span>: &#123;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- 这里可以改成app2等其他任意vue实例 --></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">p</span>></span>这是p标签<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  <span class="hljs-comment"><!-- vue.js 组件 --></span>
  <span class="hljs-tag"><<span class="hljs-name">my-component</span>></span><span class="hljs-tag"></<span class="hljs-name">my-component</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">组件基础</h2>
<p>组件本质上就是可复用的vue实例，所以它们可与 new Vue 接收相同的选项，例如data、methods以及生命周期钩子等。但 <code>el</code> 这样的选项是根实例特有的，组件无法接收 el 选项。</p>
<h3 data-id="heading-4">组件命名规则</h3>
<p>第一种（短横线分割），kebab-case: 'my-component'</p>
<p>第二种（首字母大写，驼峰命名），PascalCase: 'MyComponent'</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// kebab-case 进行注册</span>
Vue.component(<span class="hljs-string">'my-com-a'</span>, &#123;
  <span class="hljs-attr">template</span>: <span class="hljs-string">'<div>这是a组件的内容</div>'</span>
&#125;);
<span class="hljs-comment">// PascalCase 进行注册</span>
Vue.component(<span class="hljs-string">'MyComB'</span>, &#123;
  <span class="hljs-attr">template</span>: <span class="hljs-string">'<div>这是b组件的内容</div>'</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但无论采用哪种书写方式，在DOM中只有<code>kebab-case</code>方式可以使用。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- 组件使用 --></span>
<span class="hljs-tag"><<span class="hljs-name">my-com-a</span>></span><span class="hljs-tag"></<span class="hljs-name">my-com-a</span>></span>
<span class="hljs-tag"><<span class="hljs-name">my-com-b</span>></span><span class="hljs-tag"></<span class="hljs-name">my-com-b</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">template 选项</h3>
<p>template 选项用于设置组件的结构，最终被引入根实例或者其他组件中。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">Vue.component(<span class="hljs-string">'MyComA'</span>, &#123;
  <span class="hljs-attr">template</span>: <span class="hljs-string">`
    <div>
      这是组件 A 的内容: &#123;&#123; 1 + 2 * 3 &#125;&#125;
    </div>
  `</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">data 选项</h3>
<p>data 选项用于存储组件的数据，与根实例不同，组件的data 选项必须是函数，数据设置在函数返回值中。这种实现方式是为了确保每个组件实例都可以维护各自一份返回对象的拷贝，不会互相影响。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">Vue.component(<span class="hljs-string">'MyComA'</span>, &#123;
  <span class="hljs-attr">template</span>: <span class="hljs-string">`
    <div>
      <h3>&#123;&#123; title &#125;&#125;</h3>
      <p>&#123;&#123; content &#125;&#125;</p>
    </div>
  `</span>,
  data () &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">title</span>: <span class="hljs-string">'这是组件标题'</span>,
      <span class="hljs-attr">content</span>: <span class="hljs-string">'这是组件内容'</span>
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">局部注册</h2>
<p>局部注册的组件只能在当前实例中使用。</p>
<pre><code class="copyable">new Vue(&#123;
  el: '#app',
  data: &#123;
  &#125;,
  components: &#123;
    'my-com-a': &#123;
      template: `
        <div>
          <h3>&#123;&#123; title &#125;&#125;</h3>
          <p>&#123;&#123; content &#125;&#125;</p>
        </div>
      `,
      data () &#123;
        return &#123;
          title: '组件 A 标题',
          content: '组件 A 内容'
        &#125;
      &#125;
    &#125;,
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">my-com-a</span>></span><span class="hljs-tag"></<span class="hljs-name">my-com-a</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">单独配置组件的选项对象</h2>
<p>如果局部组件多了起来，当要修改组件选项内容时，则不是很方便。这时候，我们将组件选项对象单独提取出来进行配置就方便很多，有助于提高可维护性。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 组件 A 的选项对象</span>
<span class="hljs-keyword">var</span> MyComponentA = &#123;
  <span class="hljs-attr">template</span>: <span class="hljs-string">`
    <div>
      <h3>&#123;&#123; title &#125;&#125;</h3>
      <p>&#123;&#123; content &#125;&#125;</p>
    </div>
  `</span>,
  data () &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">title</span>: <span class="hljs-string">'组件 A 标题'</span>,
      <span class="hljs-attr">content</span>: <span class="hljs-string">'组件 A 内容'</span>
    &#125;
  &#125;
&#125;;
<span class="hljs-comment">// 组件 B 的选项对象</span>
<span class="hljs-keyword">var</span> MyComponentB = &#123;
  <span class="hljs-attr">template</span>: <span class="hljs-string">`
    <div>
      <h3>&#123;&#123; title &#125;&#125;</h3>
      <p>&#123;&#123; content &#125;&#125;</p>
    </div>
  `</span>,
  data () &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">title</span>: <span class="hljs-string">'组件 B'</span>,
      <span class="hljs-attr">content</span>: <span class="hljs-string">'组件 B 内容'</span>
    &#125;
  &#125;
&#125;

<span class="hljs-keyword">new</span> Vue(&#123;
  <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
  <span class="hljs-attr">data</span>: &#123;
  &#125;,
  <span class="hljs-attr">components</span>: &#123;
    <span class="hljs-string">'my-component-a'</span>: MyComponentA,
    MyComponentB  <span class="hljs-comment">//ES 语法表示 MyComponentB: MyComponentB</span>
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-9">组件通信</h1>
<p>组件通信，是指在组件间进行传递数据的操作。</p>
<h2 data-id="heading-10">父组件向子组件传值</h2>
<p>通过子组件的 props 选项接收父组件的传值。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 创建子组件</span>
Vue.component(<span class="hljs-string">'my-component-a'</span>, &#123;
  <span class="hljs-comment">// props 选项不要与data 选项有同名属性，否则会出现覆盖问题</span>
  <span class="hljs-attr">props</span>: [<span class="hljs-string">'title'</span>, <span class="hljs-string">'content'</span>],
  <span class="hljs-attr">template</span>: <span class="hljs-string">`
    <div>
      <h3>&#123;&#123; title &#125;&#125;</h3>
      <p>&#123;&#123; content &#125;&#125;</p>
    </div>
  `</span>
&#125;)

<span class="hljs-keyword">new</span> Vue(&#123;
  <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
  <span class="hljs-attr">data</span>: &#123;
    <span class="hljs-attr">item</span>: &#123;
      <span class="hljs-attr">title</span>: <span class="hljs-string">'这是示例标题'</span>,
      <span class="hljs-attr">content</span>: <span class="hljs-string">'这是示例内容'</span>
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用props 选项接收数据</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- 静态属性设置 --></span>
<span class="hljs-tag"><<span class="hljs-name">my-component-a</span> 
  <span class="hljs-attr">title</span>=<span class="hljs-string">"这是静态的标题"</span>
  <span class="hljs-attr">content</span>=<span class="hljs-string">"这是静态的内容"</span>
></span><span class="hljs-tag"></<span class="hljs-name">my-component-a</span>></span>

<span class="hljs-comment"><!-- 动态属性绑定：常用操作 --></span>
<span class="hljs-tag"><<span class="hljs-name">my-component-a</span>
  <span class="hljs-attr">:title</span>=<span class="hljs-string">"item.title"</span>
  <span class="hljs-attr">:content</span>=<span class="hljs-string">"item.content"</span>
></span><span class="hljs-tag"></<span class="hljs-name">my-component-a</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Props命名规则：
建议 prop 命名使用 camelCase（首字母小写，驼峰命名），父组件绑定时使用 kebab-case（短横线 <code>-</code> 分割）</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vuejs.org%2Fv2%2Fguide%2Fcomponents-props.html" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vuejs.org/v2/guide/components-props.html" ref="nofollow noopener noreferrer">官方文档</a></p>
<h3 data-id="heading-11">单向数据流</h3>
<p>父子组件间的所有 prop 都是单向下行绑定的，这称为组件prop的单向数据流特性。即父组件值改变则子组件相应prop值改变，反之，子组件相应prop值改变不会影响父组件值。</p>
<p>如果子组件要处理 prop 数据，应当存储在 data 中再操作，避免直接对 prop 数据进行处理。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">Vue.component(<span class="hljs-string">'my-component'</span>, &#123;
  <span class="hljs-attr">props</span>: [<span class="hljs-string">'innerTitle'</span>],
  <span class="hljs-attr">template</span>: <span class="hljs-string">`
    <div>
      <h3>&#123;&#123; title &#125;&#125;</h3>
    </div>
  `</span>,
  data () &#123; 
    <span class="hljs-keyword">return</span> &#123; 
      <span class="hljs-attr">title</span>: <span class="hljs-built_in">this</span>.innerTitle 
    &#125; 
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：如果 prop 为数组或对象时，子组件对其操作会影响到父组件的状态。因为数组或对象由父组件传入时，传递的是地址，由于 prop 单向数据流特性，我们虽然不能更改数组或对象的地址引用，却可以更改其内部的属性值，这导致父组件也受到影响。</p>
<p>有两种方案杜绝这种影响：</p>
<ul>
<li>在传入数组或对象时，将其拷贝存储在 data 中，然后再操作</li>
<li>避免传入数组，直接传入子组件需要的值</li>
</ul>
<h3 data-id="heading-12">props 类型</h3>
<p>在声明 props 时，还能设置可接收值的类型，假如传入值不符合设置的类型，Vue就会报错。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">props: &#123;
  <span class="hljs-attr">parStr</span>: <span class="hljs-built_in">String</span>,
  <span class="hljs-attr">parNum</span>: <span class="hljs-built_in">Number</span>,
  <span class="hljs-attr">parArr</span>: <span class="hljs-built_in">Array</span>,
  <span class="hljs-attr">parObj</span>: <span class="hljs-built_in">Object</span>,
  <span class="hljs-attr">parAny</span>: <span class="hljs-literal">undefined</span>, <span class="hljs-comment">// null</span>
  <span class="hljs-attr">parData</span>: [<span class="hljs-built_in">String</span>, <span class="hljs-built_in">Boolean</span>]
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">props 验证</h3>
<p>当 prop 需要设置多种规则时，可以将 prop 的值设置为选项对象。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">props: &#123;
  <span class="hljs-comment">// 基础的类型检查 (`null` 和 `undefined` 会通过任何类型验证)</span>
  <span class="hljs-attr">propA</span>: <span class="hljs-built_in">Number</span>,
  <span class="hljs-comment">// 多个可能的类型</span>
  <span class="hljs-attr">propB</span>: [<span class="hljs-built_in">String</span>, <span class="hljs-built_in">Number</span>],
  <span class="hljs-comment">// 必填的字符串</span>
  <span class="hljs-attr">propC</span>: &#123;
    <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
    <span class="hljs-attr">required</span>: <span class="hljs-literal">true</span>
  &#125;,
  <span class="hljs-comment">// 带有默认值的数字</span>
  <span class="hljs-attr">propD</span>: &#123;
    <span class="hljs-attr">type</span>: <span class="hljs-built_in">Number</span>,
    <span class="hljs-attr">default</span>: <span class="hljs-number">100</span>
  &#125;,
  <span class="hljs-comment">// 带有默认值的对象</span>
  <span class="hljs-attr">propE</span>: &#123;
    <span class="hljs-attr">type</span>: <span class="hljs-built_in">Object</span>,
    <span class="hljs-comment">// 对象或数组默认值必须从一个工厂函数获取</span>
    <span class="hljs-attr">default</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">return</span> &#123; <span class="hljs-attr">message</span>: <span class="hljs-string">'hello'</span> &#125;
    &#125;
  &#125;,
  <span class="hljs-comment">// 自定义验证函数</span>
  <span class="hljs-attr">propF</span>: &#123;
    <span class="hljs-attr">validator</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">value</span>) </span>&#123; 
      <span class="hljs-comment">// 返回值为false时，vue会提示报错</span>
      <span class="hljs-comment">// 这个值必须匹配下列字符串中的一个</span>
      <span class="hljs-keyword">return</span> [<span class="hljs-string">'success'</span>, <span class="hljs-string">'warning'</span>, <span class="hljs-string">'danger'</span>].indexOf(value) !== -<span class="hljs-number">1</span>
    &#125;
  &#125;
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：验证函数中，无法使用实例的data、methods等功能。因为验证过程在实例创建完成之前。</p>
<h3 data-id="heading-14">非 props 属性</h3>
<p>当父组件给子组件设置了属性，但此属性在 props 中不存在，这时会自动绑定到子组件的根元素上。</p>
<p>如果组件根元素已经存在对应属性，则会替换组件内部的值。class 与 style 属性是例外，当内外都设置时，属性会自动合并。</p>
<p>如果不希望继承父组件设置的属性，可以设置 <code>inheritAttrs: false</code>，但只适用于普通属性，class 与 style 不受影响。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">Vue.component(<span class="hljs-string">'MyComponent'</span>, &#123;
  <span class="hljs-attr">inheritAttrs</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">template</span>: <span class="hljs-string">`
  <div data-index="6"
       title="旧的title"
       class="abc" 
       style="width: 200px;">
    <p>这是组件的内容</p>
  </div>
  `</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>传值</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">my-component</span>
    <span class="hljs-attr">data-index</span>=<span class="hljs-string">"3"</span>
    <span class="hljs-attr">:title</span>=<span class="hljs-string">"'示例标题内容'"</span>
    <span class="hljs-attr">style</span>=<span class="hljs-string">"height: 200px;"</span>
    <span class="hljs-attr">class</span>=<span class="hljs-string">"colorRed"</span>
  ></span><span class="hljs-tag"></<span class="hljs-name">my-component</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">子组件向父组件传值</h2>
<p>当父组件传值后，子组件经过处理，可能还需要将处理后的结果返回给父组件。比如，商品为子组件，购物车为父组件，父组件需要获取商品个数，就需要子组件在个数变化时传值给父组件。</p>
<p>子组件向父组件传值需要通过 <code>$emit()</code> 触发自定义事件，父组件通过监听自定义事件来获取值。自定义事件命名方式建议采用 kebab-case（短横线分割）。</p>
<p>子组件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">Vue.component(<span class="hljs-string">'ProductItem'</span>, &#123;
  <span class="hljs-attr">props</span>: [<span class="hljs-string">'title'</span>],
  <span class="hljs-attr">template</span>: <span class="hljs-string">`
    <div>
      <span>商品名称： &#123;&#123; title &#125;&#125;, 商品个数： &#123;&#123; count &#125;&#125;</span>
      <button @click="countIns1">+1</button>
      <button @click="countIns5">+5</button>
    </div>
  `</span>,
  data () &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>
    &#125;
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    countIns1 () &#123;
      <span class="hljs-comment">// 1 为 需要传的值</span>
      <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">'count-change'</span>, <span class="hljs-number">1</span>);
      <span class="hljs-built_in">this</span>.count++;
    &#125;,
    countIns5 () &#123;
      <span class="hljs-comment">// 5 为 需要传的值</span>
      <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">'count-change'</span>, <span class="hljs-number">5</span>);
      <span class="hljs-built_in">this</span>.count += <span class="hljs-number">5</span>;
    &#125;
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>父组件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">new</span> Vue(&#123;
  <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
  <span class="hljs-attr">data</span>: &#123;
    <span class="hljs-attr">products</span>: [
      &#123;
        <span class="hljs-attr">id</span>: <span class="hljs-number">1</span>,
        <span class="hljs-attr">title</span>: <span class="hljs-string">'苹果一斤'</span>
      &#125;,
      &#123;
        <span class="hljs-attr">id</span>: <span class="hljs-number">2</span>,
        <span class="hljs-attr">title</span>: <span class="hljs-string">'香蕉一根'</span>
      &#125;,
      &#123;
        <span class="hljs-attr">id</span>: <span class="hljs-number">3</span>,
        <span class="hljs-attr">title</span>: <span class="hljs-string">'橙子一个'</span>
      &#125;
    ],
    <span class="hljs-attr">totalCount</span>: <span class="hljs-number">0</span>
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    onCountChange (productCount) &#123;
      <span class="hljs-built_in">this</span>.totalCount += productCount;
    &#125;
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>传值</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">h3</span>></span>购物车<span class="hljs-tag"></<span class="hljs-name">h3</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">product-item</span>
    <span class="hljs-attr">v-for</span>=<span class="hljs-string">"product in products"</span>
    <span class="hljs-attr">:key</span>=<span class="hljs-string">"product.id"</span>
    <span class="hljs-attr">:title</span>=<span class="hljs-string">"product.title"</span>
    
    @<span class="hljs-attr">count-change</span>=<span class="hljs-string">"onCountChange"</span>
  ></span><span class="hljs-tag"></<span class="hljs-name">product-item</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">p</span>></span>商品总个数为：&#123;&#123; totalCount &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">组件 与 v-model</h3>
<p>v-model 用于组件时，需要通过props与自定义函数实现。</p>
<p>子组件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 子组件</span>
<span class="hljs-keyword">var</span> ComInput = &#123;
  <span class="hljs-attr">props</span>: [<span class="hljs-string">'value'</span>],
  <span class="hljs-attr">template</span>: <span class="hljs-string">`
    <input
      type="text"
      :value="value"
      @input="onInput"
    >
  `</span>, <span class="hljs-comment">// @input="$emit('input', $event.target.value)"</span>
  <span class="hljs-attr">methods</span>: &#123;
    onInput (event) &#123;
      <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">'input'</span>, event.target.value)
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>父组件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">new</span> Vue(&#123;
  <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
  <span class="hljs-attr">data</span>: &#123;
    <span class="hljs-attr">iptValue</span>: <span class="hljs-string">''</span>
  &#125;,
  <span class="hljs-attr">components</span>: &#123;
    ComInput
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>传值</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">p</span>></span>输入框内容为：&#123;&#123; iptValue &#125;&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">com-input</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"iptValue"</span>></span><span class="hljs-tag"></<span class="hljs-name">com-input</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-17">非父子组件传值</h2>
<p>第一种方法是通过父组件中转数据：</p>
<p>兄弟组件B->父组件A->兄弟组件C</p>
<p>但当组件嵌套关系复杂时，这种中转传值方式就较为繁琐。</p>
<p>第二种方法，EventBus，也叫事件总线</p>
<h2 data-id="heading-18">EventBus</h2>
<p>EventBus（事件总线）是一个独立的事件中心，用于管理不同组件间的传值操作。</p>
<p>EventBus 通过一个新的 Vue 实例来管理组件传值操作，组件通过给实例注册事件、调用事件来实现数据传递。发送数据的组件触发bus事件，接收的组件给bus注册对应事件。</p>
<p>新建EventBus.js文件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// EventBus.js 文件内容</span>
<span class="hljs-keyword">const</span> bus = <span class="hljs-keyword">new</span> Vue()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>引入EventBus.js</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"lib/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-comment"><!-- EventBus.js放在vue.js引入之后 --></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"EventBus.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>组件A</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 商品组件</span>
Vue.component(<span class="hljs-string">'ProductItem'</span>, &#123;
  <span class="hljs-attr">template</span>: <span class="hljs-string">`
    <div>
      <span>商品名称：苹果，商品个数：&#123;&#123; count &#125;&#125;</spa
      <button
        @click="countIns"
      >+1</button>
    </div>
  `</span>,
  data () &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>
    &#125;
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    countIns () &#123;
      <span class="hljs-comment">// 给bus触发自定义事件，传递数据</span>
      bus.$emit(<span class="hljs-string">'countChange'</span>, <span class="hljs-number">1</span>);
      <span class="hljs-built_in">this</span>.count++;
    &#125;
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>组件B</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 计数组件</span>
Vue.component(<span class="hljs-string">'ProductTotal'</span>, &#123;
  <span class="hljs-attr">template</span>: <span class="hljs-string">`
    <p>总个数为： &#123;&#123; totalCount &#125;&#125;</p>
  `</span>,
  data () &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">totalCount</span>: <span class="hljs-number">0</span>
    &#125;
  &#125;,
  created () &#123;
    <span class="hljs-comment">// 给 bus 注册事件，并接收数据</span>
    bus.$on(<span class="hljs-string">'countChange'</span>, <span class="hljs-function">(<span class="hljs-params">productCount</span>) =></span> &#123;
      <span class="hljs-comment">// 实例创建完毕，可以使用 data 等功能</span>
      <span class="hljs-built_in">this</span>.totalCount += productCount;
    &#125;);
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>根实例</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 根实例</span>
<span class="hljs-keyword">new</span> Vue(&#123;
  <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
  <span class="hljs-attr">data</span>: &#123;
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>传值，EventBus可以实现任意组件间的传值，这里只是用兄弟组件做示例</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><div id=<span class="hljs-string">"app"</span>>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h3</span>></span>购物车<span class="hljs-tag"></<span class="hljs-name">h3</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">product-item</span>></span><span class="hljs-tag"></<span class="hljs-name">product-item</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">product-total</span>></span><span class="hljs-tag"></<span class="hljs-name">product-total</span>></span></span>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-19">其他通信方式</h2>
<p>有两种可以直接操作其他组件的方式：</p>
<ul>
<li>
<p>$root</p>
<p>用于访问当前组件树根实例，也可用于组件间传值。</p>
<p>不建议平常使用，一般只用于小的测试组件中。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vuejs.org%2Fv2%2Fguide%2Fcomponents-edge-cases.html%23%25E8%25AE%25BF%25E9%2597%25AE%25E6%25A0%25B9%25E5%25AE%259E%25E4%25BE%258B" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vuejs.org/v2/guide/components-edge-cases.html#%E8%AE%BF%E9%97%AE%E6%A0%B9%E5%AE%9E%E4%BE%8B" ref="nofollow noopener noreferrer">官方文档</a></p>
<p>另外<code>$parent</code>、<code>$children</code>和<code>$root</code>类似，用于便捷访问父子组件。也不建议平常使用。</p>
</li>
<li>
<p>$refs</p>
<p>ref属性，为HTML标签或组件赋予一个 ID 引用，用于在 JavaScript 里直接访问。</p>
<p>$refs，页面渲染后用于获取设置了ref属性的HTML标签或子组件。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vuejs.org%2Fv2%2Fguide%2Fcomponents-edge-cases.html%23%25E8%25AE%25BF%25E9%2597%25AE%25E5%25AD%2590%25E7%25BB%2584%25E4%25BB%25B6%25E5%25AE%259E%25E4%25BE%258B%25E6%2588%2596%25E5%25AD%2590%25E5%2585%2583%25E7%25B4%25A0" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vuejs.org/v2/guide/components-edge-cases.html#%E8%AE%BF%E9%97%AE%E5%AD%90%E7%BB%84%E4%BB%B6%E5%AE%9E%E4%BE%8B%E6%88%96%E5%AD%90%E5%85%83%E7%B4%A0" ref="nofollow noopener noreferrer">官方文档</a></p>
<p>组件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> ComA = &#123;
  <span class="hljs-attr">template</span>: <span class="hljs-string">`<div>组件A的内容：&#123;&#123; value &#125;&#125;</div>`</span>,
  data () &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">value</span>: <span class="hljs-string">'示例内容'</span>
    &#125;
  &#125;
&#125;

<span class="hljs-keyword">var</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
  <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
  <span class="hljs-attr">methods</span>: &#123;
    fn () &#123;
      <span class="hljs-built_in">this</span>.$refs.comA.value = <span class="hljs-string">'新的内容'</span>
    &#125;
  &#125;,
  <span class="hljs-attr">components</span>: &#123;
    ComA
  &#125;,
  <span class="hljs-comment">// 页面渲染后执行</span>
  mounted () &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.$refs)
    <span class="hljs-built_in">this</span>.$refs.comA.value = <span class="hljs-string">"修改后的内容"</span>
  &#125;,
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>HTML</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
  <span class="hljs-comment"><!-- 给子组件设置 ref 属性 --></span>
  <span class="hljs-tag"><<span class="hljs-name">com-a</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"comA"</span>></span><span class="hljs-tag"></<span class="hljs-name">com-a</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"fn"</span>></span>按钮<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h1 data-id="heading-20">组件插槽</h1>
<p>组件插槽可以便捷的设置组件内容。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- 没有组件插槽的组件无法像普通HTML标签那样设置内容 --></span>
<span class="hljs-tag"><<span class="hljs-name">com-a</span>></span><span class="hljs-tag"></<span class="hljs-name">com-a</span>></span>

<span class="hljs-comment"><!-- 有组件插槽的组件可以便捷的设置组件内容 --></span>
<span class="hljs-tag"><<span class="hljs-name">com-b</span>></span>这是有插槽的组件<span class="hljs-tag"></<span class="hljs-name">com-b</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-21">单个插槽</h2>
<p>需要使用<code><slot></slot></code>进行插槽设置。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">Vue.component(<span class="hljs-string">'ComA'</span>, &#123;
  <span class="hljs-attr">template</span>: <span class="hljs-string">`
    <div>
      <h3>组件标题</h3>
      <slot>
        这是插槽的默认内容
      </slot>
    </div>
  `</span>,
  data () &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">value</span>: <span class="hljs-string">'子组件的数据'</span>
    &#125;
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>设置组件内容</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">com-a</span>></span>这是组件的内容<span class="hljs-tag"></<span class="hljs-name">com-a</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">com-a</span>></span>
    这是第二个组件的内容：
    <span class="hljs-tag"><<span class="hljs-name">span</span>></span>这是span的内容<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">com-a</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">com-a</span>></span>
    这里是父组件的视图模板，只能使用父组件的数据:
    &#123;&#123; parValue &#125;&#125;
  <span class="hljs-tag"></<span class="hljs-name">com-a</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">com-a</span>></span><span class="hljs-tag"></<span class="hljs-name">com-a</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-22">具名插槽</h2>
<p>如果组建中有多个位置需要设置插槽，根据需要给<code><slot></code>设置name，这种有名称的插槽称为具名插槽。</p>
<p>如果<code><slot></code>未设置name，则默认name为default。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 子组件 </span>
Vue.component(<span class="hljs-string">'ComA'</span>, &#123;
  <span class="hljs-attr">template</span>: <span class="hljs-string">`
    <div>
      <header>
        <slot name="header"></slot>
      </header>
      <main>
        <slot></slot>
      </main>
      <footer>
        <slot name="footer"></slot>
      </footer>
    </div>
  `</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>设置组件内容</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">com-a</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-slot:header</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">h3</span>></span>组件的头部内容<span class="hljs-tag"></<span class="hljs-name">h3</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
    <span class="hljs-comment"><!-- <template v-slot:default>
      <p>组件的主体内容1</p>
      <p>组件的主体内容2</p>
    </template> --></span>
    <span class="hljs-comment"><!-- 等同于 上面注释部分 --></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>组件的主体内容1<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>组件的主体内容2<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-comment"><!-- v-slot: 可简写为 # --></span>
    <span class="hljs-tag"><<span class="hljs-name">template</span> #<span class="hljs-attr">footer</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span>></span>组件底部内容<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">com-a</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-23">作用域插槽</h2>
<p>一般插槽只能使用父组件数据，而作用域插槽可以使用子组件数据。</p>
<p>组件将需要被插槽使用的数据通过v-bind绑定给<code><slot></code>，这种用于给插槽传递数据的属性称为插槽prop。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 子组件B的选项对象</span>
<span class="hljs-keyword">var</span> ComB = &#123;
  <span class="hljs-attr">template</span>: <span class="hljs-string">`
    <div>
      <p>组件B的内容: </p>
      <slot
        :value="value"
        :num="num"
      ></slot>
    </div>
  `</span>,
  data () &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">value</span>: <span class="hljs-string">'这是组件B内部的数据'</span>,
      <span class="hljs-attr">num</span>: <span class="hljs-number">200</span>
    &#125;
  &#125;
&#125;

<span class="hljs-comment">// 子组件A的选项对象</span>
<span class="hljs-keyword">var</span> ComA = &#123;
  <span class="hljs-attr">template</span>: <span class="hljs-string">`
    <div>
      <p>组件A的内容: </p>
      <slot
        v-bind:value="value"
        :num="num"
      ></slot>
      <slot name="footer"
        :value="value"
      ></slot>
    </div>
  `</span>,
  data () &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">value</span>: <span class="hljs-string">'这是组件A内部的数据'</span>,
      <span class="hljs-attr">num</span>: <span class="hljs-number">100</span>
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>设置组件内容</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
  <span class="hljs-comment"><!-- 多个插槽的作用域插槽书写方式 --></span>
  <span class="hljs-tag"><<span class="hljs-name">com-a</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-slot:default</span>=<span class="hljs-string">"dataObj"</span>></span>
      &#123;&#123; dataObj.value &#125;&#125;
      &#123;&#123; dataObj.num &#125;&#125;
    <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
    
    <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-slot:footer</span>=<span class="hljs-string">"dataObj"</span>></span>
      &#123;&#123; dataObj.value &#125;&#125;
    <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">com-a</span>></span>
  <span class="hljs-comment"><!-- 只具有默认插槽的作用域插槽书写方式 --></span>
  <span class="hljs-comment"><!-- <com-b v-slot="dataObj"> --></span>
  <span class="hljs-tag"><<span class="hljs-name">com-b</span> #<span class="hljs-attr">default</span>=<span class="hljs-string">"dataObj"</span>></span>
    &#123;&#123; dataObj &#125;&#125;
  <span class="hljs-tag"></<span class="hljs-name">com-b</span>></span>
  <span class="hljs-comment"><!-- 通过 ES6 的解构操作接收作用域插槽的数据 --></span>
  <span class="hljs-tag"><<span class="hljs-name">com-b</span> <span class="hljs-attr">v-slot</span>=<span class="hljs-string">"&#123; value, num &#125;"</span>></span>
    &#123;&#123; value &#125;&#125;
    &#123;&#123; num &#125;&#125;
  <span class="hljs-tag"></<span class="hljs-name">com-b</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-24">内置组件</h1>
<h2 data-id="heading-25">动态组件</h2>
<p>动态组件适用于多个组件频繁切换的处理。例如选项卡切换等。</p>
<p><code><component></code>用于将一个‘元组件’渲染为动态组件，以is属性决定渲染哪个组件。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- component 设置动态组件 --></span>
<span class="hljs-tag"><<span class="hljs-name">component</span> <span class="hljs-attr">:is</span>=<span class="hljs-string">"currentCom"</span>></span><span class="hljs-tag"></<span class="hljs-name">component</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们动态地改变currentCom指向的组件就可以实现组件切换了。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
  <span class="hljs-comment"><!-- 按钮代表选项卡的标题功能 --></span>
  <span class="hljs-tag"><<span class="hljs-name">button</span>
    <span class="hljs-attr">v-for</span>=<span class="hljs-string">"title in titles"</span>
    <span class="hljs-attr">:key</span>=<span class="hljs-string">"title"</span>
    @<span class="hljs-attr">click</span>=<span class="hljs-string">"currentCom = title"</span>
  ></span>
    &#123;&#123; title &#125;&#125;
  <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
  <span class="hljs-comment"><!-- component 设置动态组件 --></span>
  <span class="hljs-tag"><<span class="hljs-name">component</span> <span class="hljs-attr">:is</span>=<span class="hljs-string">"currentCom"</span>></span><span class="hljs-tag"></<span class="hljs-name">component</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"lib/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="handlebars"><span class="xml">
  // 设置要切换的子组件选项对象
  var ComA = &#123;
    template: `<span class="hljs-tag"><<span class="hljs-name">p</span>></span>这是组件A的内容：<span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  &#125;;  
  var ComB = &#123;
    template: `<span class="hljs-tag"><<span class="hljs-name">p</span>></span>这是组件B的内容：<span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  &#125;;
  var ComC = &#123;
    template: `<span class="hljs-tag"><<span class="hljs-name">p</span>></span>这是组件C的内容：<span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
  &#125;;
  new Vue(&#123;
    el: '#app',
    data: &#123;
      // 所有组件名称
      titles: ['ComA', 'ComB', 'ComC'],
      // 当前组件名称
      currentCom: 'ComA'
    &#125;,
    components: &#123;
      ComA, ComB, ComC
    &#125;
  &#125;);
</span></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-26">keep-alive组件</h2>
<p>在前面使用动态组件切换时，会频繁的进行重新渲染操作且不保留组件状态，假如我们希望动态组件切换时，避免重新渲染或保留组件状态，我们就可以使用keep-alive组件。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- 通过 include 设置哪些组件会被缓存 --></span>
<span class="hljs-comment"><!-- 字符串形式的逗号分隔符间不能有空格 --></span>
<span class="hljs-comment"><!-- <keep-alive include="ComA,ComB,ComC"> --></span>
<span class="hljs-comment"><!-- <keep-alive :include="['ComA', 'ComB', 'ComC']"> --></span>
<span class="hljs-comment"><!-- <keep-alive :include="/Com[ABC]/"> --></span>
<span class="hljs-comment"><!-- 通过 exclude 设置哪些组件不会被缓存 --></span>
<span class="hljs-comment"><!-- <keep-alive exclude="ComD"> --></span>
<span class="hljs-comment"><!-- <keep-alive :exclude="['ComD']"> --></span>
<span class="hljs-comment"><!-- <keep-alive :exclude="/ComD/"> --></span>
   
<span class="hljs-comment"><!-- 设置最大缓存组件数 --></span>
<span class="hljs-tag"><<span class="hljs-name">keep-alive</span> <span class="hljs-attr">max</span>=<span class="hljs-string">"2"</span>></span>
  <span class="hljs-comment"><!-- 动态组件 --></span>
  <span class="hljs-tag"><<span class="hljs-name">component</span> <span class="hljs-attr">:is</span>=<span class="hljs-string">"currentCom"</span>></span><span class="hljs-tag"></<span class="hljs-name">component</span>></span>
<span class="hljs-tag"></<span class="hljs-name">keep-alive</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-27">过渡组件</h2>
<p>用于在Vue插入、更新或者移除DOM时，提供多种不同方式的应用过渡、动画效果。
主要有：</p>
<ul>
<li>transition组件</li>
<li>自定义过渡类名</li>
<li>transition-group组件</li>
</ul>
<h2 data-id="heading-28">transition组件</h2>
<p>用于给元素和组件提供进入或离开过渡：</p>
<ul>
<li>条件渲染（v-if）</li>
<li>条件展示（v-show）</li>
<li>动态组件</li>
<li>组件根节点</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">transition</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"show"</span>></span>hello world<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"></<span class="hljs-name">transition</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>组件提供了6个class，用于设置过渡的具体效果。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
  <span class="hljs-comment">/* 用于设置出场的最终状态 */</span>
  <span class="hljs-selector-class">.v-leave-to</span> &#123;
    <span class="hljs-attribute">opacity</span>: <span class="hljs-number">0</span>;
  &#125;
  <span class="hljs-comment">/* 用于设置过渡的执行过程 */</span>
  <span class="hljs-selector-class">.v-leave-active</span> &#123;
    <span class="hljs-attribute">transition</span>: opacity <span class="hljs-number">1s</span>;
  &#125;
  <span class="hljs-comment">/* 用于设置入场的初始状态 */</span>
  <span class="hljs-selector-class">.v-enter</span> &#123;
    <span class="hljs-attribute">opacity</span>: <span class="hljs-number">0</span>;
  &#125;
  <span class="hljs-comment">/* 用于设置入场的最终状态 */</span>
  <span class="hljs-selector-class">.v-enter-to</span> &#123;
    <span class="hljs-attribute">opacity</span>: <span class="hljs-number">0.5</span>;
  &#125;
  <span class="hljs-comment">/* 用于设置入场的过程 */</span>
  <span class="hljs-selector-class">.v-enter-active</span> &#123;
    <span class="hljs-attribute">transition</span>: all <span class="hljs-number">1s</span>;
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-29">transition组件相关属性</h3>
<ul>
<li>
<p>给组件设置name属性，可用于给多个元素、组件设置不同的过渡效果，这时需要将v-更改为对应name-的形式。</p>
<p>例如：</p>
<p><code><transition name="demo"></code>的对应类名前缀为，demo-enter等。</p>
</li>
<li>
<p>通过设置appear属性，可以让组件在初始渲染时实现过渡。
<code><transition appear"></code></p>
</li>
</ul>
<h2 data-id="heading-30">自定义过渡类名</h2>
<p>自定义类名比普通类名优先级更高，在使用第三方CSS动画库时非常有用。</p>
<p>用于设置自定义过渡类名的属性如下：</p>
<ul>
<li>enter-class</li>
<li>enter-active-class</li>
<li>enter-to-class</li>
<li>leave-class</li>
<li>leave-active-class</li>
<li>leave-to-class</li>
</ul>
<p>用于设置初始过渡类名的属性如下：</p>
<ul>
<li>appear-class</li>
<li>appear-to-class</li>
<li>appear-active-class</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">transition</span>
  <span class="hljs-attr">enter-active-class</span>=<span class="hljs-string">"test"</span>
  <span class="hljs-attr">leave-active-class</span>=<span class="hljs-string">"test"</span>
></span>
  <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"show"</span>></span>这是 p 标签<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"></<span class="hljs-name">transition</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-31">Animate.css</h3>
<p>Animate.css 是一个第三方CSS动画库，通过设置类名来给元素添加各种动画效果。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fanimate.style%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://animate.style/" ref="nofollow noopener noreferrer">Animate.css官网</a></p>
<p>CDN引用</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">link</span>
  <span class="hljs-attr">rel</span>=<span class="hljs-string">"stylesheet"</span>
  <span class="hljs-attr">href</span>=<span class="hljs-string">"https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"</span>
/></span>
<span class="hljs-comment"><!-- 不需要添加 animate__ 前缀的兼容版本，但是官方建议使用上面的完整版本 --></span>
<span class="hljs-comment"><!-- "https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.0.0/animate.compat.css" --></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- 通过自定义过渡类名设置，给组件添加第三方动画库的类名效果 --></span>
<span class="hljs-tag"><<span class="hljs-name">transition</span>
  <span class="hljs-attr">enter-active-class</span>=<span class="hljs-string">"animate__bounceInDown"</span>
  <span class="hljs-attr">leave-active-class</span>=<span class="hljs-string">"animate__bounceOutDown"</span>
></span>
  <span class="hljs-comment"><!-- 必须给要使用动画的元素设置基础类名 animate__animated --></span>
  <span class="hljs-tag"><<span class="hljs-name">p</span> 
    <span class="hljs-attr">v-if</span>=<span class="hljs-string">"show"</span>
    <span class="hljs-attr">class</span>=<span class="hljs-string">"animate__animated"</span>  
  ></span>hello world<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"></<span class="hljs-name">transition</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意事项：</p>
<ul>
<li>animate__前缀版本 与 compat版本的选择问题，推荐选择前缀版本</li>
<li>基础类名 animate__animated 不能忘</li>
</ul>
<h2 data-id="heading-32">transition-group组件</h2>
<p><code><transition-group></code>用于给系列元素设置过渡动画。</p>
<ul>
<li>tag属性用于设置容器元素，默认为<code><span></code></li>
<li>过渡会应用于内部元素，而不是容器</li>
<li>子节点须有独立的key，动画才能正常工作</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">transition-group</span>
  <span class="hljs-attr">tag</span>=<span class="hljs-string">"ul"</span>
></span>
  <span class="hljs-tag"><<span class="hljs-name">li</span>
    <span class="hljs-attr">v-for</span>=<span class="hljs-string">"item in items"</span>
    <span class="hljs-attr">:key</span>=<span class="hljs-string">"item.id"</span>
  ></span>
    &#123;&#123; item.title &#125;&#125;
  <span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"></<span class="hljs-name">transition-group</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当列表元素变更导致元素位移，可通过 .v-move 类名设置移动时的效果</p>
<pre><code class="hljs language-html copyable" lang="html">.v-move &#123;
  transition: all .5s;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其他过渡样式的设置和transition组件一样。</p></div>  
</div>
            