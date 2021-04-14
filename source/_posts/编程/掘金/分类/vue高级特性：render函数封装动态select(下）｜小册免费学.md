
---
title: 'vue高级特性：render函数封装动态select(下）｜小册免费学'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d0804b99c1ac4081bd19490d841c750a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 14 Apr 2021 03:37:17 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d0804b99c1ac4081bd19490d841c750a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>接上篇文章👉<a href="https://juejin.cn/post/6950974720015597604" target="_blank"> vue高级特性：render函数封装动态select(上）｜小册免费学</a></p>
<h2 data-id="heading-0">自定义slots</h2>
<p><code>Select Slots</code>提供了<code>prefix/empty</code>这两个内置插槽，所以我们基于<code>el-select</code>封闭的组件需要支持用户自定义插槽内容</p>
<h3 data-id="heading-1">配置项</h3>
<blockquote>
<p>先根据目前提供配置项实现组件基础功能</p>
</blockquote>























<table><thead><tr><th align="center"><strong>参数</strong></th><th align="center"><strong>说明</strong></th><th align="center"><strong>类型</strong></th><th align="center"><strong>默认值</strong></th></tr></thead><tbody><tr><td align="center">slots</td><td align="center">插槽</td><td align="center"><code>Object</code></td><td align="center"><code>&#123;&#125;</code></td></tr><tr><td align="center">scopedSlots</td><td align="center">作用域插槽</td><td align="center"><code>Object</code></td><td align="center"><code>&#123;&#125;</code></td></tr></tbody></table>
<h3 data-id="heading-2">render函数</h3>
<p><code>DynamicSelect/select.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> SlotContent <span class="hljs-keyword">from</span> <span class="hljs-string">'./slotContent'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-comment">// ...忽略上篇文章定义过的配置项</span>
  
  <span class="hljs-comment">// 注册一个函数式组件用来渲染提供给组件外层插槽内容 </span>
  <span class="hljs-attr">components</span>: &#123; SlotContent &#125;,
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params">h</span>)</span> &#123;
   <span class="hljs-comment">// 配置插槽 => 用来渲染组件内置的作用域插槽</span>
    <span class="hljs-keyword">const</span> slots = <span class="hljs-built_in">Object</span>.keys(self.slots).map(<span class="hljs-function"><span class="hljs-params">slotName</span> =></span> &#123;
      <span class="hljs-keyword">return</span> [h(<span class="hljs-string">'slot-content'</span>, &#123;
        <span class="hljs-attr">props</span>: &#123;
          <span class="hljs-attr">render</span>: self.slots[slotName],
          <span class="hljs-attr">data</span>: self
        &#125;,
        <span class="hljs-attr">slot</span>: slotName,
        <span class="hljs-attr">key</span>: slotName
      &#125;)]
    &#125;)

  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面需要修改渲染<code>el-select</code>那块代码中<code>createElement</code>的第三个参数</p>
<p>createElement方法的第三个参数是当前节点的内容, 就类似于<code>div -> 可以放多个span</code>, 所以第三个参数包括：</p>
<ul>
<li>当前渲染元素(组件)的子节点</li>
<li>当前渲染元素(组件)提供的内置作用域插槽(可以通过$scopeSlots识别到)</li>
<li>当前渲染元素(组件)的插槽内容slot</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">return</span> h(<span class="hljs-string">'el-select'</span>, &#123;
  <span class="hljs-attr">class</span>: self.className,
  <span class="hljs-attr">staticClass</span>: <span class="hljs-string">'jl-full-line'</span>,
  ....
&#125;, [<span class="hljs-built_in">Object</span>.keys(<span class="hljs-built_in">this</span>.$slots).map(<span class="hljs-function"><span class="hljs-params">s</span> =></span> <span class="hljs-built_in">this</span>.$slots[s]), ...optionsVnode, ...slots])
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>通过上面我们就能将这三种类型的内容都渲染到el-select组件里面</p>
</blockquote>
<p><code>DynamicSelect/select.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'SlotContent'</span>,
  <span class="hljs-comment">// 声明这是函数式组件</span>
  <span class="hljs-attr">functional</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">render</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Function</span>,
      <span class="hljs-attr">require</span>: <span class="hljs-literal">true</span>
    &#125;,
    <span class="hljs-attr">data</span>: <span class="hljs-built_in">Object</span>
  &#125;,
  <span class="hljs-attr">render</span>: <span class="hljs-function">(<span class="hljs-params">h, ctx</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> ctx.props.render(h, ctx.props.data)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">灵活使用render来高度自定义组件</h3>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <DynamicSelect
    ref="DynamicSelect"
    :value.sync="projectId"
    v-bind="projectSelectOption"
    :parse-data="parseData"
    :formatter="formatterValue"
    :multiple="true"
    collapse-tags
    // 添加自定义slots配置
    :slots="customSlots"
  >
  </DynamicSelect>
</template>

<script>
export default &#123;
  data() &#123;
    return &#123;
      customSlots: &#123;
        prefix: this.prefixRender
      &#125;,
    &#125;
  &#125;,
   methods: &#123;
    prefixRender(h, vue) &#123;
      // h => createElement
      // vue => DynamicSelect实例

      // 我们可以通h来渲染任意组件到这个自定义插槽里面
      return h('div', &#123;
        staticClass: 'select-prefix',
      &#125;,
      [h('svg-icon', &#123;
        props: &#123;
          'icon-class': 'bug'
        &#125;,
      &#125;)])
    &#125;,
   &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">自定义options</h2>
<p><strong>效果图💗</strong></p>
<p><img alt="1.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d0804b99c1ac4081bd19490d841c750a~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<blockquote>
<p>继续完善render函数</p>
</blockquote>
<pre><code class="hljs language-diff copyable" lang="diff"><span class="hljs-addition">+ const &#123; value, label, labelRender &#125; = self.optionsProps</span>
<span class="hljs-addition">+ // 选项格式化显示</span>
<span class="hljs-addition">+ let labelRenderNode = null</span>
<span class="hljs-addition">+ if (labelRender && typeof labelRender === 'function') &#123;</span>
<span class="hljs-addition">+   labelRenderNode = function(labelValue, op) &#123;</span>
<span class="hljs-addition">+     return labelRender(h, labelValue, op)</span>
<span class="hljs-addition">+   &#125;</span>
<span class="hljs-addition">+ &#125;</span>

// 渲染options
 const optionsVnode = self.optionsData.map((op, index) => &#123;
    return [h('el-option', &#123;
      attrs: &#123;
        value: op[value],
        label: op[label],
        disabled: op.disabled
      &#125;,
      key: op.id || op.value // 绑定唯一key
<span class="hljs-addition">+    &#125; labelRenderNode ? labelRenderNode(op[label], op) : null)]</span>
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">formatter自定义options内容</h3>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <DynamicSelect
    ...
    // 添加自定义slots配置
    :slots="customSlots"
    :props="props"
  >
  </DynamicSelect>
</template>


<script>
// 定义渲染options的props
const props = &#123;
  label: 'proName',  
  value: 'id',
  children: 'children',
  labelRender(h, label, item) &#123;
    // h => createElement
    // label => options的label
    // item => options的每一项, 也就是每一个项目对象
    return [h('span', &#123;
      staticClass: 'left',
      domProps: &#123;
        innerText: label
      &#125;
    &#125;),
    h('span', &#123;
      staticClass: 'right',
      domProps: &#123;
        // 右侧我们展示了项目id的前两位
        innerText: item?.id.substr(0, 2) || ''
      &#125;
    &#125;)]
  &#125;
&#125;


export default &#123;
  data() &#123;
    return &#123;
      customSlots: &#123;
        prefix: this.prefixRender
      &#125;,
      // 通过Object.freeze冻结对象, 避免vue给对象每个成员加上getter/setter (也是个性能优化技巧)
      props: Object.freeze(props),
    &#125;
  &#125;,
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">通过$slots给组件里面加个全选</h2>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <DynamicSelect
    ...
  >
    <el-tag
      slot="selectAll"
      type="primary"
      class="select-tag-class"
      @click="handleSelectAll"
    >
      &#123;&#123; selectAllLabel[selectAll] &#125;&#125;
    </el-tag>
  </DynamicSelect>
</template>


<script>
export default &#123;
  data() &#123;
    return &#123;
      selectAllLabel: &#123;
        false: '全选',
        true: '取消',
      &#125;,
      // 默认非全选
      selectAll: false,
    &#125;
  &#125;,
  methods: &#123;
    // 全选Or取消
    handleSelectAll() &#123;
      this.selectAll = !this.selectAll
      const list = []

     
      if (this.selectAll) &#123; // 全选

      &#125; else &#123; // 取消
        
      &#125;
      // 通过$refs将内容
      this.$refs.DynamicSelect.newValue = list
    &#125;
  &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>这里就有个问题了, 我们是动态获取的options ,我$refs虽然可以引用DynamicSelect的optionsData属性, 但是我接口拉取需要时间, 假设我走详情页面进来我之前选中的全部,我要让选项全部选中怎么搞 , tip -> (我们项目选择全部的时候传给后端的是一个<code>[]</code>）</p>
</blockquote>
<p>为什么不把所有项目的id全传进去???</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
  这里设计到一个动态响应的问题, 假设我当时新增单据的时候总共有4个项目ids: [A, B, C, D]

  后面我新增了两个项目 [E, F]
  但是我之前存给后端的还是4个项目的id，所以当时有个项目中就是这么搞的
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>回到之前的问题，动态拉取的options我怎么及时响应呢？ 👉发布订阅</p>
<h3 data-id="heading-7">发布订阅</h3>
<blockquote>
<p>很多种实现方式，这里用类来写</p>
</blockquote>
<p><code>./DynamicSelect/Publish.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 发布订阅模式（解决options异步拉取数据的问题）</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Publish</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-built_in">this</span>.pond = []
  &#125;

  <span class="hljs-function"><span class="hljs-title">on</span>(<span class="hljs-params">callBack</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.pond.push(callBack)
  &#125;

  <span class="hljs-function"><span class="hljs-title">emit</span>(<span class="hljs-params">name</span>)</span> &#123; 
    <span class="hljs-comment">// 传递回调名称，有匹配的就将回调执行</span>
    <span class="hljs-keyword">const</span> fn = <span class="hljs-built_in">this</span>.pond.find(<span class="hljs-function"><span class="hljs-params">c</span> =></span> c.name === name)
    fn && fn()
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>给之前的方法加个自定义事件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 动态拉取选项数据</span>
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">getOptionsData</span>(<span class="hljs-params"></span>)</span> &#123;
<span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">'getOptionsSuccess'</span>, <span class="hljs-built_in">this</span>.optionsData)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>监听这个自定事件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">getOptionsSuccess</span>(<span class="hljs-params">data</span>)</span> &#123;
  <span class="hljs-comment">// 外层存储一份options的引用地址</span>
<span class="hljs-built_in">this</span>.selectOptions = data
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>完善handleSelectAll</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
<span class="hljs-keyword">import</span> Publish <span class="hljs-keyword">from</span> <span class="hljs-string">'./DynamicSelect/Publish.js'</span>
<span class="hljs-keyword">const</span> subscribe = <span class="hljs-keyword">new</span> Publish()
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">handleSelectAll</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-comment">// 可以方法内部往事件池里push回调，也可以在调用方法push(看执行时机)</span>
      <span class="hljs-built_in">this</span>.$nextTick(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">this</span>.selectAll = !<span class="hljs-built_in">this</span>.selectAll
        <span class="hljs-keyword">const</span> list = []
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.selectAll) &#123; <span class="hljs-comment">// 全选</span>
list = <span class="hljs-built_in">this</span>.selectOptions.map(<span class="hljs-function"><span class="hljs-params">i</span> =></span> i.id)
        &#125; <span class="hljs-keyword">else</span> &#123; <span class="hljs-comment">// 取消</span>
list = []
        &#125;
        <span class="hljs-comment">// 主动将组件全选 -> </span>
        <span class="hljs-comment">// $refs引用到组件的newValue直接赋值</span>
        <span class="hljs-comment">// 直接变动value 推荐这个</span>
        <span class="hljs-built_in">this</span>.porjectId = list
      &#125;)
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>至此组件封装就完事了，还有远程搜索那块没有写上来，发现写这种文章不太好写，代码太多又怕读者看起来发懵，不上代码干讲也感觉很难讲明白。比较难权衡，这也是我之前文章<a href="https://juejin.cn/post/6913092522814210061" target="_blank">【以模块化的思想开发中后台项目】</a>迟迟没有后续更新的原因，不过我也一直在学习这方面，这个系列后续还是会更的。</p>
<blockquote>
<p>tip: 本组件用render函数封闭并不是因为有多高级，render函数允许我们通过写js的方式来构建组件，相较于模板语法确实灵活不少，但是也需要付出相应的代价</p>
<p>很多Vue提供的语法糖是用不了的，需要自己去实现，所以需要根据组件功能各自取舍</p>
</blockquote>
<p>组件地址👉<a href="https://github.com/it-beige/blog/tree/master/DynamicSelect" target="_blank" rel="nofollow noopener noreferrer">github.com/it-beige/bl…</a></p>
<h1 data-id="heading-8">写在最后</h1>
<p>如果文章中有那块写的不太好或有问题欢迎大家指出，我也会在后面的文章不停修改。也希望自己进步的同时能跟你们一起成长。喜欢我文章的朋友们也可以关注一下</p>
<p>我会很感激第一批关注我的人。<strong>此时，年轻的我和你，轻装上阵；而后，富裕的你和我，满载而归。</strong></p>
<h2 data-id="heading-9">往期文章</h2>
<p><a href="https://juejin.cn/post/6894412199700201485" target="_blank">【建议追更】以模块化的思想来搭建中后台项目</a></p>
<p><a href="https://juejin.cn/post/6913092522814210061" target="_blank">【以模块化的思想开发中后台项目】第一章</a></p>
<p><a href="https://juejin.im/post/6868849475008331783" target="_blank" rel="nofollow noopener noreferrer">【前端体系】从一道面试题谈谈对EventLoop的理解</a>(更新了四道进阶题的解析)</p>
<p><a href="https://juejin.im/post/6867784542338416648" target="_blank" rel="nofollow noopener noreferrer">【前端体系】从地基开始打造一座万丈高楼</a></p>
<p><a href="https://juejin.im/post/6867784542338416648" target="_blank" rel="nofollow noopener noreferrer">【前端体系】正则在开发中的应用场景可不只是规则校验</a></p>
<p><a href="https://juejin.im/post/6878941871259779085" target="_blank" rel="nofollow noopener noreferrer">「函数式编程的实用场景 | 掘金技术征文-双节特别篇」</a></p>
<p><a href="https://juejin.cn/post/6888102016007176200" target="_blank">【建议收藏】css晦涩难懂的点都在这啦</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            