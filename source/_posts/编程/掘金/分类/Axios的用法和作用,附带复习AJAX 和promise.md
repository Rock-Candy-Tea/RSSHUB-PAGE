
---
title: 'Axios的用法和作用,附带复习AJAX 和promise'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d356fa6565d14b42b8df2083a6340f71~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 20 Aug 2021 04:10:36 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d356fa6565d14b42b8df2083a6340f71~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">Axios的get请求的学习</h2>
<ul>
<li>axios是基于promise用于浏览器和nodejs的HTTP客户端,可以用在浏览器和 node.js 中。</li>
</ul>
<p>它本身有以下特征：</p>
<ul>
<li>从浏览器中创建 XMLHttpRequests</li>
<li>从 node.js 创建 http 请求</li>
<li>支持 Promise API</li>
<li>拦截请求和响应</li>
<li>转换请求数据和响应数据</li>
<li>取消请求</li>
<li>自动转换 JSON 数据</li>
<li>客户端支持防御 XSRF</li>
</ul>
<p>实际上，axios可以用在浏览器和 node.js 中是因为，它会自动判断当前环境是什么，如果是浏览器，就会基于<strong>XMLHttpRequests</strong>实现axios。如果是node.js环境，就会基于node<strong>内置核心模块http</strong>实现axios</p>
<ul>
<li>在HelloWorld中的template中添加内容</li>
</ul>
<pre><code class="copyable"><template>
<div class="hello">
<h3> I am the axios,用来发棕请求，拦截响应。</h3>

