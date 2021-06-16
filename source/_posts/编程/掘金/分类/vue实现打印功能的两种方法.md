
---
title: 'vue实现打印功能的两种方法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b36cbe545bb9482fbac5723e2b63540b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 11 Jun 2021 00:58:59 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b36cbe545bb9482fbac5723e2b63540b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>第一种方法：通过npm 安装插件</p>
<p>1，安装 <code>npm install vue-print-nb --save</code></p>
<p>2，引入 安装好以后在main.js文件中引入</p>
<pre><code class="copyable">import Print from 'vue-print-nb'　　Vue.use(Print); //注册
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3，现在就可以使用了</p>
<pre><code class="copyable"><div id="printTest" >

　　   <p>明月照于山间</p>

　　　　<p>清风来于江上 </p>

</div>

<button v-print="'#printTest'">打印</button>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4.如需通过链接地址打印：window.location.href = airway_bill; airway_bill 为链接地址。</p>
<p>5.如果内容打印不全，在打印操作时点击更多设置，然后设置缩放。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b36cbe545bb9482fbac5723e2b63540b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c14a5c6a06934dd1a57ab7a45ca85a85~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>第二种方法：手动下载插件到本地</p>
<p>插件地址：</p>
<pre><code class="copyable">https://github.com/xyl66/vuePlugs_printjs
<span class="copy-code-btn">复制代码</span></code></pre>
<p>1.在src下新建文件夹plugs,将下载好的print.js放入plugs文件夹下，然后操作如下</p>
<pre><code class="copyable">import Print from '@/plugs/print'
Vue.use(Print) // 注册
<template>
　　<section ref="print">
　　　　打印内容
　　　　<div class="no-print">不要打印我</div>
　　</section>
</template>
this.$print(this.$refs.print) // 使用
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.注意事项 需使用ref获取dom节点，若直接通过id或class获取则webpack打包部署后打印内容为空</p>
<p>3.指定不打印区域</p>
<p>方法1. 添加no-print样式类</p>
<pre><code class="copyable"><div class="no-print">不要打印我</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>方法2. 自定义类名</p>
<pre><code class="copyable"><div class="do-not-print-me-xxx">不要打印我</div>this.$print(this.$refs.print,&#123;'no-print':'.do-not-print-me-xxx'&#125;) // 使用
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            