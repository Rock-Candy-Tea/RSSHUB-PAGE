
---
title: 'vue入门：http客户端axios'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9988'
author: 掘金
comments: false
date: Thu, 12 Aug 2021 16:02:20 GMT
thumbnail: 'https://picsum.photos/400/300?random=9988'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto;border:3px solid rgba(62,175,124,.2)&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-weight:700;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-radius:6px;border:2px solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c&#125;.markdown-body a:active,.markdown-body a:hover&#123;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a:before&#123;content:"⇲"&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(62,175,124,.2)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:.5rem solid;border-color:#42b983;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none&#125;.markdown-body ul li:before&#123;content:"•";margin-right:4px;color:#3eaf7c&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与 8 月更文挑战的第 13 天，活动详情查看： 8月更文挑战</p>
<h3 data-id="heading-0">1.axiox简介</h3>
<p>jquery时代，我们使用ajax向后台提交数据请求，Vue时代，Axios提供了前端对后台数据请求的各种方式。</p>
<p>而在vue中很多都是使用axios。</p>
<p>优缺点：</p>
<ul>
<li>从 node.js 创建 http 请求</li>
<li>支持 Promise API</li>
<li>客户端支持防止CSRF</li>
<li><strong>提供了一些并发请求的接口</strong>（重要，方便了很多的操作）</li>
</ul>
<h3 data-id="heading-1">2.axios的跨域</h3>
<p>由于前后端的端口号不同，那么会又跨域的问题。而解决跨域有很多总方法，比如使用后台配置或者nginx，以下是我做过的demo。</p>
<h4 data-id="heading-2">1.nginx配置跨域</h4>
<pre><code class="copyable">#user  nobody;
worker_processes  1;

#error_log  logs/error.log;
#error_log  logs/error.log  notice;
#error_log  logs/error.log  info;

#pid        logs/nginx.pid;
daemon off;
events &#123;
    worker_connections  65535;
multi_accept on;
&#125;

http &#123;
    include       mime.types;
    default_type  application/octet-stream;

    #log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
    #                  '$status $body_bytes_sent "$http_referer" '
    #                  '"$http_user_agent" "$http_x_forwarded_for"';

    #access_log  logs/access.log  main;

    sendfile        on;
    tcp_nopush     on;
tcp_nodelay     on;

    #keepalive_timeout  0;
    keepalive_timeout  65;

    server &#123;
           listen 8080;
   server_name localhost;
   ##  = /表示精确匹配路径为/的url，真实访问为http://localhost:8088
   location = / &#123;
   proxy_pass http://localhost:8088;
   &#125;
   ##  /no 表示以/no开头的url，包括/no1,no/son，或者no/son/grandson
   ##  真实访问为http://localhost:5500/no开头的url
   ##  若 proxy_pass最后为/ 如http://localhost:3000/;匹配/no/son，则真实匹配为http://localhost:3000/son
   location /no &#123;
   proxy_pass http://localhost:8088;
   &#125;
   ##  /ok/表示精确匹配以ok开头的url，/ok2是匹配不到的，/ok/son则可以
   location /Demo/testDemoTranNew &#123;
   proxy_pass http://localhost:8088;
   &#125;           
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">2.axios配置跨域</h4>
<p><strong>同时在axios中也可以配置跨域，方式如下：</strong></p>
<h5 data-id="heading-4">1.修改config/index.js文件</h5>
<pre><code class="copyable">        //增加跨域
        proxyTable: &#123;
            "/api": &#123;
                //目标地址
                target: "http://localhost:8088",
                changeOrigin: true,
                pathRewrite: &#123;
                    '^/api': ''
                &#125;
            &#125;
        &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-5">2.main.js中增加变量</h5>
<pre><code class="copyable">//跨域处理  相当于把index中的api地址拿过来
Vue.prototype.HOST = '/api'
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><strong>直接调用就可以了，完全避免了跨域！</strong></p>
</blockquote>
<h3 data-id="heading-6">3.axios的get请求</h3>
<p>在使用时<code>main.js</code>需要导入axios组件。具体方式请参考下文。</p>
<pre><code class="copyable">// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from "axios"


Vue.config.productionTip = false

Vue.prototype.$axios = axios