</div>
</template>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>步骤：</p>
<ul>
<li>1.安装:npm install axios</li>
<li>2.引入加载：import axios from 'axios'</li>
<li>3.将axios全局挂载到vue原型上：vue.prototype.$ttp = axios</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d356fa6565d14b42b8df2083a6340f71~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>4.如何发送请求
<ul>
<li>发送请求的模板</li>
</ul>
</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/940de6a1f5d545869dfe9f0b90578126~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
得到一个API的地址，</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ed634222dd744a5be8468368ce9076d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>成功就是.then;</li>
<li>失败就是.catch</li>
<li>加入一个按钮</li>
</ul>
<pre><code class="copyable"><button @click="getData">发送请求</button>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果点击按钮，成功的话，后台console.log(res)就会出现API 的内容,如果console.log(res.data.data),就会出现更详细的的特定的内容</p>
<ul>
<li>5.把API中的标题显示在页面上</li>
</ul>
<pre><code class="copyable"><template>
<ul>
<li v-for="item in items">
&#123;&#123;item.title&#125;&#125;
</li>
</ul>
</template>
-----------传统的function方式
methods:&#123;
getData()&#123;
var self = this;
this.$http.get('https://cnodejs.org/api/v1/topics')
.then(function(res)&#123;
self.items = res.data.data
console.log(res.data.data)
&#125;)
&#125;&#125;
-----------用ES6的方法
methods:&#123;
getData()&#123;
this.$http.get('https://cnodejs.org/api/v1/topics')
.thenres=>&#123;
this.items = res.data.data;
console.log(res.data.data)
&#125;)
&#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>6.如果要加参数。例如显示多少页，每页多少内容，直接在</li>
</ul>
<pre><code class="hljs language-方法1（常用，比较方便添加删除） copyable" lang="方法1（常用，比较方便添加删除）">this.$http.get('https://cnodejs.org/api/v1/topics',&#123;
params:&#123;
page:1,
limit:10&#125;&#125;)
-------------方法2
this.$http.get('https://cnodejs.org/api/v1/topics?page=1&limit=10')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这两种传递参数数据的方法一样</p>
<h2 data-id="heading-1">Axios的post的请求用法</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f2cf86e732f04c9ab919e07d40a63c92~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b4abf1f7ab50492188d85e013ba8509f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-components/HelloWorld.vue copyable" lang="components/HelloWorld.vue">   < template>
   <div class="hello">
   <h3>我是axiosAPP,用来发送请求，拦截响应</h3>
   <button @click=“getData”>发送请求</button>//添加一个按钮，绑定那个方法
   <ul>//把API中的title渲染到页面里面去，在data中定义一个items
   <li v-for= “item in items”>
   &#123;&#123;item.title&#125;&#125;
   </li>
   </ul>
   </div>
   </template>
   --------------
   <script>
   Vue.prototype.$http = axios;//全局挂载原型上
   import axios from 'axios'//引入axios
   import vue from 'vue'
   export default&#123;
   name:'HelloWorld',
   data()&#123;
   return&#123;
  items:[]
   &#125;
   &#125;,
   methods:&#123;           //如何发送请求
   getData()&#123;
  <!-- var self = this;
   this.$http.get('https://cnodejs.org/api/v1/topics')//获取这个API
   .then(function(res)&#123;                          //如果成功，打印response
   console.log(res.data.data)&#125;
   )-->
   用es6的语法就简单：
   this.$http.get('https://cnodejs.org/api/v1/topics',&#123;//若有参数就按照斜体字这样写
   *params:&#123;
   page:1,
   limit:10
     &#125;)*
   .then(res=>&#123;
   this.items = res.data.data;
     console.log(res.data.data)&#125;
   &#125;)
   .catch(function(err)&#123;                     //如果失败，打印err
   console.log(err)&#125;)
   &#125;
   &#125;
   
   </script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>基本写法：const success = options.success
const fail = options.fail
析构赋值：const&#123;success，fail&#125; = options//</p>
<h2 data-id="heading-2">AJAX的学习</h2>
<ul>
<li>本质：用JS发请求和收响应。</li>
<li>背景：AJAX是浏览器的功能</li>
<li>浏览器可以发请求，例如输入一个百度的网站；</li>
<li>收响应，就是向大家展示了一个百度的页面；</li>
<li>服务器：浏览器发请求到服务器（server.js）上：
<ul>
<li>复制nodejs-test里面的server.js里面的代码；</li>
<li>创建一个目录AJAX1，用vscode打开，新建一个server.js，将复制的代码，粘贴进去；</li>
<li>新建打开一个终端，输入node server.js</li>
</ul>
</li>
<li>安装node-dev，可以自动更新代码重启：</li>
</ul>
<p>在终端里面输入
yarn global add node-dev
node-dev server.js 8888</p>
<h3 data-id="heading-3">AJAX的创建,加载css</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/88589fa0bbf146499d795ab7db1f083e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d694e0f5cb7427f8f6e734211af8184~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">Promise的学习</h2>
<ul>
<li><strong>异步模式</strong>，是指后一个任务不等前一个任务执行完就执行，每个任务有一个或多个回调函数。</li>
<li>Promise是异步编程的一种解决方案，比传统的解决方案——回调函数和事件——更合理和更强大。</li>
<li>所谓Promise，简单说就是一个容器，里面保存着某个未来才会结束的事件（通常是一个异步操作）的结果。</li>
<li>Promise 提供统一的 API，各种异步操作都可以用同样的方法进行处理。</li>
<li>使用Promise对象可以用同步操作的流程写法来表达异步操作，避免了层层嵌套的异步回调，代码也更加清晰易懂，方便维护，也可以捕捉异常。</li>
</ul>
<pre><code class="copyable">function fn(num) &#123;
  return new Promise(function(resolve, reject) &#123;
    if (typeof num == 'number') &#123;
      resolve();
    &#125; else &#123;
      reject();
    &#125;
  &#125;)
  .then(function() &#123;
    console.log('第1个then：参数是一个number值');
  &#125;)
  .then(null, function() &#123;
    console.log('第2个then');
  &#125;)
&#125;
fn('haha');
fn(1234);// 第1个then：参数是一个number值、第2个then

<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            