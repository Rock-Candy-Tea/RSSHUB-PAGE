
---
title: 'Element-ui Tree'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8182'
author: 掘金
comments: false
date: Thu, 13 May 2021 02:29:45 GMT
thumbnail: 'https://picsum.photos/400/300?random=8182'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><a href="https://element.eleme.io/#/zh-CN/component/tree" target="_blank" rel="nofollow noopener noreferrer">Element-ui Tree</a></p>
<p>用清晰的层级结构展示信息，可展开或折叠。</p>
<h3 data-id="heading-0">Tree Attributes</h3>








































<table><thead><tr><th>参数</th><th>说明</th><th>类型</th><th>可选值</th><th>默认值</th></tr></thead><tbody><tr><td>data</td><td>展示的数据</td><td>Array</td><td>—</td><td>—</td></tr><tr><td>node-key</td><td>每个树节点用来作为唯一标识的属性，整棵树应该是唯一的</td><td>String</td><td>—</td><td>—</td></tr><tr><td>show-checkbox</td><td>节点是否可被选择</td><td>boolean</td><td>—</td><td>false</td></tr><tr><td>default-expand-all</td><td>是否默认展开所有节点</td><td>boolean</td><td>—</td><td>fasle</td></tr></tbody></table>
<h3 data-id="heading-1">基础的树形结构展示</h3>
<pre><code class="hljs language-js copyable" lang="js"><template>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">el-tree</span> 
        <span class="hljs-attr">:data</span>=<span class="hljs-string">"data"</span> 
        <span class="hljs-attr">:props</span>=<span class="hljs-string">"defaultProps"</span> ></span>
    <span class="hljs-tag"></<span class="hljs-name">el-tree</span>></span></span>
