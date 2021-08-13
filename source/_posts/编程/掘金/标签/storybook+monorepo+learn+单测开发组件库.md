
---
title: 'storybook+monorepo+learn+单测开发组件库'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=7980'
author: 掘金
comments: false
date: Thu, 12 Aug 2021 05:47:46 GMT
thumbnail: 'https://picsum.photos/400/300?random=7980'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第11天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h3 data-id="heading-0">组件驱动开发</h3>
<p>CDD</p>
<ul>
<li>CDD(Component-Driven Development)
<ul>
<li>自下而上</li>
<li>从组件级别开始，到页面级别结束</li>
<li>先从相对完善的设计中，抽象出组件，先隔离开发组件，然后在开发页面。</li>
</ul>
</li>
<li>CDD的好处
<ul>
<li>组件在最大程度被重用</li>
<li>并行开发， 可以让组件的开发在不同的团队之间共享任务。</li>
<li>可视化测试</li>
</ul>
</li>
<li>主要完成：
<ol>
<li>处理组件的边界情况</li>
<li>快速原型开发</li>
<li>组件开发</li>
<li>开发组件库的最佳实践方式
<ol>
<li>storybook</li>
<li>monorepo</li>
</ol>
</li>
<li>基于模板生成包的结构</li>
<li>Lerna + yarn workspances</li>
<li>组件测试</li>
<li>rollup打包</li>
</ol>
</li>
</ul>
<h4 data-id="heading-1">处理组件的边界情况</h4>
<ol>
<li>
<p>$root</p>
<ol>
<li>所有的组件都有，该组件的$root属性就是根实例vm</li>
</ol>
<pre><code class="hljs language-html copyable" lang="html">root.vue
<span class="hljs-comment"><!-- 
    小型应用中可以在 vue 根实例里存储共享数据
    组件中可以通过 $root 访问根实例中成员，该成员都是响应式的
