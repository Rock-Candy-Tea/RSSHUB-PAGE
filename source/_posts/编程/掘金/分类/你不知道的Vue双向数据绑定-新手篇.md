
---
title: '你不知道的Vue双向数据绑定-新手篇'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c94ad545f3744994bb2111310784c36c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 02 Aug 2021 01:42:11 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c94ad545f3744994bb2111310784c36c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>如果你和我一样,是一位两年经验的Vue前端工程师,那么我相信你在面试时一定会经常遇到这样的询问:</p>
</blockquote>
<p><strong>面试官:请你描述一下你对Vue的数据双向绑定原理的理解</strong></p>
<p><strong>我：Vue2.0版本的数据双向绑定是基于Object.defineProperty这个API来实现的,它是底层暴露给我们的一个封装方法.参数分别是被监听的对象obj,被监听的属性a,以及第三个用来设定属性特性值的对象;我们可以利用get和set这两个回调函数来实现双向绑定</strong></p>
<p><strong>面试官:那么这两个回调函数是否还有别的作用？Vue中的响应依赖又是什么？如何进行收集和触发？你又是怎么理解观察者和监听者的？</strong></p>
<p><strong>我:</strong></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c94ad545f3744994bb2111310784c36c~tplv-k3u1fbpfcp-watermark.image" alt="123.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>以上面试场景来自笔者最近的一场真实面试,也不意外的挂掉了。于是写下这篇文章,希望能够帮助和我一样对Vue只停留在使用层面的同学有所帮助</p>
</blockquote>
<h2 data-id="heading-0">Vue的数据渲染过程</h2>
<h3 data-id="heading-1">请看下面这段代码</h3>
<pre><code class="copyable"><template>
  <div id="app">
    <div>
      &#123;&#123; msg &#125;&#125;
    </div>
    <span>&#123;&#123; msg + 1 &#125;&#125;</span>
  </div>
</template>
<script>
export default &#123;
  data() &#123;
    return &#123;
      msg: 123,
    &#125;;
  &#125;,
  computed:&#123;
    getMsg()&#123;
      return this.msg + 100;
    &#125;
  &#125;,
  watch:&#123;
    msg:function(val)&#123;
      console.log(val);
    &#125;
  &#125;
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">那么以上代码在Vue的处理中大概走这几步:</h3>
<ol>
<li>使用Object.defineProperty对data中的msg进行数据劫持</li>
<li>收集msg的数据依赖,并派一个监听者(watcher),来对这些数据依赖进行挨个监听</li>
<li>将已经收集好的数据依赖进行保存,当数据发生变化时触发它们,对数据和Dom进行双向通知</li>
<li>生成虚拟DOM->真实DOM</li>
<li>挂载到页面上</li>
</ol>
<h3 data-id="heading-3">我们来尝试一下实现以上第1，2，3步,第4第5步后面我们出续集说明。</h3>
<h4 data-id="heading-4">1.实现数据劫持</h4>
<pre><code class="copyable">function defineData(data,key,val)&#123;
     Object.defineProperty(data,key,&#123;
       get:function()&#123;
           return val;
       &#125;,
       set:function(newVal)&#123;
           if(newVal === val)&#123;
              return;
           &#125;
           val = newVal;
       &#125;
    &#125;)
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">2.收集依赖</h4>
<blockquote>
<p>那么什么是依赖呢？所谓依赖,其实就是哪里使用了被监听的属性值,哪里就需要被收集,哪里就会在数据修改时被通知.于是我们要收集以下四个依赖:</p>
</blockquote>
<ol>
<li>div标签中的引用</li>
<li>span标签中的引用</li>
<li>计算属性getMsg中的引用</li>
<li>watch监听</li>
</ol>
<p>我们将这四个依赖放入一个数组中,以便于管理触发</p>
<pre><code class="copyable">let watcherList = [依赖1,依赖2,依赖3,依赖4];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我上面说过,哪里使用了,哪里就需要收集,以便于通知.所以我们可以在使用属性值时触发的get回调中来进行收集.所以同理,当我们修改值时,触发通知的行为也应该在set函数中去执行.代码如下:</p>
<pre><code class="copyable">function defineData(data,key,val)&#123;
     let watcherList = [];
     Object.defineProperty(data,key,&#123;
       get:function()&#123;
           watcherList.push(依赖);
           return val;
       &#125;,
       set:function(newVal)&#123;
           if(newVal === val)&#123;
              return;
           &#125;
           val = newVal;
           waterList.forEach(item=>&#123;
              // 通知所属依赖的每一项进行相应的修改
              item.notice();
           &#125;)
       &#125;
    &#125;)
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在真实的Vue源码中,负责承担通知的角色正是watcher.也就是说,其实我们每一次收集使用了数据的依赖,实际上是把watcher进行了实例化,收集了watcher的实例化对象.这样当数据变化时,watcher的实例化对象就可以帮助我们进行通知修改.</p>
<h2 data-id="heading-6">Vue对所有Key值的检测</h2>
<blockquote>
<p>我们现在已经实现了对单个属性的数据检测以及通知的基本过程,在真实项目开发中,data中的属性类型五花八门,那么Vue是如何实现检测所有的key属性值呢？</p>
</blockquote>
<h3 data-id="heading-7">代码如下:</h3>
<pre><code class="copyable">       class Observer&#123;
        constructor(value)&#123;
          this.value = value;
          if(Array.isArray(value))&#123;
            // 这里是对Array类型的单独处理,下篇会详细介绍
          &#125;else&#123;
            this.walk(value);
          &#125; 
        &#125;

        walk(obj)&#123;
          const keys = Object.keys(obj);
          keys.forEach(key=>&#123;
            defineData(obj,key,obj[key]);
          &#125;);
        &#125;
       &#125;

       function defineData(data,key,val)&#123;
          // 递归判断,如果val仍然是object类型,则继续实例化Observer进行侦测
          if(Object.prototype.toString.call(val) === '[object Object]')&#123;
              new Observer(val);
          &#125;;
          let watcherList = [];
          Object.defineProperty(data,key,&#123;
            enumerable:true, // 是否可枚举
            configurable:true, // 是否可修改和可删除,
            get:function()&#123;
              watcherList.push(new watcher);
              return val;
            &#125;,
            set:function(newVal)&#123;
              if(newVal === val)&#123;
                return;
              &#125;
              val = newVal;
              waterList.forEach(item=>&#123;
                // 通知所属依赖的每一项进行相应的修改
                item.notice();
              &#125;)
            &#125;
          &#125;)
       &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>结语:个人认为,作为一个框架的使用者,熟悉框架的设计原理和思路是必需.这样能使你在工作时快速对问题进行定位,不需耗费时间百度.这是笔者第一次编写技术文章,希望可以使读者有所收获,也欢迎大家指出宝贵的意见。</p>
</blockquote>
<ul>
<li>资料来源:《深入浅出Vue.js》</li>
</ul></div>  
</div>
            