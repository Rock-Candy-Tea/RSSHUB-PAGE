
---
title: '创建虚拟滚动列表 Vue.js滚动列表'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8e2307fc805544b3a29f7fe8ab26f027~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 06 Aug 2021 01:55:42 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8e2307fc805544b3a29f7fe8ab26f027~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>单独渲染DOM上的项目会给用户带来明显的性能滞后，特别是当他们滚动浏览大型列表时。为了使滚动更有效，我们应该使用虚拟滚动列表，这样可以提高页面的加载速度，防止网络应用的卡顿。</p>
<p>虚拟滚动列表类似于标准的滚动列表，然而，在任何时候都只有用户当前视图中的数据被呈现出来。当用户向下滚动页面时，新的项目会随着旧的项目被删除而被呈现出来。</p>
<p>在这篇文章中，我们将探讨 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ftangbc%2Fvue-virtual-scroll-list" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/tangbc/vue-virtual-scroll-list" ref="nofollow noopener noreferrer"><code>vue-virtual-scroll-list</code></a>一个用于在Vue.js中创建虚拟滚动列表的神奇库。让我们开始吧!</p>
<h2 data-id="heading-0">渲染内容在<code>vue-virtual-scroll-list</code></h2>
<p><code>vue-virtual-scroll-list</code> 库有两种主要方法将网页内容渲染成列表，即<code>item</code> 模式和<code>v-for</code> 模式。</p>
<p><code>item</code> 模式是渲染静态内容的理想选择。一旦内容被追加到DOM上，<code>item</code> 模式就会释放正在使用的内存。如果你改变了数据，你将需要调用<code>forceRender()</code> ，并重新开始这个过程。</p>
<p>要渲染动态内容，更好的选择是<code>v-for</code> 模式。在<code>v-for</code> 模式下，提供给列表的数据在内存中被引用。因此，当数据发生变化时，列表项会被重新渲染，并且上下文被保持。</p>
<p>让我们通过比较<code>item</code> 模式中使用和不使用虚拟滚动列表的性能来仔细看看<code>vue-virtual-scroll-list</code> 库。</p>
<p>首先，我们将建立一个新的Vue.js项目并安装<code>vue-virtual-scroll-list</code> 。然后，我们将使用随机生成的数据创建一个列表。最后，我们将在使用和不使用虚拟滚动的情况下渲染我们的列表，比较各自的性能。</p>
<h2 data-id="heading-1">设置一个Vue.js项目</h2>
<p>首先，确保你的机器上安装了Vue.js。用以下命令创建一个新的Vue.js项目。</p>
<pre><code class="copyable">vue create virtual-scroll-demo

<span class="copy-code-btn">复制代码</span></code></pre>
<p>一旦项目设置好了，就安装<code>vue-virtual-scroll-list</code> 库。</p>
<pre><code class="copyable">npm install vue-virtual-scroll-list --save

<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在，我们的项目有如下结构。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8e2307fc805544b3a29f7fe8ab26f027~tplv-k3u1fbpfcp-watermark.image" alt="New Vue Project Structure" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">生成一个列表</h2>
<p>现在我们已经建立了项目的基础，让我们开始为创建两个列表打基础。</p>
<p>导航到你的<code>/src</code> 文件夹，创建一个名为<code>data.js</code> 的文件。让我们把下面这个生成随机数据的简单函数添加到<code>data.js</code> 。</p>
<pre><code class="copyable">let idCounter = 0;