/* eslint-disable no-new */
new Vue(&#123;
    el: '#app',
    router,
    components: &#123; App &#125;,
    template: '<App/>'
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>vue中的get请求.有两种写发，以下附上两种写法的格式。</p>
<pre><code class="copyable"><template>
<div>
      &#123;&#123;data&#125;&#125;
</div>
</template>

<script>
export default &#123;
name: 'HelloWorld',
data () &#123;
  return &#123;
    content:"组件1",
    data:&#123;&#125;
    &#125;
&#125;,
methods:&#123;

&#125;,
created() &#123;
  //第一种
  // this.$axios.get("https://api.apiopen.top/searchMusic",&#123;
  //   params:&#123;
  //      name:"雅俗共赏"
  //   &#125;
  // &#125;
  // )
  // .then(res => &#123;
  //     console.log(res)
  //     this.data = res.data
  // &#125;)
  // .catch(error => &#123;
  //     console.log(error)
  // &#125;)

  // 第二种
  this.$axios(&#123;
    method: 'get',
    url: 'https://api.apiopen.top/searchMusic',
    params: &#123;
        name:"雅俗共赏"
    &#125;
  &#125;)
  .then(res => &#123;
      console.log(res)
      this.data = res.data
  &#125;)
  .catch(error => &#123;
      console.log(error)
  &#125;)
  ;
&#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">4.axios的post请求</h3>
<p>在调用中也有两种写法，需要注意的是，需要使用qs去格式化参数，因为需要把对象转换成json格式。</p>
<pre><code class="copyable"><template>
<div>
      &#123;&#123;data&#125;&#125;
</div>
</template>

<script>
import qs from "qs"

export default &#123;
name: 'HelloWorld',
data () &#123;
  return &#123;
    content:"组件1",
    data:&#123;&#125;
    &#125;
&#125;,
methods:&#123;

&#125;,
created() &#123;
  //axios的post请求接收的参数是 form-data格式 ----   name = xiaobao 需要使用qs
  // this.$axios.post("https://api.it120.cc/common/mobile-segment/next",qs.stringify(
  //     &#123;
  //   segment: 0
  //      &#125;
  // )
  // )
  // .then(res => &#123;
  //     console.log(res)
  //     this.data = res.data
  // &#125;)
  // .catch(error => &#123;
  //     console.log(error)
  // &#125;)


   //这种写法需要transformRequest来转换格式 否则会报错 因为接受的是string类型参数 //但是不加stringify会直接变成对象传过去
   // 发送 POST 请求
  this.$axios(&#123;
    method: 'post',
    url: 'https://api.it120.cc/common/mobile-segment/next',
    data: &#123;
         segment: 0
    &#125;,
    transformRequest: [function (data) &#123;
    // 对 data 进行任意转换处理
    return qs.stringify(data);
  &#125;]
  &#125;)
  .then(res => &#123;
      console.log(res)
      this.data = res.data
  &#125;)
  .catch(error => &#123;
      console.log(error)
  &#125;);
&#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">5.url的全局配置</h3>
<p>因为如果调用的api前缀相同，那么可以使用全局配置，将url配成全局，避免多次书写。</p>
<p>这里需要时对<code>main.js</code>配置，以下附上代码。</p>
<pre><code class="copyable">// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from "axios"


Vue.config.productionTip = false

Vue.prototype.$axios = axios

axios.defaults.baseURL = 'https://api.example.com';
axios.defaults.headers.common['Authorization'] = AUTH_TOKEN;
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';

/* eslint-disable no-new */
new Vue(&#123;
    el: '#app',
    router,
    components: &#123; App &#125;,
    template: '<App/>'
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>调用时，url就可以省略baseURL中配置的</p>
<h3 data-id="heading-9">6.拦截器</h3>
<p>在axios发送前和接受前，先执行拦截器(类似java拦截器)，这里需要在<code>main.js</code>中加入配置。</p>
<pre><code class="copyable">// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from "axios"
import qs from 'qs'


Vue.config.productionTip = false

Vue.prototype.$axios = axios

axios.defaults.baseURL = 'https://api.it120.cc';
//axios.defaults.headers.common['Authorization'] = AUTH_TOKEN;
//axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';

// 添加请求拦截器
axios.interceptors.request.use(function(config) &#123;
    // 在发送请求之前做些什么
    console.log(config)
    if (config.method === "post") &#123;
        config.data = qs.stringify(config.data);
    &#125;
    return config;
&#125;, function(error) &#123;
    // 对请求错误做些什么
    return Promise.reject(error);
&#125;);

// 添加响应拦截器
axios.interceptors.response.use(function(response) &#123;
    console.log(response)
    if (response.status !== 200) &#123;
        return;
    &#125;
    // 对响应数据做点什么
    return response;
&#125;, function(error) &#123;
    // 对响应错误做点什么
    return Promise.reject(error);
&#125;);

/* eslint-disable no-new */
new Vue(&#123;
    el: '#app',
    router,
    components: &#123; App &#125;,
    template: '<App/>'
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样的话，在接下来的使用中我们拦截了qs方法，在之后的使用中就不必每一个请求都调用qs方法了。</p>
<pre><code class="copyable"><template>
<div>
      &#123;&#123;data&#125;&#125;
</div>
</template>

<script>
import qs from "qs"

export default &#123;
name: 'HelloWorld',
data () &#123;
  return &#123;
    content:"组件1",
    data:&#123;&#125;
    &#125;
&#125;,
methods:&#123;

&#125;,
created() &#123;
  // 发送 POST 请求
  this.$axios(&#123;
    method: 'post',
    url: '/common/mobile-segment/next',
    data: &#123;
         segment: 0
    &#125;
    
  &#125;)
  .then(res => &#123;
      console.log(res)
      this.data = res.data
  &#125;)
  .catch(error => &#123;
      console.log(error)
  &#125;);
&#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">7.前端测试方法</h3>
<p>在测试前端时有几种获取数据方法</p>
<ul>
<li>1.mock 请求自己的json格式 缺点：无法post请求</li>
<li>2.自己搭建服务器 获取数据</li>
<li>3.使用线上已经存在的数据 缺点：线上必须存在数据</li>
</ul>
<blockquote>
<p>注意！操作dom节点时，避免操作原生dom 如：</p>
<pre><code class="copyable"><template>
<div>
      &#123;&#123;data&#125;&#125;
      <p ref = "myp">aaa</p>
</div>
</template>

<script>
import $ from "jquery"

export default &#123;
name: 'HelloWorld',
data () &#123;
  return &#123;
    content:"组件1",
    data:&#123;&#125;
    &#125;
&#125;,
methods:&#123;

&#125;,
mounted() &#123;
  //使用原生操作dom
  console.log(this.$refs.myp.innerHTML = "BBB")
  //console.log(this.$refs.myp.style.color = "red")
  var myo2 = this.$refs.myp
  myo2.addEventListener("click",function()&#123;
    console.log("666")
  &#125;)
  //使用jquery操作dom
  $(myo2).css("color","YELLOW");

&#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
</blockquote></div>  
</div>
            