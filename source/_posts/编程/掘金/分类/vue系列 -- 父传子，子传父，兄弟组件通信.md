
---
title: 'vue系列 -- 父传子，子传父，兄弟组件通信'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/869dc7f8fe4043929a1ff54e6a332052~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 22 May 2021 02:48:23 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/869dc7f8fe4043929a1ff54e6a332052~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">父传子（父通过<code>import + component</code>写入子组件，然后<code>v-bind</code>绑定数据，子通过<code>props</code>接收）</h2>
<h4 data-id="heading-1">思路</h4>
<blockquote>
<ul>
<li>父：自定义属性名 + 数据（要传递）=> v-bind:value="数据"</li>
<li>子：props ["父组件上的自定义属性名“] => 进行数据接收</li>
</ul>
</blockquote>
<h4 data-id="heading-2">子组件：child.vue</h4>
<p>要点：</p>
<ul>
<li><code>props</code> 数组里面是父组件上的自定义属性名</li>
<li>在 <code>template</code> 里面进行数据接收</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/869dc7f8fe4043929a1ff54e6a332052~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-3">父组件：father.vue</h4>
<p>要点：</p>
<ul>
<li>引入 child.vue 文件，并为其创建一个变量</li>
<li>在 <code>components</code> 里面写出这个变量</li>
<li>在 <code>template</code> 里面需要注册子组件</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c8bc6d393b2458586678add6035b880~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>保存修改的文件，查看浏览器</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/06807ad526a745b5918f59f7d698ada9~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们可以对 message 的值进行 v-bind 动态绑定</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d46c20667a9a48e8b5317af38a5e1b64~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>此时浏览器中</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/136b8699e4b2471aae07b7d12532ce1e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-4">总结</h4>
<ul>
<li>子组件在props中创建一个属性，用以接收父组件传过来的值</li>
<li>父组件中注册子组件</li>
<li>在子组件标签中添加子组件props中创建的属性</li>
<li>把需要传给子组件的值赋给该属性</li>
</ul>
<h2 data-id="heading-5">子传父（子<code>click</code>设置点击事件，<code>$emit</code>设置通道后传参，父在<code>methods</code>接收）</h2>
<h4 data-id="heading-6">思路</h4>
<blockquote>
<ul>
<li>子：this.$emit('自定义事件名称', 数据) 子组件标签上绑定@自定义事件名称 = '回调函数'</li>
<li>父：methods: &#123;    回调函数() &#123;      //逻辑处理  &#125;  &#125;</li>
</ul>
</blockquote>
<h4 data-id="heading-7">子组件：child.vue</h4>
<ol>
<li>在子组件中创建一个按钮，给按钮绑定一个点击事件</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe726bcdf2bd4e6c94139c7ffc5472b7~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>在响应该点击事件的函数中使用 <code>$emit</code> 来触发一个自定义事件，并传递一个参数</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67b3676a238841cfa1bcffc28e560999~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-8">父组件：father.vue</h4>
<ol start="3">
<li>在父组件中的子标签中监听该自定义事件并添加一个响应该事件的处理方法</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e5fa201f7d7745e08ff133316d995241~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="4">
<li>保存修改的文件，在浏览器中点击按钮</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d31e120d3f3d415d92c6c0a6a6ddcc8c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-9">总结</h4>
<ul>
<li>子组件中需要以某种方式例如点击事件的方法来触发一个自定义事件</li>
<li>将需要传的值作为$emit的第二个参数，该值将作为实参传给响应自定义事件的方法</li>
<li>在父组件中注册子组件并在子组件标签上绑定对自定义事件的监听</li>
<li>在通信中，无论是子组件向父组件传值还是父组件向子组件传值，他们都有一个共同点就是有中间介质，子向父的介质是自定义事件，父向子的介质是props中的属性。抓准这两点对于父子通信就好理解了</li>
</ul>
<h2 data-id="heading-10">兄弟组件（兄<code>click</code>设置点击事件，用<code>$emit</code>设置通道传参给中转站，弟通过<code>$on</code>接收来自中转站的参数）</h2>
<h4 data-id="heading-11">思路</h4>
<blockquote>
<ul>
<li>通过中转站 let bus = new Vue（）</li>
<li>A：methods :&#123; 函数&#123;bus.$emit(‘自定义事件名’，数据)&#125;  发送</li>
<li>B：created （）&#123;bus.$on(‘A发送过来的自定义事件名’，函数)&#125;  进行数据接受</li>
</ul>
</blockquote>
<h4 data-id="heading-12">中转站文件</h4>
<p>创建 bus.js 做为中转站文件</p>
<p>bus.js 内容为</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a2f8da60f52b4d038e5f6e557c079a60~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-13">child1.vue</h4>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ded0fc06e78449e18ef87b028b069455~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-14">child2.vue</h4>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9242cae4b6ba47f8aa1802fb0802a2e5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-15">总结</h4>
<ul>
<li>兄组件通过<code>click</code>设置点击事件</li>
<li>兄组件通过<code>$emit</code>设置通道传参给中转站</li>
<li>弟组件通过<code>$on</code>接收来自中转站的参数</li>
</ul>
<h2 data-id="heading-16">参考文章</h2>
<ul>
<li><a href="https://www.cnblogs.com/chenhongshuang/p/8678207.html" target="_blank" rel="nofollow noopener noreferrer">【vue组件之间互相传值：父传子，子传父】</a></li>
<li><a href="https://www.jianshu.com/p/415ff66f8bd5" target="_blank" rel="nofollow noopener noreferrer">Vue 父传子，子传父，兄弟组件通信的使用</a></li>
</ul></div>  
</div>
            