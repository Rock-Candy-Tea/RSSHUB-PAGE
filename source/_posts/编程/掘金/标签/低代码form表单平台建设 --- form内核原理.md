
---
title: '低代码form表单平台建设 --- form内核原理'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/417c0e5af84a47889e85aab2f052b541~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 24 Jul 2021 23:34:08 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/417c0e5af84a47889e85aab2f052b541~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>我们的目标是将<code>schema => form</code>表单，<code>schema</code>就是一个json对象，我们看看阿里的<code>form-render</code>库（一个低代码<code>react</code>的<code>form</code>表单库）的<code>schema</code>长什么样子：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
  <span class="hljs-string">"type"</span>: <span class="hljs-string">"object"</span>, 
  <span class="hljs-string">"properties"</span>: &#123;
    <span class="hljs-string">"count"</span>: &#123;
      <span class="hljs-comment">// 基础属性</span>
      <span class="hljs-string">"title"</span>: <span class="hljs-string">"代号"</span>,
      <span class="hljs-string">"type"</span>: <span class="hljs-string">"string"</span>,
      <span class="hljs-string">"min"</span>: <span class="hljs-number">6</span>,
      <span class="hljs-comment">// rules (补充校验信息)</span>
      <span class="hljs-string">"rules"</span>: [
        &#123;
          <span class="hljs-string">"pattern"</span>: <span class="hljs-string">"^[A-Za-z0-9]+$"</span>,
          <span class="hljs-string">"message"</span>: <span class="hljs-string">"只允许填写英文字母和数字"</span>
        &#125;
      ],
      <span class="hljs-comment">// props (补充antd组件props)</span>
      <span class="hljs-string">"props"</span>: &#123;
        <span class="hljs-string">"allowClear"</span>: <span class="hljs-literal">true</span>
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>虽然官方网站说这个JSON， 遵循<code>JSON Schema</code> 国际规范，但是我觉得这个规范太麻烦了，我是按照ant-design的使用习惯来定义schema的，主要是更符合使用习惯，类似ant是这样使用组件的，vue的elementUI好像也是类似的用法：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><Form 这里可以定义Form的属性>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Form.Item</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"account"</span> 这里可以定义<span class="hljs-attr">Form.Item</span>的属性></span>
        <span class="hljs-tag"><<span class="hljs-name">Input</span> 这里可以定义表单组件的属性 /></span>
    <span class="hljs-tag"></<span class="hljs-name">Form.Item</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Form.Item</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"password"</span>></span>
         <span class="hljs-tag"><<span class="hljs-name">Input</span> 这里可以定义表单组件的属性 /></span>
    <span class="hljs-tag"></<span class="hljs-name">Form.Item</span>></span></span>
</Form>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以对应跟组件使用差不多的schema定义如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
    <span class="hljs-comment">// 相当于在上面的 Form组件上定义的属性</span>
    <span class="hljs-attr">formOptions</span>:&#123;
        <span class="hljs-comment">// 当字段被删除时保留字段值</span>
        <span class="hljs-comment">// preserve:true</span>
    &#125;, 
    <span class="hljs-attr">formItems</span>: [ <span class="hljs-comment">// 相当于Form组件里所有Form.Item组件</span>
      &#123;
        <span class="hljs-comment">// 这个属性太重要了，必填，相当于每一个组件的标识符，可以是数组</span>
        <span class="hljs-comment">// 数组可以是字符串或者数字，以此定义嵌套对象，嵌套数组</span>
        <span class="hljs-attr">name</span>: <span class="hljs-string">'account'</span>, 
        <span class="hljs-comment">// value: '', 这里可以定义初始值，也可以不设置</span>
        <span class="hljs-attr">options</span>: &#123; <span class="hljs-comment">// 相当于Form.Item组件属性</span>
           <span class="hljs-comment">// hidden: xx 隐藏表单逻辑</span>
        &#125;, 
        <span class="hljs-comment">// 布局属性，后续会用这些属性控制组件的布局</span>
        <span class="hljs-comment">// 布局属性就是设置一行几列表单，表单label宽高等等ui属性</span>
        <span class="hljs-comment">// 可以看到我们是把ui属性和逻辑上表单属性解耦了的</span>
        <span class="hljs-comment">// 本篇文章不会涉及到这个属性</span>
        <span class="hljs-attr">layoutOptions</span>: &#123; <span class="hljs-comment">// 留给和面的布局组件属性</span>
            <span class="hljs-comment">// label: xx</span>
        &#125;, 
        <span class="hljs-comment">// 组件名，这里'input'会被转化为ant的Input组件</span>
        <span class="hljs-comment">// 会有一个map将字符串转换为组件</span>
        <span class="hljs-attr">Wiget</span>: <span class="hljs-string">'input'</span>,
        <span class="hljs-attr">WigetOptions</span>: &#123;&#125;, <span class="hljs-comment">// 表单组件属性</span>
      &#125;,
    ],
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>上面的name因为可以定义为数组，比如<code>['a', 'b']</code>,所以对应form表单的<code>&#123;a : &#123; b: '更改这里' &#125;&#125;</code></p>
</li>
<li>
<p>还可以定义为<code>[a, 1]</code>,会被解析为更改<code>&#123; a: [ undefined, '更改这里' ] &#125;</code>,</p>
</li>
</ul>
<p>通过这个name的命名设置，可以满足几乎全部表单对象值的格式要求。</p>
<p>所以我们希望form内核大概使用的方式是：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 定义schema</span>
<span class="hljs-keyword">const</span> schema = &#123;
  <span class="hljs-attr">formItems</span>: [
    &#123;
      <span class="hljs-attr">name</span>: <span class="hljs-string">'account'</span>,
      <span class="hljs-attr">value</span>: <span class="hljs-number">1</span>,
      <span class="hljs-attr">options</span>: &#123;
      &#125;,
      <span class="hljs-attr">Wiget</span>: <span class="hljs-string">'input'</span>
    &#125;
  ]
&#125;

