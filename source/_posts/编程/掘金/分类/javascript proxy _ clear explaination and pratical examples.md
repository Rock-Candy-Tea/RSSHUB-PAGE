
---
title: 'javascript proxy _ clear explaination and pratical examples'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99d3279b5cc945dd850dab850b56d7db~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 17 Jul 2021 18:35:21 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99d3279b5cc945dd850dab850b56d7db~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">What is proxy</h2>
<p>Proxy enalbes us to intercept and customize operations performed on objects (such as getting ,setting properties). They are metaprogramming feature.</p>
<blockquote>
<p>metaProgramming:</p>
<blockquote>
<p>Metaprogramming is writing a program which outputs another program , which enables one to intercept and define custome behavior for fundamental language operations(e.g. property lookup, assignment, enumeration, function invocation, etc).</p>
</blockquote>
</blockquote>
<h2 data-id="heading-1">The basic syntax</h2>
<blockquote>
<p>let proxy = new Proxy(target,handler)</p>
</blockquote>
<ul>
<li>target: is an object to wrap , can be anything ,including functions</li>
<li>handler: proxy configuration: an object with "traps", method that intercept operations. -e.g. get trap for reading property of target,set trap for writing a property into target,and so on .</li>
</ul>
<p>for operations on proxy, if there's a corresponding trap in handler , then it runs ,and the proxy has the chance to handle it , otherwise the operation is performed on target.</p>
<p>At first , let's create a proxy without any traps:</p>
<pre><code class="copyable">let target = &#123;&#125;;

let proxy = new Proxy(target,&#123;&#125;); // empty handler

proxy.test = 5;

console.log(target.test) // 5
console.log(proxy.test)  //5
<span class="copy-code-btn">复制代码</span></code></pre>
<p>As there are no traps , all operations on proxy are forwarded to target.</p>
<p>1.A writing operation proxy.test = sets the value on target.</p>
<p>2.A reading operation proxy.test returns the value from target .</p>
<p>Proxy is a special “exotic object”. It doesn’t have own properties. With an empty handler it transparently forwards operations to target.</p>
<p>To activate more capabilities , let's add traps. For most operations on object , there's a so-called 'internal method' in the javascript specification that describes how it works at the lowest level . For instance [[GET]], the internal method to read propery , [[SET]] , the internal method to write a property, and so on .</p>
<p>Proxy traps intercept invocations of these methods. They are listed in the below picture .</p>
<p>For every internal method, there's a trap in this table : the name of the method that we can add to the handler parameter of new Proxy to intercept the operation :</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99d3279b5cc945dd850dab850b56d7db~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">GET</h3>
<p>The most common trap for reading the propery . The handler should have a method get(taregt,property,receiver)</p>
<ul>
<li>target: the target object , the one passed as the first argument to new Proxy.</li>
<li>property : property name</li>
<li>receiver : optional , the proxy object itslef .</li>
</ul>
<p>below , is a demo example . Usually if we try to get the non-existing array item , it returns undefined , but we will wrap a regular array into the proxy that traps reading and returns 0 if there's no such property .</p>
<pre><code class="copyable">let arr =[1,2,3,4];

let arr = new Proxy(arr,&#123;
    get(target,prop)&#123;
       if(prop in target)&#123;
           return target[prop]
       &#125;else&#123;
           return 0;
       &#125;
    &#125;
&#125;)

let res1 = arr[0];
let res100 = arr[100];

console.log(res1);  //1

console.log(res100);  //0
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">SET</h3>
<p>The most common trap for writing the property . THe handler should have a method set(target,property,value,receiver)</p>
<ul>
<li>target: the target object , the one passed as the first argument to new Proxy.</li>
<li>property: property name.</li>
<li>value: the value that we want to assign to the property.</li>
<li>receiver: optional,the proxy object itslef .</li>
</ul>
<pre><code class="copyable">let validator = &#123;
  set: function(obj, prop, value) &#123;
    if (prop === 'age') &#123;
      if (!Number.isInteger(value)) &#123;
        throw new TypeError('The age is not an integer');
      &#125;
      if (value > 200) &#123;
        throw new RangeError('The age seems invalid');
      &#125;
    &#125;

    // if valid,assign the vlaue to the property
    obj[prop] = value;
    return true;
  &#125;
&#125;;

let person = new Proxy(&#123;&#125;, validator);

person.age = 100;

person.age // 100
person.age = 'young' // error
person.age = 300 // error
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Those aboe are the most comomen ones and for more you can visit <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FProxy" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy" ref="nofollow noopener noreferrer">MDN DOCS</a></p>
<h2 data-id="heading-4">Reference</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FProxy" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy" ref="nofollow noopener noreferrer">MDN</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fjavascript.info%2Fproxy" target="_blank" rel="nofollow noopener noreferrer" title="https://javascript.info/proxy" ref="nofollow noopener noreferrer">Javascript INFO</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fes6.ruanyifeng.com%2F%23docs%2Fproxy%23Proxy-%25E5%25AE%259E%25E4%25BE%258B%25E7%259A%2584%25E6%2596%25B9%25E6%25B3%2595" target="_blank" rel="nofollow noopener noreferrer" title="https://es6.ruanyifeng.com/#docs/proxy#Proxy-%E5%AE%9E%E4%BE%8B%E7%9A%84%E6%96%B9%E6%B3%95" ref="nofollow noopener noreferrer">Proxy</a></p></div>  
</div>
            