
---
title: '前端入门学习-Vue内置组件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ba839ba0f5845d984eaa1ba65f11115~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 30 Apr 2021 04:37:29 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ba839ba0f5845d984eaa1ba65f11115~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">动态组件</h2>
<ul>
<li>动态组件适用于多个组件频繁切换的处理。</li>
<li><code><component></code> 用于将一个‘元组件’渲染为动态组件，以 is 属性值决定渲染哪个组件。</li>
<li>用于实现多个组件的快速切换，例如选项卡效果。</li>
<li>is 属性会在每次切换组件时，Vue 都会创建一个新的组件实例。</li>
</ul>
<pre><code class="copyable"><div id="app">
    <!-- 按钮代表选项卡的标题功能 -->
    <button
      v-for="title in titles"
      :key="title"
      @click="currentCom = title"
    >
      &#123;&#123; title &#125;&#125;
    </button>

    <!-- component 设置动态组件 -->
    <component :is="currentCom"></component>
</div>

<script>
    // 设置要切换的子组件选项对象
    var ComA = &#123;
      template: `<p>这是组件A的内容：<input type="text"></p>`
    &#125;;  
    var ComB = &#123;
      template: `<p>这是组件B的内容：<input type="text"></p>`
    &#125;;
    var ComC = &#123;
      template: `<p>这是组件C的内容：<input type="text"></p>`
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
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">keep-alive 组件</h2>
<ul>
<li>主要用于保留组件状态或避免组件重新渲染。</li>
<li>include 属性用于指定哪些组件会被缓存，具有多种设置方式。</li>
<li>exclude 属性用于指定哪些组件不会被缓存。</li>
<li>max 属性用于设置最大缓存个数。</li>
</ul>
<pre><code class="copyable"><div id="app">
    <button 
      v-for="title in titles"
      :key="title"
      @click="currentCom = title"
    >
      &#123;&#123;title&#125;&#125;
    </button>

    <!-- 通过 include 设置哪些组件会被缓存 -->
    <!-- <keep-alive include="ComA,ComB,ComC"> -->
    <!-- <keep-alive :include="['ComA', 'ComB', 'ComC']"> -->
    <!-- <keep-alive :include="/Com[ABC]/"> -->

    <!-- 通过 exclude 设置哪些组件不会被缓存 -->
    <!-- <keep-alive exclude="ComD"> -->
    <!-- <keep-alive :exclude="['ComD']"> -->
    <!-- <keep-alive :exclude="/ComD/"> -->

    <keep-alive max="2">
      <!-- 动态组件 -->
      <component :is="currentCom"></component>
    </keep-alive>
</div>