<span class="hljs-keyword">const</span> Demo = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> [form] = useForm(&#123; schema &#125;);
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Form</span> <span class="hljs-attr">form</span>=<span class="hljs-string">&#123;form&#125;</span> /></span></span>;
&#125;;

ReactDOM.render(
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Demo</span> /></span></span>,
  <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'app'</span>)
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上配置就渲染一个Input的组件，并且<code>form</code>提供一系列方法就像<code>ant</code>一样，可以<code>getFiledsValue</code>, <code>setFieldsValue</code>等等方法，让我们的使用跟<code>ant</code>几乎是无缝连接，</p>
<p>有人会说，直接用ant就可以改装啊，但是你要知道，</p>
<p>但是ant本身一些属性是函数，<code>JSON</code>上是不能挂函数的，因为<code>JSON.stringify</code>会把函数过滤掉，所以，很多ant属性需要挂函数，内部就不支持了，比如<code>onFinish</code>事件，<code>shouldUpdate</code>方法等等</p>
<p>还有如果我们业务某个产品需要很多自定义的需求，可能涉及到要改底层的form库，就需要自己开发一套了，所以魔改<code>ant</code>的<code>form</code>不太好，还不如自己开发一套呢</p>
<p>废话不多说，开始编码！</p>
<p>我们的大体架构如下（没有写form渲染器器（即可视化拖拽表单这块功能）后续加）：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/417c0e5af84a47889e85aab2f052b541~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图比较简陋，我们先把<code>FormStore</code>搭建好，毕竟它是调度组件的老大，为了省时间，就不用ts了，先js跑通。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 使用ramda库提供的一些工具函数</span>
<span class="hljs-keyword">import</span> &#123; path, clone, assocPath, merge,
type, equals &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'ramda'</span>

      <span class="hljs-comment">// 此标识符意味着通知所有组件更新</span>
      <span class="hljs-keyword">const</span> ALL = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'*'</span>);
      <span class="hljs-comment">// 此标识符用来标识formStore</span>
      <span class="hljs-keyword">const</span> FORM_SIGN = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'formStoreSign'</span>);
      <span class="hljs-comment">// 导出内部方法的标识符</span>
      <span class="hljs-keyword">const</span> INNER_HOOKS_SIGN = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">"innerHooks"</span>);

      <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">FormStore</span> </span>&#123;
        <span class="hljs-comment">// 参数是初始化的values</span>
        <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">initialValue</span>)</span> &#123;
          <span class="hljs-comment">// 后续有resetValue，也就是重置表单的方法，所以要留住它</span>
          <span class="hljs-built_in">this</span>.initialValue = initialValue
          <span class="hljs-comment">// values存储form表单的值</span>
          <span class="hljs-comment">// clone是ramda提供的深克隆功能</span>
          <span class="hljs-built_in">this</span>.values = initialValue ? clone(initialValue) : &#123;&#125;
          <span class="hljs-comment">// 事件收集器，订阅的事件（函数）都存放在这里</span>
          <span class="hljs-built_in">this</span>.listeners = []
        &#125;

        <span class="hljs-comment">// 获取表单值</span>
        getFieldValues = <span class="hljs-function">(<span class="hljs-params">name</span>) =></span> &#123;
          <span class="hljs-keyword">return</span> clone(<span class="hljs-built_in">this</span>.values)
        &#125;

        <span class="hljs-comment">// 这里的name不一定是字符串，也有可能是字符串数组,或者数组下标（string | string | number[]）</span>
        <span class="hljs-comment">//  例如：name = ['a', 'b']意思是获取form表单值（value）对象的value[a][b]属性值</span>
        getFieldValue = <span class="hljs-function">(<span class="hljs-params">name</span>) =></span> &#123;
          <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> name !== <span class="hljs-string">'string'</span> && !<span class="hljs-built_in">Array</span>.isArray(name)) &#123;
            <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">`参数 <span class="hljs-subst">$&#123;name&#125;</span> 需要是字符串或者数组`</span>)
          &#125;
          <span class="hljs-comment">// strToArray定义在下面，就是转化为数组的函数</span>
          <span class="hljs-comment">// 因为path第一个参数必须是数组，name有可能是字符串</span>
          <span class="hljs-comment">// path用法：</span>
          <span class="hljs-comment">// path(['a', 'b'], &#123;a: &#123;b: 2&#125;&#125;) => 2</span>
          <span class="hljs-keyword">return</span> path(strToArray(name), <span class="hljs-built_in">this</span>.values)
        &#125;

        <span class="hljs-comment">// 设置form表单 单个值的方法</span>
        setFieldValue = <span class="hljs-function">(<span class="hljs-params">name, value</span>) =></span> &#123;
          <span class="hljs-keyword">const</span> newName = strToArray(name)
          <span class="hljs-comment">// assocPath是ramda用来给对象设置值的函数</span>
          <span class="hljs-comment">// assocPath用法：</span>
          <span class="hljs-comment">// assocPath(['a', 'b', 'c'], 42, &#123;a: &#123;b: &#123;c: 0&#125;&#125;&#125;)</span>
          <span class="hljs-comment">// => &#123;a: &#123;b: &#123;c: 42&#125;&#125;&#125;</span>
          <span class="hljs-built_in">this</span>.values = assocPath(newName, value, <span class="hljs-built_in">this</span>.values)
          <span class="hljs-comment">// 发布事件，我们的事件都是以名字字符串作为标识</span>
          <span class="hljs-built_in">this</span>.notify(name)
        &#125;

        <span class="hljs-comment">// 设置form表单 多个值的方法</span>
        setFieldsValue = <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
          <span class="hljs-comment">// 如果value不是对象（&#123;&#125;这样的对象，其它数组这些对象不行，此函数不执行</span>
          <span class="hljs-keyword">if</span> (R.type(value) !== <span class="hljs-string">'Object'</span>) <span class="hljs-keyword">return</span>
          <span class="hljs-comment">// pickPath方法能把对象解析为路径</span>
          <span class="hljs-comment">// pickPaths(&#123;a: 2, c: 3 &#125;)</span>
          <span class="hljs-comment">// => [[&#123;path: 'a', value: 2 &#125;], [&#123; path: 'c', vlaue: 3 &#125;]]</span>
          <span class="hljs-keyword">const</span> paths = pickPaths(value)
          paths.forEach(<span class="hljs-function">(<span class="hljs-params">item</span>) =></span> &#123;
            <span class="hljs-built_in">this</span>.values = assocPath(item.path, item.value, <span class="hljs-built_in">this</span>.values)
          &#125;)
          <span class="hljs-built_in">this</span>.notify(ALL)
        &#125;

        <span class="hljs-comment">// 通知的方法,通知单个或者所有组件更新表单值</span>
        notify = <span class="hljs-function">(<span class="hljs-params">name</span>) =></span> &#123;
          <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> listener <span class="hljs-keyword">of</span> <span class="hljs-built_in">this</span>.listeners) listener(name)
        &#125;

        <span class="hljs-comment">// 订阅事件的方法，返回清除事件的函数，在组件卸载的时候需要清除这个组件订阅的事件</span>
        subscribe = <span class="hljs-function">(<span class="hljs-params">listener</span>) =></span> &#123;
          <span class="hljs-built_in">this</span>.listeners.push(listener)
          <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> &#123;
            <span class="hljs-comment">// 取消订阅</span>
            <span class="hljs-keyword">const</span> index = <span class="hljs-built_in">this</span>.listeners.indexOf(listener)
            <span class="hljs-keyword">if</span> (index > -<span class="hljs-number">1</span>) <span class="hljs-built_in">this</span>.listeners.splice(index, <span class="hljs-number">1</span>)
          &#125;
        &#125;

        <span class="hljs-comment">// 暴露formStore的内部方法给外面，不让其直接访问FormStore</span>
        getFormExport = <span class="hljs-function">(<span class="hljs-params">schema</span>) =></span> &#123;
          <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">signType</span>: FORM_SIGN,
            <span class="hljs-attr">getFieldValue</span>: <span class="hljs-built_in">this</span>.getFieldValue,
            <span class="hljs-attr">setFieldValue</span>: <span class="hljs-built_in">this</span>.setFieldValue,
            <span class="hljs-attr">setFieldsValue</span>: <span class="hljs-built_in">this</span>.setFieldsValue,
            <span class="hljs-attr">isSamePath</span>: <span class="hljs-built_in">this</span>.isSamePath,
            <span class="hljs-attr">getInnerHooks</span>: <span class="hljs-built_in">this</span>.getInnerHooks(schema),
          &#125;
        &#125;
        <span class="hljs-comment">// 判断两个路径是否相等，如下</span>
        <span class="hljs-comment">// equals([1, 2, 3], [1, 2, 3]); //=> true</span>
        isSamePath = <span class="hljs-function">(<span class="hljs-params">path1, path2</span>) =></span> &#123;
          <span class="hljs-keyword">if</span> (type(path1) !== <span class="hljs-string">'Array'</span> || type(path2) !== <span class="hljs-string">'Array'</span>) &#123;
            <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">`isSamePath函数的参数均需数组`</span>)
          &#125;
          <span class="hljs-keyword">return</span> equals(path1, path2) <span class="hljs-comment">//=> true</span>
        &#125;
        
        <span class="hljs-comment">// 获取内部方法，只在内部组件使用</span>
        getInnerHooks = <span class="hljs-function"><span class="hljs-params">schema</span> =></span> <span class="hljs-function"><span class="hljs-params">sign</span> =></span> &#123;
          <span class="hljs-keyword">if</span>(sign === INNER_HOOKS_SIGN) &#123;
            <span class="hljs-keyword">return</span> &#123;
              <span class="hljs-attr">getFieldValue</span>: <span class="hljs-built_in">this</span>.getFieldValue,
              <span class="hljs-attr">setFieldValue</span>: <span class="hljs-built_in">this</span>.setFieldValue,
              <span class="hljs-attr">setFieldsValue</span>: <span class="hljs-built_in">this</span>.setFieldsValue,
              <span class="hljs-attr">isSamePath</span>: <span class="hljs-built_in">this</span>.isSamePath,
              <span class="hljs-attr">subscribe</span>: <span class="hljs-built_in">this</span>.subscribe,
              <span class="hljs-attr">notify</span>: <span class="hljs-built_in">this</span>.notify,
              schema
            &#125;
          &#125;
          <span class="hljs-built_in">console</span>.warn(<span class="hljs-string">'外部禁止使用getInnerHooks方法'</span>);
          <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;
        &#125;
      &#125;

      <span class="hljs-comment">// 下面是工具函数</span>

      <span class="hljs-comment">// 此函数就是把字符串转数组的函数</span>
      <span class="hljs-keyword">const</span> strToArray = <span class="hljs-function">(<span class="hljs-params">name</span>) =></span> &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> name === <span class="hljs-string">'string'</span>) <span class="hljs-keyword">return</span> [name]
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(name)) <span class="hljs-keyword">return</span> name
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">`<span class="hljs-subst">$&#123;name&#125;</span> 参数必须是数组或者字符串`</span>)
      &#125;

      <span class="hljs-comment">// 这个函数是用来提取对象的路径的比如说：</span>
      <span class="hljs-comment">// pickPaths(&#123;a: 2, c: 3 &#125;)</span>
      <span class="hljs-comment">// => [[&#123;path: 'a', value: 2 &#125;], [&#123; path: 'c', vlaue: 3 &#125;]]</span>
      <span class="hljs-comment">// pickPaths(&#123; b:[ &#123; a : 1 &#125; ] )</span>
      <span class="hljs-comment">// => [[ &#123; path: [ "b", 0, "a"], value: 1 &#125;]]</span>
      <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">pickPaths</span>(<span class="hljs-params">root, collects = [], resultPaths = []</span>) </span>&#123;
        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">dfs</span>(<span class="hljs-params">root, collects</span>) </span>&#123;
          <span class="hljs-keyword">if</span> (type(root) === <span class="hljs-string">'Object'</span>) &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-built_in">Object</span>.keys(root).map(<span class="hljs-function">(<span class="hljs-params">item</span>) =></span> &#123;
              <span class="hljs-keyword">const</span> newCollect = clone(collects)
              newCollect.push(item)
              <span class="hljs-keyword">return</span> dfs(root[item], newCollect)
            &#125;)
          &#125;
          <span class="hljs-keyword">if</span> (type(root) === <span class="hljs-string">'Array'</span>) &#123;
            <span class="hljs-keyword">return</span> root.map(<span class="hljs-function">(<span class="hljs-params">item, index</span>) =></span> &#123;
              <span class="hljs-keyword">const</span> newCollect = clone(collects)
              newCollect.push(index)
              <span class="hljs-keyword">return</span> dfs(item, newCollect)
            &#125;)
          &#125;
          <span class="hljs-keyword">return</span> resultPaths.push(&#123; <span class="hljs-attr">path</span>: collects, <span class="hljs-attr">value</span>: root &#125;)
        &#125;
        dfs(root, collects)
        <span class="hljs-keyword">return</span> resultPaths
      &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面需要注意的是：</p>
<ul>
<li><code>this.notify(name)</code>中的的<code>name</code>，可以是数组或者字符串，比如<code>['account', 'CCB']</code>, <code>['account', 0]</code></li>
</ul>
<p>好了，我们可以试试我们刚才写的的<code>FormStore</code>组件能干啥了</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> formStore = <span class="hljs-keyword">new</span> FormStore(&#123; <span class="hljs-attr">account</span>: [ &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'CCB'</span> &#125; ] &#125;);
formStore.setFieldsValue(&#123; <span class="hljs-attr">account</span>: [ &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'xiaoming'</span> &#125;, <span class="hljs-number">123</span> ] &#125;);

<span class="hljs-comment">// 打印formStore.value</span>
<span class="hljs-comment">// => &#123; account: [ &#123; name: 123 &#125;, 123 ] &#125;</span>
<span class="hljs-built_in">console</span>.log(formStore.values)


formStore.setFieldValue([ <span class="hljs-string">'account'</span>, <span class="hljs-number">1</span>, <span class="hljs-string">'age'</span> ], <span class="hljs-number">10</span>)
<span class="hljs-comment">// =>  &#123; account: [ &#123; name: 123 &#125;, age: 10 ] &#125;</span>
<span class="hljs-built_in">console</span>.log(formStore.values)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>上面可以看到，这个路径解析模块对我们来说非常重要，所以后续我会把它<code>单独提取</code>出来作为一个服务，我们在平时的业务代码里，也需要把这些比较重要的模块，单独提取成<code>服务类</code>，或者<code>hooks</code>。</p>
</li>
<li>
<p>其次后面会用函数式写法再重构一下具体的函数。上面的写法只是为了不了解函数式和不会使用<code>ramda库</code>的同学看。</p>
</li>
</ul>
<p>我们接着再简单试一下formStore的注册函数功能</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> formStore = <span class="hljs-keyword">new</span> FormStore(&#123; <span class="hljs-attr">account</span>: [&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"CCB"</span> &#125;] &#125;);
formStore.subscribe(<span class="hljs-function">(<span class="hljs-params">name</span>)=></span>&#123; 
   <span class="hljs-keyword">if</span>(name === ALL || formStore.isSamePath(name, [ <span class="hljs-string">'account'</span>, <span class="hljs-number">0</span>, <span class="hljs-string">'name'</span> ]))&#123;
   <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'路径匹配 [ account, 0, name ]'</span>)
   &#125;
&#125;)
 <span class="hljs-comment">//  formStore.setFieldsValue(&#123; account: [&#123; name: "A" &#125;] &#125;)</span>
 <span class="hljs-comment">// => 打印 路径匹配 [ account, 0, name ]</span>
 formStore.setFieldValue([ <span class="hljs-string">'account'</span>, <span class="hljs-number">0</span>, <span class="hljs-string">'name'</span> ], <span class="hljs-string">'A'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>好了，这个模块按道理我的测试用例需要用测试库的，这里就不用了，欢迎过两天大家去看我的即将发布的<code>jest入门</code>。（主要是为了宣传这个，不停的学习，棒棒哒😄）</p>
<p>上面<code>subscribe</code>订阅事件和<code>notify</code>发布事件是一个简单的发布订阅模型。说白了跟redux的源码差不多，订阅事件就是把订阅的函数放到一个数组，发布事件就是把数组里的函数拿出来调用一遍。</p>
<p>接下来我们看看Form组件是怎样的</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; INNER_HOOKS_SIGN &#125; form <span class="hljs-string">'./utils'</span>;
<span class="hljs-keyword">import</span> &#123; FormContext &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./context'</span>;

<span class="hljs-comment">// form组件映射关系</span>
<span class="hljs-keyword">const</span> WigetsMap = &#123;
  <span class="hljs-attr">input</span>: Input
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Form</span>(<span class="hljs-params">props</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (props.form.signType !== FORM_SIGN) <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'form类型错误'</span>);
  <span class="hljs-comment">// 这里的form是后面useForm产生的对象</span>
  <span class="hljs-comment">// 这个对象实际是formStore的exportForm方法导出的对象</span>
  <span class="hljs-comment">// signType用来标示是我们的formStore.exportForm方法导出的对象</span>
  <span class="hljs-keyword">if</span>(form.signType !== FORM_SIGN) <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'form类型错误'</span>);
  <span class="hljs-comment">// 外部传的form</span>
  <span class="hljs-keyword">const</span> &#123; form, ...restProps &#125; = props;
  <span class="hljs-comment">// 获取到fromStore的getInnerHooks方法导出的内部函数</span>
  <span class="hljs-keyword">const</span> innerForm = form.getInnerHooks(INNER_HOOKS_SIGN);
  
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">form</span>
      &#123;<span class="hljs-attr">...restProps</span>&#125;
      <span class="hljs-attr">onSubmit</span>=<span class="hljs-string">&#123;(event)</span> =></span> &#123;
        event.preventDefault();
        event.stopPropagation();
        // 调用了formInstance 提供的submit方法
        // innerForm.submit();
      &#125;&#125;
    >
      &#123;/* formInstance 当做全局的 context 传递下去 */&#125;
      <span class="hljs-tag"><<span class="hljs-name">FormContext.Provider</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;innerForm&#125;</span>></span>
        &#123;/* useForm的时候schema会传给form */&#125;
        &#123;innerForm.schema?.formItem?.map((item, index) => &#123;
          return (
             &#123;/* formItem属性在传递给下面 */&#125;
            <span class="hljs-tag"><<span class="hljs-name">FormItem</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;index&#125;</span> <span class="hljs-attr">name</span>=<span class="hljs-string">&#123;item.name&#125;</span> &#123;<span class="hljs-attr">...item.options</span>&#125;></span>
              &#123;/* WigetOptions属性在传递给下面 */&#125;
               &#123;WigetsMap[item.Wiget] ? <span class="hljs-tag"><<span class="hljs-name">item.Wiget</span> &#123;<span class="hljs-attr">...item.WigetOptions</span>&#125; /></span> : null&#125;
            <span class="hljs-tag"></<span class="hljs-name">FormItem</span>></span>
          );
        &#125;)&#125;
      <span class="hljs-tag"></<span class="hljs-name">FormContext.Provider</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">form</span>></span></span>
  );
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>Form组件主要的功能就是把innerForm传递给Form.Item组件，这个innerFrom我们看上面的FormStore组件getInnerHooks是怎么样的：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">        <span class="hljs-comment">// 获取内部方法，只在内部组件使用</span>
        getInnerHooks = <span class="hljs-function"><span class="hljs-params">schema</span> =></span> <span class="hljs-function"><span class="hljs-params">sign</span> =></span> &#123;
          <span class="hljs-keyword">if</span>(sign === INNER_HOOKS_SIGN) &#123;
            <span class="hljs-keyword">return</span> &#123;
              <span class="hljs-attr">getFieldValue</span>: <span class="hljs-built_in">this</span>.getFieldValue,
              <span class="hljs-attr">setFieldValue</span>: <span class="hljs-built_in">this</span>.setFieldValue,
              <span class="hljs-attr">setFieldsValue</span>: <span class="hljs-built_in">this</span>.setFieldsValue,
              <span class="hljs-attr">isSamePath</span>: <span class="hljs-built_in">this</span>.isSamePath,
              <span class="hljs-attr">subscribe</span>: <span class="hljs-built_in">this</span>.subscribe,
              <span class="hljs-attr">notify</span>: <span class="hljs-built_in">this</span>.notify,
              schema,
            &#125;
          &#125;
          <span class="hljs-built_in">console</span>.warn(<span class="hljs-string">'外部禁止使用getInnerHooks方法'</span>);
          <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到导出的对象必须传入INNER_HOOKS_SIGN标识符才能获取，INNER_HOOKS_SIGN是组件内部的，外面使用useForm的开发者是拿不到的，所以道处对象只服务于组件内部。</p>
<p>目的就是用来获取和设置属性，已经订阅和发布事件。</p>
<p>上文还有FormContext这个context，我们看下这个文件长什么样</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>

<span class="hljs-keyword">const</span> warningFunc: any = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">console</span>.warn(
    <span class="hljs-string">'Please make sure to call the getInternalHooks correctly'</span>
    );
  &#125;;
  
  <span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> FormContext = React.createContext(&#123;
    <span class="hljs-attr">getInnerHooks</span>: <span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">getFieldValue</span>: warningFunc,
        <span class="hljs-attr">setFieldValue</span>: warningFunc,
        <span class="hljs-attr">setFieldsValue</span>: warningFunc,
        <span class="hljs-attr">isSamePath</span>: warningFunc,
        <span class="hljs-attr">subscribe</span>: warningFunc,
        <span class="hljs-attr">notify</span>: warningFunc,
      &#125;;
    &#125;,
  &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>默认的参数就是我们在<code>FormStore</code>定义的<code>getInnerHooks</code>的方法，保证它们两个函数导出属性名字一致，这里就体现了<code>typescript</code>的重要性了。</p>
<p>欢迎大家去我的博客里看，以一篇<a href="https://juejin.cn/post/6844903862390751240" target="_blank" title="https://juejin.cn/post/6844903862390751240">typescript基础入门</a></p>
<p>接下来，我们看一下,外部的useForm是怎么使用的</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> useForm = <span class="hljs-function">(<span class="hljs-params">props</span>) =></span> &#123;
  <span class="hljs-comment">// 检测schema是否符合规范，不符合报错</span>
  checkSchema(props.schema);
  <span class="hljs-comment">// 保存schema的值</span>
  <span class="hljs-keyword">const</span> schemaRef = useRef(props.schema);
  <span class="hljs-comment">// 保存form的引用对象</span>
  <span class="hljs-keyword">const</span> formRef = useRef();
  
  <span class="hljs-comment">// 第一次渲染初始化formStore</span>
  <span class="hljs-keyword">if</span> (!formRef.current) &#123;
    formRef.current = <span class="hljs-keyword">new</span> FormStore(setSchemaToValues(props.schema)).getFormExport(props.schema);
  &#125;
  <span class="hljs-comment">// 如果schema发生变化，formStore重新生成</span>
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">JSON</span>.stringify(props.schema) !== <span class="hljs-built_in">JSON</span>.stringify(schemaRef.current)) &#123;
    schemaRef.current = props.schema;
    formRef.current = <span class="hljs-keyword">new</span> FormStore(setSchemaToValues(props.schema)).getFormExport(props.schema);
  &#125;
  <span class="hljs-keyword">return</span> [formRef.current];
&#125;;

<span class="hljs-comment">// 工具函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">checkSchema</span>(<span class="hljs-params">schema</span>) </span>&#123;
  ifElse(
    isArrayAndNotNilArray,
    forEach(checkFormItems),
    <span class="hljs-function">() =></span> &#123; <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'formItems property of schema need to an Array'</span>) &#125;
  )(path([<span class="hljs-string">'formItems'</span>], schema));
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">checkFormItems</span>(<span class="hljs-params">item</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (!all(equals(<span class="hljs-literal">true</span>))([isObject(item), isNameType(item.name)])) &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'please check whether formItems field of schema meet the specifications'</span>);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面唯一指值得一说的就是useRef的使用，可以当做单例模式来用，如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> a = useRef();
<span class="hljs-keyword">if</span>(!a.current) <span class="hljs-keyword">return</span> <span class="hljs-number">1</span>;
<span class="hljs-keyword">return</span> a.current
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第一次赋值1，如果存在就一直是1，不会变</p>
<p>接着我们看一下<code>Form.Item</code>组件的代码</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> React, &#123; cloneElement, useEffect, useContext, useState &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>
<span class="hljs-keyword">import</span> &#123; FormContext &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./context'</span>;
<span class="hljs-keyword">import</span> &#123; ALL &#125; form <span class="hljs-string">'./utils'</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">FormItem</span>(<span class="hljs-params">props: any</span>) </span>&#123;
  <span class="hljs-keyword">const</span> &#123; name, children &#125; = props;

  <span class="hljs-comment">// 这个是获得store的Context，后面会有讲解</span>
  <span class="hljs-keyword">const</span> innerForm = useContext(FormContext);

  <span class="hljs-comment">// 如果如果我们schema初始化有值，就会传到这里</span>
  <span class="hljs-keyword">const</span> [value, setValue] = useState(name && store ? innerForm.getFieldValue(name) : <span class="hljs-literal">undefined</span>);

  useEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">if</span> (!name || !innerForm) <span class="hljs-keyword">return</span>;
    <span class="hljs-comment">// 判断n如果是ALL表示大家都要更新</span>
    <span class="hljs-comment">// 或者单独更新这个form表单</span>
    <span class="hljs-comment">// 要求n和name相同</span>
    <span class="hljs-keyword">return</span> innerForm.subscribe(<span class="hljs-function">(<span class="hljs-params">n</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (n === ALL || (<span class="hljs-built_in">Array</span>.isArray(n) 
      && innerForm.isSamePath(n, name))) &#123;
        setValue(store.getFieldValue(name));
      &#125;
    &#125;);
  &#125;, [name, innerForm]);

  <span class="hljs-keyword">return</span> cloneElement(children, &#123;
    value,
    <span class="hljs-attr">onChange</span>: <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
      innerForm.setFieldValue(name, e.target.value);
    &#125;,
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里需要注意的是，cloneElement把children包装了一下，传入了value和onChange方法，例如:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><Form.Item name=<span class="hljs-string">"account"</span> 这里可以定义Form.Item的属性>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Input</span> 这里可以定义表单组件的属性 /></span></span>
</Form.Item>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里的Input就能自动接收到value和onChange属性和方法了</p>
<ul>
<li>并且onChange方法会调用innerForm的setFieldValue方法</li>
<li>这个方法就会调用formItem在useEffect里面注册的方法，实现单独更新组件的目标，不用全局刷新</li>
</ul>
<p>这篇文章完全是自己感兴趣低代码的form平台表单实现原理，自己查了些资料，写了一个能跑通的demo，但是原理是没有问题的，可能里面还是会有bug，欢迎大家评论区提出，周末还在写文章，看在辛苦的份上，大哥点个赞吧，😀</p>
<p>下面的代码使用ramda库重构了一版，自己跑了一下，暂时没发现问题。本文后续计划如下：</p>
<ul>
<li>加入typescript</li>
<li>加入jest测试函数功能</li>
<li>加入可视化的表单生成界面</li>
</ul>
<pre><code class="hljs language-JAVASCRIPT copyable" lang="JAVASCRIPT"><span class="hljs-keyword">import</span> ReactDOM <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom'</span>;
<span class="hljs-keyword">import</span> React, &#123; useState, useContext, useEffect, useRef, cloneElement &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> &#123; path, clone, assocPath, type, equals, pipe, __, all, when, ifElse, F, forEach, reduce &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'ramda'</span>;
<span class="hljs-keyword">import</span> &#123; Input &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'antd'</span>;

<span class="hljs-comment">// 常量模块</span>
<span class="hljs-keyword">const</span> ALL = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'*'</span>);
<span class="hljs-keyword">const</span> FORM_SIGN = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'formStoreSign'</span>);
<span class="hljs-keyword">const</span> INNER_HOOKS_SIGN = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'innerHooks'</span>);

<span class="hljs-comment">// 工具函数模块</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isString</span>(<span class="hljs-params">name</span>) </span>&#123;
  <span class="hljs-keyword">return</span> type(name) === <span class="hljs-string">'String'</span>;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isArray</span>(<span class="hljs-params">name</span>) </span>&#123;
  <span class="hljs-keyword">return</span> type(name) === <span class="hljs-string">'Array'</span>;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isArrayAndNotNilArray</span>(<span class="hljs-params">name</span>) </span>&#123;
  <span class="hljs-keyword">if</span>(type(name) !== <span class="hljs-string">'Array'</span>) <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
  <span class="hljs-keyword">return</span> name.length === <span class="hljs-number">0</span> ? <span class="hljs-literal">false</span> : <span class="hljs-literal">true</span>;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isUndefined</span>(<span class="hljs-params">name</span>) </span>&#123;
  <span class="hljs-keyword">return</span> type(name) === <span class="hljs-string">'Undefined'</span>;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isObject</span>(<span class="hljs-params">name</span>) </span>&#123;
  <span class="hljs-keyword">return</span> type(name) === <span class="hljs-string">'Object'</span>;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">strToArray</span>(<span class="hljs-params">name</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (isString(name)) <span class="hljs-keyword">return</span> [name];
  <span class="hljs-keyword">if</span> (isArray(name)) <span class="hljs-keyword">return</span> name;
  <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">`<span class="hljs-subst">$&#123;name&#125;</span> params need to an Array or String`</span>);
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isStrOrArray</span>(<span class="hljs-params">name</span>) </span>&#123;
  <span class="hljs-keyword">return</span> isString(name) || isArray(name);
&#125;

<span class="hljs-keyword">const</span> returnNameOrTrue = <span class="hljs-function"><span class="hljs-params">returnName</span> =></span> <span class="hljs-function"><span class="hljs-params">name</span> =></span> &#123;
  <span class="hljs-keyword">return</span> returnName ? name : <span class="hljs-literal">true</span>;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isNameType</span>(<span class="hljs-params">name, returnName = <span class="hljs-literal">false</span></span>) </span>&#123;
  <span class="hljs-keyword">return</span> ifElse(
    isStrOrArray,
    returnNameOrTrue(returnName),
    F,
  )(name)
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">checkSchema</span>(<span class="hljs-params">schema</span>) </span>&#123;
  ifElse(
    isArrayAndNotNilArray,
    forEach(checkFormItems),
    <span class="hljs-function">() =></span> &#123; <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'formItems property of schema need to an Array'</span>) &#125;
  )(path([<span class="hljs-string">'formItems'</span>], schema));
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">checkFormItems</span>(<span class="hljs-params">item</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (!all(equals(<span class="hljs-literal">true</span>))([isObject(item), isNameType(item.name)])) &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'please check whether formItems field of schema meet the specifications'</span>);
  &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">setFormReduce</span>(<span class="hljs-params">acc, item</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (!isUndefined(item.value)) &#123;
    acc = assocPath(strToArray(item.name), item.value, acc)
  &#125;
  <span class="hljs-keyword">return</span> acc;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">setSchemaToValues</span>(<span class="hljs-params">initialSchema</span>) </span>&#123;
  <span class="hljs-keyword">return</span> pipe(
    path([<span class="hljs-string">'formItems'</span>]),
    reduce(setFormReduce, &#123;&#125;)
  )(initialSchema)
&#125;

<span class="hljs-keyword">const</span> warningFunc = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.warn(
    <span class="hljs-string">'Please make sure to call the getInternalHooks correctly'</span>
  );
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> FormContext = React.createContext(&#123;
  <span class="hljs-attr">getInnerHooks</span>: <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">getFieldsValue</span>: warningFunc,
      <span class="hljs-attr">getFieldValue</span>: warningFunc,
      <span class="hljs-attr">setFieldValue</span>: warningFunc,
      <span class="hljs-attr">setFieldsValue</span>: warningFunc,
      <span class="hljs-attr">isSamePath</span>: warningFunc,
      <span class="hljs-attr">subscribe</span>: warningFunc,
      <span class="hljs-attr">notify</span>: warningFunc
    &#125;;
  &#125;
&#125;);


<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">pickPaths</span>(<span class="hljs-params">root, collects = [], resultPaths = []</span>) </span>&#123;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">dfs</span>(<span class="hljs-params">root, collects</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (isObject(root)) &#123;
      <span class="hljs-keyword">return</span> dfsObj(root)
    &#125;
    <span class="hljs-keyword">if</span> (isArray(root)) &#123;
      <span class="hljs-keyword">return</span> dfsArr(root)
    &#125;
    <span class="hljs-keyword">return</span> resultPaths.push(&#123; <span class="hljs-attr">path</span>: collects, <span class="hljs-attr">value</span>: root &#125;)
  &#125;

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">dfsObj</span>(<span class="hljs-params">root</span>) </span>&#123;
    <span class="hljs-built_in">Object</span>.keys(root).map(<span class="hljs-function">(<span class="hljs-params">item</span>) =></span> &#123;
      <span class="hljs-keyword">const</span> newCollect = clone(collects)
      newCollect.push(item)
      <span class="hljs-keyword">return</span> dfs(root[item], newCollect)
    &#125;)
  &#125;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">dfsArr</span>(<span class="hljs-params">root</span>) </span>&#123;
    root.map(<span class="hljs-function">(<span class="hljs-params">item, index</span>) =></span> &#123;
      <span class="hljs-keyword">const</span> newCollect = clone(collects)
      newCollect.push(index)
      <span class="hljs-keyword">return</span> dfs(item, newCollect)
    &#125;)
  &#125;
  dfs(root, collects)
  <span class="hljs-keyword">return</span> resultPaths
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">FormStore</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">initialValue</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.initialValue = initialValue
    <span class="hljs-built_in">this</span>.values = initialValue ? clone(initialValue) : &#123;&#125;
    <span class="hljs-built_in">this</span>.listeners = []
  &#125;
  getFieldsValue = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">return</span> clone(<span class="hljs-built_in">this</span>.values)
  &#125;

  getFieldValue = <span class="hljs-function">(<span class="hljs-params">name</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> ifElse(
      isNameType,
      pipe(strToArray, path(__, <span class="hljs-built_in">this</span>.values)),
      F,
    )(name, <span class="hljs-literal">true</span>)
  &#125;
  setFieldValue = <span class="hljs-function">(<span class="hljs-params">name, value</span>) =></span> &#123;
    pipe(
      strToArray,
      <span class="hljs-function">(<span class="hljs-params">newName</span>) =></span> &#123;
        <span class="hljs-built_in">this</span>.values = assocPath(newName, value, <span class="hljs-built_in">this</span>.values);
        <span class="hljs-built_in">this</span>.notify(name);
      &#125;,
    )(name)
  &#125;

  setFieldsValue = <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> when(
      isObject,
      pipe(pickPaths, forEach(<span class="hljs-function">(<span class="hljs-params">item</span>) =></span> &#123;
        <span class="hljs-built_in">this</span>.values = assocPath(item.path, item.value, <span class="hljs-built_in">this</span>.values)
      &#125;), <span class="hljs-function">() =></span> <span class="hljs-built_in">this</span>.notify(ALL)),
    )(value)
  &#125;

  notify = <span class="hljs-function">(<span class="hljs-params">name</span>) =></span> &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> listener <span class="hljs-keyword">of</span> <span class="hljs-built_in">this</span>.listeners) listener(name)
  &#125;


  subscribe = <span class="hljs-function">(<span class="hljs-params">listener</span>) =></span> &#123;
    <span class="hljs-built_in">this</span>.listeners.push(listener)
    <span class="hljs-keyword">return</span> <span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">const</span> index = <span class="hljs-built_in">this</span>.listeners.indexOf(listener)
      <span class="hljs-keyword">if</span> (index > -<span class="hljs-number">1</span>) <span class="hljs-built_in">this</span>.listeners.splice(index, <span class="hljs-number">1</span>)
    &#125;
  &#125;


  getFormExport = <span class="hljs-function">(<span class="hljs-params">schema</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">signType</span>: FORM_SIGN,
      <span class="hljs-attr">getFieldValue</span>: <span class="hljs-built_in">this</span>.getFieldValue,
      <span class="hljs-attr">setFieldValue</span>: <span class="hljs-built_in">this</span>.setFieldValue,
      <span class="hljs-attr">setFieldsValue</span>: <span class="hljs-built_in">this</span>.setFieldsValue,
      <span class="hljs-attr">isSamePath</span>: <span class="hljs-built_in">this</span>.isSamePath,
      <span class="hljs-attr">getFieldsValue</span>: <span class="hljs-built_in">this</span>.getFieldsValue,
      <span class="hljs-attr">getInnerHooks</span>: <span class="hljs-built_in">this</span>.getInnerHooks(schema)
    &#125;
  &#125;


  isSamePath = <span class="hljs-function">(<span class="hljs-params">path1, path2</span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (type(path1) !== <span class="hljs-string">'Array'</span> || type(path2) !== <span class="hljs-string">'Array'</span>) &#123;
      <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'isSamePath函数的参数均需数组'</span>)
    &#125;
    <span class="hljs-keyword">return</span> equals(path1, path2)
  &#125;


  getInnerHooks = <span class="hljs-function"><span class="hljs-params">schema</span> =></span> <span class="hljs-function"><span class="hljs-params">sign</span> =></span> &#123;
    <span class="hljs-keyword">if</span> (sign === INNER_HOOKS_SIGN) &#123;
      <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">getFieldsValue</span>: <span class="hljs-built_in">this</span>.getFieldsValue,
        <span class="hljs-attr">getFieldValue</span>: <span class="hljs-built_in">this</span>.getFieldValue,
        <span class="hljs-attr">setFieldValue</span>: <span class="hljs-built_in">this</span>.setFieldValue,
        <span class="hljs-attr">setFieldsValue</span>: <span class="hljs-built_in">this</span>.setFieldsValue,
        <span class="hljs-attr">isSamePath</span>: <span class="hljs-built_in">this</span>.isSamePath,
        <span class="hljs-attr">subscribe</span>: <span class="hljs-built_in">this</span>.subscribe,
        <span class="hljs-attr">notify</span>: <span class="hljs-built_in">this</span>.notify,
        schema
      &#125;
    &#125;
    <span class="hljs-built_in">console</span>.warn(<span class="hljs-string">'外部禁止使用getInnerHooks方法'</span>);
    <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;
  &#125;
&#125;

<span class="hljs-keyword">const</span> useForm = <span class="hljs-function">(<span class="hljs-params">props</span>) =></span> &#123;
  checkSchema(props.schema);
  <span class="hljs-keyword">const</span> schemaRef = useRef(props.schema);
  <span class="hljs-keyword">const</span> formRef = useRef();
  <span class="hljs-keyword">if</span> (!formRef.current) &#123;
    formRef.current = <span class="hljs-keyword">new</span> FormStore(setSchemaToValues(props.schema)).getFormExport(props.schema);
  &#125;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">JSON</span>.stringify(props.schema) !== <span class="hljs-built_in">JSON</span>.stringify(schemaRef.current)) &#123;
    schemaRef.current = props.schema;
    formRef.current = <span class="hljs-keyword">new</span> FormStore(setSchemaToValues(props.schema)).getFormExport(props.schema);
  &#125;
  <span class="hljs-keyword">return</span> [formRef.current];
&#125;;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">FormItem</span>(<span class="hljs-params">props</span>) </span>&#123;
  <span class="hljs-keyword">const</span> &#123; name, children &#125; = props;

  <span class="hljs-comment">// 这个是获得store的Context，后面会有讲解</span>
  <span class="hljs-keyword">const</span> innerForm = useContext(FormContext);

  <span class="hljs-comment">// 如果我们new FormStore有</span>
  <span class="hljs-keyword">const</span> [value, setValue] = useState(name && innerForm ? innerForm.getFieldValue(name) : <span class="hljs-literal">undefined</span>);

  useEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">if</span> (!name || !innerForm) <span class="hljs-keyword">return</span>;
    <span class="hljs-keyword">return</span> innerForm.subscribe(<span class="hljs-function">(<span class="hljs-params">n</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (n === ALL || (<span class="hljs-built_in">Array</span>.isArray(n)
        && innerForm.isSamePath(n, strToArray(name)))) &#123;
        setValue(innerForm.getFieldValue(name));
      &#125;
    &#125;);
  &#125;, [name, innerForm, innerForm]);

  <span class="hljs-keyword">return</span> cloneElement(children, &#123;
    value,
    <span class="hljs-attr">onChange</span>: <span class="hljs-function">(<span class="hljs-params">e</span>) =></span> &#123;
      innerForm.setFieldValue(name, e.target.value);
    &#125;
  &#125;);
&#125;

<span class="hljs-keyword">const</span> WigetsMap = &#123;
  <span class="hljs-attr">input</span>: Input
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Form</span>(<span class="hljs-params">props</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (props.form.signType !== FORM_SIGN) <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'form类型错误'</span>);

  <span class="hljs-keyword">const</span> &#123; form, ...restProps &#125; = props;
  <span class="hljs-keyword">const</span> innerForm = form.getInnerHooks(INNER_HOOKS_SIGN);
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">form</span>
      &#123;<span class="hljs-attr">...restProps</span>&#125;
      <span class="hljs-attr">onSubmit</span>=<span class="hljs-string">&#123;(event)</span> =></span> &#123;
        event.preventDefault();
        event.stopPropagation();


      &#125;&#125;
    >
      <span class="hljs-tag"><<span class="hljs-name">FormContext.Provider</span> <span class="hljs-attr">value</span>=<span class="hljs-string">&#123;innerForm&#125;</span>></span>
        &#123;innerForm.schema.formItems.map((item, index) => &#123;
          return (
            <span class="hljs-tag"><<span class="hljs-name">FormItem</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;index&#125;</span>
              <span class="hljs-attr">name</span>=<span class="hljs-string">&#123;item.name&#125;</span>
              &#123;<span class="hljs-attr">...item.options</span>&#125;
            ></span>
              &#123;WigetsMap[item.Wiget] ? <span class="hljs-tag"><<span class="hljs-name">item.Wiget</span> &#123;<span class="hljs-attr">...item.WigetOptions</span>&#125; /></span> : null&#125;
            <span class="hljs-tag"></<span class="hljs-name">FormItem</span>></span>
          );
        &#125;)&#125;
      <span class="hljs-tag"></<span class="hljs-name">FormContext.Provider</span>></span>
    </form >
  );
&#125;

const schema = &#123;
  formItems: [
    &#123;
      name: 'account',
      value: 1,
      options: &#123;
      &#125;,
      Wiget: 'input'
    &#125;
  ]
&#125;

const Demo = () => &#123;
  const [form] = useForm(&#123; schema &#125;);
  window.f = form;
  return <span class="hljs-tag"><<span class="hljs-name">Form</span> <span class="hljs-attr">form</span>=<span class="hljs-string">&#123;form&#125;</span> /></span>;
&#125;;

ReactDOM.render(
  <span class="hljs-tag"><<span class="hljs-name">Demo</span> /></span>,
  document.getElementById('app')
);

</span><span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            