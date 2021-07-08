
---
title: 'VueJS 组件编码规范'
categories: 
 - 编程
 - 掘金
 - 收藏集
headimg: 'https://picsum.photos/400/300?random=9168'
author: 掘金
comments: false
date: Wed, 08 Mar 2017 19:19:39 GMT
thumbnail: 'https://picsum.photos/400/300?random=9168'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>原文地址：<a href="https://link.juejin.cn/?target=http%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2Fpablohpsilva%2Fvuejs-component-style-guide%2Fblob%2Fmaster%2FREADME-CN.md%2523%2525E7%25259B%2525AE%2525E5%2525BD%252595" target="_blank" title="http://link.zhihu.com/?target=https%3A//github.com/pablohpsilva/vuejs-component-style-guide/blob/master/README-CN.md%23%25E7%259B%25AE%25E5%25BD%2595" ref="nofollow noopener noreferrer">pablohpsilva/vuejs-component-style-guide<i></i></a></p>
<h2 data-id="heading-0">目标</h2>
<p>本规范提供了一种统一的编码规范来编写 <a href="https://link.juejin.cn/?target=http%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttp%253A%2F%2Fvuejs.org%2F" target="_blank" title="http://link.zhihu.com/?target=http%3A//vuejs.org/" ref="nofollow noopener noreferrer">Vue.js<i></i></a> 代码。这使得代码具有如下的特性：</p>
<ul>
    <li>其它开发者或是团队成员更容易阅读和理解。</li>
    <li>IDEs 更容易理解代码，从而提供高亮、格式化等辅助功能</li>
    <li>更容易使用现有的工具</li>
    <li>更容易实现缓存以及代码包的分拆</li>
</ul>
<p>本指南为 <a href="https://link.juejin.cn/?target=http%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2Fvoorhoede" target="_blank" title="http://link.zhihu.com/?target=https%3A//github.com/voorhoede" ref="nofollow noopener noreferrer">De Voorhoede<i></i></a> 参考 <a href="https://link.juejin.cn/?target=http%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2Fvoorhoede%2Friotjs-style-guide" target="_blank" title="http://link.zhihu.com/?target=https%3A//github.com/voorhoede/riotjs-style-guide" ref="nofollow noopener noreferrer">RiotJS 编码规范<i></i></a> 而写。</p>
<h2 data-id="heading-1">目录</h2>
<ul>
    <li>基于模块开发</li>
    <li>vue 组件命名</li>
    <li>组件表达式简单化</li>
    <li>组件 props 原子化</li>
    <li>验证组件的 props</li>
    <li>将 this 赋值给 component 变量</li>
    <li>组件结构化</li>
    <li>组件事件命名</li>
    <li>避免 this.$parent</li>
    <li>谨慎使用 this.$refs</li>
    <li>使用组件名作为样式作用域空间</li>
    <li>提供组件 API 文档</li>
    <li>提供组件 demo</li>
    <li>对组件文件进行代码校验</li>
</ul>
<h2 data-id="heading-2">基于模块开发</h2>
<p>始终基于模块的方式来构建你的 app，每一个子模块只做一件事情。</p>
<p>Vue.js 的设计初衷就是帮助开发者更好的开发界面模块。一个模块是应用程序中独立的一个部分。</p>
<h3 data-id="heading-3">怎么做？</h3>
<p>每一个 Vue 组件(等同于模块)首先必须专注于解决一个单一的问题，<em>独立的</em>, <em>可复用的</em>, <em>微小的</em> and <em>可测试的</em>。</p>
<p>如果你的组件做了太多的事或是变得臃肿，请将其拆分成更小的组件并保持单一的原则。一般来说，尽量保证每一个文件的代码行数不要超过 100 行。也请保证组件可独立的运行。比较好的做法是增加一个单独的 demo 示例。</p>
<p>Vue 组件命名<br></p>
<p>组件的命名需遵从以下原则：</p>
<ul>
    <li>有意义的: 不过于具体，也不过于抽象</li>
    <li>简短: 2 到 3 个单词</li>
    <li>具有可读性: 以便于沟通交流</li>
