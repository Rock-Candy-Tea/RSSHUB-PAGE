
---
title: 'Element.scrollIntoView() 方法让当前的元素滚动到浏览器窗口的可视区域'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e763da48404846e387021739a6f1d85d~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 11 Jun 2021 10:14:01 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e763da48404846e387021739a6f1d85d~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><a href="https://juejin.cn/post/undefined">MDN地址</a></p>
<h3 data-id="heading-0">问题描述: 页面的最底部有分页器,但是每次点击切换页码,要让页面恢复到最顶端</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e763da48404846e387021739a6f1d85d~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">语法</h3>
<pre><code class="copyable">element.scrollIntoView(); // 等同于element.scrollIntoView(true) 
element.scrollIntoView(alignToTop); // Boolean型参数 
element.scrollIntoView(scrollIntoViewOptions); // Object型参数
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">参数有两种写法</h3>
<p><code>alignToTop</code> : 布尔值类型</p>
<blockquote>
<p>+<code> true</code> 元素的顶端将和其所在滚动区的可视区域的最顶端对齐, 等同于<code>scrollIntoViewOptions: &#123;block: "start", inline: "nearest"&#125;</code>默认值
+<code> false</code> 元素的底部将和其所在的滚动区域的可视区域的底部的对齐,等同于<code>scrollIntoViewOptions: &#123;block: "end", inline: "nearest"&#125;</code>默认值</p>
</blockquote>
<p><code>scrollIntoViewOptions</code> :对象类型(可选参数)</p>
<blockquote>
<p>一个包含下列属性的对象：</p>
</blockquote>
<p><code>behavior </code>可选
定义动画过渡效果，<code> "auto"或 "smooth"</code> 之一。默认为 <code>"auto"</code>。
<code>block </code>可选
定义垂直方向的对齐，<code> "start", "center", "end"</code>, 或 <code>"nearest"</code>之一。默认为<code> "start"</code>。
<code>inline</code> 可选
定义水平方向的对齐， <code>"start", "center", "end"</code>, 或 <code>"nearest"</code>之一。默认为<code> "nearest"</code>。</p>
<p><strong>示例</strong></p>
<pre><code class="copyable">var element = document.getElementById("box");
element.scrollIntoView();
element.scrollIntoView(false);
element.scrollIntoView(&#123;block: "end"&#125;);
element.scrollIntoView(&#123;behavior: "instant", block: "end", inline: "nearest"&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">案例:</h3>
<h3 data-id="heading-4">效果每次点击按钮,新增的元素都在滚动区域的最底端</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4e1a0e49b3f94c2c967f18dffa76bcff~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable"><template>
  <div>
    <div ref="contain" class="container"></div>
    <button @click="toadd">点击添加元素</button>
  </div>
</template>

<script>
export default &#123;
  data() &#123;
    return &#123;
      num: 1
    &#125;;
  &#125;,
  methods: &#123;
    toadd() &#123;
      this.num++;
      let outdom = this.$refs.contain;
      let vli = document.createElement("li");
      vli.innerText = this.num;
      outdom.appendChild(vli);
      vli.scrollIntoView(&#123;
        behavior: "smooth",
        block: "end"
      &#125;);
    &#125;
  &#125;
&#125;;
</script>
<style>
.app &#123;
  text-align: center;
  width: 100vw;
  height: 100vh;
&#125;
.container &#123;
  width: 100px;
  height: 200px;
  margin: 0 auto;
  border: 1px solid #ccc;
  overflow: auto;
&#125;
button &#123;
  width: 100px;
  display: block;
  margin: 30px auto;
&#125;

li &#123;
  margin-top: 20px;
&#125;
</style>

<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            