--></span>
$root.title: &#123;&#123; $root.title &#125;&#125;
<span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"$root.handleClick"</span>></span>获取title<span class="hljs-tag"></<span class="hljs-name">button</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span>></span><span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"$root.title = 'hello $root'"</span>></span>改变title<span class="hljs-tag"></<span class="hljs-name">button</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>p</mi><mi>a</mi><mi>r</mi><mi>e</mi><mi>n</mi><mi>t</mi><mi mathvariant="normal">/</mi></mrow><annotation encoding="application/x-tex">parent/</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathnormal">p</span><span class="mord mathnormal">a</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">e</span><span class="mord mathnormal">n</span><span class="mord mathnormal">t</span><span class="mord">/</span></span></span></span></span>children</p>
<ol>
<li>$parent  可以获取到父组件中的成员，可以直接操作父组件中成员，可以替换prop的使用，可以直接在子组件中修改父组件中的成员，如果应用复杂，则会导致应用数据流不清晰，难以维护。而且在组件嵌套层级多的话，会更麻烦。</li>
<li>$children 可以获取到当前组件的所有子组件， 是一个数组，代码的可读性不高，要用索引的方式获取单个组件。可以使用ref。
<ol>
<li>只能获取组件，不能获取原始的标签</li>
</ol>
</li>
</ol>
</li>
<li>
<p>$refs</p>
<ol>
<li>通过this.<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>r</mi><mi>e</mi><mi>f</mi><mtext>可以获取当前</mtext><mi>t</mi><mi>h</mi><mi>i</mi><mi>s</mi><mtext>也就是当前组件的所有带有</mtext><mi>r</mi><mi>e</mi><mi>f</mi><mtext>属性的组件。每一条数据都是一个组件实例</mtext><mo>:</mo><mi>V</mi><mi>u</mi><mi>e</mi><mi>C</mi><mi>o</mi><mi>m</mi><mi>p</mi><mi>o</mi><mi>n</mi><mi>e</mi><mi>n</mi><mi>t</mi><mtext>。如果</mtext><mi>r</mi><mi>e</mi><mi>f</mi><mtext>用在普通</mtext><mi>h</mi><mi>t</mi><mi>m</mi><mi>l</mi><mtext>标签上，我们通过</mtext></mrow><annotation encoding="application/x-tex">ref可以获取当前this也就是当前组件的所有带有ref属性的组件。每一条数据都是一个组件实例:VueComponent。如果ref用在普通html标签上，我们通过</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">e</span><span class="mord mathnormal" style="margin-right:0.10764em;">f</span><span class="mord cjk_fallback">可</span><span class="mord cjk_fallback">以</span><span class="mord cjk_fallback">获</span><span class="mord cjk_fallback">取</span><span class="mord cjk_fallback">当</span><span class="mord cjk_fallback">前</span><span class="mord mathnormal">t</span><span class="mord mathnormal">h</span><span class="mord mathnormal">i</span><span class="mord mathnormal">s</span><span class="mord cjk_fallback">也</span><span class="mord cjk_fallback">就</span><span class="mord cjk_fallback">是</span><span class="mord cjk_fallback">当</span><span class="mord cjk_fallback">前</span><span class="mord cjk_fallback">组</span><span class="mord cjk_fallback">件</span><span class="mord cjk_fallback">的</span><span class="mord cjk_fallback">所</span><span class="mord cjk_fallback">有</span><span class="mord cjk_fallback">带</span><span class="mord cjk_fallback">有</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">e</span><span class="mord mathnormal" style="margin-right:0.10764em;">f</span><span class="mord cjk_fallback">属</span><span class="mord cjk_fallback">性</span><span class="mord cjk_fallback">的</span><span class="mord cjk_fallback">组</span><span class="mord cjk_fallback">件</span><span class="mord cjk_fallback">。</span><span class="mord cjk_fallback">每</span><span class="mord cjk_fallback">一</span><span class="mord cjk_fallback">条</span><span class="mord cjk_fallback">数</span><span class="mord cjk_fallback">据</span><span class="mord cjk_fallback">都</span><span class="mord cjk_fallback">是</span><span class="mord cjk_fallback">一</span><span class="mord cjk_fallback">个</span><span class="mord cjk_fallback">组</span><span class="mord cjk_fallback">件</span><span class="mord cjk_fallback">实</span><span class="mord cjk_fallback">例</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">:</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span></span><span class="base"><span class="strut" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="mord mathnormal" style="margin-right:0.22222em;">V</span><span class="mord mathnormal">u</span><span class="mord mathnormal">e</span><span class="mord mathnormal" style="margin-right:0.07153em;">C</span><span class="mord mathnormal">o</span><span class="mord mathnormal">m</span><span class="mord mathnormal">p</span><span class="mord mathnormal">o</span><span class="mord mathnormal">n</span><span class="mord mathnormal">e</span><span class="mord mathnormal">n</span><span class="mord mathnormal">t</span><span class="mord cjk_fallback">。</span><span class="mord cjk_fallback">如</span><span class="mord cjk_fallback">果</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">e</span><span class="mord mathnormal" style="margin-right:0.10764em;">f</span><span class="mord cjk_fallback">用</span><span class="mord cjk_fallback">在</span><span class="mord cjk_fallback">普</span><span class="mord cjk_fallback">通</span><span class="mord mathnormal">h</span><span class="mord mathnormal">t</span><span class="mord mathnormal">m</span><span class="mord mathnormal" style="margin-right:0.01968em;">l</span><span class="mord cjk_fallback">标</span><span class="mord cjk_fallback">签</span><span class="mord cjk_fallback">上</span><span class="mord cjk_fallback">，</span><span class="mord cjk_fallback">我</span><span class="mord cjk_fallback">们</span><span class="mord cjk_fallback">通</span><span class="mord cjk_fallback">过</span></span></span></span></span>refs获取到的就是普通dom对象，如果$refs用在组件上，则获取到的是该this所对应的ref的组件对象，等待组件渲染完毕之后，才能用ref获取。</li>
</ol>
</li>
<li>
<p>依赖注入 provide/inject</p>
<ol>
<li>
<p>如果 父组件向子组件传递数据的话，父组件数据改变，那么子组件也会更新，因为在updateChildren的时候，传入了<em>propsData</em>数据，</p>
<p><code>const propOptions: *any* = *vm*.$options.props // wtf flow?</code>  // 赋值动作。所以如果传递的是引用数据类型，那么还是同一个引用。 但是如果子组件数据改变了，那么父组件是不会改变的，因为updateChildren的时候， 仅仅改变的是本组件。因为updateChildren的时候，没有传入了<em>propsData</em>数据，因为是否有<em>propsData</em> 是根据 此组件是否有props数据的，而且<em>propsData</em> 的值是此组件的props属性的值。so，父组件不会改变。</p>
</li>
<li>
<p>provide/inject 亦如是。</p>
</li>
<li>
<p>结论：所以修改传递过来的数据只能本组件的使用的数据</p>
</li>
<li>
<p>首先需要在父组件中使用provide提供成员，子组件中使用inject接收父组件中的成员，相当于大范围的props。带来的影响：组件之间的耦合度变高，子组件依赖父组件。使得重构变得困难。</p>
</li>
</ol>
</li>
<li>
<p><span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>a</mi><mi>t</mi><mi>t</mi><mi>r</mi><mi>s</mi><mi mathvariant="normal">/</mi></mrow><annotation encoding="application/x-tex">attrs / </annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathnormal">a</span><span class="mord mathnormal">t</span><span class="mord mathnormal">t</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">s</span><span class="mord">/</span></span></span></span></span>listeners</p>
<ul>
<li>
<p>$attrs</p>
<ul>
<li>
<p>把父组件中没有用props接收的属性绑定到内部组件</p>
<ol>
<li><strong>从父组件传给自定义子组件的属性，没有 被props 接收的属性会自动设置到子组件内部的最外层标签上，如果是 class 和 style 的话，会合并最外层标签的 class 和 style。</strong></li>
</ol>
<pre><code class="hljs language-html copyable" lang="html">父组件引用子组件
<span class="hljs-tag"><<span class="hljs-name">myinput</span> <span class="hljs-attr">required</span> <span class="hljs-attr">placeholder</span>=<span class="hljs-string">"Enter your username"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"theme-dark"</span><span class="hljs-attr">style</span>=<span class="hljs-string">"color: red"</span> <span class="hljs-attr">data-test</span>=<span class="hljs-string">"test"</span>></span>
子组件
<span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"myipt"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"font-size: 14px"</span> /></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
渲染到浏览器上的情况
<span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"myipt theme-dark"</span> <span class="hljs-attr">required</span>=<span class="hljs-string">"required"</span> <span class="hljs-attr">placeholder</span>=<span class="hljs-string">"Enter your username"</span> <span class="hljs-attr">data-test</span>=<span class="hljs-string">"test"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"color: red; font-size: 14px;"</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>
<p><strong>在 1 的基础上如果使用了props接收。</strong></p>
<pre><code class="hljs language-html copyable" lang="html">myinput组件中使用props接收： props: ['placeholder', 'style', 'class']  // 组件报错，"class/style" is a reserved attribute and cannot be used as component prop.

