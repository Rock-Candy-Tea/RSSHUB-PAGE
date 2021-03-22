
---
title: """""""""""'小试牛刀的 Vue3 多选框'"""""""""""
categories: 
    - 编程
    - 掘金 - 分类
author: 掘金 - 分类
comments: false
date: Sun, 21 Mar 2021 19:14:11 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d6061506d4941f6bc5699fdaf64be9a~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>源码：<a href="https://github.com/one-pupil/vue-components" target="_blank" rel="nofollow noopener noreferrer">地址</a></p>
</blockquote>
<p>由于自己最近一直在使用 <code>Vue3</code>，本着学了不用就作废的原则就自己尝试着写了 UI 组件示例。而刚开始选择的就是<a href="https://github.com/one-pupil/vue-components/blob/main/src/libs/ainui/components/Checkbox/index.vue" target="_blank" rel="nofollow noopener noreferrer">多选框</a>这个组件。
多选框 <code>Checkbox</code> 组件是平时使用频率蛮高的一个组件，我们现在一步步来完善自己的组件。</p>
<h2 data-id="heading-0">开始</h2>
<p>先定义组件</p>
<pre><code class="hljs language-vue copyable" lang="vue"> <ani-checkbox>选项</ani-checkbox>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>创建组件 <code>Checkbox.vue</code> 文件</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <label
    class="checkbox-wrap"
  >
    <input
      type="checkbox"
      v-model="model"
    />
    <i class="check-icon">✓</i>
    <slot></slot>
  </label>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对 <code>Checkbox</code> 进行美化，主要先隐藏 <code>input[type=checkbox]</code> 再对 <code>input[type=checkbox]:checked</code> 选择器进行处理</p>
<pre><code class="hljs language-less copyable" lang="less"><<span class="hljs-selector-tag">style</span> <span class="hljs-selector-tag">lang</span>="<span class="hljs-selector-tag">less</span>" <span class="hljs-selector-tag">scoped</span>>
@<span class="hljs-selector-tag">color</span>: <span class="hljs-selector-id">#333</span>;
@<span class="hljs-selector-tag">activeColor</span>: <span class="hljs-selector-id">#409eff</span>;
<span class="hljs-selector-class">.checkbox-wrap</span> &#123;
  <span class="hljs-attribute">margin-right</span>: <span class="hljs-number">15px</span>;
  <span class="hljs-attribute">font-size</span>: <span class="hljs-number">14px</span>;
  user-select: <span class="hljs-attribute">none;
  cursor</span>: pointer;
  <span class="hljs-attribute">transition</span>: all <span class="hljs-number">0.3s</span> cubic-bezier(<span class="hljs-number">0.645</span>, <span class="hljs-number">0.045</span>, <span class="hljs-number">0.355</span>, <span class="hljs-number">1</span>);
  <span class="hljs-selector-class">.check-icon</span> &#123;
    <span class="hljs-attribute">margin-right</span>: <span class="hljs-number">5px</span>;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">14px</span>;
    <span class="hljs-attribute">font-style</span>: normal;
    <span class="hljs-attribute">display</span>: inline-block;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">14px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">14px</span>;
    <span class="hljs-attribute">text-align</span>: center;
    <span class="hljs-attribute">line-height</span>: <span class="hljs-number">14px</span>;
    <span class="hljs-attribute">color</span>: <span class="hljs-number">#fff</span>;
    <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid <span class="hljs-variable">@color</span>;
    <span class="hljs-attribute">transition</span>: all <span class="hljs-number">0.3s</span> cubic-bezier(<span class="hljs-number">0.645</span>, <span class="hljs-number">0.045</span>, <span class="hljs-number">0.355</span>, <span class="hljs-number">1</span>);
  &#125;
  <span class="hljs-selector-tag">input</span><span class="hljs-selector-attr">[type=<span class="hljs-string">'checkbox'</span>]</span> &#123;
    <span class="hljs-attribute">display</span>: none;
  &#125;
  <span class="hljs-selector-tag">input</span><span class="hljs-selector-attr">[type=<span class="hljs-string">'checkbox'</span>]</span><span class="hljs-selector-pseudo">:checked</span> + <span class="hljs-selector-class">.check-icon</span> &#123;
    <span class="hljs-attribute">background-color</span>: <span class="hljs-variable">@activeColor</span>;
    <span class="hljs-attribute">border-color</span>: <span class="hljs-variable">@activeColor</span>;
  &#125;
  <span class="hljs-selector-tag">&</span><span class="hljs-selector-class">.is-checked-text</span> &#123;
    <span class="hljs-attribute">color</span>: <span class="hljs-variable">@activeColor</span>;
  &#125;