</template>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">data</span>: [&#123;
          <span class="hljs-attr">label</span>: <span class="hljs-string">'一级 1'</span>,
          <span class="hljs-attr">children</span>: [&#123;
            <span class="hljs-attr">label</span>: <span class="hljs-string">'二级 1-1'</span>,
            <span class="hljs-attr">children</span>: [&#123;
              <span class="hljs-attr">label</span>: <span class="hljs-string">'三级 1-1-1'</span>
            &#125;]
          &#125;]
        &#125;, &#123;
          <span class="hljs-attr">label</span>: <span class="hljs-string">'一级 2'</span>,
        &#125;],
        <span class="hljs-attr">defaultProps</span>: &#123;
          <span class="hljs-attr">children</span>: <span class="hljs-string">'children'</span>,
          <span class="hljs-attr">label</span>: <span class="hljs-string">'label'</span>
        &#125;
      &#125;;
    &#125;,
  &#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">Tree 结构</h3>
<h4 data-id="heading-3">实现思路</h4>
<ul>
<li>tree.vue 渲染树</li>
<li>tree-node.vue 渲染子树</li>
<li>tree-store.js 树的状态管理器</li>
<li>node.js 定义树节点的树形和方法</li>
</ul>
<h4 data-id="heading-4">tree.vue</h4>
<p>tree.vue 为树组件的入口</p>
<ul>
<li>接收 props 传递的数据 data</li>
<li>根据 data 生成树节点 root</li>
<li>根据 root 渲染树</li>
</ul>
<h5 data-id="heading-5">接收 props 传递的数据 data</h5>
<pre><code class="hljs language-js copyable" lang="js">props: &#123;
    <span class="hljs-comment">// 树要展示的数据</span>
    <span class="hljs-attr">data</span>: &#123;
        <span class="hljs-attr">type</span>: <span class="hljs-built_in">Array</span>,
    &#125;,
    <span class="hljs-comment">// 树节点的key</span>
    <span class="hljs-attr">nodeKey</span>: <span class="hljs-built_in">String</span>,
    <span class="hljs-comment">// 配置项</span>
    <span class="hljs-attr">props</span>: &#123;
        <span class="hljs-attr">type</span>: <span class="hljs-built_in">Object</span>,
        <span class="hljs-attr">default</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-keyword">return</span> &#123;
                <span class="hljs-comment">// 指定子树为节点某个对象的值即"children"对应值表示子节点的数据</span>
                <span class="hljs-attr">children</span>: <span class="hljs-string">'children'</span>,
                <span class="hljs-comment">// 指定节点标签为节点对象的某个属性的值</span>
                <span class="hljs-attr">label</span>: <span class="hljs-string">'label'</span>,
            &#125;
        &#125;
    &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-6">根据 data 生成树节点 root</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// 给子树判断父组件是否为树</span>
    <span class="hljs-built_in">this</span>.isTree = <span class="hljs-literal">true</span>;

    <span class="hljs-comment">// 创建树的store</span>
    <span class="hljs-built_in">this</span>.store = <span class="hljs-keyword">new</span> TreeStore(&#123;
        <span class="hljs-attr">key</span>: <span class="hljs-built_in">this</span>.nodeKey,
        <span class="hljs-attr">data</span>: <span class="hljs-built_in">this</span>.data,
        <span class="hljs-attr">props</span>: <span class="hljs-built_in">this</span>.props,
    &#125;);

    <span class="hljs-comment">// 从树根开始</span>
    <span class="hljs-built_in">this</span>.root = <span class="hljs-built_in">this</span>.store.root;
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">根据 root 渲染树</h4>
<pre><code class="hljs language-js copyable" lang="js"><template>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>
        <span class="hljs-attr">class</span>=<span class="hljs-string">"y-tree"</span>></span>
        <span class="hljs-comment"><!-- 子树如何渲染?循环生成?多层嵌套? --></span>
        <span class="hljs-tag"><<span class="hljs-name">y-tree-node</span>
            <span class="hljs-attr">v-for</span>=<span class="hljs-string">"(child) in root.childNodes"</span>
            <span class="hljs-attr">:node</span>=<span class="hljs-string">"child"</span>
            <span class="hljs-attr">:show-checkbox</span>=<span class="hljs-string">"showCheckbox"</span>
            <span class="hljs-attr">:key</span>=<span class="hljs-string">"getNodeKey(child)"</span>
        ></span>
        <span class="hljs-tag"></<span class="hljs-name">y-tree-node</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">tree-node.vue</h4>
<p>tree-node.vue 渲染子树</p>
<blockquote>
<p>如何渲染子树的子树...循环嵌套渲染子树？我原来的想法是循环嵌套就是顺下去,往下走；实际上，循环嵌套式一个环,往下走完还要往回走</p>
</blockquote>
<ul>
<li>渲染该节点展示的内容</li>
<li>渲染该节点的子树</li>
</ul>
<h5 data-id="heading-9">渲染子树</h5>
<pre><code class="hljs language-js copyable" lang="js"><template>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>
        <span class="hljs-attr">class</span>=<span class="hljs-string">"y-tree-node"</span>
        <span class="hljs-attr">:aria-expanded</span>=<span class="hljs-string">"expanded"</span>
        @<span class="hljs-attr">click.stop</span>=<span class="hljs-string">"handleClick"</span>
    ></span>
        <span class="hljs-comment"><!-- 1.渲染树节点
            节点内容的展示,el-tree节点主要分四部分(展开图标展示,多选框,加载中图标,节点内容展示)
            动态计算偏移量:(node.level - 1) * treeC.indent + 'px', 形成阶梯式子树效果
        --></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>
            <span class="hljs-attr">class</span>=<span class="hljs-string">"y-tree-node__content"</span>
            <span class="hljs-attr">:style</span>=<span class="hljs-string">"&#123;'padding-left': (node.level - 1) * treeC.indent + 'px'&#125;"</span>
        ></span>
            <span class="hljs-comment"><!-- 多选框 
                @click.native.stop 阻止事件冒泡
                事件修饰符-官方文档:https://cn.vuejs.org/v2/guide/events.html
            --></span>
            <span class="hljs-tag"><<span class="hljs-name">y-checkbox</span>
                <span class="hljs-attr">v-if</span>=<span class="hljs-string">"showCheckbox"</span>
                <span class="hljs-attr">v-model</span>=<span class="hljs-string">"node.checked"</span>
                @<span class="hljs-attr">click.native.stop</span>
            ></span>
            <span class="hljs-tag"></<span class="hljs-name">y-checkbox</span>></span>
            <span class="hljs-comment"><!-- 内容 --></span>
            <span class="hljs-tag"><<span class="hljs-name">node-content</span> <span class="hljs-attr">:node</span>=<span class="hljs-string">"node"</span>></span><span class="hljs-tag"></<span class="hljs-name">node-content</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-comment"><!-- 2.渲染该节点的子树
            子树如何渲染?
            组件YCollapseTransition是一个函数式组件
            官方文档:https://cn.vuejs.org/v2/guide/render-function.html
            这里为什么要用函数式组件(无状态、无实例)来包装树节点组件从而实现子树的渲染?为什么不直接使用? -- 子树的展开和收缩效果
         --></span>
         <span class="hljs-tag"><<span class="hljs-name">y-collapse-transition</span>></span>
             <span class="hljs-comment"><!-- v-if="node.expanded && node.childNodes.length"
                v-if: 动态的控制DOM元素的添加和删除
                v-show: 同css的display来控制元素的显示和隐藏
              --></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span>
                <span class="hljs-attr">v-if</span>=<span class="hljs-string">"childNodeRendered"</span>
                <span class="hljs-attr">v-show</span>=<span class="hljs-string">"expanded"</span>
                <span class="hljs-attr">class</span>=<span class="hljs-string">"y-tree-node__children"</span>
                <span class="hljs-attr">:aria-expanded</span>=<span class="hljs-string">"expanded"</span>
            ></span>
                <span class="hljs-tag"><<span class="hljs-name">y-tree-node</span>
                    <span class="hljs-attr">v-for</span>=<span class="hljs-string">"(child) in node.childNodes"</span>
                    <span class="hljs-attr">:key</span>=<span class="hljs-string">"getNodeKey(child)"</span>
                    <span class="hljs-attr">:node</span>=<span class="hljs-string">"child"</span>
                    <span class="hljs-attr">:show-checkbox</span>=<span class="hljs-string">"showCheckbox"</span>
                ></span>
                <span class="hljs-tag"></<span class="hljs-name">y-tree-node</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
         <span class="hljs-tag"></<span class="hljs-name">y-collapse-transition</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">tree-store.js</h4>
<p>tree-store 树的状态管理器，生成树节点集</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> Node <span class="hljs-keyword">from</span> <span class="hljs-string">'./node'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TreeStore</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">options</span>)</span> &#123;

        <span class="hljs-comment">// 赋值初始化:options是对象,遍历使用for...in...</span>
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> option <span class="hljs-keyword">in</span> options) &#123;
            <span class="hljs-keyword">if</span>(options.hasOwnProperty(option)) &#123;
                <span class="hljs-built_in">this</span>[option] = options[option];
            &#125;
        &#125;
        
        <span class="hljs-comment">/**
         * 实例化根节点Node
         * 根节点实例化
         * 由根节点开始生成树
         * 根节点->根节点的childNodes->...
         */</span>
        <span class="hljs-built_in">this</span>.root = <span class="hljs-keyword">new</span> Node(&#123;
            <span class="hljs-attr">data</span>: <span class="hljs-built_in">this</span>.data,
            <span class="hljs-attr">store</span>: <span class="hljs-built_in">this</span>,
        &#125;);
    &#125;
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">node.js</h4>
<p>node.js 树节点的属性和方法, 每个节点都有的，保证节点的独立性</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> objectAssign <span class="hljs-keyword">from</span> <span class="hljs-string">'../../../../src/utils/merge'</span>;
<span class="hljs-keyword">import</span> &#123;
    markNodeData,
&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./utils'</span>;

<span class="hljs-comment">/**
 * getPropertyFromData(this, 'children')
 * node.store为tree-store中的this
 * node.store.children: 函数 | 字符串 | undefined
 * 从node.data中获取prop对应的值
 * 
 * store.props 是树的配置项
 * 
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>node 
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>prop 
 */</span>
<span class="hljs-keyword">const</span> getPropertyFromData = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">node, prop</span>) </span>&#123;
    <span class="hljs-keyword">const</span> props = node.store.props;

    <span class="hljs-keyword">const</span> data = node.data || &#123;&#125;;

    <span class="hljs-keyword">const</span> config = props && props[prop];
    <span class="hljs-comment">// console.log('888', props, config, data[config]);</span>

    <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> config === <span class="hljs-string">'function'</span>) &#123;
        <span class="hljs-keyword">return</span> config(data, node);
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> config === <span class="hljs-string">'string'</span>) &#123;
        <span class="hljs-keyword">return</span> data[config];
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> config === <span class="hljs-string">'undefined'</span>) &#123;
        <span class="hljs-keyword">const</span> dataProp = data[prop];
        <span class="hljs-comment">// console.log('children', dataProp)</span>
        <span class="hljs-keyword">return</span> dataProp === <span class="hljs-literal">undefined</span> ? <span class="hljs-string">''</span> : dataProp;
    &#125;