</ul>
<p>同时还需要注意：</p>
<ul>
    <li>必须符合自定义元素规范: <a href="https://link.juejin.cn/?target=http%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fwww.w3.org%2FTR%2Fcustom-elements%2F%2523concepts" target="_blank" title="http://link.zhihu.com/?target=https%3A//www.w3.org/TR/custom-elements/%23concepts" ref="nofollow noopener noreferrer">使用连字符<i></i></a>分隔单词，切勿使用保留字。</li>
    <li>app- 前缀作为命名空间: 如果非常通用的话可使用一个单词来命名，这样可以方便于其它项目里复用。</li>
</ul>
<h3 data-id="heading-4">为什么？</h3>
<ul>
    <li>组件是通过组件名来调用的。所以组件名必须简短、富有含义并且具有可读性。</li>
</ul>
<h3 data-id="heading-5">如何做？</h3><br> <pre><code class="copyable"><!-- 推荐 -->
<app-header></app-header>
<user-list></user-list>
<range-slider></range-slider>

<!-- 避免 -->
<btn-group></btn-group> <!-- 虽然简短但是可读性差. 使用 `button-group` 替代 -->
<ui-slider></ui-slider> <!-- ui 前缀太过于宽泛，在这里意义不明确 -->
<slider></slider> <!-- 与自定义元素规范不兼容 -->
<span class="copy-code-btn">复制代码</span></code></pre>
<p>组件表达式简单化<br></p>
<p>Vue.js 的表达式是 100% 的 Javascript 表达式。这使得其功能性很强大，但也带来潜在的复杂性。因此，你应该尽量保持表达式的简单化。</p>
<h3 data-id="heading-6">为什么？</h3>
<ul>
    <li>复杂的行内表达式难以阅读。</li>
    <li>行内表达式是不能够通用的，这可能会导致重复编码的问题。</li>
    <li>IDE 基本上不能识别行内表达式语法，所以使用行内表达式 IDE 不能提供自动补全和语法校验功能。</li>
</ul>
<h3 data-id="heading-7">怎么做？</h3>
<p>如果你发现写了太多复杂并难以阅读的行内表达式，那么可以使用 method 或是 computed 属性来替代其功能。</p><br> <pre><code class="copyable"><!-- 推荐 -->
<template>
    <h1>
        &#123;&#123; `$&#123;year&#125;-$&#123;month&#125;` &#125;&#125;
    </h1>
</template>
<script type="text/javascript">
  export default &#123;
    computed: &#123;
      month() &#123;
        return this.twoDigits((new Date()).getUTCMonth() + 1);
      &#125;,
      year() &#123;
        return (new Date()).getUTCFullYear();
      &#125;
    &#125;,
    methods: &#123;
      twoDigits(num) &#123;
        return ('0' + num).slice(-2);
      &#125;
    &#125;,
  &#125;;
</script>

<!-- 避免 -->
<template>
    <h1>
        &#123;&#123; `$&#123;(new Date()).getUTCFullYear()&#125;-$&#123;('0' + ((new Date()).getUTCMonth()+1)).slice(-2)&#125;` &#125;&#125;
    </h1>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>组件 props 原子化<br></p>
<p>虽然 Vue.js 支持传递复杂的 JavaScript 对象通过 props 属性，但是你应该尽可能的使用原始类型的数据。尽量只使用<a href="https://link.juejin.cn/?target=http%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FGlossary%2FPrimitive" target="_blank" title="http://link.zhihu.com/?target=https%3A//developer.mozilla.org/en-US/docs/Glossary/Primitive" ref="nofollow noopener noreferrer">JavaScript 原始类型<i></i></a>(字符串、数字、布尔值) 和 函数。尽量避免复杂的对象。</p>
<h3 data-id="heading-8">为什么？</h3>
<ul>
    <li>使得组件 API 清晰直观</li>
    <li>只使用原始类型和函数作为 props 使得组件的 API 更接近于 HTML(5) 原生元素。</li>
    <li>其它开发者更好的理解每一个 prop 的含义，作用</li>
    <li>传递过于复杂的对象使得我们不能够清楚的知道哪些属性或方法被自定义组件使用，这使得代码难以重构和维护。</li>
