
---
title: 'vue：五分钟，让你从0开始搭建国际化（多语言）vue-i18n'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9109'
author: 掘金
comments: false
date: Thu, 05 Aug 2021 00:41:44 GMT
thumbnail: 'https://picsum.photos/400/300?random=9109'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>公司的项目涉及到国际化，之前也没搞过，所以稍微查阅了一些资料，然后自己从0开始实现了国际化。
记录下来以后供以后再次使用。（结尾附源码）第一次写，可能会不尽如人意，不喜可喷，欢迎交流。</p>
<h1 data-id="heading-1">正文</h1>
<h2 data-id="heading-2">安装依赖</h2>
<p>依赖vue-i18n，先装依赖：yarn add vue-i18n 或 npm install vue-i18n</p>
<h2 data-id="heading-3">准备工作</h2>
<p>在src下创建：</p>
<p>locale/langs/zh.js 和 locale/langs/en.js 用于存放待翻译的内容</p>
<pre><code class="copyable">const lang = &#123;
  title: 'title',//（标题）
  title1: 'title1',//（标题2）
  placeholder: 'please enter',//请输入中文
&#125;

export default lang
<span class="copy-code-btn">复制代码</span></code></pre>
<p>locale/index.js 创建vuei18n实例，导入element-ui和自己的待翻译的内容</p>
<pre><code class="copyable">import Vue from 'vue'
import VueI18n from 'vue-i18n'
import en from './langs/en.js'
import zh from './langs/zh.js'
import enLocale from 'element-ui/lib/locale/lang/en'
import zhLocale from 'element-ui/lib/locale/lang/zh-CN'

Vue.use(VueI18n)

const i18n = new VueI18n(&#123;
  locale: 'zh-CN',
  messages: &#123;
    'zh-CN': &#123; ...zhLocale, ...zh &#125;,
    'en': &#123; ...enLocale, ...en &#125;
  &#125;
&#125;)

export default i18n
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在main.js文件中导入创建好的vuei18n实例</p>
<pre><code class="copyable">import Vue from 'vue'
import App from './App.vue'

import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css';
import i18n from './locale'

Vue.use(ElementUI, &#123;
  i18n: (key, value) => i18n.t(key, value)
&#125;)

Vue.config.productionTip = false;

new Vue(&#123;
  i18n,
  render: h => h(App),
&#125;).$mount('#app')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到此全部的准备工作就做完了。</p>
<h2 data-id="heading-4">使用</h2>
<p>切换国际化语言</p>
<pre><code class="copyable">methods: &#123;
  changeLocale (lang) &#123;
    this.$i18n.locale = lang
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>模板里使用</p>
<pre><code class="copyable"><el-date-picker
  v-model="value1"
  type="datetime"
  :placeholder="$t('placeholder')">
</el-date-picker>
<div>
  &#123;&#123; $t('title') &#125;&#125;
</div>
<div>
  &#123;&#123; $t('title1') &#125;&#125;
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fliangtao125061github%2Fvue-0to100-i18n.git" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/liangtao125061github/vue-0to100-i18n.git" ref="nofollow noopener noreferrer">源码地址：https://github.com/liangtao125061github/vue-0to100-i18n.git</a></p>
<h1 data-id="heading-5">结尾</h1>
<p>喜欢的请点个赞吧。</p></div>  
</div>
            