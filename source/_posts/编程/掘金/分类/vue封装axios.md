
---
title: 'vue封装axios'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/34fbf8d878ad4e07a0a40c4a5f45a025~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 08 Jun 2021 18:44:53 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/34fbf8d878ad4e07a0a40c4a5f45a025~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">安装</h3>
<p>npm install axios;</p>
<h3 data-id="heading-1">引入</h3>
<p>一般我会在项目的src目录中，新建一个request文件夹，然后在里面新建一个http.js和一个api.js文件。http.js文件用来封装我们的axios，api.js用来统一管理我们的接口。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/34fbf8d878ad4e07a0a40c4a5f45a025~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-2">// 在http.js中引入axios</h4>
<p>import axios from 'axios'; // 引入axios</p>
<h4 data-id="heading-3">// 环境的切换</h4>
<p>if (process.env.NODE_ENV == 'development') &#123;<br>
axios.defaults.baseURL = '<a href="https://www.baidu.com';&#125;/" target="_blank" rel="nofollow noopener noreferrer">www.baidu.com';&#125;</a>
else if (process.env.NODE_ENV == 'debug') &#123;<br>
axios.defaults.baseURL = '<a href="https://www.ceshi.com/" target="_blank" rel="nofollow noopener noreferrer">www.ceshi.com</a>';
&#125;
else if (process.env.NODE_ENV == 'production') &#123;<br>
axios.defaults.baseURL = '<a href="https://www.production.com/" target="_blank" rel="nofollow noopener noreferrer">www.production.com</a>';
&#125;//复制</p>
<h4 data-id="heading-4">设置请求超时</h4>
<p>通过axios.defaults.timeout设置默认的请求超时时间。例如超过了10s，就会告知用户当前请求超时，请刷新等。</p>
<p>axios.defaults.timeout = 10000;//复制</p>
<h4 data-id="heading-5">post请求头的设置</h4>
<p>post请求的时候，我们需要加上一个请求头，所以可以在这里进行一个默认的设置，即设置post的请求头为application/x-www-form-urlencoded;charset=UTF-8</p>
<p>axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=UTF-8'; //复制</p>
<h4 data-id="heading-6">请求拦截</h4>
<p>// 先导入vuex,因为我们要使用到里面的状态对象
// vuex的路径根据自己的路径去写
import store from '@/store/index';</p>
<p>// 请求拦截器axios.interceptors.request.use(<br>
config => &#123;<br>
// 每次发送请求之前判断vuex中是否存在token<br>
// 如果存在，则统一在http请求的header都加上token，这样后台根据token判断你的登录情况
// 即使本地存在token，也有可能token是过期的，所以在响应拦截器中要对返回状态进行判断
const token = store.state.token;<br>
token && (config.headers.Authorization = token);<br>
return config;<br>
&#125;,<br>
error => &#123;<br>
return Promise.error(error);<br>
&#125;)
复制代码</p>
<h4 data-id="heading-7">这里说一下token，一般是在登录完成之后，将用户的token通过localStorage或者cookie存在本地，然后用户每次在进入页面的时候（即在main.js中），会首先从本地存储中读取token，如果token存在说明用户已经登陆过，则更新vuex中的token状态。然后，在每次请求接口的时候，都会在请求的header中携带token，后台人员就可以根据你携带的token来判断你的登录是否过期，如果没有携带，则说明没有登录过。这时候或许有些小伙伴会有疑问了，就是每个请求都携带token，那么要是一个页面不需要用户登录就可以访问的怎么办呢？其实，你前端的请求可以携带token，但是后台可以选择不接收啊！</h4>
<h4 data-id="heading-8">// 响应拦截器</h4>
<pre><code class="copyable">axios.interceptors.response.use(    
    response => &#123;   
        // 如果返回的状态码为200，说明接口请求成功，可以正常拿到数据     
        // 否则的话抛出错误
        if (response.status === 200) &#123;            
            return Promise.resolve(response);        
        &#125; else &#123;            
            return Promise.reject(response);        
        &#125;    
    &#125;,    
    // 服务器状态码不是2开头的的情况
    // 这里可以跟你们的后台开发人员协商好统一的错误状态码    
    // 然后根据返回的状态码进行一些操作，例如登录过期提示，错误提示等等
    // 下面列举几个常见的操作，其他需求可自行扩展
    error => &#123;            
        if (error.response.status) &#123;            
            switch (error.response.status) &#123;                
                // 401: 未登录
                // 未登录则跳转登录页面，并携带当前页面的路径
                // 在登录成功后返回当前页面，这一步需要在登录页操作。                
                case 401:                    
                    router.replace(&#123;                        
                        path: '/login',                        
                        query: &#123; 
                            redirect: router.currentRoute.fullPath 
                        &#125;
                    &#125;);
                    break;

                // 403 token过期
                // 登录过期对用户进行提示
                // 清除本地token和清空vuex中token对象
                // 跳转登录页面                
                case 403:
                     Toast(&#123;
                        message: '登录过期，请重新登录',
                        duration: 1000,
                        forbidClick: true
                    &#125;);
                    // 清除token
                    localStorage.removeItem('token');
                    store.commit('loginSuccess', null);
                    // 跳转登录页面，并将要浏览的页面fullPath传过去，登录成功后跳转需要访问的页面 
                    setTimeout(() => &#123;                        
                        router.replace(&#123;                            
                            path: '/login',                            
                            query: &#123; 
                                redirect: router.currentRoute.fullPath 
                            &#125;                        
                        &#125;);                    
                    &#125;, 1000);                    
                    break; 

                // 404请求不存在
                case 404:
                    Toast(&#123;
                        message: '网络请求不存在',
                        duration: 1500,
                        forbidClick: true
                    &#125;);
                    break;
                // 其他错误，直接抛出错误提示
                default:
                    Toast(&#123;
                        message: error.response.data.message,
                        duration: 1500,
                        forbidClick: true
                    &#125;);
            &#125;
            return Promise.reject(error.response);
        &#125;
    &#125;    
&#125;);复制代码

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">响应拦截器很好理解，就是服务器返回给我们的数据，我们在拿到之前可以对他进行一些处理。例如上面的思想：如果后台返回的状态码是200，则正常返回数据，否则的根据错误的状态码类型进行一些我们需要的错误，其实这里主要就是进行了错误的统一处理和没登录或登录过期后调整登录页的一个操作。</h4>
<p>要注意的是，上面的Toast()方法，是我引入的vant库中的toast轻提示组件，你根据你的ui库，对应使用你的一个提示组件。</p>
<h2 data-id="heading-10">封装get方法和post方法</h2>
<h3 data-id="heading-11">封装get方法</h3>
<pre><code class="copyable">/**
 * get方法，对应get请求
 * @param &#123;String&#125; url [请求的url地址]
 * @param &#123;Object&#125; params [请求时携带的参数]
 */
export function get(url, params)&#123;    
    return new Promise((resolve, reject) =>&#123;        
        axios.get(url, &#123;            
            params: params        
        &#125;).then(res => &#123;
            resolve(res.data);
        &#125;).catch(err =>&#123;
            reject(err.data)        
    &#125;)    
&#125;);&#125;复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">封装post</h3>
<pre><code class="copyable">/** 
 * post方法，对应post请求 
 * @param &#123;String&#125; url [请求的url地址] 
 * @param &#123;Object&#125; params [请求时携带的参数] 
 */
export function post(url, params) &#123;
    return new Promise((resolve, reject) => &#123;
         axios.post(url, QS.stringify(params))
        .then(res => &#123;
            resolve(res.data);
        &#125;)
        .catch(err =>&#123;
            reject(err.data)
        &#125;)
    &#125;);
&#125;复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-13">axios的封装基本就完成了。</h4></div>  
</div>
            