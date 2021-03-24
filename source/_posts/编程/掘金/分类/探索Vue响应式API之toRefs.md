
---
title: '探索Vue响应式API之toRefs'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e29f8b1f7594f37a8f9bd5fd788c034~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 23 Mar 2021 19:15:23 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e29f8b1f7594f37a8f9bd5fd788c034~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><pre><code class="copyable">//输入
const &#123;ref, reactive, toRefs&#125; = VueReactivity;
const counter = reactive(&#123;a:1&#125;);
const counterToRefs = toRefs(counter);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>先看toRefs函数。</p>
<pre><code class="copyable">function toRefs(object) &#123;    
    if (!isProxy(object)) &#123;      
        console.warn(        `toRefs() expects a reactive object 
            but received a plain one.`      );    
    &#125;    
    const ret = isArray(object) ? new Array(object.length) : &#123;&#125;;    
    for (const key in object) &#123;      
        ret[key] = toRef(object, key);    
    &#125;    
    return ret;  
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里传入进去的counter因为调用了reactive，所以是一个proxy，也就是vue中所说的响应性对象。toRefs函数首先判断传入进去的对象是不是Proxy，如果不是将会警告。因为我们传入进去的是一个Object，所以ret=&#123;&#125;。看遍历里的toRef函数都做了什么。</p>
<pre><code class="copyable">function toRef(object, key) &#123;    
    return isRef(object[key]) ? object[key] : new ObjectRefImpl(object, key);  
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>函数内判断每个key在对象内是不是一个ref，如果不是，new一个ObjectRefImpl对象。看看ObjectRefImpl。</p>
<pre><code class="copyable">class ObjectRefImpl &#123;    
    constructor(_object, _key) &#123;      
        this._object = _object;      
        this._key = _key;      
        this.__v_isRef = true;    
    &#125;    
    get value() &#123;      
        return this._object[this._key];    
    &#125;    
    set value(newVal) &#123;      
        this._object[this._key] = newVal;    
    &#125;  
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看的出来，做的工作很简单，实例化了一个ObjectRefImpl对象，这个对象内分别挂载了_object，_key，__v_isRef三个属性，如果触发get操作，将返回Object[key]，如果触发set操作,将给Object内指定的key赋新值。</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e29f8b1f7594f37a8f9bd5fd788c034~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>counterToRefs的结果打印出来，可以发现，实际上toRefs函数要做的事情其实很简单，就是生成一个新的对象，对象中的每个key都对应着proxy的每个key，双方建立映射关系。对a做的任何操作实际上就是对proxy[a]做的任何操作。</p>
<p><img alt class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c81cdc0f46a4de6986b0097d29713b5~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>看下Vue官网所说的，会思考一个问题，为什么解构的时候要用toRefs，否则将丢失反应性？</p>
<p>看到这里可能已经了解了，因为props是个proxy，如果不toRefs直接解构，得到的title跟原来的props没有任何关系，如果title发生了改变或被使用到，props都无法进行track（依赖收集）和trigger（触发依赖）。因此也就丢失了相应性。</p>
<p>而通过建立这样的映射关系，实例化了一个ObjectRefImpl对象，巧妙的解决了问题。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            