<script>
    var ComA = &#123;
      template: `
        <div>
          请选择主食：
          <br>
          <label for="mantou">馒头：</label>
          <input id="mantou" type="radio" name="zhushi" value="mantou">
          <br>
          <label for="mifan">米饭：</label>
          <input id="mifan" type="radio" name="zhushi" value="mifan">
        </div>
      `
    &#125;;
    var ComB = &#123;
      template: `
        <div>
          请选择菜品：
          <br>
          <label for="luobo">炒萝卜：</label>
          <input id="luobo" type="checkbox" name="cai" value="luobo">
          <br>
          <label for="niurou">炒牛肉：</label>
          <input id="niurou" type="checkbox" name="cai" value="niurou">
          <br>
          <label for="pingguo">炒苹果：</label>
          <input id="pingguo" type="checkbox" name="cai" value="pingguo">
        </div>
      `
    &#125;;
    var ComC = &#123;
      template: `
        <div>
          请选择汤：
          <br>
          <label for="tang1"">西红柿鸡蛋汤：</label>
          <input id="tang1"" type="radio" name="tang" value="tang1"">
          <br>
          <label for="tang2">紫菜蛋花汤：</label>
          <input id="tang2" type="radio" name="tang" value="tang2">
          <br>
          <label for="tang3">清汤</label>
          <input id="tang3" type="radio" name="tang" value="tang3">
        </div>
      `
    &#125;;

    var ComD = &#123;
      template: `
        <div>
          请输入支付信息：
          <br>
          <label for="account"">请输入账号：</label>
          <input id="account"" type="text" name="account">
          <br>
          <label for="password">请输入密码：</label>
          <input id="password" type="password" name="password">
          <br>
        </div>

      `
    &#125;;

    new Vue(&#123;
      el: '#app',
      data: &#123;
        titles: ['ComA', 'ComB', 'ComC', 'ComD'],
        currentCom: 'ComA'
      &#125;,
      components: &#123;
        ComA, ComB, ComC, ComD
      &#125;
    &#125;);
  </script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">过渡组件</h2>
<p>用于在 Vue 插入、更新或者移除 DOM 时， 提供多种不同方式的应用过渡、动画效果。</p>
<h3 data-id="heading-3">transition 组件</h3>
<ul>
<li><strong>用于给元素和组件添加进入/离开过渡:</strong>
条件渲染 (使用 v-if )
条件展示 (使用 v-show )
动态组件
组件根节点</li>
<li><strong>组件提供了 6个 class，用于设置过渡的具体效果。</strong>
v-enter
v-enter-to
v-enter-active
v-leave
v-leave-to
v-leave-active</li>
</ul>
<pre><code class="copyable"><style>
    /* 用于设置出场的最终状态 */
    .v-leave-to &#123;
      opacity: 0;
    &#125;

    /* 用于设置过渡的执行过程 */
    .v-leave-active &#123;
      transition: opacity 1s;
    &#125;

    /* 用于设置入场的初始状态 */
    .v-enter &#123;
      opacity: 0;
    &#125;

    /* 用于设置入场的最终状态 */
    .v-enter-to &#123;
      opacity: 0.5;
    &#125;

    /* 用于设置入场的过程 */
    .v-enter-active &#123;
      transition: all 1s;
    &#125;
</style>

<div id="app">
    <button @click="show = !show">切换</button>

    <transition>
      <p v-if="show">hello world</p>
    </transition>
</div>  
<script>
    new Vue(&#123;
      el: '#app',
      data: &#123;
        show: true
      &#125;
    &#125;);
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">相关属性</h4>
<ul>
<li>给组件设置 name 属性，可用于给多个元素、组件设置不同的过渡效果，这时需要将 v- 更改为对应 name- 的形式。</li>
<li>通过 appear 属性，可以让组件在初始渲染时实现过渡。</li>
</ul>
<pre><code class="copyable"><style>
    /* 第一组过渡效果设置 */
    .v-enter, .v-leave-to &#123;
      opacity: 0;
    &#125;

    .v-enter-active, .v-leave-active &#123;
      transition: opacity .5s;
    &#125;

    /* 第二组过渡效果设置 */
    .demo-enter, .demo-leave-to &#123;
      opacity: 0;
      transform: translateX(200px);
    &#125;

    .demo-enter-active, .demo-leave-active &#123;
      transition: all .5s;
    &#125;
</style>

<div id="app">
    <button @click="show = !show">切换1</button>
    <!-- 没有设置 name 命名的 transition 组件，类名采用 v- 前缀 -->
    <transition appear>
      <p v-if="show">这是要切换的元素1</p>
    </transition>

    <br>

    <button @click="showDemo = !showDemo">切换2</button>
    <!-- 设置了 name 的 transition 组件，类名需要将 v- 修改为 demo- -->
    <transition 
      name="demo"
      appear
      >
      <p v-if="showDemo">这是要切换的元素2</p>
    </transition>
</div>  

<script>
    new Vue(&#123;
      el: '#app',
      data: &#123;
        show: true,
        showDemo: true
      &#125;
    &#125;);
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">自定义过渡类名</h3>
<ul>
<li>自定义类名比普通类名优先级更高，在使用第三方 CSS 动画库时非常有用。</li>
<li>用于设置自定义过渡类名的属性如下:
enter-class
enter-active-class
enter-to-class
leave-class
leave-active-class
leave-to-class
appear-class
appear-to-class
appear-active-class</li>
</ul>
<pre><code class="copyable"><style>
    .v-enter, .v-leave-to &#123;
      opacity: 0;
    &#125;

    .v-enter-active, .v-leave-active &#123;
      transition: all .5s;
    &#125;

    .test &#123;
      transition: all 3s;
    &#125;
</style>

<div id="app">
    <button @click="show = !show">切换</button>

    <transition
      enter-active-class="test"
      leave-active-class="test"
    >
      <p v-if="show">这是 p 标签</p>
    </transition>
</div>  

<script>
    new Vue(&#123;
      el: '#app',
      data: &#123;
        show: true
      &#125;
    &#125;);
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">transition-group 组件</h3>
<ul>
<li><code><transition-group></code> 用于给列表统一设置过渡动画。</li>
<li>tag 属性用于设置容器元素，默认为 <code><span></code>。</li>
<li>过渡会应用于内部元素，而不是容器。</li>
<li>子节点必须有独立的 key，动画才能正常工作。</li>
<li>当列表元素变更导致元素位移，可以通过 .v-move 类名设置移动时的效果。</li>
</ul>
<pre><code class="copyable"><style>
    ul &#123;
      position: relative;
    &#125;

    .v-enter, .v-leave-to &#123;
      opacity: 0;
      transform: translateX(100px);
    &#125;

    .v-enter-active, .v-leave-active &#123;
      transition: all .5s;
    &#125;

    /* 让元素在离场的过程中脱离标准流 */
    .v-leave-active &#123;
      position: absolute;
    &#125;

    .v-move &#123;
      transition: all .5s;
    &#125;
</style>

<div id="app">
    <input type="text"
      v-model="newTitle"
      @keyup.enter="addItem"
    >

    <transition-group
      tag="ul"
    >
      <li
        v-for="item in items"
        :key="item.id"
        @click="removeItem(item)"
      >
        &#123;&#123; item.title &#125;&#125;
      </li>
    </transition-group>
</div>  

<script>
    new Vue(&#123;
      el: '#app',
      data: &#123;
        items: [
          &#123; id: 1, title: '示例内容1'&#125;,
          &#123; id: 2, title: '示例内容2'&#125;,
          &#123; id: 3, title: '示例内容3'&#125;,
          &#123; id: 4, title: '示例内容4'&#125;,
          &#123; id: 5, title: '示例内容5'&#125;,
        ],
        newTitle: '',
        latestId: 5
      &#125;,
      methods: &#123;
        addItem () &#123;
          this.items.push(&#123;
            id: this.latestId + 1,
            title: this.newTitle
          &#125;);
          this.latestId++;
          this.newTitle = '';
        &#125;,
        removeItem (item) &#123;
          var i = this.items.indexOf(item);
          this.items.splice(i, 1);
        &#125;
      &#125;
    &#125;);
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">总结</h2>
<p>如果你已经下定决心要转行做编程行业，在最开始的时候就要对自己的学习有一个基本的规划，还要对这个行业的技术需求有一个基本的了解。有一个已就业为目的的学习目标，然后为之努力，坚持到底。如果你有幸看到这篇文章，希望对你有所帮助，祝你找到满意的工作。</p>
<p>不管你是零基础的萌新，还是想转行的小伙伴 ，只要你想了解前端，精通前端，都欢迎你们加入我们的前端自学团。</p>
<p>在这里，你可以找到志同道合的朋友，相互激励的学习伙伴，还能得到大神的经验分享，和加入项目实战的机会。 想加入自学团的小伙伴赶快行动起来吧 ~</p>
<pre><code class="copyable">想学习前端web和需要PDF文档的朋友都可以加入这边的企鹅裙，前面：938，，中间：051，，最后：673

裙里从学生到大佬都有，还有资源免费分享，不见不散哦！

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ba839ba0f5845d984eaa1ba65f11115~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            