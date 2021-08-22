
---
title: 'vue 项目中element组件库交互bug-2'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/92213b57fc3442c785283448a3b6c9d3~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 21 Aug 2021 19:49:24 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/92213b57fc3442c785283448a3b6c9d3~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第7天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<blockquote>
<p>前言：在现在这种大的社会背景下，人们的需求更加的个性化了，而之前为了解放开发复杂的原生开发状态，现有的组件库已经远远不能满足人们高质量的需求了，这两天开发发现了一些element UI交互上的缺陷，当然也是一些容易大意疏忽的细节问题，希望能给大家带来帮助</p>
</blockquote>
<h2 data-id="heading-0">1.element Message 消息提示</h2>
<h3 data-id="heading-1">1.项目中Message组件的引用</h3>
<pre><code class="copyable">//全部引入组件库使用方便
import ElementUI from "element-ui";
//按需引入，这种好处就是代码体积小
import &#123; Message &#125; from "element-ui";

//全局挂载，便捷的this引用
Vue.prototype.$message = Message;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">2.Message组件的问题</h3>
<p>页面运行时代码报错：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/92213b57fc3442c785283448a3b6c9d3~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-22 上午10.58.20.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6d05a43cb0e54323908c1e88d7d5da0b~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-22 上午11.01.28.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>element组件源码报错位置
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d3d9d5a0a12742fe9b4369f5c6e08af7~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-22 上午10.59.30.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">3.这里大家大概也能看出问题的所在了</h3>
<p>点击查看自己代码报错位置，基本就可以看出报错原因
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4554cbf3a9374b6d91a7184eaed67deb~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-22 上午11.04.21.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4"><code>基本总结研究总结：Message组件在使用的过程中调用的入参不能为 null 和 undefined </code></h3>
<blockquote>
<p>一般发生这种问题的位置原因：大概可以多注意一下axios或者fetch请求的返回结果的地方引用处，如果有Message组件异常提示设置，但是后端返回的数据里面缺少字段，则就会产生   “undefined”   的上面的报错。</p>
</blockquote>
<h2 data-id="heading-5">2.element  NavMenu 导航菜单</h2>
<p>a.官方代码逻辑：</p>
<pre><code class="copyable"><el-menu
  :default-active="baseroute"
  class="vertical"
  @select="menuclick"
  :router="menurouter"
>

   <el-menu-item :index="items.router" v-for="items in menu" :key="items.id">
     <span slot="title">&#123;&#123;items.label&#125;&#125;</span>
   </el-menu-item>
</el-menu>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>b.官方的API：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/22a6a8fe47b14ac1b733fa16c7371115~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-22 上午11.22.25.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">看着这个组件没有问题很完美，使用也很顺畅，但是问题出就出在<code>:router="true"</code>这个配置上，大家有没有发现这个配置项无法传参，</h3>
<p>c.当然遇到问题我们就需要研究解决：（初步的解决方案）</p>
<pre><code class="copyable">watch: &#123;
 "$route.path": function(newVal) &#123;
    //menu就是展示菜单的数组
    this.menu.forEach(item=>&#123;
      if(newVal==item.router)&#123;
         this.$router.push(&#123;path:newVal ,query:&#123;...this.routermsg&#125;&#125;)
      &#125;
    &#125;)
  &#125;,
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">d.<code>又有问题出现了，那就时当你点击当前高亮菜单时（一个菜单点两次），watch是监听不到的（认为路由是没有变化的），组件会以 router 定义的 index 作为 path 进行路由跳转，也就是没有了路由传参的功能，页面就会各种报错和参数错误</code></h3>
<p>e.在此情形下后面改善代码兼容了 NavMenu 导航菜单传参的功能,</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ba8980c657c141429642632e81ad9152~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-22 上午11.40.04.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable"><script>
methods: &#123;
   menuclick(index,indexPath)&#123;
     this.baseroute=index
     this.$router.push(&#123;path:indexPath[0] ,query:&#123;...this.routermsg&#125;&#125;)
   &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>兼容了传参功能，那么watch监听也就不需要了，可以注释或删除</p>
</blockquote></div>  
</div>
            