渲染到浏览器上的情况
<span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"myipt theme-dark"</span> <span class="hljs-attr">required</span>=<span class="hljs-string">"required"</span> <span class="hljs-attr">data-test</span>=<span class="hljs-string">"test"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"font-size: 14px; color: red;"</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>a</mi><mi>t</mi><mi>t</mi><mi>r</mi><mi>s</mi><mtext>与</mtext><mi>p</mi><mi>r</mi><mi>o</mi><mi>p</mi><mi>s</mi><mtext>是互斥的，如果没有用</mtext><mi>p</mi><mi>r</mi><mi>o</mi><mi>p</mi><mi>s</mi><mtext>接收父组件传递过来的属性的话，则会放到</mtext></mrow><annotation encoding="application/x-tex">attrs 与 props是互斥的，如果没有用props接收父组件传递过来的属性的话，则会放到</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.8777699999999999em;vertical-align:-0.19444em;"></span><span class="mord mathnormal">a</span><span class="mord mathnormal">t</span><span class="mord mathnormal">t</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">s</span><span class="mord cjk_fallback">与</span><span class="mord mathnormal">p</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">o</span><span class="mord mathnormal">p</span><span class="mord mathnormal">s</span><span class="mord cjk_fallback">是</span><span class="mord cjk_fallback">互</span><span class="mord cjk_fallback">斥</span><span class="mord cjk_fallback">的</span><span class="mord cjk_fallback">，</span><span class="mord cjk_fallback">如</span><span class="mord cjk_fallback">果</span><span class="mord cjk_fallback">没</span><span class="mord cjk_fallback">有</span><span class="mord cjk_fallback">用</span><span class="mord mathnormal">p</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">o</span><span class="mord mathnormal">p</span><span class="mord mathnormal">s</span><span class="mord cjk_fallback">接</span><span class="mord cjk_fallback">收</span><span class="mord cjk_fallback">父</span><span class="mord cjk_fallback">组</span><span class="mord cjk_fallback">件</span><span class="mord cjk_fallback">传</span><span class="mord cjk_fallback">递</span><span class="mord cjk_fallback">过</span><span class="mord cjk_fallback">来</span><span class="mord cjk_fallback">的</span><span class="mord cjk_fallback">属</span><span class="mord cjk_fallback">性</span><span class="mord cjk_fallback">的</span><span class="mord cjk_fallback">话</span><span class="mord cjk_fallback">，</span><span class="mord cjk_fallback">则</span><span class="mord cjk_fallback">会</span><span class="mord cjk_fallback">放</span><span class="mord cjk_fallback">到</span></span></span></span></span>attrs上，否则放到props上。</p>
</li>
<li>
<p>一般用法：v-bind="$attrs"</p>
</li>
<li>
<p>**如果要禁用掉 1 的话， 则设置inheritAttrs: false， 但是$attrs是可以用的，只是把 1 效果禁用掉了。**但是这不会改变 class 和 style， class和style还是会设置到最外层的根元素上的。</p>
</li>
</ol>
</li>
</ul>
</li>
<li>
<p>$listeners</p>
<ul>
<li>把父组件中的dom原生事件绑定到内部组件。
<ol>
<li>一般用法： v-on="$listeners"</li>
<li>也是展开传递过来的事件，但是没有互斥</li>
<li>与我原先想的一样，就是展开传递函数，没有额外的副作用。</li>
</ol>
</li>
</ul>
</li>
</ul>
</li>
</ol>
<h4 data-id="heading-2">快速原型开发</h4>
<p>vue serve</p>
<ul>
<li>vue serve 如果不指定默认参数默认会在当前目录找以下的入口文件
<ul>
<li>main.js、 index.js 、App.vue、 app.vue</li>
</ul>
</li>
<li>可以指定要加载的组件
<ul>
<li>vue serve ./src/login.vue</li>
</ul>
</li>
</ul>
<h4 data-id="heading-3">快速原型开发 - elementui</h4>
<ul>
<li>初始化package.json
<ul>
<li>npm init -y</li>
</ul>
</li>
<li>安装element ui
<ul>
<li>vue add element  // 使用vue add 命令添加vue-clielement插件</li>
</ul>
</li>
<li>加载elementui，使用Vue.use() 安装插件</li>
<li>创建main.js 使用vue serve 启动应用程序</li>
</ul>
<h4 data-id="heading-4">组件分类</h4>
<ul>
<li>第三方组件 elementui  iview</li>
<li>基础组件</li>
<li>业务组件</li>
</ul>
<h4 data-id="heading-5">表单验证</h4>
<ol>
<li>在form-item中对此表单项进行验证</li>
</ol>
<ul>
<li>form-item组件需要获取到要验证的数据和验证的规则，而验证的数据和验证的规则都在form组件上， 也就是:model="user"  :rules="rules"。我们可以直接把form这个组件对象传给form-item。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// form-item </span>
<span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.prop) <span class="hljs-keyword">return</span>
    <span class="hljs-keyword">const</span> &#123; rules, model &#125; = <span class="hljs-built_in">this</span>.Form
    <span class="hljs-keyword">const</span> value = rules[<span class="hljs-built_in">this</span>.prop]
    <span class="hljs-keyword">const</span> key = model[<span class="hljs-built_in">this</span>.prop]
    <span class="hljs-comment">// 如果规则中没有配置这个属性的话，就直接通过</span>
    <span class="hljs-keyword">if</span> (!value) <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resolve()
    <span class="hljs-comment">// 设置校验描述符</span>
    <span class="hljs-keyword">const</span> descriptor = &#123;
        [<span class="hljs-built_in">this</span>.prop]: value
    &#125;
    <span class="hljs-keyword">const</span> validator = <span class="hljs-keyword">new</span> Schema(descriptor)
    <span class="hljs-comment">// 进行校验</span>
    <span class="hljs-keyword">return</span> validator.validate(&#123; [<span class="hljs-built_in">this</span>.prop]: key &#125;, <span class="hljs-function"><span class="hljs-params">errors</span> =></span> &#123;
        <span class="hljs-keyword">if</span> (errors) &#123;
            <span class="hljs-built_in">this</span>.errMessage = errors[<span class="hljs-number">0</span>].message
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-built_in">this</span>.errMessage = <span class="hljs-string">''</span>
        &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>实现input/blur/change 事件时校验。</p>
<ul>
<li>在单选框/多选框/input等组件上，在input/blur等事件处理函数上，递归查找上层的form-item， 找到之后，调用form-item的validate方法，而这个操作决定了form-item中的errormsg的显示与否.</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">inputHandle (e) &#123;
    <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">'input'</span>, e.target.value)
    <span class="hljs-comment">// 递归查找formItem组件，执行validate， 控制errorMsg</span>
    <span class="hljs-keyword">const</span> searchFormItem = <span class="hljs-function">(<span class="hljs-params">parent</span>) =></span> &#123;
        <span class="hljs-keyword">if</span> (!parent) <span class="hljs-keyword">return</span>
        <span class="hljs-keyword">if</span> (parent.$options.name !== <span class="hljs-string">'LgFormItem'</span>) &#123;
            parent = parent.$parent
            <span class="hljs-keyword">return</span> searchFormItem(parent)
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-comment">// hasFormItem = parent</span>
            <span class="hljs-keyword">return</span> parent
        &#125;
    &#125;
    <span class="hljs-keyword">const</span> formItem = searchFormItem(<span class="hljs-built_in">this</span>.$parent)
    formItem && formItem.validate()<span class="hljs-comment">// 也可以使用发布订阅模式， 在此发布，在formItem中订阅，并调用formItem的validate方法，区别是啥？</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>用户调用form组件的validate方法传入callback进行校验</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">validate</span>(<span class="hljs-params">cb</span>)</span> &#123;
    <span class="hljs-keyword">let</span> findItem = [] <span class="hljs-comment">// 找到所有的children</span>
    <span class="hljs-keyword">const</span> searchFormItem = <span class="hljs-function"><span class="hljs-params">children</span> =></span> &#123;
        <span class="hljs-keyword">if</span> (!children || !<span class="hljs-built_in">Array</span>.isArray(children) || children.length === <span class="hljs-number">0</span>)
            <span class="hljs-keyword">return</span>
        children.map(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
            <span class="hljs-keyword">if</span> (item.$options.name !== <span class="hljs-string">'LgFormItem'</span>) &#123;
                searchFormItem(item.$children)
            &#125; <span class="hljs-keyword">else</span> &#123;
                findItem.push(item)
            &#125;
        &#125;)
    &#125;

    <span class="hljs-comment">// 获取到所有是form-item 的 children 放到findItem中</span>
    searchFormItem(<span class="hljs-built_in">this</span>.$children)
    <span class="hljs-comment">// 过滤出有prop属性的组件</span>
    findItem = findItem.filter(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item.prop)

    <span class="hljs-comment">// 获取校验的结果</span>
    <span class="hljs-keyword">const</span> tasks = findItem
    .filter(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item.$options.name === <span class="hljs-string">'LgFormItem'</span>)
    .map(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item.validate())

    <span class="hljs-comment">// 执行用户传入的提交组件时的callback</span>
    <span class="hljs-built_in">Promise</span>.all(tasks)
        .then(<span class="hljs-function">() =></span> cb(<span class="hljs-literal">true</span>))
        .catch(<span class="hljs-function">() =></span> cb(<span class="hljs-literal">false</span>))
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h5 data-id="heading-6">Monorepo</h5>
<p>管理开发库的项目的组织方式</p>
<ul>
<li>
<p>Multirepo(Multiple Repository)</p>
<ul>
<li>
<p>使用monorepo的时候要把所有的包放到一个指定的文件夹下，一般这个文件夹叫packages</p>
</li>
<li>
<p>每一个包对应一个项目</p>
</li>
<li>
<p>每一个包都可以单独发布，单独测试，统一管理依赖</p>
</li>
<li>
<p>一般是在项目的根目录下建立 packages 文件夹</p>
</li>
<li>
<p>vue3就是采用了这种方式</p>
<p><code>https://github.com/vuejs/vue-next/blob/master/package.json</code></p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-string">"private"</span>: <span class="hljs-literal">true</span>   <span class="hljs-comment">// 禁止把当前的包发布到npm</span>
<span class="hljs-string">"workspaces"</span>: [
    <span class="hljs-string">"packages/*"</span>  <span class="hljs-comment">// 开启yarn 的工作区， (会将package下的所有文件发布到npm上)</span>
],
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>vue根目录下的packages下的每一个文件夹都是一个包，这里的每个包都可以单独发布、下载和使用。</p>
<ul>
<li>每个包下面有这些相同的文件结构</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">__tests__<span class="hljs-comment">// 存储的是测试相关的代码</span>
src<span class="hljs-comment">// 源码</span>
LICENSE<span class="hljs-comment">// 版权，开源协议的描述</span>
README.md
api-extractor.json<span class="hljs-comment">// 配置文件</span>
index.js<span class="hljs-comment">// 打包时的入口</span>
package.json<span class="hljs-comment">// 包的描述</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
</li>
<li>
<p>Monorepo(Monolithic Repository)</p>
<ul>
<li>一个项目仓库中管理多个模块/包</li>
</ul>
</li>
</ul>
<h5 data-id="heading-7">重新组织目录结构</h5>
<ol>
<li>
<p>在根目录下创建packages， 然后分别创建文件夹</p>
<pre><code class="hljs language-js copyable" lang="js">packages
button
    __tests__..
        dist..
        src..
        index.js
LiCENSE
        README.md
.... <span class="hljs-comment">// 每一个组件都是相同的模板，只是内容不一样，所以可以使用plop等工具进行命令式创建模板。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<h5 data-id="heading-8">Storybook</h5>
<blockquote>
<p>我们可以把每一个组件想象成一个故事，storybook就像是讲一个一个的故事</p>
</blockquote>
<ul>
<li>
<p>开发组件库的必备开源工具</p>
</li>
<li>
<p>可视化的组件展示平台</p>
</li>
<li>
<p>在隔离的开发环境中，以交互式的方式展示组件</p>
</li>
<li>
<p>独立开发组件， 不必担心与业务有任何耦合性。</p>
</li>
<li>
<p>支持的框架： React、RN、Vue、ng、Svelte、HTML、Riot、Ember</p>
</li>
</ul>
<p>安装(结合vue)</p>
<ul>
<li>自动安装
<ul>
<li>npx -p @storybook/cli sb init --type vue</li>
<li>yarn add vue // 需要使用yarn的工作区</li>
<li>vue yarn add vue-loader vue-template-compiler --dev</li>
</ul>
</li>
<li>手动安装</li>
</ul>
<p>创建好目录结构之后</p>
<ol>
<li>
<p>将写好的packages文件夹复制进去，在每一个组件下新建stories/xxx.stories.js。</p>
</li>
<li>
<p>修改.storybook文件夹下的main.js配置文件， 将查找的stories文件路径改为<code>['../packages/**/*.stories.@(js|jsx|ts|tsx)']</code></p>
</li>
<li>
<p>xxx.stories中的内容</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 建立stories文件</span>
<span class="hljs-keyword">import</span> HrInput <span class="hljs-keyword">from</span> <span class="hljs-string">'../'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123; <span class="hljs-comment">// 一级目录</span>
  <span class="hljs-attr">title</span>: <span class="hljs-string">'HrInput'</span>,
  <span class="hljs-attr">component</span>: HrInput
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> Text = <span class="hljs-function">() =></span> (&#123; <span class="hljs-comment">// 二级目录</span>
  <span class="hljs-attr">components</span>: &#123; HrInput &#125;,
  <span class="hljs-attr">template</span>: <span class="hljs-string">'<hr-input v-model="value"></hr-input>'</span>,
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">value</span>: <span class="hljs-string">'admin'</span>
    &#125;
  &#125;
&#125;)
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> Password = <span class="hljs-function">() =></span> (&#123; <span class="hljs-comment">// 二级目录</span>
  <span class="hljs-attr">components</span>: &#123; HrInput &#125;,
  <span class="hljs-attr">template</span>: <span class="hljs-string">'<hr-input type="password" v-model="value"></hr-input>'</span>,
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">value</span>: <span class="hljs-string">'admin'</span>
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>在form-item中需要async-validator插件，需要在packages/formitem文件夹下yarn add async-validator.</p>
<p>ps: 如果多个包都需要这个插件需要重复安装？不需要，后面通过yarn的workspace解决.</p>
</li>
</ol>
<h4 data-id="heading-9">yarn workspace</h4>
<ul>
<li>
<p>Monorepo的仓库代码形式一般与yarn workspaces配合</p>
</li>
<li>
<p>常规情况下我们需要给不同的包安装不同的依赖</p>
</li>
<li>
<p>如果不同的包出现相同的依赖，这个时候如果安装依赖的话，会出现重复下载，占用硬盘的情况。</p>
</li>
<li>
<p>开启workspace 后，可以让在根目录中使用yarn install 给所有的包安装依赖，这时候如果出现了相同的依赖会把依赖提升到根目录下的node_modules中，减少重复，如果引入的包的版本不同，只会将版本相同的包提升到根目录的node_modules中。</p>
</li>
<li>
<p>npm 是不支持workspace的。</p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-number">1.</span> 开启yarn的workspace工作区
在项目根目录的package.json
<span class="hljs-string">"private"</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 必须设置的，组件库开发完毕时，发布到npm上，工作区的根目录一般是脚手架不需要发布，防止意外把内容暴露出去</span>
<span class="hljs-string">"workspaces"</span>: [
<span class="hljs-string">"./packages/*"</span>  <span class="hljs-comment">// 设置工作区的子目录</span>
]
<span class="hljs-number">2.</span> yarn workspaces 使用
<span class="hljs-number">2.1</span> 给工作区根目录安装开发依赖 
    yarn add jest -D -W   <span class="hljs-comment">// -D是开发依赖 -W是工作区，意思是安装到根目录</span>
<span class="hljs-number">2.2</span> 给指定工作区安装依赖
    yarn workspace lg-button(package.json的name属性) add lodash@<span class="hljs-number">4</span>
<span class="hljs-number">3.</span> 给所有的工作区安装依赖
<span class="hljs-number">3.1</span> yarn install
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">Learn</h4>
<ul>
<li>方便把项目中的包统一发布</li>
<li>babel开源的项目</li>
<li>一般learn与yarn workspace一起使用</li>
</ul>
<ol>
<li>介绍
<ul>
<li>lerna 是一个优化使用git和npm管理多包仓库的工作流工具</li>
<li>用于管理具有多个包的js项目</li>
<li>它可以一键把代码提交到git和npm仓库</li>
</ul>
</li>
<li>使用(在项目根目录)
<ul>
<li>全局安装： yarn global add lerna</li>
<li>初始化： lerna init</li>
<li>发布：lerna publish</li>
<li>使用注意事项： 初始化git仓库，push到仓库中。登录npm， scripts中添加<code>"lerna": "lerna publish"</code></li>
<li>一定要先把东西提交到git仓库上在执行yarn lerna。</li>
<li>发布到npm上的包的名字是package.json中的名字。</li>
</ul>
</li>
</ol>
<h4 data-id="heading-11">单元测试</h4>
<blockquote>
<p>单元测试就是对一个函数的输入和输入进行测试，使用断言的方式根据输入判断实际的输出和预测的输出是否相同，使用单元测试的目的是用来发现模块的内部可能存在的各种错误，组件的单元测试是用单元测试工具对组件的行为和状态进行测试，确保组件发布之后在项目中使用组件过程中不会出现错误。</p>
</blockquote>
<p>组件单元测试好处</p>
<ul>
<li>提供描述组件行为的文档</li>
<li>节省手动测试的时间</li>
<li>减少研发新特性时产生的bug</li>
<li>改进设计</li>
<li>促进重构</li>
</ul>
<p>配置组件单元测试的环境</p>
<ul>
<li>vue Test Utils vue官方提供的组件单元测试的官方库，需要结合单元测试框架一起使用</li>
<li>Jest       facebook出品，单元测试框架，和vue结合比较方便，但是不支持单文件组件</li>
<li>vue-jest     vue官方提供了一个为jest提供的预处理器，可以将单文件组件编译成js代码给jest使用。</li>
<li>babel-jest    测试文件使用es新特性的语法和esm的语法，需要使用babel-jest对测试代码进行降级处理</li>
<li>安装
<ul>
<li><code>yarn add jest @vue/test-utils vue-jest babel-jest -D -W</code></li>
</ul>
</li>
</ul>
<p>配置测试脚本</p>
<ul>
<li>
<p>package.json</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-string">"test"</span>: <span class="hljs-string">"jest"</span>,
     ...
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p>jest配置文件</p>
<ul>
<li>
<p>jest.config.js(根目录下)</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-string">"testMatch"</span>: [<span class="hljs-string">"**/__tests__/**/*.[jt]s?(x)"</span>], <span class="hljs-comment">// 运行jest时去哪里找测试文件</span>
  <span class="hljs-string">"moduleFileExtensions"</span>: [  <span class="hljs-comment">// 测试文件中导入文件的后缀</span>
    <span class="hljs-string">"js"</span>,
    <span class="hljs-string">"json"</span>,
    <span class="hljs-comment">// 告诉 Jest 处理 `*.vue` 文件</span>
    <span class="hljs-string">"vue"</span>
  ],
  <span class="hljs-string">"transform"</span>: &#123;<span class="hljs-comment">// 通过正则匹配文件交由对应的模块去处理</span>
    <span class="hljs-comment">// 用 `vue-jest` 处理 `*.vue` 文件</span>
    <span class="hljs-string">".*\\.(vue)$"</span>: <span class="hljs-string">"vue-jest"</span>,
    <span class="hljs-comment">// 用 `babel-jest` 处理 js</span>
    <span class="hljs-string">".*\\.(js)$"</span>: <span class="hljs-string">"babel-jest"</span> 
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p>babel配置文件</p>
<ul>
<li>
<p>babel.config.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
    <span class="hljs-attr">presets</span>: [
        [
            <span class="hljs-string">'@babel/preset-env'</span>
        ]
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ps: babel的版本不一样，比如项目中的babel和@vue/test-utils依赖的babel的版本不一致，可以使用babel这个文档进行桥接</p>
<p><code>yarn add babel-core@bridge -D -W</code></p>
</li>
</ul>
<blockquote>
<p>以上在@vue/utils-test中都有</p>
</blockquote>
<h4 data-id="heading-12">jest种常见的api</h4>
<ul>
<li>全局函数
<ul>
<li>describe(name. fn) 创建代码块把相关测试函数组合在一起</li>
<li>test(name, fn)        测试方法</li>
<li>expect(value)         断言 在测试方法种调用expect, value是希望的值， 把希望的值和匹配到的值进行比较，如果相等，该测试成功，否则匹配失败</li>
</ul>
</li>
<li>匹配器
<ul>
<li>toBe(value)     判断值是否相等</li>
<li>toEqual(obj)    判断对象是否相等</li>
<li>toContain(value)    判断数组或者字符串种是否包含</li>
<li>...</li>
</ul>
</li>
<li>快照
<ul>
<li>toMatchSnapshot() 第一次调用会将expect中的值以字符串的形式存到文本文件中。用来对比</li>
</ul>
</li>
</ul>
<h4 data-id="heading-13">vue test utils常用api</h4>
<ul>
<li>mount()
<ul>
<li>创建一个包含被挂载和渲染的vue组件的wrapper</li>
</ul>
</li>
<li>wrapper
<ul>
<li>vmwrapper包裹的组件实例</li>
<li>props()   返回vue实例选项中的props对象</li>
<li>html()      组件生成的html标签</li>
<li>find()        通过选择器返回匹配到的组件中的dom元素</li>
<li>trigger()    触发dom原生事件,自定义事件 wrapper.vm.$emit()</li>
</ul>
</li>
</ul>
<h4 data-id="heading-14">rollup</h4>
<ul>
<li>rollup是一个模块打包器</li>
<li>rollup支持tree-shaking</li>
<li>打包的结果比webpack更小</li>
<li>开发框架/组件库的时候使用rollup更合适</li>
</ul>
<p>安装依赖: <code>yarn add rollup rollup-plugin-terser rollup-plugin-vue@5.1.9 vue-template-compiler -D -W</code></p>
<p>配置文件</p>
<ol>
<li>
<p>在button目录中创建rollup.config.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; terser &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'rollup-plugin-terser'</span>
<span class="hljs-keyword">import</span> vue <span class="hljs-keyword">from</span> <span class="hljs-string">'rollup-plugin-vue'</span>

<span class="hljs-built_in">module</span>.exports = [
  &#123;
    <span class="hljs-attr">input</span>: <span class="hljs-string">'index.js'</span>,
    <span class="hljs-attr">output</span>: [
      &#123;
        <span class="hljs-attr">file</span>: <span class="hljs-string">'dist/index.js'</span>,
        <span class="hljs-attr">format</span>: <span class="hljs-string">'es'</span>
      &#125;
    ],
    <span class="hljs-attr">plugins</span>: [
      vue(&#123;
        <span class="hljs-comment">// Dynamically inject css as a <style> tag</span>
        <span class="hljs-attr">css</span>: <span class="hljs-literal">true</span>, 
        <span class="hljs-comment">// Explicitly convert template to render function</span>
        <span class="hljs-attr">compileTemplate</span>: <span class="hljs-literal">true</span>
      &#125;),
      terser()
    ]
  &#125;
]
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>配置 build 脚本并运行</p>
<p>找到 button 包中的 package.json 的 scripts 配置</p>
<p><code>"build": "rollup -c"</code></p>
</li>
<li>
<p>运行打包</p>
<p><code>yarn workspace rr-button run build</code></p>
<p>如果有很多包的话, 那么我们不可能一个个的去打包, 我们希望把packages中的所有包一次性进行打包处理.</p>
</li>
<li>
<p>打包所有组件</p>
</li>
<li>
<p>需要安装这些组件</p>
<p><code>yarn add @rollup/plugin-json rollup-plugin-postcss @rollup/plugin-node-resolve -D -W</code></p>
<p>@rollup/plugin-json 让rollup可以将json文件作为模块进行加载,通过配置文件进行打包</p>
<p>@rollup/plugin-node-resolve  在打包的过程中将组件依赖的包打包进来</p>
</li>
<li>
<p>项目根目录创建rollup.config.js</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> fs <span class="hljs-keyword">from</span> <span class="hljs-string">'fs'</span>
<span class="hljs-keyword">import</span> path <span class="hljs-keyword">from</span> <span class="hljs-string">'path'</span>
<span class="hljs-keyword">import</span> json <span class="hljs-keyword">from</span> <span class="hljs-string">'@rollup/plugin-json'</span>
<span class="hljs-keyword">import</span> vue <span class="hljs-keyword">from</span> <span class="hljs-string">'rollup-plugin-vue'</span>
<span class="hljs-keyword">import</span> postcss <span class="hljs-keyword">from</span> <span class="hljs-string">'rollup-plugin-postcss'</span>
<span class="hljs-keyword">import</span> &#123; terser &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'rollup-plugin-terser'</span>
<span class="hljs-keyword">import</span> &#123; nodeResolve &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@rollup/plugin-node-resolve'</span>

<span class="hljs-keyword">const</span> isDev = process.env.NODE_ENV !== <span class="hljs-string">'production'</span>

<span class="hljs-comment">// 公共插件配置</span>
<span class="hljs-keyword">const</span> plugins = [
  vue(&#123;
    <span class="hljs-comment">// Dynamically inject css as a <style> tag</span>
    <span class="hljs-attr">css</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-comment">// Explicitly convert template to render function</span>
    <span class="hljs-attr">compileTemplate</span>: <span class="hljs-literal">true</span>
  &#125;),
  json(),
  nodeResolve(),
  postcss(&#123;
    <span class="hljs-comment">// 把 css 插入到 style 中</span>
    <span class="hljs-comment">// inject: true,</span>
    <span class="hljs-comment">// 把 css 放到和js同一目录</span>
    <span class="hljs-attr">extract</span>: <span class="hljs-literal">true</span>
  &#125;)
]

<span class="hljs-comment">// 如果不是开发环境，开启压缩</span>
isDev || plugins.push(terser())

<span class="hljs-comment">// packages 文件夹路径</span>
<span class="hljs-keyword">const</span> root = path.resolve(__dirname, <span class="hljs-string">'packages'</span>)

<span class="hljs-built_in">module</span>.exports = fs.readdirSync(root)
  <span class="hljs-comment">// 过滤，只保留文件夹</span>
  .filter(<span class="hljs-function"><span class="hljs-params">item</span> =></span> fs.statSync(path.resolve(root, item)).isDirectory())
  <span class="hljs-comment">// 为每一个文件夹创建对应的配置</span>
  .map(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
    <span class="hljs-keyword">const</span> pkg = <span class="hljs-built_in">require</span>(path.resolve(root, item, <span class="hljs-string">'package.json'</span>))
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">input</span>: path.resolve(root, item, <span class="hljs-string">'index.js'</span>),
      <span class="hljs-attr">output</span>: [
        &#123;
          <span class="hljs-attr">exports</span>: <span class="hljs-string">'auto'</span>,
          <span class="hljs-attr">file</span>: path.resolve(root, item, pkg.main),
          <span class="hljs-attr">format</span>: <span class="hljs-string">'cjs'</span>
        &#125;,
        &#123;
          <span class="hljs-attr">exports</span>: <span class="hljs-string">'auto'</span>,
          <span class="hljs-attr">file</span>: path.join(root, item, pkg.module),
          <span class="hljs-attr">format</span>: <span class="hljs-string">'es'</span>
        &#125;,
      ],
      <span class="hljs-attr">plugins</span>: plugins
    &#125;
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>在rollup.config.js配置文件中,  要获取每一个包的package.json中的main和module字段作为打包出口的路径, 作用是分别打包两种模块类型cjs 和 es类型. 这也是别人在使用我们这个包时的入口</p>
<p>在每一个包中设置 package.json 中的 main 和 module 字段</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-string">"main"</span>: <span class="hljs-string">"dist/cjs/index.js"</span>,
<span class="hljs-string">"module"</span>: <span class="hljs-string">"dist/es/index.js"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>根目录的 package.json 中配置 scripts</p>
<p><code>"build": "rollup -c"</code></p>
</li>
<li>
<p>区分环境的script脚本</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-string">"build:prod"</span>: <span class="hljs-string">"cross-env NODE_ENV=production rollup -c"</span>,
<span class="hljs-string">"build:dev"</span>: <span class="hljs-string">"cross-env NODE_ENV=development rollup -c"</span>,
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<h4 data-id="heading-15">清理所有包下的node_modules</h4>
<p>使用lerna clean就可以</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-string">"scripts"</span>: &#123;
<span class="hljs-string">"clean"</span>: <span class="hljs-string">"lerna clean"</span>,
...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-16">清除dist,上一次打包的图片或样式可能不再使用</h4>
<p>安装依赖: <code>yarn add rimraf -D -W</code></p>
<p>在每一个包中配置脚本</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-string">"del"</span>: <span class="hljs-string">"rimraf dist"</span>
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用yarn workspaces run del来执行所有包下的命令.</p>
<h4 data-id="heading-17">基于模板生成组件</h4>
<blockquote>
<p>我们创建了Monorepo的目录结构, 在一个项目中管理多个包, 这个方法更适合来管理组件库和发布每一个组件,  使用storybook搭建项目, 可以让用户快速预览组件, 使用yarn workspaces管理所有包的依赖,使用lerna发布包.</p>
</blockquote>
<ul>
<li>当组件的结构固定以后,我们可以把组件相同的部分提取出来, 制作模板,通过plop生成一个组件结构.</li>
</ul>
<ol>
<li>安装依赖 <code>yarn plop</code></li>
<li>创建项目结构并在文件中写好模板.</li>
<li>新建plopfile.js 在文件中写配置文件,promot --> actions</li>
</ol>
<h4 data-id="heading-18">发布新的包</h4>
<ul>
<li>如果要发布别忘了生产环境下打个包,然后提交到git仓库上.</li>
</ul></div>  
</div>
            