export function getData(count) &#123;
  const data = [];
  for (let index = 0; index < count; index++) &#123;
    data.push(&#123;
      id: String(idCounter++),
      text: Math.random()
        .toString(16)
        .substr(10),
    &#125;);
  &#125;
  return data;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来，我们将创建一个名为<code>Item.vue</code> 的新文件，它是我们要渲染的<code>item</code> 组件。在<code>Item.vue</code> 中，我们将包括以下代码块，它为我们的列表创建一个模板和样式，以及检索和显示上面生成的数据的道具。</p>
<pre><code class="copyable"><template>
  <div class="item">
    <div class="id">&#123;&#123; source.id &#125;&#125; - &#123;&#123; source.text &#125;&#125;</div>
  </div>
</template>

<script>
export default &#123;
  name: 'item',
  props: &#123;
    source: &#123;
      type: Object,
      default() &#123;
        return &#123;&#125;
      &#125;
    &#125;
  &#125;
&#125;
</script>

<style scoped>
.item &#123;
  display: flex;
  flex-direction: column;
  border-bottom: 1px solid lightgrey;
  padding: 1em;
&#125;
</style>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">渲染一个没有虚拟滚动的列表</h3>
<p>现在我们已经创建了一个列表，让我们在不使用<code>vue-virtual-scroll-list</code> 的情况下在我们的DOM上渲染列表项。添加以下代码到 <code>App.vue</code> 。</p>
<pre><code class="copyable"><template>
  <div id="app">
    <div class="wrapper">
    <div class="list">
      <p  v-for="item in items" :key="item">
    &#123;&#123;item&#125;&#125;
  </p>
      </div>

    </div>
  </div>
</template>

<script>
import Item from './Item'
import &#123; getData &#125; from './data'

export default &#123;
  name: 'App',
  data() &#123;
    return &#123;
      item: Item,
      items: getData(100000)
    &#125;
  &#125;
&#125;
</script>

<style>
#app &#123;
  text-align: center;
  color: #2c3e50;
  margin-top: 1em;
  padding: 1em;
&#125;
.list &#123;
  border: 2px solid red;
  border-radius: 3px;
&#125;
</style>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上面的代码块中，我们在DOM中渲染了100,000个项目。让我们看看在这么多数据和没有虚拟滚动的情况下，我们的列表将如何执行。用下面的npm命令启动该项目。</p>
<pre><code class="copyable">npm run serve

<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们会得到以下的输出。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/185c2588872c49449f8192d2822bfbfc~tplv-k3u1fbpfcp-watermark.image" alt="List Item Render Standard Scroll" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当我们在浏览器中检查<code>inspect</code> 元素时，我们会看到所有的HTML元素都被追加到<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.logrocket.com%2Fhow-the-virtual-dom-works-in-vue-js%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.logrocket.com/how-the-virtual-dom-works-in-vue-js/" ref="nofollow noopener noreferrer">浏览器DOM</a>中，如下图所示。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7def506773f94f95a518efd939e11662~tplv-k3u1fbpfcp-watermark.image" alt="Browser Inspect Element HTML Output" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在浏览器DOM中追加元素会增加DOM的大小。因此，浏览器将需要更多的时间来追加每一个项目到DOM中，可能会造成明显的性能滞后。让我们仔细观察一下浏览器将我们的列表追加到DOM中所花费的时间。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/995cdcfd50f64e53a982c035e36cc3c4~tplv-k3u1fbpfcp-watermark.image" alt="Standard List Component Browser Dom Load Time" loading="lazy" referrerpolicy="no-referrer"></p>
<p>事件<code>DOMContentLoaded</code> 在22秒后启动，这意味着浏览器标签在显示最终渲染的列表之前需要22秒的加载时间。同样地，如下图所示，渲染我们的列表消耗了128MB的内存。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4b98fbd639b14df285303b77a5aab98f~tplv-k3u1fbpfcp-watermark.image" alt="Standard List Component Browser Dom Memory Consumption" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">用虚拟卷轴渲染一个列表</h3>
<p>现在，让我们试着用虚拟卷轴来渲染我们的列表。在<code>main.js</code> 中导入<code>vue-virtual-scroll-list</code> 包。</p>
<pre><code class="copyable">import Vue from "vue";
import App from "./App.vue";

Vue.config.productionTip = false;

import VirtualList from "vue-virtual-scroll-list";

Vue.component("virtual-list", VirtualList);
new Vue(&#123;
  render: (h) => h(App),
&#125;).$mount("#app");

<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来，我们将渲染<code>virtual-list</code> 组件内的项目的数据。让我们把我们的<code>App.js</code> 文件改成以下代码块的样子。</p>
<pre><code class="copyable"><template>
  <div id="app">
    <div class="wrapper">


       <virtual-list
        class="list"
        style="height: 360px; overflow-y: auto;"
        :data-key="'id'"
        :data-sources="items"
        :data-component="item"
        :estimate-size="50"
      />
    </div>
  </div>
</template>

<script>
import Item from './Item'
import &#123; getData &#125; from './data'

export default &#123;
  name: 'App',
  data() &#123;
    return &#123;
      item: Item,
      items: getData(100000)
    &#125;
  &#125;
&#125;
</script>

<style>
#app &#123;
  text-align: center;
  color: #2c3e50;
  margin-top: 1em;
  padding: 1em;
&#125;
.list &#123;
  border: 2px solid red;
  border-radius: 3px;
&#125;
</style>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意，数据道具是虚拟列表渲染项目所需要的。运行上面的代码块将给我们带来以下输出。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c15ebe8d7d9740649a967e9c167ca8d5~tplv-k3u1fbpfcp-watermark.image" alt="Virtual Scroll Component Output" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们可以在下面的图片中看到，一次只渲染了几个项目。当用户向下滚动时，更多的项目被呈现出来。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75b010782fee445b9595fc8d69b8c475~tplv-k3u1fbpfcp-watermark.image" alt="Virtual Scroll Item Render Order" loading="lazy" referrerpolicy="no-referrer"></p>
<p>现在，我们的DOM树比以前小多了当我们渲染我们的虚拟滚动列表时，<code>DOMContentLoaded</code> ，将比以前快得多!</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/484b4d4b5d834542bd6b8511b2a30052~tplv-k3u1fbpfcp-watermark.image" alt="Virtual Scroll List Dom Render Time" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如上图所示，该事件的触发时间只有563毫秒。同样，我们的操作只消耗了79MB的内存，这比我们没有使用虚拟滚动时要少得多。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6973646d7a78470aa57ede2f6c7c4d95~tplv-k3u1fbpfcp-watermark.image" alt="Virtual Scroll List DOM Memory Consumption" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">总结</h2>
<p>现在你知道了如何使用<code>vue-virtual-scroll-list</code> 库在Vue.js中创建一个虚拟滚动列表了吧!</p>
<p>在本教程中，我们创建了一个使用随机生成的数据的静态列表，然后在我们的Vue.js应用程序中实现了它，比较了使用和不使用虚拟滚动的性能。</p>
<p>虚拟滚动列表的性能很高，特别是当你的网页上有大量的项目列表时。使用虚拟滚动列表可以提高页面的加载速度，并全面改善用户体验</p></div>  
</div>
            