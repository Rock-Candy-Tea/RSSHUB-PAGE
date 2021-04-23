
---
title: 'javascript防篡改对象'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e4ecb3f74fe470bba2dcf3279a9e963~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 21 Apr 2021 19:22:55 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e4ecb3f74fe470bba2dcf3279a9e963~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e4ecb3f74fe470bba2dcf3279a9e963~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>大家好，我是德莱问。</p>
<h2 data-id="heading-0">javascript防篡改对象</h2>
<p>这个东西吧，用到的很少，个人感觉用处不大，但是，可以作为装逼的利器，哈哈，开搞。。</p>
<h2 data-id="heading-1">1、不可扩展对象</h2>
<p>默认情况下对象都是可以扩展的，也就是说，任何时候都可以向对象中添加属性和方法。现在使用Object.preventExtensions(object)方法可以改变这个行为，让你不能再给对象添加属性和方法。例如：</p>
<pre><code class="copyable">var person=&#123;name : 'jack'&#125;;
Object.preventExtensions(person);
person.age=13;
console.log(person.age);///undefine
<span class="copy-code-btn">复制代码</span></code></pre>
<p>虽然不能给对象添加新成员，但是已有的成员则丝毫不受影响，你仍然可以修改和删除自己的已有的成员。另外使用isExtensible()方法还可以确定对象是否可以扩展。例如：</p>
<pre><code class="copyable">var person=&#123;name : 'jack'&#125;;
alert(Object.isExtensible(person));//true

Object.preventExtensions(person);
alert(Object.istExtensible(person));//false

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">2、密封的对象</h2>
<p>ECMAScript 5 为对象定义的第二个保护级别是密封对象。使用Object.seal(object)方法可以将对象改为密封对象。密封对象不可扩展，而且已有成员的[[configurable]]特性将被设置为false。这就意味着不能删除属性和方法，因为不能使用Object.defineProperty()把数据修改为访问其属性，或者相反。<strong>但是属性值是可以修改的</strong>。</p>
<pre><code class="copyable">var person = &#123;name:'tom'&#125;;
Object.seal(person);
person.age=12;
console.log(person.age);//undefine

delete person.name;
console.log(person.name);//tom

person.name="jack";
alert(person.name);//jack

<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用Object.isSealed()方法可以确定对象是否被密封了，因为被密封的对象也是不可扩展的，所以使用Object.istExtensible()检测密封对象也会返回false（即不可扩展）</p>
<pre><code class="copyable">var person = &#123;name:'tom'&#125;;
alert(Object.isExtensible(person));///true,可扩展
alert(Object.isSealed(person));////false,未加密
               
Object.seal(person);
alert(Object.isExtensible(person));///false,不可扩展
alert(Object.isSealed(person));////true,已经加密
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">3、冻结的对象</h2>
<p>最严格的的防止篡改级别的是冻结对象，冻结的对象既不可扩展，又是密封的，而且对象的数据属性的[[Writable]]特性会被设置为false,如果定义set函数，访问器属性仍然是可写的,现在使用Object.freeze(object)方法可以将对象改为冻结的对象。</p>
<pre><code class="copyable">var person=&#123;name : 'tony'&#125;;
Object.freeze(person);
person.age=12;
alert(person.age);//undefine

delete person.name;
alert(person.name);//tony

person.name = 'jack';
alert(person.name);//tony
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用Object.isFrozen()方法可以检测对象是否是冻结对象，因为冻结对象既是不可扩展对象，又是密封的对象，所以用isExtensible()<br>
和Object.istExtensible()检测冻结对象将分别返回false和true，</p>
<pre><code class="copyable">var person = &#123;name:'tom'&#125;;
alert(Object.isExtensible(person));///true,可扩展
alert(Object.isSealed(person));////false,未加密
alert(Object.isFrozen(person));////false,未加密
               
Object.seal(person);
alert(Object.isExtensible(person));///false,不可扩展
alert(Object.isSealed(person));////true,已经加密
alert(Object.isFrozen(person));////true,已经冻结
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            