
---
title: 'uniapp入门级最佳实践（一） _ 8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d989869c641d40a8bb072c19754440ef~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 18 Aug 2021 02:09:26 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d989869c641d40a8bb072c19754440ef~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第18天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831?utm_campaign=31day&utm_medium=Push&utm_source=20210803" title="https://juejin.cn/post/6987962113788493831?utm_campaign=31day&utm_medium=Push&utm_source=20210803" target="_blank">8月更文挑战</a></strong></p>
<h3 data-id="heading-0">一、简介（先了解uniapp）</h3>
<p>在众多跨端开发框架中，我觉得uniapp还是比较容易上手的，因为我会vue比较多。</p>
<p><strong>跨端框架</strong></p>
<p>1、页面渲染方式：</p>
<p>    1）纯web渲染：inoic</p>
<p>    2）纯native原生渲染：rn、weex</p>
<p>    3）Hybrid渲染，就是web和native的结合版本：<a href="https://link.juejin.cn/?target=https%3A%2F%2Funiapp.dcloud.io%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://uniapp.dcloud.io/" ref="nofollow noopener noreferrer"><strong>uniapp</strong></a>(可以选择weex渲染)</p>
<p>2、uniapp：</p>
<p>开发工具：HbuilderX</p>
<p>跨端能力：可以跨10个不同的平台，开发ios的APP可以不使用mac电脑，Hbuilder可以直接帮你上传</p>
<p>会使用vue就可以使用uniapp，支持云开发</p>
<p>3、nvue（native vue）</p>
<p>uniapp的App端内置了一个基于weex改进的原生渲染引擎，提供原生渲染的能力。在APP端，如果用vue页面，就会使用webView渲染，但是如果用nvue页面就会用原生渲染。一个app中可以同时用两种页面，例如首页用nvue，详情页用vue页面。但是nvue的css写法有限制，如果不准备开发APP端，就不要用nvue。</p>
<h3 data-id="heading-1">二、实战开发</h3>
<p>先看下文件目录：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d989869c641d40a8bb072c19754440ef~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>1、可以在App.vue中globalData写入公共变量，可以全局访问</p>
<pre><code class="copyable">App.vue
<script>
export default &#123;
globalData: &#123;//全局变量
serverUrl: 'https://abc.cn',
token: '',
&#125;,
                //生命周期
onShow: function(options) &#123;
                    console.log('onShow');
&#125;
&#125;
</script>


//页面访问方式：
getApp().globalData.token
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、main.js引入公共js文件（封装的各种方法），可以全局访问</p>
<pre><code class="copyable">import Vue from 'vue'
import App from './App'

import utils from '@/utils/utils.js';//封装的公共js文件

Vue.config.productionTip = false;

Vue.prototype.$utils = utils;

App.mpType = 'app'

const app = new Vue(&#123;
    ...App
&#125;)
app.$mount()
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3、pages.json配置页面路由，标题，标题背景，tabbar等</p>
<pre><code class="copyable">&#123;
"pages": [ //pages数组中第一项表示应用启动页，参考：https://uniapp.dcloud.io/collocation/pages
&#123;
"path": "pages/home/home",
"style": &#123;
"navigationBarTitleText": "首页"
&#125;
&#125;
        ],
"globalStyle": &#123;
"navigationBarTextStyle": "#FFFFFF",//设置导航栏文字颜色
"navigationBarTitleText": "hello uniapp",//设置页面名称
"navigationBarBackgroundColor": "#19AD78",//设置导航栏背景色
"backgroundColor": "#F8F8F8"//设置背景色
        &#125;,
        //配置tabbar
"tabBar": &#123;
"selectedColor":"#19AD78",
"color":"#A8A8A8",
"list": [
&#123;
"text": "首页",
"pagePath": "pages/home/home","iconPath": "static/images/a.png",
"selectedIconPath": "static/images/a_selected.png"
&#125;,&#123;
"text": "消息",
"pagePath": "pages/message/message",
"iconPath": "static/images/b.png",
"selectedIconPath": "static/images/b_selected.png"
&#125;,&#123;
"text": "我的",
"pagePath": "pages/mine/mine",
"iconPath": "static/images/c.png",
"selectedIconPath": "static/images/c_selected.png"
&#125;
]
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4、判断不同的平台使用不同的代码，使用注释的方式进行判断，ifdef后面的平台名称官网有全的可以看下<a href="https://link.juejin.cn/?target=https%3A%2F%2Funiapp.dcloud.io%2Fplatform%3Fid%3D%25e7%25bb%2584%25e4%25bb%25b6%25e7%259a%2584%25e6%259d%25a1%25e4%25bb%25b6%25e7%25bc%2596%25e8%25af%2591" target="_blank" rel="nofollow noopener noreferrer" title="https://uniapp.dcloud.io/platform?id=%e7%bb%84%e4%bb%b6%e7%9a%84%e6%9d%a1%e4%bb%b6%e7%bc%96%e8%af%91" ref="nofollow noopener noreferrer"><strong>uniapp条件编译</strong></a></p>
<p>页面：</p>
<pre><code class="copyable"> <!-- #ifdef MP-WEIXIN -->
      <official-account></official-account>
 <!-- #endif -->
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里是只在微信小程序的平台中才展示这个组件</p>
<p>js：</p>
<pre><code class="copyable">                                // #ifdef MP-WEIXIN
uni.navigateTo(&#123;
url: '/pages/login/login',
&#125;);
// #endif

// #ifdef H5
uni.navigateTo(&#123;
url: '/pages/loginH5/loginH5',
&#125;);
// #endif
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里js判断是微信小程序还是H5浏览器，跳转到不同的登录页面，因为微信小程序和H5小程序的登录和授权样式和功能都不太一样，我就写了两个页面，如果你们的页面差不多就可以用同一个页面，在里面判断就行。</p>
<p>css：</p>
<pre><code class="copyable">/*  #ifdef  MP-WEIXIN */平台特有样式
/*  #endif  */
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里是只在微信小程序平台才展示这个样式，其他平台不启用这个样式。</p>
<p>先写这么多，我感觉uniapp很容易上手很好用，推荐推荐。</p></div>  
</div>
            