&#125;

<span class="hljs-comment">// 树节点的id</span>
<span class="hljs-keyword">let</span> nodeIdSeed = <span class="hljs-number">0</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Node</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">options</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.id = nodeIdSeed++;

        <span class="hljs-comment">// 节点data</span>
        <span class="hljs-built_in">this</span>.data = <span class="hljs-literal">null</span>;

        <span class="hljs-comment">// 是否选中,默认false:取消选中(true:选中)</span>
        <span class="hljs-built_in">this</span>.checked = <span class="hljs-literal">false</span>;

        <span class="hljs-comment">// 半选中,默认false</span>
        <span class="hljs-built_in">this</span>.indeterminate = <span class="hljs-literal">false</span>;

        <span class="hljs-comment">// 父亲节点</span>
        <span class="hljs-built_in">this</span>.parent = <span class="hljs-literal">null</span>;

        <span class="hljs-comment">// 是否展开</span>
        <span class="hljs-built_in">this</span>.expanded = <span class="hljs-literal">false</span>;
        
        <span class="hljs-comment">// 是否是当前节点</span>
        <span class="hljs-built_in">this</span>.isCurrent = <span class="hljs-literal">false</span>;

        <span class="hljs-comment">// 赋初值</span>
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> option <span class="hljs-keyword">in</span> options) &#123;
            <span class="hljs-keyword">if</span>(options.hasOwnProperty(option)) &#123;
                <span class="hljs-built_in">this</span>[option] = options[option];
            &#125;
        &#125;

        <span class="hljs-comment">// internal</span>
        <span class="hljs-comment">// 该节点的层级,默认为0</span>
        <span class="hljs-built_in">this</span>.level = <span class="hljs-number">0</span>;
        <span class="hljs-comment">// 该节点的子节点</span>
        <span class="hljs-built_in">this</span>.childNodes = [];

        <span class="hljs-comment">// 计算层级 根节点层级为0</span>
        <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.parent) &#123;
            <span class="hljs-built_in">this</span>.level = <span class="hljs-built_in">this</span>.parent.level + <span class="hljs-number">1</span>;
        &#125;

        <span class="hljs-keyword">const</span> store = <span class="hljs-built_in">this</span>.store;
        <span class="hljs-keyword">if</span>(!store) &#123;
            <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'[Node]store is required!'</span>);
        &#125;

        <span class="hljs-comment">// 构建子树</span>
        <span class="hljs-built_in">this</span>.setData(<span class="hljs-built_in">this</span>.data);

        <span class="hljs-comment">// 设置节点的展开属性</span>
        <span class="hljs-comment">// console.log('store', this.store.defaultExpandAll);</span>
        <span class="hljs-keyword">if</span>(store.defaultExpandAll) &#123;
            <span class="hljs-built_in">this</span>.expanded = <span class="hljs-literal">true</span>;
        &#125;

        <span class="hljs-comment">// 节点注册,为什么会在tree-store中呢?为什么要注册?</span>
        <span class="hljs-comment">// store.registerNode(this);</span>

        <span class="hljs-comment">// console.log('Node', this, options);</span>
    &#125;

    <span class="hljs-comment">/**
     * 通过 node.label 调用(即执行get方法)
     */</span>
    <span class="hljs-keyword">get</span> <span class="hljs-title">label</span>() &#123;
        <span class="hljs-keyword">return</span> getPropertyFromData(<span class="hljs-built_in">this</span>, <span class="hljs-string">'label'</span>);
    &#125;

    <span class="hljs-comment">/**
     * A instanceof B:A是否是B的实例
     * 设置该节点的data和childNodes
     * 根节点下的data是一个数组,其子节点便是根据此生成的
     * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>data 
     */</span>
    <span class="hljs-function"><span class="hljs-title">setData</span>(<span class="hljs-params">data</span>)</span> &#123;
        <span class="hljs-comment">// console.log('setData', Array.isArray(data), data instanceof Array);</span>
        
        <span class="hljs-comment">// 如果data不是数组即非根节点,则需要给节点标记id</span>
        <span class="hljs-keyword">if</span>(!<span class="hljs-built_in">Array</span>.isArray(data)) &#123;
            markNodeData(<span class="hljs-built_in">this</span>, data);
        &#125;

        <span class="hljs-built_in">this</span>.data = data;
        <span class="hljs-built_in">this</span>.childNodes = [];

        <span class="hljs-keyword">let</span> children;
        <span class="hljs-comment">// 如果该节点的层级为0,且该data为数组类型</span>
        <span class="hljs-comment">// 根节点下的data是一个数组,其子节点便是根据此生成的</span>
        <span class="hljs-keyword">if</span>(<span class="hljs-built_in">this</span>.level === <span class="hljs-number">0</span> && <span class="hljs-built_in">this</span>.data <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Array</span>) &#123;
            children = <span class="hljs-built_in">this</span>.data;
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-comment">// 非根节点,看其children字段是否还存在</span>
            children = getPropertyFromData(<span class="hljs-built_in">this</span>, <span class="hljs-string">'children'</span>) || [];
        &#125;

        <span class="hljs-comment">// 子节点的生成</span>
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>, j = children.length; i < j; i++) &#123;
            <span class="hljs-built_in">this</span>.insertChild(&#123;<span class="hljs-attr">data</span>: children[i]&#125;);
        &#125;

        <span class="hljs-comment">// console.log('ndoe', this);</span>
    &#125;

    <span class="hljs-comment">/**
     * 插入子节点childNodes
     * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>child 
     * <span class="hljs-doctag">@param <span class="hljs-type">&#123;*&#125;</span> </span>index 
     */</span>
    <span class="hljs-function"><span class="hljs-title">insertChild</span>(<span class="hljs-params">child, index</span>)</span> &#123;
        <span class="hljs-comment">// console.log('insertChild', child, child instanceof Node);</span>

        <span class="hljs-comment">// 如果child不是Node的实例对象</span>
        <span class="hljs-keyword">if</span>(!(child <span class="hljs-keyword">instanceof</span> Node)) &#123;
            <span class="hljs-comment">// 将后面的对象值添加到child</span>
            objectAssign(child, &#123;
                <span class="hljs-attr">parent</span>: <span class="hljs-built_in">this</span>,
                <span class="hljs-attr">store</span>: <span class="hljs-built_in">this</span>.store,
            &#125;);

            <span class="hljs-comment">// 创建child节点</span>
            child = <span class="hljs-keyword">new</span> Node(child);
            <span class="hljs-comment">// console.log('chi', child);</span>
        &#125;

        child.level = <span class="hljs-built_in">this</span>.level + <span class="hljs-number">1</span>;
        <span class="hljs-comment">// console.log('ch', child, index);</span>

        <span class="hljs-comment">/**
         * typeof index !== 'undefined'
         * index !== undefined
         * 
         * 将child插入到childNodes
         */</span>
        <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> index === <span class="hljs-string">'undefined'</span> || index < <span class="hljs-number">0</span>) &#123;
            <span class="hljs-comment">// console.log(typeof index !== 'undefined')</span>
            <span class="hljs-built_in">this</span>.childNodes.push(child);
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-comment">// console.log(index, index === undefined)</span>
            <span class="hljs-built_in">this</span>.childNodes.splice(index, <span class="hljs-number">0</span>, child)
        &#125;
    &#125;

    <span class="hljs-comment">/**
     * 子树收缩
     * 设置展开属性
     * node.expanded = false
     */</span>
    <span class="hljs-function"><span class="hljs-title">collapse</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.expanded = <span class="hljs-literal">false</span>;
        <span class="hljs-comment">// console.log('collapse', this, this.expanded);</span>
    &#125;

    <span class="hljs-comment">/**
     * 展开子树
     * 设置节点的展开属性
     * node.expanded = true
     * 
     * 注意:树上的每个节点都具有展开和伸缩子树的方法,而不是将这两个方法共享
     * 保证了树节点的独立性质
     */</span>
    <span class="hljs-function"><span class="hljs-title">expand</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-comment">// console.log('展开子树', this);</span>
        <span class="hljs-built_in">this</span>.expanded = <span class="hljs-literal">true</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">总结</h3>
<h4 data-id="heading-13">实现思路</h4>
<ul>
<li>tree.vue 渲染树</li>
<li>tree-node.vue 渲染子树</li>
<li>tree-store.js 树的状态管理器</li>
<li>node.js 定义树节点的属性和方法</li>
</ul></div>  
</div>
            