&#125;
</<span class="hljs-selector-tag">style</span>>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下
<img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d6061506d4941f6bc5699fdaf64be9a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">逻辑处理</h2>
<p>先定义 <code>props</code></p>
<pre><code class="hljs language-vue copyable" lang="vue"><ani-checkbox v-model="checked" @change="onChange">选项</ani-checkbox>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们知道 <code>Vue3</code> 对于 <code>v-model</code> 的处理和以前稍稍有点不同。
<img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d57864247514ba8a546e3f86bd0788f~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
由文档所述，其中的 <code>prop</code> 的 <code>value</code> 变成了 <code>modelValue</code>，所以我们组件内定义的 <code>props</code> 需要改变</p>
<pre><code class="hljs language-vue copyable" lang="vue">props: &#123;
  modelValue: &#123;
    type: [Boolean, Number, String],
    default: () => undefined
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们利用 <code>computed</code> 实现双向绑定</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">props, &#123; emit &#125;</span>)</span> &#123;
    <span class="hljs-keyword">const</span> model = computed(&#123;
      <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> props.modelValue;
      &#125;,
      <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">val</span>)</span> &#123;
        emit(<span class="hljs-string">"update:modelValue"</span>, val);
      &#125;,
    &#125;);

    <span class="hljs-keyword">return</span> &#123;
      model
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再添加事件回调</p>
<pre><code class="hljs language-vue copyable" lang="vue"><input type="checkbox" v-model="model" @change="onChange"/>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里需要注意，<code>emit</code> 事件时需要在 <code>emits</code> 中注册</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  emits: [<span class="hljs-string">'change'</span>],
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">props, &#123; emit &#125;</span>)</span> &#123;
...
    <span class="hljs-keyword">const</span> onChange = <span class="hljs-function">() =></span> &#123;
      emit(<span class="hljs-string">'change'</span>, model.value);
    &#125;

    <span class="hljs-keyword">return</span> &#123;
      onChange
    &#125;
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由此，一个简单的 <code>checkbox</code> 组件就完成了。不过我们现在使用的 <code>composition-api</code> 形式，我们可以封装一下整个逻辑 <code>useCheckbox</code> 函数</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; getCurrentInstance &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>;
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useCheckbox</span>(<span class="hljs-params">props</span>) </span>&#123;
  <span class="hljs-keyword">const</span> &#123; proxy &#125; = getCurrentInstance()
  <span class="hljs-keyword">const</span> model = computed(&#123;
    <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> props.modelValue;
    &#125;,
    <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">val</span>)</span> &#123;
      proxy.emit(<span class="hljs-string">"update:modelValue"</span>, val);
    &#125;,
  &#125;);

  <span class="hljs-keyword">const</span> onChange = <span class="hljs-function">() =></span> &#123;
    proxy.emit(<span class="hljs-string">'change'</span>, model.value);
  &#125;

  <span class="hljs-keyword">return</span> &#123;
    model,
    onChange
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再在组件中引入</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; useCheckbox &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./useCheckbox'</span>;

<span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">props</span>)</span> &#123;
  <span class="hljs-keyword">return</span> useCheckbox(props);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">多选框组</h2>
<p>我们使用了很多 UI 库组件，<code>checkbox</code> 存在多选，大多数组件库也有这个多选组，我们接下来封装一个多选框组。
新建一个 <code>checkbox-group.vue</code> 文件</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div class="ani-checkbox-group">
    <slot></slot>
  </div>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而实际使用时，我们利用 <code>checkbox-group</code> 包裹 <code>checkbox</code> 组件</p>
<pre><code class="hljs language-vue copyable" lang="vue"><ani-checkbox-group v-model="checkList">
  <ani-checkbox>选项一</ani-checkbox>
  <ani-checkbox>选项二</ani-checkbox>
  <ani-checkbox>选项三</ani-checkbox>
</ani-checkbox-group>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>模板文件我们已经写完了，接下来我们来完善逻辑；这里利用 <code>provide/inject</code> 来传递父组件参数</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'AniCheckboxGroup'</span>,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">modelValue</span>: &#123;
      <span class="hljs-attr">type</span>: [<span class="hljs-built_in">Array</span>],
      <span class="hljs-attr">default</span>: <span class="hljs-function">() =></span> <span class="hljs-literal">undefined</span>
    &#125;
  &#125;,
  <span class="hljs-attr">emits</span>: [<span class="hljs-string">'change'</span>],
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">props, ctx</span>)</span> &#123;
    <span class="hljs-comment">// 定义事件</span>
    <span class="hljs-keyword">const</span> changeEvent = <span class="hljs-function"><span class="hljs-params">value</span> =></span> &#123;
      ctx.emit(<span class="hljs-string">'update:modelValue'</span>, value);
      nextTick(<span class="hljs-function">() =></span> &#123;
        ctx.emit(<span class="hljs-string">'change, value);
      &#125;);
    &#125;;

    const modelValue = computed(&#123;
      get() &#123;
        return props.modelValue;
      &#125;,
      set(val) &#123;
        changeEvent(val);
      &#125;
    &#125;);

    // 向子组件传递
    provide('</span>CheckboxGroup<span class="hljs-string">', &#123;
      name: '</span>CheckboxGroup<span class="hljs-string">',
      modelValue,
      ...toRefs(props),
      changeEvent
    &#125;);
  &#125;
&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>子组件中 <code>inject</code> 接收</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 接收父组件消息</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> useCheckboxGroup = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-comment">// 这里的名称对应 provide 名称</span>
  <span class="hljs-keyword">const</span> checkboxGroup = inject(<span class="hljs-string">'CheckboxGroup'</span>, &#123;&#125;);
  <span class="hljs-comment">// 判断是否为多选框组</span>
  <span class="hljs-keyword">const</span> isGroup = computed(
    <span class="hljs-function">() =></span> checkboxGroup && checkboxGroup.name === <span class="hljs-string">'CheckboxGroup'</span>
  );

  <span class="hljs-keyword">return</span> &#123;
    isGroup,
    checkboxGroup
  &#125;;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>useCheckbox</code> 中需要判断是否为多选框组，具体思路看注释吧🤣，其实逻辑也简单~</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> useCheckbox = <span class="hljs-function"><span class="hljs-params">props</span> =></span> &#123;
  <span class="hljs-keyword">const</span> &#123; emit &#125; = getCurrentInstance();

  <span class="hljs-keyword">const</span> &#123; isGroup, checkboxGroup &#125; = useCheckboxGroup();

  <span class="hljs-comment">// 存在多选组，则使用多选组 modelValue</span>
  <span class="hljs-keyword">const</span> store = computed(<span class="hljs-function">() =></span>
    checkboxGroup ? checkboxGroup.modelValue.value : props.modelValue
  );

  <span class="hljs-comment">// 还是判断多选组</span>
  <span class="hljs-keyword">const</span> model = computed(&#123;
    <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> isGroup.value ? store.value : props.modelValue;
    &#125;,
    <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">val</span>)</span> &#123;
      <span class="hljs-keyword">if</span> (isGroup.value && <span class="hljs-built_in">Array</span>.isArray(val)) &#123;
        checkboxGroup.changeEvent(val);
      &#125; <span class="hljs-keyword">else</span> &#123;
        emit(<span class="hljs-string">'update:modelValue'</span>, val);
      &#125;
    &#125;
  &#125;);

  <span class="hljs-comment">// 判断多选框是否选中</span>
  <span class="hljs-keyword">const</span> isChecked = computed(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> value = model.value;
    <span class="hljs-keyword">if</span> (isPropType(value, <span class="hljs-string">'boolean'</span>)) &#123;
      <span class="hljs-keyword">return</span> value;
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (isPropType(value, <span class="hljs-string">'array'</span>)) &#123;
      <span class="hljs-keyword">return</span> value.includes(props.label);
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;
  &#125;);

  <span class="hljs-keyword">const</span> onChange = <span class="hljs-function"><span class="hljs-params">e</span> =></span> &#123;
    <span class="hljs-keyword">const</span> target = e.target;
    <span class="hljs-keyword">const</span> value = target.checked ? <span class="hljs-literal">true</span> : <span class="hljs-literal">false</span>;
    emit(<span class="hljs-string">'change'</span>, value, e);
  &#125;;

  <span class="hljs-keyword">return</span> &#123;
    model,
    isChecked,
    onChange
  &#125;;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里模板需要修改，我们需要传入选中的选项字段 <code>value</code> 和多选框是否选中 <code>checked</code></p>
<pre><code class="hljs language-vue copyable" lang="vue">  <label
    class="checkbox-wrap"
  >
    <input
      type="checkbox"
      v-model="model"
      :value="label"
      :checked="isChecked"
      @change="onChange"
    />
    <i class="check-icon">✓</i>
    <slot></slot>
  </label>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实现效果
<img alt="12.gif" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e88ba55ec85d4eb3b9cd2fc33adc80e7~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">总结</h2>
<p>还是要自己动手封装，组件内的一些细节和思路对于业务逻辑还是有一定的启发作用。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            