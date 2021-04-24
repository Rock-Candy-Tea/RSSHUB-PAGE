
---
title: 'Element-ui checkbox'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/376c5626344d4f56bcef269d38a7f81e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 23 Apr 2021 20:09:27 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/376c5626344d4f56bcef269d38a7f81e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><a href="https://element.eleme.io/#/zh-CN/component/checkbox" target="_blank" rel="nofollow noopener noreferrer">Element-ui checkbox</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/376c5626344d4f56bcef269d38a7f81e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <!-- <span class="hljs-string">`checked`</span> 为 <span class="hljs-literal">true</span> 或 <span class="hljs-literal">false</span> -->
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">el-checkbox</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"checked"</span>></span>备选项<span class="hljs-tag"></<span class="hljs-name">el-checkbox</span>></span></span>
</template>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">checked</span>: <span class="hljs-literal">true</span>
      &#125;;
    &#125;
  &#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-0">剖析</h3>
<ul>
<li>checkbox 有三种状态：选中，取消选中，半选</li>
<li>checkbox 有三种使用情况：</li>
<li>单独使用, v-model绑定的值为布尔类型</li>
<li>单独使用，v-model绑定的值为数组类型，且需与label搭配</li>
<li>与checkbox-group搭配使用，且需与label搭配（checkbox-group见下回）</li>
</ul>
<h4 data-id="heading-1">测试代码</h4>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>checkbox<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-comment"><!-- 第一种情况 --></span>
    <span class="hljs-tag"><<span class="hljs-name">y-checkbox</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"checkboxValue"</span> @<span class="hljs-attr">change</span>=<span class="hljs-string">"handleChange"</span>></span>杭州<span class="hljs-tag"></<span class="hljs-name">y-checkbox</span>></span>
    <span class="hljs-comment"><!-- 第二种情况 --></span>
    <span class="hljs-tag"><<span class="hljs-name">y-checkbox</span> <span class="hljs-attr">v-model</span>=<span class="hljs-string">"checkboxArr"</span> <span class="hljs-attr">label</span>=<span class="hljs-string">"1"</span> @<span class="hljs-attr">change</span>=<span class="hljs-string">"handleChange"</span>></span>杭州<span class="hljs-tag"></<span class="hljs-name">y-checkbox</span>></span>
    <span class="hljs-comment"><!-- 半选中状态 --></span>
    <span class="hljs-tag"><<span class="hljs-name">y-checkbox</span> 
      <span class="hljs-attr">:indeterminate</span>=<span class="hljs-string">"checkboxIndeterminate"</span> 
      <span class="hljs-attr">v-model</span>=<span class="hljs-string">"checkboxIndeterminateValue"</span>
      @<span class="hljs-attr">change</span>=<span class="hljs-string">"handleIndeterminate"</span>></span>半选中状态<span class="hljs-tag"></<span class="hljs-name">y-checkbox</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">checkboxValue</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">checkboxArr</span>: [
        <span class="hljs-string">'1'</span>,
        <span class="hljs-string">'2'</span>,
        <span class="hljs-string">'3'</span>,
      ],
      <span class="hljs-attr">checkboxIndeterminate</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">checkboxIndeterminateValue</span>: <span class="hljs-literal">false</span>,
    &#125;
  &#125;,
  <span class="hljs-attr">watch</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">checkboxValue</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'父组件checkboxValue'</span>, <span class="hljs-built_in">this</span>.checkboxValue)
    &#125;
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">handleChange</span>(<span class="hljs-params">data</span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'父组件change事件'</span>, data);
    &#125;,
    <span class="hljs-function"><span class="hljs-title">handleIndeterminate</span>(<span class="hljs-params">data</span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'半选'</span>, data);
      <span class="hljs-comment">// 将半选控制标识更改为false, 便可以正常选中和取消选中了</span>
      <span class="hljs-built_in">this</span>.checkboxIndeterminate = <span class="hljs-literal">false</span>;
    &#125;
  &#125;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>注意：单独使用checkbox时，且设置了半选中<code>:indeterminate="checkboxIndeterminate" </code>，则需要绑定change事件以更改该checkboxIndeterminate为false，从而正常选中和取消选中</li>
