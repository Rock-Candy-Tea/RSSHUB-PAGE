
---
title: '【VUE】组件参数校验与非props特性'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/33f7bdc1cd0b42d399a6262e63a07b4f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 17 Aug 2021 19:22:13 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/33f7bdc1cd0b42d399a6262e63a07b4f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第16天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<h2 data-id="heading-0">组件参数校验</h2>
<p>父组件向子组件传递一些内容，子组件有权对接收的内容进行一些约束（即组件接收的参数是有规则可定义的），这些约束就是组件参数校验。</p>
<p><strong>场景需求：</strong> 父组件调用子组件的时候，传递过来的这个<code>content</code>必须是一个字符串。</p>
<p><strong>解决方法：</strong> 将接收的props定义称对象，并指定类型。</p>
<pre><code class="copyable">props:  &#123;
    content: String
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>需求升级：</strong> 如果我需要的参数类型是字符串或者数组。</p>
<pre><code class="copyable">props:  &#123;
    content: [String, Number]
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>更复杂的参数校验：</strong> 子组件通过props接收传递参数，并说明传递的参数有如下属性：</p>
<ul>
<li>type —— 参数类型</li>
<li>required —— 是否必传</li>
<li>default —— 默认传的值</li>
<li>validator —— 自定义校验器，要求字符串长度等</li>
</ul>
<pre><code class="copyable">props:  &#123;
    content: &#123;
            type:  String, 
            required: true,
            default: 'default value',
            validator: function(value) &#123;
                    return (value.length > 5)
            &#125;
    &#125;
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">非props特性与props特性</h2>
<h3 data-id="heading-2">props特性（父子组件之间有对应关系）</h3>
<p>父组件通过属性(如content)向子组件传值时，而子组件在props中声明了这个属性(如content)的数据。当父子组件关于数据传值的时候，出现了对应的属性(如content)，那么这个属性则为 <strong>props特性</strong>。</p>
<p><strong>[重点]特点如下：</strong></p>
<ul>
<li>
<p>子组件所带的属性传递是不会出现在dom上；</p>
</li>
<li>
<p>父组件通过属性传值后，子组件就会通过 <strong>template中的插值表达式</strong> 或通过 <strong>this.content去取得该属性中的内容</strong></p>
</li>
</ul>
<h3 data-id="heading-3">非props特性（使用场景较少）</h3>
<p>父组件向子组件传递了一个属性，但是子组件并没有<code>props</code>这块的内容，也就是说子组件并没有声明我要接收父组件的传递过来的内容。</p>
<pre><code class="copyable"><div id="root">
    <child content="123" ></child>
</div>
var child = &#123;
        template: '<div>&#123;&#123;content&#125;&#125;</div>'
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样会报错：显示父组件的属性content未被定义</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/33f7bdc1cd0b42d399a6262e63a07b4f~tplv-k3u1fbpfcp-watermark.image" alt="1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>将子组件中的引用去掉后，可以看到该<code>content属性(即非props特性)</code>则会展现在子组件template中的页面模板的dom标签的属性中。</p>
<pre><code class="copyable"><div id="root">
    <child content="123" ></child>
</div>
var child = &#123;
    template: '<div>子组件的内容</div>'
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/68dc62e20d544aad8b2f1872b6f253b9~tplv-k3u1fbpfcp-watermark.image" alt="1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>非props特点</strong></p>
<ul>
<li>
<p>若子组件未定义props进行接收父组件属性传来的值，那么这个属性（如content）则为<strong>非props特性</strong>。</p>
</li>
<li>
<p>父组件如果使用一个非props特性，子组件没有通过peopes接收属性数据，但该属性则会展现在子组件template中的页面模板的dom标签的属性中。</p>
</li>
</ul></div>  
</div>
            