
---
title: 'new 关键字'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f869bf08d0c0450d84788f164e83f3c2~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 16 Aug 2021 01:34:21 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f869bf08d0c0450d84788f164e83f3c2~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">new</h1>
<h2 data-id="heading-1">new 做了什么</h2>
<ul>
<li>创建了一个全新的对象</li>
<li>实例与构造函数通过原型链链接了起来</li>
<li>将空对象作为构造函数的this上下文，执行构造函数</li>
<li>返回新对象</li>
</ul>
<h2 data-id="heading-2">实现一个new</h2>
<pre><code class="copyable">  function testNew (fn) &#123;
    // 获取传入的参数;
    const args = [].slice.call(arguments, 1);
    // 新建一个对象
    const newObj = &#123;&#125;;
    // 把这个对象与构造函数的原型对接
    Object.setPrototypeOf(newObj, fn.prototype)
    // this指向新对象
    fn.apply(newObj, args);
    // 返回这个对象
    return newObj       
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对比下看</p>
<pre><code class="copyable">   function Person(name) &#123;
       this.name = name
   &#125;

   const obj = new Person('你好')

   function testNew (fn) &#123;
        // 获取传入的参数;
        const args = [].slice.call(arguments, 1);
        // 新建一个对象
        const newObj = &#123;&#125;;
        // 把这个对象与构造函数的原型对接
        Object.setPrototypeOf(newObj, fn.prototype)
        // this指向新对象
        fn.apply(newObj, args);
        // 返回这个对象
        return newObj       
   &#125;



   const  testObj = testNew(Person, '我好啊')

   console.log(obj, testObj, '测试');
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f869bf08d0c0450d84788f164e83f3c2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>一模一样有木有</p>
<p>但是要注意如果构造函数中返回了一个对象那么new了之后返回的就是构造函数的对象，所以我们还是要再改动下</p>
<pre><code class="copyable">   function testNew (fn) &#123;
        // 获取传入的参数;
        const args = [].slice.call(arguments, 1);
        // 新建一个对象
        const newObj = &#123;&#125;;
        // 把这个对象与构造函数的原型对接
        Object.setPrototypeOf(newObj, fn.prototype)
        // this指向新对象
        const fnObj = fn.apply(newObj, args);
        // 返回这个对象
        return fnObj instanceof Object ? fnObj : newObj;       
   &#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            