</ul>
<h4 data-id="heading-2">组件checkbox</h4>
<h5 data-id="heading-3">template</h5>
<pre><code class="hljs language-js copyable" lang="js"><template>
    <!-- checkbox选中状态: 选中, 不选中, 半选
        单独使用checkbox，如何判断选中状态呢?
        prop接收的value值类型需为布尔类型: <span class="hljs-literal">true</span>选中, <span class="hljs-literal">false</span>不选中
        半选中状态如何处理?
        半选中状态下，如果再次点击，将indeterminate置为<span class="hljs-literal">false</span>, 便可以选中和取消选中了
        但是只能在父组件中控制indeterminate的值（因为子组件不能更改父组件prop传进来的值） -->
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">label</span>
        <span class="hljs-attr">class</span>=<span class="hljs-string">"y-checkbox"</span>
        <span class="hljs-attr">role</span>=<span class="hljs-string">"checkbox"</span>></span>
        <span class="hljs-comment"><!-- checkbox分两部分, 一部分是多选框，一部分是标签 --></span>
        <span class="hljs-tag"><<span class="hljs-name">span</span> 
            <span class="hljs-attr">class</span>=<span class="hljs-string">"y-checkbox__input"</span>
            <span class="hljs-attr">:class</span>=<span class="hljs-string">"&#123;
                'is-checked': isChecked,
                'is-indeterminate': indeterminate,
            &#125;"</span>
            ></span>
            <span class="hljs-comment"><!-- y-checkbox__inner 替换了原生多选框的样式，原生多选框只有两种状态，通过自定义的样式可定义第三种半选状态--></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"y-checkbox__inner"</span>></span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-comment"><!-- 原生多选框, 如果value和labl都没有传, 则选中状态变化后, model值为true或false 
                定义ref以便获取该dom元素从而通知该原生多选框的选中状态
                自定义属性 aria-hidden 可直观明白该html是否展示
            --></span>
            <span class="hljs-tag"><<span class="hljs-name">input</span>
                <span class="hljs-attr">ref</span>=<span class="hljs-string">"checkbox"</span>
                <span class="hljs-attr">class</span>=<span class="hljs-string">"y-checkbox__original"</span>
                <span class="hljs-attr">type</span>=<span class="hljs-string">"checkbox"</span>
                <span class="hljs-attr">:value</span>=<span class="hljs-string">"label"</span>
                <span class="hljs-attr">aria-hidden</span>=<span class="hljs-string">"false"</span>
                <span class="hljs-attr">v-model</span>=<span class="hljs-string">"model"</span>
                @<span class="hljs-attr">change</span>=<span class="hljs-string">"handleChange"</span>/></span>    
        <span class="hljs-tag"></<span class="hljs-name">span</span>></span>
        <span class="hljs-comment"><!-- 标签, 如果子元素存在则展示子元素, 否则标签为label --></span>
        <span class="hljs-tag"><<span class="hljs-name">span</span> 
            <span class="hljs-attr">class</span>=<span class="hljs-string">"y-checkbox__label"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">slot</span>></span><span class="hljs-tag"></<span class="hljs-name">slot</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">templat</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"!$slots.default"</span>></span>&#123;&#123;label&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">templat</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">span</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">label</span>></span></span>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">scripts</h4>