</ul>
<h3 data-id="heading-9">怎么做？</h3>
<p>组件的每一个属性单独使用一个 props，并且使用函数或是原始类型的值。</p><br> <pre><code class="copyable"><!-- 推荐 -->
<range-slider
  :values="[10, 20]"
  min="0"
  max="100"
  step="5"
  :on-slide="updateInputs"
  :on-end="updateResults">
</range-slider>

<!-- 避免 -->
<range-slider :config="complexConfigObject"></range-slider>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">验证组件的 props</h2>
<p>在 Vue.js 中，组件的 props 即 API，一个稳定并可预测的 API 会使得你的组件更容易被其他开发者使用。</p>
<p>组件 props 通过自定义标签的属性来传递。属性的值可以是 Vue.js 字符串(:attr="value" 或 v-bind:attr="value")或是不传。你需要保证组件的 props 能应对不同的情况。</p>
<h3 data-id="heading-11">为什么？</h3>
<p>验证组件 props 可以保证你的组件永远是可用的(防御性编程)。即使其他开发者并未按照你预想的方法使用时也不会出错。</p>
<h3 data-id="heading-12">怎么做？</h3>
<ul>
    <li>提供默认值</li>
    <li>使用 type 属性<a href="https://link.juejin.cn/?target=http%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttp%253A%2F%2Fvuejs.org%2Fv2%2Fguide%2Fcomponents.html%2523Prop-Validation" target="_blank" title="http://link.zhihu.com/?target=http%3A//vuejs.org/v2/guide/components.html%23Prop-Validation" ref="nofollow noopener noreferrer">校验类型<i></i></a></li>
    <li>使用 props 之前先检查该 prop 是否存在</li>
</ul> <pre><code class="copyable"><template>
  <input type="range" v-model="value" :max="max" :min="min">
</template>
<script type="text/javascript">
  export default &#123;
    props: &#123;
      max: &#123;
        type: Number, // 这里添加了数字类型的校验
        default() &#123; return 10; &#125;,
      &#125;,
      min: &#123;
        type: Number,
        default() &#123; return 0; &#125;,
      &#125;,
      value: &#123;
        type: Number,
        default() &#123; return 4; &#125;,
      &#125;,
    &#125;,
  &#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre><br>
