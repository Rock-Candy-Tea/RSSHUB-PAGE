
---
title: 'vue-web全屏问题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2267'
author: 掘金
comments: false
date: Wed, 21 Jul 2021 22:46:52 GMT
thumbnail: 'https://picsum.photos/400/300?random=2267'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>方法一</strong></p>
<ul>
<li>自己写一个开启和关闭全屏的方法,会存在全屏时无法监听按键事件ESC退出全屏时修改状态值问题。(亲测谷歌、火狐、360、QQ；浏览器、Microsoft Edge都可以)</li>
</ul>
<pre><code class="copyable"><template>
  <div class="aaa">
    <el-button type="primary" @click="handleFullScreen">全屏</el-button>
  </div>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">data()&#123;
    return &#123;
      fullScreen: false,
    &#125;
&#125;,
methods:&#123;
    handleFullScreen()&#123;
      let dom = document.documentElement;
      // 判断是否已经全屏，是全屏时则退出全屏状态;否则则进入全屏
      if(this.fullScreen)&#123;
        if(document.exitFullscreen)&#123;
            document.exitFullscreen();
        &#125;else if(document.webkitCancelFullScreen)&#123;
            document.webkitCancelFullScreen();
        &#125;else if(document.mozCancelFullScreen)&#123;
            document.mozCancelFullScreen();
        &#125;else if(document.msExitFullScreen)&#123;
            document.msExitFullScreen();
        &#125;
      &#125;else&#123;
        if(dom.requestFullscreen)&#123;
            dom.requestFullscreen();
        &#125;else if(dom.webkitRequestFullScreen)&#123;
            dom.webkitRequestFullScreen();
        &#125;else if(dom.mozRequestFullScreen)&#123;
            dom.mozRequestFullScreen();
        &#125;else if(dom.msRequestFullScreen)&#123;
            dom.msRequestFullScreen();// IE11
        &#125;
      &#125;
      this.fullScreen = !this.fullScreen;
    &#125;,
    // 判断当前是否为全屏状态
    checkFull()&#123;
      let isFull = document.fullscreenElement || document.mozFullScreenElement || document.webkitFullscreenElement
       || document.msFullscreenElement;
      if( !isFull)&#123;
        isFull = false;
      &#125;else &#123;
        isFull = true;
      &#125;
      return isFull;
    &#125;
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>解决方案</strong></p>
<ul>
<li>写一个方法在页面大小发生变化时在mounted监听事件返回值，确定当前是全屏状态还是退出全屏状态，再进行确定是否修改状态值。</li>
</ul>
<pre><code class="copyable">//判断全屏关闭状态和状态值同事满足条件时，修改状态
mounted()&#123;
    window.addEventListener('resize', () => &#123;
      if(!this.checkFull() && this.fullScreen)&#123;
        this.fullScreen = false;
      &#125;
    &#125;)
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>方法二</strong></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fscreenfull" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/screenfull" ref="nofollow noopener noreferrer">采用第三方插件screenfull</a>能够完美解决web端的浏览器全屏问题，自己简单使用了一下（本人是单独写成一个组件，来进行使用；想要更深一步的了解插件可以自行去官方查看文档），在下面贴出代码：</li>
</ul>
<pre><code class="copyable">使用npm命令下载插件  npm install screenfull
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable"><template>
    <div style="float:left">
        <el-button type="primary"  @click="handleScreenFull"><i class="iconfont">&#xe8b8;</i></el-button>
    </div>
</template>
<script>
import screenfull from 'screenfull';

export default &#123;
    name: "ScreenFull",
    data()&#123;
        return &#123;
            isFullScreen: false,
        &#125;
    &#125;,
    mounted() &#123;
        this.init();
    &#125;,
    methods: &#123;
        handleScreenFull() &#123;
            if(!screenfull.isEnabled)&#123;
                return false;
            &#125;
            screenfull.toggle();
        &#125;,
        change() &#123;
            this.isFullScreen = screenfull.isFullscreen;
        &#125;,
        init() &#123;
            if(screenfull.isEnabled)&#123;
                screenfull.on('change', this.change);
            &#125;
        &#125;,
    &#125;,
    destroy() &#123;
        if(screenfull.isEnabled)&#123;
            screenfull.off('change', this.change);
        &#125;
    &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">父组件中使用
<template>
  <div class="aaa">
    <screen-full />
  </div>
</template>

<script>
import screenFull from "@/components/ScreenFull.vue"
export default &#123;
  name: "Header",
  components: &#123;
    screenFull
  &#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>以上是自己解决全屏问题的两种方案，如各位大佬有更好的解决方案，欢迎在下方评论</strong></p></div>  
</div>
            