
---
title: 'uniapp中的请求接口封装'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4060'
author: 掘金
comments: false
date: Wed, 09 Jun 2021 01:04:29 GMT
thumbnail: 'https://picsum.photos/400/300?random=4060'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h5 data-id="heading-0">安装</h5>
<pre><code class="copyable">npm install qs // 用来序列化post类型的数据
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-1">引入</h5>
<pre><code class="copyable">import baseUrl from '../baseUrl'; // url地址信息import qs from 'qs' // 处理data
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-2">环境切换</h5>
<p><code>uni-app</code> 可通过 <code>process.env.NODE_ENV</code> 判断当前环境是开发环境还是生产环境。一般用于连接测试服务器或生产服务器的动态切换。</p>
<p>uniapp有自己的生产和开发环境，也可以配置其他的环境；大家可以去观看官方文档</p>
<p><a href="https://uniapp.dcloud.io/frame?id=%E5%BC%80%E5%8F%91%E7%8E%AF%E5%A2%83%E5%92%8C%E7%94%9F%E4%BA%A7%E7%8E%AF%E5%A2%83" target="_blank" rel="nofollow noopener noreferrer">开发环境和生产环境</a></p>
<pre><code class="copyable">if(process.env.NODE_ENV === 'development')&#123;
    console.log('开发环境')
&#125;else&#123;
    console.log('生产环境')
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-3">post请求头的设置</h5>
<p>post请求的时候，需要添加一些请求头；一般默认的请求头是：‘ application/x-www-form-urlencoded ’</p>
<pre><code class="copyable">header = &#123;    'Content-Type': 'application/x-www-form-urlencoded',&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-4">响应数据</h5>
<p>当请求参数返回的时候；查看code数据，给出响应</p>
<pre><code class="copyable">switch (dataType.code * 1) &#123; // 拦截返回参数
case 0:
resolve(dataType)
break;
case 1003:
uni.showModal(&#123;
title: '登录已过期',
content: '很抱歉，登录已过期，请重新登录',
confirmText: '重新登录',
success: function(res) &#123;
if (res.confirm) &#123; // 点击确定
//去登录页面
console.log('用户');
uni.navigateTo(&#123;
    // 切记这儿需要哈pages.json保持一致；不能有.vue后缀
    url: '/pages/views/login/index'
        &#125;);
&#125; else if (res.cancel) &#123;
console.log('用户点击取消');
&#125;
&#125;
&#125;)
    break;
case -1:
    uni.showModal(&#123;
title: '请求数据失败',
content: '获取数据失败！',
confirmText: '确定',
showCancel: false,
            success: function(res) &#123;
    if (res.confirm) &#123;&#125; else if (res.cancel) &#123;
console.log('用户点击取消');
    &#125;
&#125;
&#125;)
break
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-5">完整版</h5>
<pre><code class="copyable">import baseUrl from '../baseUrl';
import qs from 'qs' // 处理data
const request = (params) => &#123;
/*
 * 1.初始化值
 */
let _self = this;
let url = params.url;
let method = params.method || 'GET';
let data = params.data || &#123;&#125;;
data.token = "default-access_token" // default-access_token
/*
 *2.判断token
 */
if (!params.token) &#123; // 如果没有传递token
let token = uni.getStorageSync('token'); // 在本地查找
if (!token) &#123; // 如果本地没有就跳转到登录页面
uni.navigateTo(&#123;
url: 'pages/views/login/index'
&#125;);
&#125; else &#123;
data.token = '179509245-9c91827e0224bdc18d0b118b8be1b5af';
&#125;
&#125;
/*
 * 3.添加头部
 */
let defaultOpot = &#123;
// 'Content-Type': 'application/x-www-form-urlencoded',
'Terminal-Type': 'innerH5',
'Content-Type': 'application/json;charset=UTF-8',
&#125;
/*
 * 4.处理 POST
 */
let header = &#123;&#125;
method = method.toUpperCase()
if (method == 'POST') &#123;
header = &#123;
'Content-Type': 'application/x-www-form-urlencoded',
&#125;
data = qs.stringify(data)
&#125;
// 5.请求地址
const requestUrl = baseUrl.server + url;
uni.showLoading(&#123;
title: '加载中...'
&#125;);
// 6.用 Promise 创建回调
return new Promise((resolve, reject) => &#123;
uni.request(&#123;
url: requestUrl,
method: method,
header: Object.assign(&#123;&#125;, defaultOpot, header),
data: data,
dataType: 'json',
&#125;)
.then(res => &#123; // 成功
if (res[1] && res[1].statusCode === 200) &#123;
let &#123;
data: dataType
&#125; = res[1]
switch (dataType.code * 1) &#123; // 拦截返回参数
case 0:
resolve(dataType)
break;
case 1003:
uni.showModal(&#123;
title: '登录已过期',
content: '很抱歉，登录已过期，请重新登录',
confirmText: '重新登录',
success: function(res) &#123;
if (res.confirm) &#123; // 点击确定
//去登录页面
console.log('用户');
uni.navigateTo(&#123;
// 切记这儿需要哈pages.json保持一致；不能有.vue后缀
url: '/pages/views/login/index'
&#125;);
&#125; else if (res.cancel) &#123;
console.log('用户点击取消');
&#125;
&#125;
&#125;)
break;
case -1:
uni.showModal(&#123;
title: '请求数据失败',
content: '获取数据失败！',
confirmText: '确定',
showCancel: false,
success: function(res) &#123;
if (res.confirm) &#123;&#125; else if (res.cancel) &#123;
console.log('用户点击取消');
&#125;
&#125;
&#125;)
break
&#125;
&#125;
&#125;)
.catch(err => &#123; // 错误
reject(err)
&#125;)
.finally(() => &#123;
console.log('不管是否成功都要执行')
uni.hideLoading();
&#125;)
&#125;)
&#125;
export default request
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-6">在api中封装接口</h5>
<pre><code class="copyable">import request from '../../utils/request.js'

/*
* 1.获取商城楼层列表
*/
export function getFloorList()&#123;
return request(&#123;
url:'/***',
method:'get'
&#125;)
&#125;

export function getCartProducts()&#123;
return request(&#123;
url:'/***',
method:'POST'
&#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-7">在组件中使用</h5>
<h6 data-id="heading-8">引入</h6>
<pre><code class="copyable">import &#123;getFloorList,getCartProducts&#125; from '../../api/mall/index.js';
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-9">使用</h6>
<pre><code class="copyable">getFloorList().then(res=>&#123;
this.list = res.data
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上可能不是很完整；大家可以根据自己的需要进行配置即可</p></div>  
</div>
            