<h2 data-id="heading-13">将 this 赋值给 component 变量(</h2>
<p>在 Vue.js 组件上下文中，this指向了组件实例。因此当你切换到了不同的上下文时，要确保 this 指向一个可用的 component 变量。</p>
<p>换句话说，不要在编写这样的代码 const self = this; ，而是应该直接使用变量 component。</p>
<h3 data-id="heading-14">为什么？</h3>
<ul>
    <li>将组件 this 赋值给变量 component可用让开发者清楚的知道任何一个被使用的地方，它代表的是组件实例。</li>
</ul>
<h3 data-id="heading-15">怎么做？</h3><br> <pre><code class="copyable"><script type="text/javascript">
export default &#123;
  methods: &#123;
    hello() &#123;
      return 'hello';
    &#125;,
    printHello() &#123;
      console.log(this.hello());
    &#125;,
  &#125;,
&#125;;
</script>

<!-- 避免 -->
<script type="text/javascript">
export default &#123;
  methods: &#123;
    hello() &#123;
      return 'hello';
    &#125;,
    printHello() &#123;
      const self = this; // 没有必要
      console.log(self.hello());
    &#125;,
  &#125;,
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre><br>
<h2 data-id="heading-16">组件结构化</h2>
<p>按照一定的结构组织，使得组件便于理解。</p>
<h3 data-id="heading-17">为什么？</h3>
<ul>
    <li>导出一个清晰、组织有序的组件，使得代码易于阅读和理解。同时也便于标准化。</li>
    <li>按首字母排序属性，data, computed, watches 和 methods 使得属性便于查找。</li>
    <li>合理组织，使得组件易于阅读。(name; extends; props, data and computed; components; watch and methods; lifecycle methods, 等.);</li>
    <li>使用 name 属性。借助于<a href="https://link.juejin.cn/?target=http%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fchrome.google.com%2Fwebstore%2Fdetail%2Fvuejs-devtools%2Fnhdogjmejiglipccpnnnanhbledajbpd%253Fhl%253Den" target="_blank" title="http://link.zhihu.com/?target=https%3A//chrome.google.com/webstore/detail/vuejs-devtools/nhdogjmejiglipccpnnnanhbledajbpd%3Fhl%3Den" ref="nofollow noopener noreferrer">vue devtools<i></i></a>可以让你更方便的测试</li>
    <li>合理的 CSS 结构，如 <a href="https://link.juejin.cn/?target=http%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fmedium.com%2Ftldr-tech%2Fbem-blocks-elements-and-modifiers-6b3b0af9e3ea%2523.bhnomd7gw" target="_blank" title="http://link.zhihu.com/?target=https%3A//medium.com/tldr-tech/bem-blocks-elements-and-modifiers-6b3b0af9e3ea%23.bhnomd7gw" ref="nofollow noopener noreferrer">BEM<i></i></a> 或 oo<a href="https://link.juejin.cn/?target=http%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2Frstacruz%2Frscss" target="_blank" title="http://link.zhihu.com/?target=https%3A//github.com/rstacruz/rscss" ref="nofollow noopener noreferrer">css<i></i></a>        - <a href="https://link.juejin.cn/?target=http%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2Fpablohpsilva%2Fvuejs-component-style-guide%2Fblob%2Fmaster%2FREADME-CN.md%2523%2525E4%2525BD%2525BF%2525E7%252594%2525A8%2525E7%2525BB%252584%2525E4%2525BB%2525B6%2525E5%252590%25258D%2525E4%2525BD%25259C%2525E4%2525B8%2525BA%2525E6%2525A0%2525B7%2525E5%2525BC%25258F%2525E4%2525BD%25259C%2525E7%252594%2525A8%2525E5%25259F%25259F%2525E7%2525A9%2525BA%2525E9%252597%2525B4" target="_blank" title="http://link.zhihu.com/?target=https%3A//github.com/pablohpsilva/vuejs-component-style-guide/blob/master/README-CN.md%23%25E4%25BD%25BF%25E7%2594%25A8%25E7%25BB%2584%25E4%25BB%25B6%25E5%2590%258D%25E4%25BD%259C%25E4%25B8%25BA%25E6%25A0%25B7%25E5%25BC%258F%25E4%25BD%259C%25E7%2594%25A8%25E5%259F%259F%25E7%25A9%25BA%25E9%2597%25B4" ref="nofollow noopener noreferrer">详情?<i></i></a>;</li>
    <li>使用单文件 .vue 文件格式来组件代码</li>
</ul>
<h3 data-id="heading-18">怎么做？</h3>
<p>组件结构化</p><br> <pre><code class="copyable"><template lang="html">
    <div class="Ranger__Wrapper">
        <!-- ... -->
    </div>
</template>

<script type="text/javascript">
  export default &#123;
        // 不要忘记了 name 属性
    name: 'RangeSlider',
    // 组合其它组件
    extends: &#123;&#125;,
    // 组件属性、变量
    props: &#123;
            bar: &#123;&#125;, // 按字母顺序
            foo: &#123;&#125;,
            fooBar: &#123;&#125;,
        &#125;,
    // 变量
    data() &#123;&#125;,
    computed: &#123;&#125;,
    // 使用其它组件
    components: &#123;&#125;,
    // 方法
    watch: &#123;&#125;,
    methods: &#123;&#125;,
    // 生命周期函数
    beforeCreate() &#123;&#125;,
    mounted() &#123;&#125;,
&#125;;
</script>

<style scoped>
  .Ranger__Wrapper &#123; /* ... */ &#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre><br>
<h2 data-id="heading-19">组件事件命名</h2>
<p>Vue.js 提供的处理函数和表达式都是绑定在 ViewModel 上的，组件的每一个事件都应该按照一个好的命名规范来，这样可以避免不少的开发问题，具体可见如下 ** 为什么**。</p>
<h3 data-id="heading-20">为什么？</h3>
<ul>
    <li>开发者可以随意给事件命名，即使是原生事件的名字，这样会带来迷惑性。</li>
    <li>过于宽松的事件命名可能与<a href="https://link.juejin.cn/?target=http%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fvuejs.org%2Fv2%2Fguide%2Fcomponents.html%2523DOM-Template-Parsing-Caveats" target="_blank" title="http://link.zhihu.com/?target=https%3A//vuejs.org/v2/guide/components.html%23DOM-Template-Parsing-Caveats" ref="nofollow noopener noreferrer">DOM模板不兼容<i></i></a>。</li>
</ul>
<h3 data-id="heading-21">怎么做？</h3>
<ul>
    <li>事件命名也连字符命名</li>
    <li>一个事件的名字对应组件外的一组意义操作，如：upload-success, upload-error 以及 dropzone-upload-success, dropzone-upload-error (如果需要前缀的话)。</li>
    <li>事件命名应该以动词(如 client-api-load) 或是 形容词(如 drive-upload-success)结尾。(<a href="https://link.juejin.cn/?target=http%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2FGoogleWebComponents%2Fstyle-guide%2523events" target="_blank" title="http://link.zhihu.com/?target=https%3A//github.com/GoogleWebComponents/style-guide%23events" ref="nofollow noopener noreferrer">出处<i></i></a>)</li>
</ul><br>
<h2 data-id="heading-22">避免 this.$parent</h2>
<p>Vue.js 支持组件嵌套，并且子组件可访问父组件的上下文。访问组件之外的上下文违反了基于模块开发的第一原则。因此你应该尽量避免使用 this.$parent。</p>
<h3 data-id="heading-23">为什么？</h3>
<ul>
    <li>组件必须相互保持独立，Vue 组件也是。如果组件需要访问其父层的上下文就违反了该原则。</li>
    <li>如果一个组件需要访问其父组件的上下文，那么该组件将不能再其它上下文中复用。</li>
</ul>
<h3 data-id="heading-24">怎么做？</h3>
<ul>
    <li>通过 props 将值传递给子组件</li>
    <li>通过 props 传递回调函数给子组件来达到调用父组件方法的目的</li>
    <li>通过在子组件触发事件来通知父组件</li>
</ul><br>
<h2 data-id="heading-25">谨慎使用 this.$refs</h2>
<p>Vue.js 支持通过 ref 属性来访问其它组件和 HTML 元素。并通过 this.$refs 可以得到组件或 HTML 元素的上下文。在大多数情况下，通过 this.$refs来访问其它组件的上下文是可以避免的。在使用的的时候你需要注意避免调用了不恰当的组件 API，所以应该尽量避免使用 this.$refs。</p>
<h3 data-id="heading-26">为什么？</h3>
<ul>
    <li>组件必须是保持独立的，如果一个组件的 API 不能够提供所需的功能，那么这个组件在设计、实现上是有问题的。</li>
    <li>组件的属性和事件必须足够的给大多数的组件使用</li>
</ul>
<h3 data-id="heading-27">怎么做？</h3>
<ul>
    <li>提供良好的组件 API</li>
    <li>总是关注于组件本身的目的</li>
    <li>拒绝定制代码。如果你在一个通用的组件内部编写特定需求的代码，那么代表这个组件的 API 不够通用，或者你可能需要一个新的组件来应对该需求</li>
    <li>检查所有的 props 是否有缺失的，如果有提一个 issue 或是完善这个组件</li>
    <li>检查所有的事件。子组件向父组件通信一般是通过事件来实现的，但是大多数的开发者更多的关注于 props 从忽视了这点。</li>
    <li>Props向下传递，事件向上传递！。以此为目标升级你的组件，提供良好的 API 和 独立性。</li>
    <li>当遇到 props 和 events 难以实现的功能时，通过 this.$refs来实现。</li>
    <li>当需要操作 DOM 无法通过指令来做的时候可使用 this..$ref 而不是 JQuery, document.getElement* , document.queryElement。</li>
</ul> <pre><code class="copyable"><!-- 推荐，并未使用 this.$refs -->
<range :max="max"
  :min="min"
  @current-value="currentValue"
  :step="1"></range>
<span class="copy-code-btn">复制代码</span></code></pre> <pre><code class="copyable"><!-- 使用 this.$refs 的适用情况-->
<modal ref="basicModal">
  <h4>Basic Modal</h4>
  <button class="primary" @click="$refs.basicModal.close()">Close</button>
</modal>
<button @click="$refs.basicModal.open()">Open modal</button>

<!-- Modal component -->
<template>
  <div v-show="active">
    <!-- ... -->
  </div>
</template>

<script>
  export default &#123;
    // ...
    data() &#123;
        return &#123;
            active: false,
        &#125;;
    &#125;,
    methods: &#123;
      open() &#123;
        this.active = true;
      &#125;,
      hide() &#123;
        this.active = false;
      &#125;,
    &#125;,
    // ...
  &#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre> <pre><code class="copyable"><!-- 如果可通过 emited 来做则避免通过 this.$refs 直接访问 -->
<template>
  <range :max="max"
    :min="min"
    ref="range"
    :step="1"></range>
</template>

<script>
  export default &#123;
    // ...
    methods: &#123;
      getRangeCurrentValue() &#123;
        return this.$refs.range.currentValue;
      &#125;,
    &#125;,
    // ...
  &#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre><br>
<h2 data-id="heading-28">使用组件名作为样式作用域空间</h2>
<p>Vue.js 的组件是自定义元素，这非常适合用来作为样式的根作用域空间。可以将组件名作为 css 类的命名空间。</p>
<h3 data-id="heading-29">为什么？</h3>
<ul>
    <li>给样式加上作用域空间可以避免组件样式影响外部的样式</li>
    <li>保持模块名、目录名、样式根作用域名一样，可以很好的将其关联起来，便于开发者理解。</li>
</ul>
<h3 data-id="heading-30">怎么做？</h3>
<p>使用组件名作为样式命名的前缀，可基于 BEM 或 OOCSS 范式。同时给style标签加上 scoped 属性。加上 scoped 属性编译后会给组件的 class 自动加上唯一的前缀从而避免样式的冲突。</p><br> <pre><code class="copyable"><style scoped>
    /* 推荐 */
    .MyExample &#123; &#125;
    .MyExample li &#123; &#125;
    .MyExample__item &#123; &#125;

    /* 避免 */
    .My-Example &#123; &#125; /* not scoped to component or module name, not BEM compliant */
</style>
<span class="copy-code-btn">复制代码</span></code></pre><br>
<h2 data-id="heading-31">提供组件 API 文档</h2>
<p>使用 Vue.js 组件的过程中会创建 Vue 组件实例，这个实例是通过自定义属性配置的。为了便于其他开发者使用该组件，对于这些自定义属性即组件API应该在 README.md 文件中进行说明。</p>
<h2 data-id="heading-32">为什么？</h2>
<ul>
    <li>良好的文档可以让开发者比较容易的对组件有一个整体的认识，而不用去阅读组件的源码，也更方便开发者使用</li>
    <li>组件配置属性即组件的 API，对于组件的用户来说他们更感兴趣的是 API 而不是实现原理。</li>
    <li>正式的文档会告诉开发者组件 API 变更以及向后的兼容性情况</li>
    <li>README.md 是标准的我们应该首先阅读的文档文件。代码托管网站 (github/bitbucket/gitlab 等) 会默认在仓库中展示 该文件作为仓库的介绍。</li>
</ul>
<h3 data-id="heading-33">怎么做？</h3>
<p>在模块目录中添加 README.md 文件：</p> <pre><code class="copyable">range-slider/
├── range-slider.vue
├── range-slider.less
└── README.md
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 README 文件中说明模块的功能以及使用场景。对于 vue 组件来说，比较有用的描述是组件的自定义属性即 API 的描述介绍。</p>
<h1 data-id="heading-34">Range slider</h1>
<h2 data-id="heading-35">功能</h2>
<p>range slider 组件可通过拖动的方式来设置一个给定范围内的数值。</p>
<p>该模块使用 <a href="https://link.juejin.cn/?target=http%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttp%253A%2F%2Frefreshless.com%2Fnouislider%2F" target="_blank" title="http://link.zhihu.com/?target=http%3A//refreshless.com/nouislider/" ref="nofollow noopener noreferrer">noUiSlider<i></i></a> 来实现夸浏览器和 touch 功能的支持。</p>
<h2 data-id="heading-36">如何使用</h2>
<p><range-slider> 支持如下的自定义属性：</p>* attributetypedescriptionminNumber
<p>可拖动的最小值.maxNumber可拖动的最大值.</p>
<p>* valuesNumber</p>
<p><em>optional，</em>包含最大值和最小值的数组. 如. values="[10, 20]". Defaults to [opts.min, opts.max].</p>
<p>* stepNumber </p>
<p><em>optional，</em>增加减小的数值单位，默认为 1.</p>
<p>* on-slideFunction </p>
<p><em>optional，</em>用户拖动开始按钮或者结束按钮时的回调函数，函数接受 (values, HANDLE) 格式的参数。 如： on-slide=&#123; updateInputs &#125;, component.updateInputs = (values, HANDLE) => &#123; const value = values[HANDLE]; &#125;.</p>
<p>* on-endFunction </p>
<p><em>optional，</em>当用户停止拖动时触发的回调函数，函数接受 (values, HANDLE) 格式的参数。</p>
<p>如需要自定义 slider 的样式可参考 noUiSlider 文档</p><br>
<h2 data-id="heading-37">提供组件 demo</h2>
<p>添加 index.html 文件作为组件的 demo 示例，并提供不同配置情况的效果，说明组件是如何使用的。</p>
<h3 data-id="heading-38">为什么？</h3>
<ul>
    <li>demo 可以说明组件是独立可使用的</li>
    <li>demo 可以让开发者预览组件的功能效果</li>
    <li>demo 可以展示组件各种配置参数下的功能</li>
</ul><br>
<h2 data-id="heading-39">对组件文件进行代码校验</h2>
<p>代码校验可以保持代码的统一性以及追踪语法错误。.vue 文件可以通过使用 eslint-plugin-html插件来校验代码。你可以通过 vue-cli 来开始你的项目，vue-cli 默认会开启代码校验功能。</p>
<h2 data-id="heading-40">为什么？</h2>
<ul>
    <li>保证所有的开发者使用同样的编码规范。</li>
    <li>更早的感知到语法错误</li>
    <li>怎么做？</li>
</ul>
<p>为了校验工具能够校验 *.vue文件，你需要将代码编写在 <script>标签中，并使组件表达式简单化，因为校验工具无法理解行内表达式，配置校验工具可以访问全局变量 vue 和组件的 props。</p>
<h2 data-id="heading-41">ESLint</h2>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttp%253A%2F%2Feslint.org%2F" target="_blank" title="http://link.zhihu.com/?target=http%3A//eslint.org/" ref="nofollow noopener noreferrer">ESLint<i></i></a> 需要通过 <a href="https://link.juejin.cn/?target=http%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2FBenoitZugmeyer%2Feslint-plugin-html%2523eslint-plugin-html" target="_blank" title="http://link.zhihu.com/?target=https%3A//github.com/BenoitZugmeyer/eslint-plugin-html%23eslint-plugin-html" ref="nofollow noopener noreferrer">ESLint HTML 插件<i></i></a>来抽取组件中的代码。</p>
<p>通过 .eslintrc 文件来配置 ESlint，这样 IED 可以更好的理解校验配置项。 ESlint，这样.</p><br> <pre><code class="copyable">&#123;
  "extends": "eslint:recommended",
  "plugins": ["html"],
  "env": &#123;
    "browser": true
  &#125;,
  "globals": &#123;
    "opts": true,
    "vue": true
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行 ESLint</p><br> <pre><code class="copyable">eslint src/**/*.vue
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-42">JSHint</h2>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttp%253A%2F%2Fjshint.com%2F" target="_blank" title="http://link.zhihu.com/?target=http%3A//jshint.com/" ref="nofollow noopener noreferrer">JSHint<i></i></a> 可以解析 HTML (使用 --extra-ext命令参数) 和 抽取代码（使用 --extract=auto命令参数).</p>
<p>通过 .jshintrc 文件来配置 ESlint，这样 IED 可以更好的理解校验配置项。</p><br> <pre><code class="copyable">&#123;
  "browser": true,
  "predef": ["opts", "vue"]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行 JSHint</p><br> <pre><code class="copyable">jshint --config modules/.jshintrc --extra-ext=html --extract=auto modules/
<span class="copy-code-btn">复制代码</span></code></pre><br>
<p>注：JSHint 不接受 vue 扩展名的文件，只支持 html。</p> </div>  
</div>
            