<p>checkbox 选中状态判定</p>
<pre><code class="hljs language-js copyable" lang="js"><script>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'YCheckbox'</span>,
    <span class="hljs-attr">props</span>: &#123;
        <span class="hljs-attr">value</span>: &#123;&#125;,
        <span class="hljs-comment">// label选中状态的值, 只有在checkbox-group或者value为数组类型的时候方可有效</span>
        <span class="hljs-attr">label</span>: &#123;&#125;,
        <span class="hljs-comment">// 半选中状态</span>
        <span class="hljs-attr">indeterminate</span>: <span class="hljs-built_in">Boolean</span>,
    &#125;,
    <span class="hljs-attr">computed</span>: &#123;
        <span class="hljs-comment">// 原生多选框值的选中状态</span>
        <span class="hljs-attr">model</span>: &#123;
            <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params"></span>)</span> &#123;
                <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.value;
            &#125;,
            <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">val</span>)</span> &#123;
                <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'model发生了变化'</span>, val);
                <span class="hljs-comment">/**
                 * 通知父组件value值发生了变化
                 * v-model双向绑定, 手动通知父组件吗？这是因为并非是value值发生了变化，
                 * 而是另一个依赖变量model发生了变化, model发生变化后value也要变, 所以需要手动触发
                 */</span>
                <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">'input'</span>, val);
            &#125;
        &#125;,
        <span class="hljs-comment">/**
         * 选中状态的判定
         * 如何判定选中状态？
         * 这里分三种情况，一种是单个使用(value为布尔类型, label为undefined)
         * 一种情况是单个使用(value为数组类型, label为数组中的某一项)
         * 一种情况是父组件为checkbox-group(value为undefined, label有值)
         */</span>
        <span class="hljs-function"><span class="hljs-title">isChecked</span>(<span class="hljs-params"></span>)</span> &#123;
            <span class="hljs-comment">// this.model.toString(), &#123;&#125;.toString.call(this.model)有什么区别？</span>
            <span class="hljs-comment">// 若this.model=true, 则 this.model.toString()->true, &#123;&#125;.toString.call(this.model)->[object Boolean]</span>
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'第一种情况'</span>, &#123;&#125;.toString.call(<span class="hljs-built_in">this</span>.model), &#123;&#125;.toString.call(<span class="hljs-built_in">this</span>.model) === <span class="hljs-string">'[object Boolean]'</span>)
            
            <span class="hljs-comment">// 如果是第一种情况, 单独使用多选框且value值为布尔类型</span>
            <span class="hljs-keyword">if</span>(&#123;&#125;.toString.call(<span class="hljs-built_in">this</span>.model) === <span class="hljs-string">'[object Boolean]'</span>) &#123;
                <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.model;
            &#125;
            <span class="hljs-comment">// 如果是第二种情况，单独使用且value为数组类型</span>
            <span class="hljs-comment">// 数组的判定类型有几种？</span>
            <span class="hljs-comment">// console.log('第二种情况', this.model, Array.isArray(this.model), this.model.indexOf(this.label), this.model.includes(this.label));</span>
            <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(<span class="hljs-built_in">Array</span>.isArray(<span class="hljs-built_in">this</span>.model)) &#123;
                <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.model, <span class="hljs-built_in">this</span>.label);
                <span class="hljs-comment">// 判断值是否存在于数组中</span>
                <span class="hljs-comment">// indexOf和includes的区别</span>
                <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.model.indexOf(<span class="hljs-built_in">this</span>.label) > -<span class="hljs-number">1</span>;
            &#125;
            <span class="hljs-comment">// 第三种情况，父组件是checkbox-group</span>
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'第三种情况，父组件是checkbox-group'</span>);
        &#125;
    &#125;,
    <span class="hljs-attr">methods</span>: &#123;
        <span class="hljs-comment">/**
         * 父组件可能有change事件，即选中状态变化后的回调
         * 因为这是由原生多选框选中状态变化后的回调，需要等视图更新后方可获取到新值，并将新值传给回调函数
         */</span>
        <span class="hljs-function"><span class="hljs-title">handleChange</span>(<span class="hljs-params"></span>)</span> &#123;
            <span class="hljs-comment">// console.log('原生checkbox发生了变化', this.model);</span>
            <span class="hljs-built_in">this</span>.$nextTick(<span class="hljs-function">()=></span>&#123;
                <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">'change'</span>, <span class="hljs-built_in">this</span>.model);
            &#125;)
        &#125;,
    &#125;,
    <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'checkbox'</span>, <span class="hljs-built_in">this</span>.value, <span class="hljs-built_in">this</span>.label);
        <span class="hljs-comment">// console.log(this.model.toString(), &#123;&#125;.toString.call(this.model), &#123;&#125;.toString.call(this.model) === '[object Boolean]')</span>
    &#125;,
    <span class="hljs-attr">watch</span>: &#123;
        <span class="hljs-function"><span class="hljs-title">isChecked</span>(<span class="hljs-params"></span>)</span> &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'watchisChecked'</span>, <span class="hljs-built_in">this</span>.isChecked)
        &#125;
    &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>this.model.toString()</code> 与<code>&#123;&#125;.toString.call(this.model)</code>的区别</li>
<li><code>indexOf</code> 与 <code>includes</code> 的区别</li>
</ul>
<h4 data-id="heading-5">style</h4>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.y-checkbox</span> &#123;
    <span class="hljs-attribute">position</span>: relative;
    <span class="hljs-attribute">margin-right</span>: <span class="hljs-number">30px</span>;
&#125;
<span class="hljs-selector-class">.y-checkbox</span><span class="hljs-selector-pseudo">:last-child</span> &#123;
    <span class="hljs-attribute">margin-right</span>: <span class="hljs-number">0</span>;
&#125;
<span class="hljs-selector-class">.y-checkbox__input</span> &#123;
    <span class="hljs-attribute">position</span>: relative;
