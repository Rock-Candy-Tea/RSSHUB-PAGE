
---
title: 'vue-i18n语言开发'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b24620e0d124170a431f750c53edcc7~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 23 Aug 2021 06:44:03 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b24620e0d124170a431f750c53edcc7~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">多语言的功能的实现</h2>
<ul>
<li>下载</li>
</ul>
<pre><code class="copyable">npm install vue-i18n
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>创建对应的文件包i18n</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b24620e0d124170a431f750c53edcc7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-1">1、看了很多都是下面这样写的</h4>
<ul>
<li>都是英文来定义的，这样对应我们英语不好的可读性太差了</li>
<li>比如index 到时候页面多起来，比较复杂，就会命名index1,index2,index3,index4....</li>
</ul>
<pre><code class="copyable">
&#123;&#123;$t('wheel')&#125;&#125;

&#123;&#123;$t('index')&#125;&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67dccd56879542de9dbb6a193166e6be~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-2">2、我也找了很多资料，最后我比较忠于下面这种写法</h4>
<ul>
<li>跟其他人不同的地方在于，我是以中文作为Key的</li>
<li>这样写，以后维护起来的时候看的明白些！</li>
</ul>
<pre><code class="copyable">
<!-- 页面赋值 -->
&#123;&#123;$t('造轮子')&#125;&#125;
&#123;&#123;$t('首页')&#125;&#125;

<!-- 提示的时候 -->
uni.showLoading(&#123;
title: this.$t('加载中')
&#125;)
 
<!-- 循环时候使用 -->
<view class="cu-item bg-img shadow-blur" v-for="(item,index) in list" :key="index">
<view class="cardTitle">
&#123;&#123;$t(item.title)&#125;&#125;
</view>
</view>

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>实列</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/15faa859f4ea48f29a6d1b3c447dd4c6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/91724b27e0044488a7b4f546bc3a2ac2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-3">3、上面截图是vue开发的，uniapp和vue 是一样的用法</h4>
<ul>
<li>下面来看下这个怎么实现的</li>
<li>就是在i18函数里面加一段函数即可</li>
</ul>
<pre><code class="copyable">import Vue from 'vue'
import VueI18n from 'vue-i18n'

Vue.use(VueI18n)

// 看懂这个函数！！！
// 看懂的解释下，我感觉我解释不清楚
function loadLocaleMessages() &#123;
const locales = require.context('.', true, /[A-Za-z0-9-_,\s]+\/index\.js$/i)
const messages = &#123;&#125;
locales.keys().forEach(key => &#123;
messages[key.replace('./', '').replace('/index.js', '')] = locales(key).default
&#125;)
return messages
&#125;

const locale = 'cn'
const i18n = new VueI18n(&#123;
locale, //// 语言标识
fallbackLocale: locale, //默认语言
messages: loadLocaleMessages(),
silentFallbackWarn: true, //抑制警告
silentTranslationWarn: true, //关闭waring提示信息
&#125;)


export default i18n

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">4、源码地址</h4>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodechina.csdn.net%2Fqq_32292395%2FWheel_Multilingual.git" target="_blank" rel="nofollow noopener noreferrer" title="https://codechina.csdn.net/qq_32292395/Wheel_Multilingual.git" ref="nofollow noopener noreferrer">codechina.csdn.net/qq_32292395…</a></p></div>  
</div>
            