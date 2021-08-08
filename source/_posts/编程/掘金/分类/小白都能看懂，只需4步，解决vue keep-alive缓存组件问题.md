
---
title: '小白都能看懂，只需4步，解决vue keep-alive缓存组件问题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6214'
author: 掘金
comments: false
date: Sun, 08 Aug 2021 02:15:51 GMT
thumbnail: 'https://picsum.photos/400/300?random=6214'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">1.首先在路由中配置需要缓存组件的标识:(keepAlive: true)，尝试过先设置为false,然后在路由守卫里通过判断条件设置为true,但是遇到第一次不生效，第二次才生效的问题</h3>
<pre><code class="copyable">export default [
  &#123;
    path: '/',
    component: () =>
      import(
        /* webpackChunkName: "mainContainer" */ '@/views/mainContainer/index.vue'
      ),
    children: [
      &#123;
        path: 'list',
        meta: &#123;
          keepAlive: true,
        &#125;,
        component: () =>
          import(
            /* webpackChunkName: "resource" */ '@/views/index.vue'
          ),
      &#125;,
    ],
  &#125;,
]

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">2.在App.vue中添加相关代码</h3>
<pre><code class="copyable"><div id="app">
    <keep-alive>
      <router-view v-if="$route.meta.keepAlive"></router-view>
    </keep-alive>
    <router-view v-if="!$route.meta.keepAlive"></router-view>
  </div>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">3.在缓存的组件中使用activated生命周期钩子函数，当组件在 keep-alive 内被切换时activated被激活，简单来讲就是在什么情况下需要请求数据，什么时候直接使用缓存的数据</h3>
<pre><code class="copyable">activated() &#123;
    console.log('没错我在缓存组件中')
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">4. 业务场景，现在有A,B,C三个页面，在B页面做一些操作，比如说通过输入搜索条件搜出相关的数据，然后点击一条数据，跳转到详情页C，在C页面点击返回按钮，B还保持搜索后的状态，除此之外A跳到B不需要缓存组件，始终是最新的数据状态，此时可以通过添加一个type来区分</h3>
<pre><code class="copyable">c页面点击返回按钮，返回到B
 this.$router.push(&#123;path:'b?type=needToKeep'&#125;)  /* needToKeep是需要使用缓存的标识*/
 
 A页面到B页面，
 this.$router.push(&#123;path:'b'&#125;)
 
 B页面中：
 activated() &#123;
    const &#123; type &#125; = this.$route.query
    console.log('没错我在缓存组件中')
    if(type !=='needToKeep')&#123;
      this.initdata() // 需要重新请求数据
    &#125;else&#123;
     // 直接使用缓存的组件，假如说此时想刷新页面，重新请求数据怎么办呢，安排！
     const &#123; type &#125; = window.performance.navigation  // 1：刷新页面，0:返回页面
     type === 1 ? this.initdata() : '' 
    &#125;
 &#125;,

<span class="copy-code-btn">复制代码</span></code></pre>
<p>总结：keep-alive是比较方便的一个功能，用法也比较简单，但结合业务场景，别人的解决方案可能并不太适合，多多少少会遇到一点问题，所以找到适合自己业务的解决方案才是最好的</p></div>  
</div>
            