&#125;
<span class="hljs-selector-class">.y-checkbox__inner</span> &#123;
    <span class="hljs-attribute">display</span>: inline-block;
    <span class="hljs-attribute">position</span>: relative;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">14px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">14px</span>;
    <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#dcdfe6</span>;
    <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">2px</span>;
    <span class="hljs-attribute">box-sizing</span>: border-box;
    <span class="hljs-attribute">vertical-align</span>: middle;
&#125;
<span class="hljs-selector-class">.y-checkbox__inner</span><span class="hljs-selector-pseudo">::after</span> &#123;
    <span class="hljs-attribute">content</span>: <span class="hljs-string">''</span>;
    <span class="hljs-attribute">display</span>: content-box;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">3px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">7px</span>;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">top</span>: <span class="hljs-number">2px</span>;
    <span class="hljs-attribute">left</span>: <span class="hljs-number">4px</span>;
    <span class="hljs-attribute">box-sizing</span>: border-box;
    <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#fff</span>;
    <span class="hljs-attribute">border-top</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">border-left</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">0deg</span>) <span class="hljs-built_in">scale</span>(<span class="hljs-number">0</span>);
&#125;
<span class="hljs-comment">/* 选中样式 */</span>
<span class="hljs-selector-class">.y-checkbox__input</span><span class="hljs-selector-class">.is-checked</span> <span class="hljs-selector-class">.y-checkbox__inner</span> &#123;
    <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#409eff</span>;
    <span class="hljs-attribute">border-color</span>: <span class="hljs-number">#409eff</span>;
&#125;
<span class="hljs-comment">/* 选中后中间的对号,通过旋转45度得到 */</span>
<span class="hljs-selector-class">.y-checkbox__input</span><span class="hljs-selector-class">.is-checked</span> <span class="hljs-selector-class">.y-checkbox__inner</span><span class="hljs-selector-pseudo">::after</span> &#123;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">45deg</span>) <span class="hljs-built_in">scale</span>(<span class="hljs-number">1</span>);
&#125;
<span class="hljs-comment">/* 半选中状态 */</span>
<span class="hljs-selector-class">.y-checkbox__input</span><span class="hljs-selector-class">.is-indeterminate</span> <span class="hljs-selector-class">.y-checkbox__inner</span> &#123;
    <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#409eff</span>;
    <span class="hljs-attribute">border-color</span>: <span class="hljs-number">#409eff</span>;
&#125;
<span class="hljs-comment">/* 半选中状态 中间的横杠 */</span>
<span class="hljs-selector-class">.y-checkbox__input</span><span class="hljs-selector-class">.is-indeterminate</span> <span class="hljs-selector-class">.y-checkbox__inner</span><span class="hljs-selector-pseudo">::after</span> &#123;
    <span class="hljs-attribute">content</span>: none;
&#125;
<span class="hljs-selector-class">.y-checkbox__input</span><span class="hljs-selector-class">.is-indeterminate</span> <span class="hljs-selector-class">.y-checkbox__inner</span><span class="hljs-selector-pseudo">::before</span> &#123;
    <span class="hljs-attribute">content</span>: <span class="hljs-string">''</span>;
    <span class="hljs-attribute">display</span>: inline-block;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">2px</span>;
    <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#fff</span>;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">top</span>: <span class="hljs-number">5px</span>;
    <span class="hljs-attribute">right</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">scale</span>(.<span class="hljs-number">5</span>);
&#125;
<span class="hljs-comment">/* 隐藏原生多选框 */</span>
<span class="hljs-selector-class">.y-checkbox__original</span> &#123;
    <span class="hljs-attribute">opacity</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">outline</span>: none;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">right</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">bottom</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">z-index</span>: -<span class="hljs-number">1</span>;
    <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
&#125;
<span class="hljs-selector-class">.y-checkbox__label</span> &#123;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">14px</span>;
    <span class="hljs-attribute">display</span>: inline-block;
    <span class="hljs-attribute">padding-left</span>: <span class="hljs-number">10px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">总结</h3>
<ul>
<li>该 checkbox 测试，实现v-model、lable属性和change事件</li>
<li>checkbox 逻辑跟 radio 有很多相似之处，相似的html结构、判定逻辑</li>
<li>checkbox 三种选中状态（注意半选中状态切换到选中状态和取消选中状态）以及其两种使用形式</li>
<li>indexOf 与 includes 的区别</li>
<li>&#123;&#125;.toString.call(obj) 与 obj.toString() 的区别</li>
<li>checkbox 选中状态下中间的对号的生成（伪元素创建，旋转）</li>
</ul></div>  
</div>
            